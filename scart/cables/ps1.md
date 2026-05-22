# Cabo SCART RGB — PlayStation 1
---

## Conector AV proprietário PS1

| Pin | Sinal |
|-----|-------|
| 1 | GND |
| 2 | Audio R |
| 3 | GND |
| 4 | Audio L |
| 5 | Luma (Y) |
| 6 | CSync |
| 7 | Chroma (C) |
| 8 | GND |
| 9 | Blue |
| 10 | +5V |
| 11 | Red |
| 12 | Green |

IC de vídeo: CXA1645 + resistor 75Ω de saída (interno).

---

## Fiação PS1 → SCART

```
PS1 AV                   Componentes              SCART
──────                   ───────────              ─────
Pin 11 (R) ──────────────────────────────────►  Pin 15 (Red In)
Pin 12 (G) ──────────────────────────────────►  Pin 11 (Green In)
Pin 9  (B) ──────────────────────────────────►  Pin 7  (Blue In)
Pin 6  (CSync) ──────────────────────────────►  Pin 20 (Sync In)
Pin 10 (+5V) ── R1 (820Ω) ─┬─ R2 (1kΩ) ─ GND ► Pin 16 (Blanking ~2.6V)
Pin 4  (Audio L) ────────────────────────────►  Pin 6  (Audio In L)
Pin 2  (Audio R) ────────────────────────────►  Pin 2  (Audio In R)
Pin 1,3,8 (GND) ─────────────────────────────►  Pins GND
```

PS1 **não tem DC offset** nas linhas RGB — caps de acoplamento não necessários.

---

## Sync — opções PS1

| Opção | Pino | Notas |
|-------|------|-------|
| CSync | Pin 6 | Melhor; limpo |
| Luma | Pin 5 | Alternativa |
| CVBS | (não disponível diretamente) | — |

**Nota:** PS1 não suporta componente direto; requer conversor ou cabo SCART RGB.

---

## Resoluções

| Modo | Frequência H | Compatibilidade KV-21FS140 |
|------|-------------|---------------------------|
| 240p | 15.7 kHz | ✓ |
| 480i | 15.7 kHz | ✓ |
| 480p (raro) | 31.5 kHz | ✗ (sem mod) |

Quase todos jogos PS1 usam 240p ou 480i — 100% compatível com o mod.

---

## Referências

- [PlayStation 1 — RetroRGB](https://retrorgb.com/playstation1.html)
- [Game Console SCART Diagrams — arcadecontrols mirror](https://mirrors.arcadecontrols.com/eviltim/eviltim/gamescart/gamescart.htm)
