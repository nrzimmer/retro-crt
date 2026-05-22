#!/usr/bin/env python3
"""Generate KiCad 6 schematic — RGB mod KV-21FS140.
Wire-connected layout: IC pins A1/B1/C1 connected via L-wires to bias networks.
U = 1.27mm grid throughout.
"""
import uuid, sys, os

SCH_UUID = str(uuid.uuid4())
_n = [0]
def u(): return str(uuid.uuid4())
def pn():
    _n[0] += 1
    return f"#PWR{_n[0]:03d}"

U = 1.27  # mm per grid unit

def f(v): return f"{v*U:.2f}"  # grid units → mm string

def extract_sym(lib, name):
    txt = open(lib).read()
    pat = f'\t(symbol "{name}"'
    s = txt.find(pat)
    if s < 0: return ""
    d, i = 0, s
    while i < len(txt):
        if txt[i]=='(': d+=1
        elif txt[i]==')':
            d-=1
            if d==0: return txt[s:i+1]
        i+=1
    return ""

def embed(lib, name, prefix):
    s = extract_sym(lib, name)
    return s.replace(f'(symbol "{name}"', f'(symbol "{prefix}:{name}"', 1) if s else ""

LIB    = "/usr/share/kicad/symbols"
DEVICE = f"{LIB}/Device.kicad_sym"
CONN   = f"{LIB}/Connector_Generic.kicad_sym"
POWER  = f"{LIB}/power.kicad_sym"
ANALOG = f"{LIB}/Analog_Switch.kicad_sym"

items = []
A = items.append

# ── primitives ─────────────────────────────────────────────────────────────

def wire(x1,y1,x2,y2):
    return (f'\t(wire\n\t\t(pts (xy {f(x1)} {f(y1)}) (xy {f(x2)} {f(y2)}))\n'
            f'\t\t(stroke (width 0) (type solid))\n\t\t(uuid "{u()}")\n\t)')

def junc(x,y):
    return f'\t(junction (at {f(x)} {f(y)}) (diameter 0) (color 0 0 0 0) (uuid "{u()}"))'

def nc(x,y):
    return f'\t(no_connect (at {f(x)} {f(y)}) (uuid "{u()}"))'

def lbl(text,x,y,angle=0):
    return (f'\t(label "{text}"\n\t\t(at {f(x)} {f(y)} {angle})\n'
            f'\t\t(fields_autoplaced yes)\n'
            f'\t\t(effects (font (size 1.27 1.27)))\n'
            f'\t\t(uuid "{u()}")\n\t)')

def pwr(lib_id, x, y, rot=0):
    ref = pn(); val = lib_id.split(':')[1]
    return (f'\t(symbol\n\t\t(lib_id "{lib_id}")\n\t\t(at {f(x)} {f(y)} {rot})\n'
            f'\t\t(unit 1)\n\t\t(exclude_from_sim no)\n\t\t(in_bom yes)\n\t\t(on_board yes)\n\t\t(dnp no)\n'
            f'\t\t(uuid "{u()}")\n'
            f'\t\t(property "Reference" "{ref}" (at {f(x)} {f(y)} {rot}) (effects (font (size 1.27 1.27)) (hide yes)))\n'
            f'\t\t(property "Value" "{val}" (at {f(x)} {f(y)} {rot}) (effects (font (size 1.27 1.27)) (hide yes)))\n'
            f'\t\t(pin "1" (uuid "{u()}"))\n'
            f'\t\t(instances (project "rgb_mod" (path "/{SCH_UUID}" (reference "{ref}") (unit 1))))\n'
            f'\t)')

