# RGB Mod Netlist — KV-21FS140

## Schematic (ASCII)

```
                       ┌───────────────────────────────────────────┐
                       │              IC01  74HCT4053               │
                       │                                            │
  J01-1 (R_TV) ────────┤ A0                              A ├──── R_OUT ──► J02-1
  J01-2 (G_TV) ────────┤ B0                              B ├──── G_OUT ──► J02-2
  J01-3 (B_TV) ────────┤ C0                              C ├──── B_OUT ──► J02-3
                       │                                            │
  SELECT ─────┬─────── ┤ S1                           VDD ├── +5V  │
              ├─────── ┤ S2                           VEE ├── GND  │
              └─────── ┤ S3                           VSS ├── GND  │
                       │ INH ──── GND                               │
                       │                                            │
  R_BIAS ──────────────┤ A1                                         │
  G_BIAS ──────────────┤ B1                                         │
  B_BIAS ──────────────┤ C1                                         │
                       └───────────────────────────────────────────┘


  Bias network  ×3  (R shown; G and B identical on their own nets)

       +5V
        │
       R01 (10 kΩ)
        │
        ├──────────────────────────────── R_BIAS ──────────────► IC01 A1
        │                                    │
       R02 (1.5 kΩ)              C01  (+) ───┘───── (−) ────┬──── J03  R_IN
        │                           47 µF 16 V              │
       GND                                                  R03 (75 Ω)
                                                             │
                                                            GND


  VCC decoupling  (near IC01)

       +5V ──┬─────────────────────┐
             │                     │
            C04 (100 nF)          C05 (10 µF 16 V)  (+)
             │                     │
            GND                   GND


  Blanking detect  (SELECT driver)

               +5V
                │
               R10 (10 kΩ)
                │
   SELECT ──────┴──────────────────────────── Q01 (C)
                                               │
   J06  ──── R11 (10 kΩ) ──┬──── Q01 (B)     Q01  BC547 NPN
   FBLK_IN                  │                  │
                            R12 (10 kΩ)       Q01 (E) ──── GND
                             │
                            GND

   FBLK HIGH → Q01 sat → SELECT = LOW  → IC01 routes A1/B1/C1 (RGB)
   FBLK LOW  → Q01 off → R10 pulls SELECT HIGH → IC01 routes A0/B0/C0 (TV)
```

---
## Notation
- Resistors: leg **(a)** = pin1 (lower when vertical / left when horizontal), **(b)** = pin2
- Caps non-polarized: **(a)** and **(b)**
- Caps polarized: **(+)** = anode, **(-)** = cathode
- Transistor: **(B)** base, **(C)** collector, **(E)** emitter
- IC: function names per pin
- Connectors: pin number

## Net aliases
| Net name | Description |
|---|---|
| +5V | 5 V supply |
| GND | Ground |
| R_BIAS | R-channel DC bias node (~0.65 V) |
| G_BIAS | G-channel DC bias node |
| B_BIAS | B-channel DC bias node |
| R_EXT | R-channel signal output (after C_couple + term) |
| G_EXT | G-channel signal output |
| B_EXT | B-channel signal output |
| R_OUT | R output to CN701 / IC01 A pin |
| G_OUT | G output to CN701 / IC01 B pin |
| B_OUT | B output to CN701 / IC01 C pin |
| R_TV | R TV input → IC01 A0 |
| G_TV | G TV input → IC01 B0 |
| B_TV | B TV input → IC01 C0 |
| SELECT | Mux control (LOW=RGB, HIGH=TV) — driven by Q01 collector |
| FBLK_IN | Fast blanking input (SCART pin 16 equivalent) |

---

## IC01 — 74HCT4053 (triple 2:1 analog mux)

| Pin | Net |
|---|---|
| A (R out) | R_OUT |
| B (G out) | G_OUT |
| C (B out) | B_OUT |
| A0 (R TV in) | R_TV |
| B0 (G TV in) | G_TV |
| C0 (B TV in) | B_TV |
| A1 (R RGB in) | R_BIAS |
| B1 (G RGB in) | G_BIAS |
| C1 (B RGB in) | B_BIAS |
| S1 (select ch A) | SELECT |
| S2 (select ch B) | SELECT |
| S3 (select ch C) | SELECT |
| INH (inhibit) | GND |
| VDD (supply) | +5V |
| VEE (neg supply) | GND |
| VSS (ground) | GND |

