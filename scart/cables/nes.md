# Cabo SCART RGB — NES / Famicom


> ⚠️ NES não tem saída RGB nativa. Mod obrigatório antes de usar este cabo.  
> Ver [`consoles/nes/README.md`](../../consoles/nes/README.md) para opções de mod (NESRGB, PPU-LITE).

---

## NESRGB — conector e cabo

O NESRGB instala um conector **Multi-out estilo SNES** no NES. Após instalado:

**Cabo idêntico ao SNES NTSC** — com caps 220µF nas linhas RGB.

```
Multi-out NESRGB         Componentes              SCART
────────────────         ───────────              ─────
R  ──── C+ 220µF C- ─────────────────────────►  Pin 15 (Red In)
G  ──── C+ 220µF C- ─────────────────────────►  Pin 11 (Green In)
B  ──── C+ 220µF C- ─────────────────────────►  Pin 7  (Blue In)
CSync ───────────────────────────────────────►  Pin 20 (Sync In)
+5V ── 820Ω ─┬─ 1kΩ ─ GND ──────────────────►  Pin 16 (Blanking)
Audio L ─────────────────────────────────────►  Pin 6
Audio R ─────────────────────────────────────►  Pin 2
GND ─────────────────────────────────────────►  Pins GND
```

---

## ⚠️ NESRGB — nível de sync (jumper J8)

O NESRGB tem jumper J8 para configurar o nível do csync:

| J8 | Modo csync | Usar com |
|----|-----------|---------|
| Aberto | **75Ω** — nível correto para video | Cabo sem resistor no sync |
| Fechado | **TTL** — nível alto (~5V) | Cabo SNES padrão com resistor no sync |

> Se usar cabo SNES padrão comprado pronto: verificar se tem resistor na linha de sync.  
> Configurar J8 conforme o cabo. Maioria dos cabos NTSC usa csync direto → J8 aberto (75Ω).

---

## Diferenças em relação ao SNES

| Aspecto | SNES | NES (com NESRGB) |
|---------|------|-----------------|
| RGB nativo | ✓ | ✗ — mod obrigatório |
| Conector MultiAV | Original | Instalado pelo mod |
| Cabo RGB SCART | Mesmo | **Mesmo cabo SNES NTSC** |
| Caps 220µF | ✓ no cabo | ✓ no cabo (igual) |
| Jumper de sync | — | J8 define nível csync |
| Cabo PAL SNES | ✗ não usar | ✗ não usar — resistores 75Ω interferem |

---

## Resoluções — compatibilidade KV-21FS140

| Modo | Freq H | Compatível |
|------|--------|-----------|
| 240p | 15.7 kHz | ✓ |

NES só opera em 240p — **100% compatível**.

---

## Referências

- [NES RGB — RetroRGB](https://retrorgb.com/nesrgb.html)
- [NESRGB SNES SCART cable — shmups.system11.org](https://shmups.system11.org/viewtopic.php?t=69121)
- [SNES Multi-Out for NESRGB — Humble Bazooka](https://www.humblebazooka.com/products/snes-style-multi-out-connector-for-nesrgb/)