def comp(lib_id, ref, value, x, y, rot=0, mirror="", pins=None):
    ms = f'\n\t\t(mirror {mirror})' if mirror else ''
    ps = "".join(f'\n\t\t(pin "{p}" (uuid "{u()}"))' for p in (pins or []))
    return (f'\t(symbol\n\t\t(lib_id "{lib_id}")\n\t\t(at {f(x)} {f(y)} {rot}){ms}\n'
            f'\t\t(unit 1)\n\t\t(exclude_from_sim no)\n\t\t(in_bom yes)\n\t\t(on_board yes)\n\t\t(dnp no)\n'
            f'\t\t(uuid "{u()}")\n'
            f'\t\t(property "Reference" "{ref}" (at {f(x)} {f(y-2)} {rot}) (effects (font (size 1.27 1.27))))\n'
            f'\t\t(property "Value" "{value}" (at {f(x+3)} {f(y)} {rot}) (effects (font (size 1.27 1.27))))\n'
            f'\t\t(property "Footprint" "" (at {f(x)} {f(y)} {rot}) (effects (font (size 1.27 1.27)) (hide yes)))\n'
            f'\t\t(property "Datasheet" "~" (at {f(x)} {f(y)} {rot}) (effects (font (size 1.27 1.27)) (hide yes)))\n'
            f'{ps}\n'
            f'\t\t(instances (project "rgb_mod" (path "/{SCH_UUID}" (reference "{ref}") (unit 1))))\n'
            f'\t)')

# ═══════════════════════════════════════════════════════════════════
# LAYOUT (all coordinates in grid units, U=1.27mm)
#
# IC at (40, 100).  Pin connection points:
#   A1 (RGB R in): (50, 102)    A0 (TV R in):  (50, 104)
#   B1 (RGB G in): (50, 96)     B0 (TV G in):  (50, 98)
#   C1 (RGB B in): (50, 90)     C0 (TV B in):  (50, 92)
#   A  (R out):    (30, 104)    S1: (30, 110)
#   B  (G out):    (30, 100)    S2: (30, 108)
#   C  (B out):    (30, 92)     S3: (30, 106)
#   INH:           (30, 90)     VDD: (42, 114)
#   VEE: (38, 86)  VSS: (40, 86)
#
# RGB bias networks:  R at bias(60,110), G at bias(60,84), B at bias(60,58)
#
# L-wire IC→bias (no crossings):
#   A1(50,102)→(55,102)→(55,110)→(60,110)
#   B1(50,96) →(57,96) →(57,84) →(60,84)
#   C1(50,90) →(53,90) →(53,58) →(60,58)
# ═══════════════════════════════════════════════════════════════════

# ── IC U1 ──────────────────────────────────────────────────────────
A(comp("Analog_Switch:CD4053B","U1","74HCT4053",40,100,
       pins=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]))

# Power pins
A(wire(42,114, 42,116)); A(pwr("power:+5V",  42,116))
A(wire(38,86,  38,84));  A(pwr("power:GND",  38,84))
A(wire(40,86,  40,84));  A(pwr("power:GND",  40,84))
# INH → GND
A(wire(30,90, 28,90)); A(pwr("power:GND", 28,90))

# Output labels (left side A/B/C, angle=180 → text goes left)
A(lbl("R_OUT", 30,104, 180))
A(lbl("G_OUT", 30,100, 180))
A(lbl("B_OUT", 30,92,  180))

# TV input labels (right side A0/B0/C0, angle=0)
A(lbl("R_TV", 50,104, 0))
A(lbl("G_TV", 50,98,  0))
A(lbl("B_TV", 50,92,  0))

# SELECT labels on S1/S2/S3
A(lbl("SELECT", 30,110, 180))
A(lbl("SELECT", 30,108, 180))
A(lbl("SELECT", 30,106, 180))

# ── L-wire routing: IC RGB inputs → bias nodes ─────────────────────
# R: A1(50,102)→(55,102)→(55,110)→(60,110)
A(wire(50,102, 55,102)); A(wire(55,102, 55,110)); A(wire(55,110, 60,110))
# G: B1(50,96)→(57,96)→(57,84)→(60,84)
A(wire(50,96,  57,96));  A(wire(57,96,  57,84));  A(wire(57,84,  60,84))
# B: C1(50,90)→(53,90)→(53,58)→(60,58)
A(wire(50,90,  53,90));  A(wire(53,90,  53,58));  A(wire(53,58,  60,58))