---

## R channel bias network

| Ref | Value | Pin | Net | Note |
|---|---|---|---|---|
| R01 | 10 kΩ | (a) | +5V | pull-up to bias |
| R01 | 10 kΩ | (b) | R_BIAS | |
| R02 | 1.5 kΩ | (a) | R_BIAS | pull-down |
| R02 | 1.5 kΩ | (b) | GND | |
| C01 | 47 µF 16 V | (+) | R_BIAS | AC coupling cap |
| C01 | 47 µF 16 V | (-) | R_EXT | |
| R03 | 75 Ω | (a) | R_EXT | 75 Ω termination |
| R03 | 75 Ω | (b) | GND | |

## G channel bias network

| Ref | Value | Pin | Net | Note |
|---|---|---|---|---|
| R04 | 10 kΩ | (a) | +5V | |
| R04 | 10 kΩ | (b) | G_BIAS | |
| R05 | 1.5 kΩ | (a) | G_BIAS | |
| R05 | 1.5 kΩ | (b) | GND | |
| C02 | 47 µF 16 V | (+) | G_BIAS | |
| C02 | 47 µF 16 V | (-) | G_EXT | |
| R06 | 75 Ω | (a) | G_EXT | |
| R06 | 75 Ω | (b) | GND | |

## B channel bias network

| Ref | Value | Pin | Net | Note |
|---|---|---|---|---|
| R07 | 10 kΩ | (a) | +5V | |
| R07 | 10 kΩ | (b) | B_BIAS | |
| R08 | 1.5 kΩ | (a) | B_BIAS | |
| R08 | 1.5 kΩ | (b) | GND | |
| C03 | 47 µF 16 V | (+) | B_BIAS | |
| C03 | 47 µF 16 V | (-) | B_EXT | |
| R09 | 75 Ω | (a) | B_EXT | |
| R09 | 75 Ω | (b) | GND | |

---

## VCC decoupling

| Ref | Value | Pin | Net | Note |
|---|---|---|---|---|
| C04 | 100 nF | (a) | +5V | bypass cap near IC01 |
| C04 | 100 nF | (b) | GND | |
| C05 | 10 µF 16 V | (+) | +5V | bulk bypass |
| C05 | 10 µF 16 V | (-) | GND | |

---

## Q01 — BC547 NPN (blanking detect / SELECT driver)

| Pin | Net | Note |
|---|---|---|
| (B) base | Q01_B | driven via R11 from FBLK_IN; R12 pulls down |
| (C) collector | SELECT | open-collector → SELECT; R10 pulls to +5V |
| (E) emitter | GND | |

| Ref | Value | Pin | Net | Note |
|---|---|---|---|---|
| R10 | 10 kΩ | (a) | GND | collector pull-down to GND |
| R10 | 10 kΩ | (b) | SELECT | |
| R11 | 10 kΩ | (a) | FBLK_IN | base series resistor |
| R11 | 10 kΩ | (b) | Q01_B | |
| R12 | 10 kΩ | (a) | Q01_B | base pull-down |
| R12 | 10 kΩ | (b) | GND | |

> Q01 logic: FBLK_IN HIGH → Q01 saturates → SELECT = LOW → IC01 routes RGB inputs.
> FBLK_IN LOW (or open) → Q01 off → R10 pulls SELECT HIGH → IC01 routes TV inputs.

---

## Connectors

### J01 — CN004 TV input (3-pin)
| Pin | Net |
|---|---|
| 1 | R_TV |
| 2 | G_TV |
| 3 | B_TV |

### J02 — CN701 output to C-board (3-pin)
| Pin | Net |
|---|---|
| 1 | R_OUT |
| 2 | G_OUT |
| 3 | B_OUT |

### J03 — R RGB input (1-pin)
| Pin | Net |
|---|---|
| 1 | R_EXT |

### J04 — G RGB input (1-pin)
| Pin | Net |
|---|---|
| 1 | G_EXT |

### J05 — B RGB input (1-pin)
| Pin | Net |
|---|---|
| 1 | B_EXT |

### J06 — FBLK blanking input (1-pin)
| Pin | Net |
|---|---|
| 1 | FBLK_IN |
