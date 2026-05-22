# Cabo SCART RGB — Sega Mega Drive / Genesis
---

## Mega Drive 1 — Conector DIN-8 fêmea "U"

| Pin | Sinal |
|-----|-------|
| 1 | Audio (mono) |
| 2 | GND |
| 3 | CVBS (composite) |
| 4 | +5V |
| 5 | Green |
| 6 | Red |
| 7 | CSync |
| 8 | Blue |

IC de vídeo: Sony CXA1145 — RGB sai direto do chip (sem resistor interno).

### Fiação MD1 → SCART

```
DIN-8                    Componentes              SCART
──────                   ───────────              ─────
Pin 6  (R)  ─────────────────────────────────►  Pin 15 (Red In)
Pin 5  (G)  ─────────────────────────────────►  Pin 11 (Green In)
Pin 8  (B)  ─────────────────────────────────►  Pin 7  (Blue In)
Pin 7  (CSync) ──────────────────────────────►  Pin 20 (Sync In)
Pin 4  (+5V) ── R1 (820Ω) ─┬─ R2 (1kΩ) ─ GND ► Pin 16 (Blanking ~2.6V)
Pin 1  (Audio mono) ────────────────────────►  Pin 6 + Pin 2 (L+R)
Pin 2  (GND) ────────────────────────────────►  Pins GND
```

> MD1 só tem áudio mono pelo DIN-8. Stereo: capturar do jack de fone (3.5mm frontal) ou [fazer mod stereo interno](../../consoles/megadrive/).

---

## Mega Drive 2 — Conector mini-DIN 9

| Pin | Sinal |
|-----|-------|
| 1 | Blue |
| 2 | +5V |
| 3 | Green |
| 4 | CVBS |
| 5 | CSync |
| 6 | Audio mono |
| 7 | Red |
| 8 | Audio L |
| 9 | Audio R |
| Shield | GND |

IC de vídeo: CXA1145 / CXA1645 / KA2195 / MB3514 — RGB direto do chip.

### Fiação MD2 → SCART

```
mini-DIN 9               Componentes              SCART
──────────               ───────────              ─────
Pin 7  (R)  ─────────────────────────────────►  Pin 15 (Red In)
Pin 3  (G)  ─────────────────────────────────►  Pin 11 (Green In)
Pin 1  (B)  ─────────────────────────────────►  Pin 7  (Blue In)
Pin 5  (CSync) ──────────────────────────────►  Pin 20 (Sync In)
Pin 2  (+5V) ── R1 (820Ω) ─┬─ R2 (1kΩ) ─ GND ► Pin 16 (Blanking)
Pin 8  (Audio L) ────────────────────────────►  Pin 6  (Audio In L)
Pin 9  (Audio R) ────────────────────────────►  Pin 2  (Audio In R)
Shield (GND) ────────────────────────────────►  Pins GND
```

---

## Componentes necessários

| Ref | Valor | Função |
|-----|-------|--------|
| R1 | 820Ω | Divisor blanking |
| R2 | 1kΩ | Divisor blanking → ~2.6V |

Mega Drive **não tem DC offset** nas linhas RGB — caps de acoplamento não necessários (ao contrário do SNES).

---

## Compatibilidade com o mod KV-21FS140

Mesmo esquema do SNES — sync pelo AV2 frontal, RGB pelo mod board. Sem caps extras no cabo se usar o mod board que já tem acoplamento. Ver [`tv/mod_rgb/rgb_mod.md`](../../tv/mod_rgb/rgb_mod.md).

---

## Referências

- [Genesis RGB Cables — RetroRGB](https://retrorgb.com/genesisrgbcables.html)
- [Game Console SCART Diagrams — arcadecontrols mirror](https://mirrors.arcadecontrols.com/eviltim/eviltim/gamescart/gamescart.htm)
