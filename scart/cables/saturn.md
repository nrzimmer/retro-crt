# Cabo SCART RGB — Sega Saturn
---

## Conector AV — mini-DIN 10 pinos

Conector raro — extremamente difícil de encontrar avulso.

| Pin | Sinal |
|-----|-------|
| 1 | CSync |
| 2 | Audio L |
| 3 | Audio R |
| 4 | +5V |
| 5 | Red |
| 6 | Green |
| 7 | Blue |
| 8 | CVBS |
| 9 | Luma (Y) |
| 10 | Chroma (C) |

IC de vídeo: CXA1645 com resistor 75Ω + cap de acoplamento de saída (interno).

---

## Fiação Saturn → SCART

```
Saturn AV                Componentes              SCART
─────────                ───────────              ─────
Pin 5  (R)  ─────────────────────────────────►  Pin 15 (Red In)
Pin 6  (G)  ─────────────────────────────────►  Pin 11 (Green In)
Pin 7  (B)  ─────────────────────────────────►  Pin 7  (Blue In)
Pin 1  (CSync) ─── R_s (470Ω) ─── C_s (220µF) ► Pin 20 (Sync In)
Pin 4  (+5V) ── R1 (820Ω) ─┬─ R2 (1kΩ) ─ GND ► Pin 16 (Blanking)
Pin 2  (Audio L) ────────────────────────────►  Pin 6  (Audio In L)
Pin 3  (Audio R) ────────────────────────────►  Pin 2  (Audio In R)
GND ─────────────────────────────────────────►  Pins GND
```

---

## ⚠️ Componentes obrigatórios na linha de sync

**Saturn Model 2 tem problema conhecido:** sem esses componentes aparecem artefatos horizontais graves na imagem.

| Ref | Valor | Função |
|-----|-------|--------|
| R_s | 470Ω | Proteção / atenuação da linha csync |
| C_s | 220µF | Acoplamento AC — remove DC do sync |

Polaridade do cap: `+` para o console, `−` para o SCART.

Cabos sem esses componentes **não funcionam corretamente** no Saturn Model 2.

---

## Referências

- [Sega Saturn — RetroRGB](https://retrorgb.com/saturn.html)
- [Game Console SCART Diagrams — arcadecontrols mirror](https://mirrors.arcadecontrols.com/eviltim/eviltim/gamescart/gamescart.htm)