# ── Bias networks ──────────────────────────────────────────────────
# For each channel ch at bias (bx, by):
#   R_top (10k) vertical at (bx, by+3): pin2(bot)=bias, pin1(top)→+5V
#   R_bot (1.5k) vertical at (bx, by-4): pin1(top)=by-1, wire→bias
#   C_couple (47u) rot=90 (horizontal) at (bx+4, by): pin1(L)=bx+1, pin2(R)=bx+7
#     wire: bias(bx,by) → C_couple pin1(bx+1,by)
#   R_term (75R) vertical at (bx+7, by-3): pin1(top)=by, pin2(bot)→GND
#   junction at bias (bx,by) and at EXT node (bx+7,by)
#
# Device:R vertical: pin1 at (cx, cy+3), pin2 at (cx, cy-3)  [in U]
# Device:C_Polarized rot=90: pin1(+) at (cx-3, cy), pin2(-) at (cx+3, cy)

def bias_net(ch, ref_rt, ref_rb, ref_c, ref_rterm, bx, by, pwr_n):
    # R_top (10k): center at (bx, by+3), pin2(bot) at by = bias, pin1(top) at by+6
    A(comp("Device:R", ref_rt, "10k", bx, by+3, pins=["1","2"]))
    A(wire(bx, by+6, bx, by+8)); A(pwr("power:+5V", bx, by+8))
    # junction at bias
    A(junc(bx, by))
    # R_bot (1.5k): center at (bx, by-4), pin1(top)=by-1, pin2(bot)=by-7
    A(comp("Device:R", ref_rb, "1k5", bx, by-4, pins=["1","2"]))
    A(wire(bx, by, bx, by-1))       # bias → R_bot pin1
    A(wire(bx, by-7, bx, by-9)); A(pwr("power:GND", bx, by-9))
    # C_couple (47u/16V) rot=90, center (bx+4, by)
    # rot=90: pin1(+) left at (bx+4-3, by)=(bx+1,by), pin2(-) right at (bx+7,by)
    A(comp("Device:C_Polarized", ref_c, "47u/16V", bx+4, by, rot=90, pins=["1","2"]))
    A(wire(bx, by, bx+1, by))       # bias → C_couple pin1
    # R_term (75R) vertical: center (bx+7, by-3), pin1(top)=by, pin2(bot)=by-6
    A(comp("Device:R", ref_rterm, "75R", bx+7, by-3, pins=["1","2"]))
    # junction at EXT node where C_couple pin2 meets R_term pin1 (both at bx+7,by)
    A(junc(bx+7, by))
    A(wire(bx+7, by-6, bx+7, by-8)); A(pwr("power:GND", bx+7, by-8))
    # net label EXT at connector side (right of R_term pin1)
    A(lbl(f"{ch}_EXT", bx+7, by, 0))

bias_net("R", "R1","R2","C1","R3",  60, 110, 1)
bias_net("G", "R4","R5","C2","R6",  60, 84,  2)
bias_net("B", "R7","R8","C3","R9",  60, 58,  3)

# ── RGB input connectors (one per channel) ─────────────────────────
# Conn_01x01 pin at (cx-4, cy)
# Place at (76, 110/84/58) → pin at (72, y)
# Wire from EXT node (67, y) to connector pin (72, y)
for ch, y in [("R",110),("G",84),("B",58)]:
    jn = f"J_{ch}_RGB"
    A(comp("Connector_Generic:Conn_01x01", jn, f"{ch}_IN", 76, y, pins=["1"]))
    A(wire(67, y, 72, y))
    A(lbl(f"{ch}_EXT", 72, y, 0))   # redundant label makes intent clear

# ── TV input connector J2 (CN004) ──────────────────────────────────
# Place at (8, 100), pins at (4, 102/100/98)
A(comp("Connector_Generic:Conn_01x03","J2","CN004_TV_IN",8,100,pins=["1","2","3"]))
A(lbl("R_TV", 4,102, 180))
A(lbl("G_TV", 4,100, 180))
A(lbl("B_TV", 4,98,  180))

# ── Output connector J3 (CN701) ────────────────────────────────────
A(comp("Connector_Generic:Conn_01x03","J3","CN701_OUT",8,74,pins=["1","2","3"]))
A(lbl("R_OUT", 4,76, 180))
A(lbl("G_OUT", 4,74, 180))
A(lbl("B_OUT", 4,72, 180))

