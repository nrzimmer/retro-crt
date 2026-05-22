# Cabos SCART RGB

Documentação para construção de cabos SCART RGB para consoles retro.  
Alvo principal: mod RGB no KV-21FS140 (`../tv/mod_rgb/rgb_mod.md`).

## Índice

| Arquivo | Conteúdo |
|---------|----------|
| [standard.md](standard.md) | Padrão SCART 21 pinos — referência |
| [switch.md](switch.md) | Switch SCART: topologias, chips, projetos OSS |
| [fornecedores.md](fornecedores.md) | Onde comprar conectores e componentes |

### Cabos por console (`cables/`)

| Arquivo | Console | Conector | Status |
|---------|---------|----------|--------|
| [cables/nes.md](cables/nes.md) | NES / Famicom | MultiAV 12P (via NESRGB mod) | documentado — requer mod RGB |
| [cables/snes.md](cables/snes.md) | Super Nintendo / Super Famicom | MultiAV 12P card-edge | documentado |
| [cables/megadrive.md](cables/megadrive.md) | Sega Mega Drive 1 e 2 | DIN-8U / mini-DIN 9 | documentado |
| [cables/ps1.md](cables/ps1.md) | PlayStation 1 / PSone | Proprietário 12P | documentado |
| [cables/ps2.md](cables/ps2.md) | PlayStation 2 | Proprietário 12P (= PS1) | documentado |
| [cables/n64.md](cables/n64.md) | Nintendo 64 | MultiAV 12P (= SNES) | documentado — requer mod RGB |
| [cables/saturn.md](cables/saturn.md) | Sega Saturn | mini-DIN 10 | documentado |
| [cables/neogeo.md](cables/neogeo.md) | SNK Neo Geo AES/MVS | DIN-8C | documentado |

### Mods de consoles (`../consoles/`)

| Arquivo | Console | Conteúdo |
|---------|---------|----------|
| [../consoles/nes/](../consoles/nes/) | NES / Famicom | NESRGB, PPU-LITE, mods de áudio |
| [../consoles/n64/](../consoles/n64/) | Nintendo 64 | THS7316, opções de mod RGB |

## Componentes comuns a todos os cabos

| Componente | Valor | Função |
|-----------|-------|--------|
| R_blank_top | 820Ω | Divisor blanking (SCART pin 16) |
| R_blank_bot | 1kΩ | Divisor blanking → ~2.6V |

## Componentes específicos por console

| Console | Componente extra | Motivo |
|---------|-----------------|--------|
| SNES NTSC | 220µF ×3 nas linhas RGB | DC offset ~1V na saída |
| SNES PAL | 75Ω ×3 para GND nas linhas RGB | Redução de contraste |
| NES (NESRGB) | 220µF ×3 nas linhas RGB | Mesmo DC offset do SNES |
| N64 (após mod) | 220µF ×3 nas linhas RGB | Mesmo DC offset do SNES |
| PS1 | 220µF ×3 nas linhas RGB | PS1 não tem caps internamente |
| PS2 | Nenhum extra | PS2 já tem 220µF internamente |
| Saturn | 470Ω + 220µF na linha csync | Artefatos no Model 2 sem eles |

## Avisos críticos

> ⚠️ **SNES PAL:** Pin 3 = +12V. Cabo NTSC em SNES PAL danifica equipamento.  
> ⚠️ **NES:** sem mod NESRGB, zero RGB — nem composite RGB.  
> ⚠️ **N64 NTSC:** sem mod RGB interno, cabo SCART RGB não funciona.  
> ⚠️ **PS1 ≠ PS2:** cabos não são intercambiáveis — caps nos canais RGB diferem.  
> ⚠️ **PS2 + 480p:** muitos jogos forçam 480p (31kHz) — incompatível com KV-21FS140.
