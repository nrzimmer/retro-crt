# SCART — Padrão Euro (IEC 60807-9 / BS EN 50049-1)

## Pinagem completa (conector fêmea, vista frontal)

```
         ┌─────────────────────────────────────────┐
         │  1   3   5   7   9  11  13  15  17  19  21 │
         │   2   4   6   8  10  12  14  16  18  20    │
         └─────────────────────────────────────────┘
```

| Pin | Sinal | Direção (TV) | Nível | Impedância |
|-----|-------|--------------|-------|------------|
| 1 | Audio Out R | saída | 0.5 Vrms | <1kΩ |
| 2 | Audio In R | entrada | 0.5 Vrms | >10kΩ |
| 3 | Audio Out L + Mono | saída | 0.5 Vrms | <1kΩ |
| 4 | Audio GND | — | — | — |
| 5 | Blue GND | — | — | — |
| 6 | Audio In L + Mono | entrada | 0.5 Vrms | >10kΩ |
| 7 | **Blue In** | entrada | 0.7 Vpp | 75Ω |
| 8 | Switch / Widescreen | — | 0V=4:3, 12V=16:9 | — |
| 9 | Green GND | — | — | — |
| 10 | Clock Out (legado) | — | — | — |
| 11 | **Green In** | entrada | 0.7 Vpp | 75Ω |
| 12 | Data Out (legado) | — | — | — |
| 13 | Red GND | — | — | — |
| 14 | Data GND | — | — | — |
| 15 | **Red In** | entrada | 0.7 Vpp | 75Ω |
| 16 | **Fast Blanking** | entrada | 1–3V=RGB / 0–0.4V=composto | 75Ω |
| 17 | Video / Luma GND | — | — | — |
| 18 | Blanking GND | — | — | — |
| 19 | Composite Video Out | saída | 1 Vpp | 75Ω |
| 20 | **Composite Video In / Sync** | entrada | 1 Vpp | 75Ω |
| 21 | Shield / Chassis GND | — | — | — |

## Modos de operação

| Pin 16 (Blanking) | Pin 20 (sync) | Modo |
|-------------------|---------------|------|
| 0–0.4V (ou aberto) | composite video | composite |
| 1–3V | csync ou composite | **RGB** ← usar este |

## Fast Blanking — como gerar

Fonte típica dos consoles é 5V (de pino de alimentação do conector AV). Precisa reduzir para 1–3V:

**Divisor resistivo simples:**
```
+5V ──┬── R1 (820Ω) ──┬── SCART pin 16
      │               │
      │              R2 (1kΩ) ── GND   → ~2.6V ✓
```

**Ou via pino de controle do console (quando disponível):**
Alguns consoles já fornecem sinal de blanking correto — verificar pinout específico.

## Sync — opções por ordem de preferência

1. **csync** — sync composto dedicado, melhor opção
2. **luma** (pino Y do S-Video) — sync em cima do sinal de luminância
3. **composite video** — sync extraído do sinal composto (aceito pela maioria dos CRTs)

> Para displays que exigem csync limpo (PVMs, scalers): usar sync stripper (LM1881 ou 74HC04).

## Aterramento — regra

Conectar **todos** os GNDs de vídeo ao aterramento comum do cabo:
- Pins 4 (audio), 5 (B), 9 (G), 13 (R), 17 (video), 18 (blanking), 21 (shield)

Malha do cabo blindado → pin 21 (shield), conectada em **uma ponta apenas** para evitar ground loop.

## Referências

- Fonte: [SCART pinout — PinoutGuide](https://pinoutguide.com/Audio-Video-Hardware/Scart_pinout.shtml)
- Fonte: [SCART specs — sector.sunthar.com](https://sector.sunthar.com/guides/crt-rgb-mod/scart.html)
- Fonte: [RGB Blanking — martin.hinner.info](http://martin.hinner.info/vga/scart.html)