# ── VCC decoupling ─────────────────────────────────────────────────
for cx, ref, val in [(45,"C10","100nF"), (48,"C11","10u/16V")]:
    lib = "Device:C" if "n" in val else "Device:C_Polarized"
    A(comp(lib, ref, val, cx, 118, pins=["1","2"]))
    A(wire(cx,121, cx,123)); A(pwr("power:+5V", cx,123))
    A(wire(cx,115, cx,113)); A(pwr("power:GND", cx,113))

# ── Blanking detect Q1 ─────────────────────────────────────────────
# Q_NPN at (30,145): B at (26,145), C at (32,149), E at (32,141)
A(comp("Device:Q_NPN","Q1","BC547",30,145,pins=["B","C","E"]))
# E → GND
A(wire(32,141, 32,139)); A(pwr("power:GND",32,139))
# C → R_pu → +5V, SELECT label at C
A(lbl("SELECT", 32,149, 0))
A(comp("Device:R","R10","10k",32,155,pins=["1","2"]))
A(wire(32,149, 32,152))             # C to R_pu pin2
A(wire(32,158, 32,160)); A(pwr("power:+5V",32,160))
# B ← R_base ← FBLK_IN label; R_pd to GND
A(comp("Device:R","R11","10k",18,145,rot=90,pins=["1","2"]))  # horizontal: pin1 left=(15,145), pin2 right=(21,145)
A(lbl("FBLK_IN",15,145,180))        # pin1 left at x=18-3=15
A(wire(21,145, 26,145))             # R_base pin2(x=21) → Q1 base(x=26)
A(junc(26,145))
A(comp("Device:R","R12","10k",26,152,pins=["1","2"]))  # vertical pull-down
A(wire(26,145, 26,149))             # B → R_pd pin1
A(wire(26,155, 26,157)); A(pwr("power:GND",26,157))

# FBLK connector
A(comp("Connector_Generic:Conn_01x01","J4","FBLK_IN",8,145,pins=["1"]))
A(lbl("FBLK_IN",4,145,180))

# ── Title ──────────────────────────────────────────────────────────
A(f'\t(text "RGB Mod — KV-21FS140 | 74HCT4053 inject CN004/CN701"\n'
  f'\t\t(at {f(5)} {f(5)} 0)\n'
  f'\t\t(effects (font (size 2 2)))\n'
  f'\t\t(uuid "{u()}")\n\t)')
A(f'\t(text "A1/B1/C1=RGB(SELECT=LOW)  A0/B0/C0=TV(SELECT=HIGH)"\n'
  f'\t\t(at {f(5)} {f(8)} 0)\n'
  f'\t\t(effects (font (size 1.27 1.27)))\n'
  f'\t\t(uuid "{u()}")\n\t)')

# ── lib_symbols + write ────────────────────────────────────────────
lib_syms = "\n".join([
    embed(DEVICE,"R","Device"),
    embed(DEVICE,"C","Device"),
    embed(DEVICE,"C_Polarized","Device"),
    embed(DEVICE,"Q_NPN","Device"),
    embed(CONN,"Conn_01x01","Connector_Generic"),
    embed(CONN,"Conn_01x03","Connector_Generic"),
    embed(POWER,"+5V","power"),
    embed(POWER,"GND","power"),
    embed(ANALOG,"CD4053B","Analog_Switch"),
])

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rgb_mod.kicad_sch")
with open(out,"w") as fh:
    fh.write(
        f'(kicad_sch\n'
        f'\t(version 20231120)\n\t(generator "gen_kicad_sch")\n'
        f'\t(generator_version "1.0")\n\t(uuid "{SCH_UUID}")\n'
        f'\t(paper "A3")\n'
        f'\t(title_block\n'
        f'\t\t(title "RGB Mod — KV-21FS140")\n'
        f'\t\t(comment 1 "A1/B1/C1=RGB(SELECT=LOW) A0/B0/C0=TV(SELECT=HIGH)")\n'
        f'\t)\n'
        f'\t(lib_symbols\n{lib_syms}\n\t)\n'
        + "\n".join(items) + "\n"
        + f'\t(sheet_instances\n\t\t(path "/"\n\t\t\t(page "1")\n\t\t)\n\t)\n'
        + f'\t(embedded_fonts no)\n'
        + ")\n"
    )
print(f"Written: {out}")
