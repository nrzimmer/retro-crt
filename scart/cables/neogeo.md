# Cabo SCART RGB — SNK Neo Geo AES / MVS
---

## Conector — DIN-8 "C" fêmea

| Pin | Sinal |
|-----|-------|
| 1 | Audio mono |
| 2 | GND |
| 3 | CVBS |
| 4 | +5V |
| 5 | Green |
| 6 | Red |
| 7 | CSync |
| 8 | Blue |

IC de vídeo: CXA1145 / MB3514 — RGB sai com resistor 75Ω + cap de acoplamento internos.

---

## Fiação Neo Geo → SCART

```
DIN-8 "C"                Componentes              SCART
─────────                ───────────              ─────
Pin 6  (R)  ─────────────────────────────────►  Pin 15 (Red In)
Pin 5  (G)  ─────────────────────────────────►  Pin 11 (Green In)
Pin 8  (B)  ─────────────────────────────────►  Pin 7  (Blue In)
Pin 7  (CSync) ──────────────────────────────►  Pin 20 (Sync In)
Pin 4  (+5V) ── R1 (820Ω) ─┬─ R2 (1kΩ) ─ GND ► Pin 16 (Blanking)
Pin 1  (Audio mono) ────────────────────────►  Pin 6 + Pin 2 (L+R)
Pin 2  (GND) ────────────────────────────────►  Pins GND
```

Neo Geo já tem resistor 75Ω + cap de acoplamento internos — cabo simples funciona.

---

## Referências

- [Game Console SCART Diagrams — arcadecontrols mirror](https://mirrors.arcadecontrols.com/eviltim/eviltim/gamescart/gamescart.htm)
