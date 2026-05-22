# Service Mode — Todas as Categorias de Ajuste

**Chassis:** BX1S | **Modelo:** KV-21FS140 | **IC:** TDA12009H | **NVM:** CAT24WC16WI

## Acesso ao service mode

```
[DISPLAY] → [5] → [VOL+] → [POWER]  (em standby)
```

- **Navegar item:** [1] / [4]
- **Ajustar valor:** [3] / [6]
- **Gravar:** [MUTING] → [−]
- **Cancelar:** [POWER] (standby) → [POWER] novamente
- **Inicialização de dados:** 7, 8, Display, 2, 5 (usar com cautela)

---

## GEOM — Geometria

Parâmetros de deflexão H/V via IC001. Veja arquivo `geom_service_params.md` para detalhes completos.

| Item# | Nome | Range | Init | Função resumida |
|---|---|---|---|---|
| 000 | HPOS | 0–63 | 31 | Posição horizontal |
| 001 | HPAR | 0–63 | 31 | Paralelogramo H |
| 002 | HBOW | 0–63 | 31 | Curvatura H |
| 003 | VLIN | 0–63 | 31 | Linearidade vertical |
| 004 | VSCR | 0–63 | 31 | Scroll vertical |
| 005 | HSIZ | 0–63 | 31 | Largura EW |
| 006 | EWPW | 0–63 | 31 | Parábola EW (pincushion principal) |
| 007 | UCOP | 0–63 | 17 | Pincushion canto superior |
| 008 | LCOP | 0–63 | 17 | Pincushion canto inferior |
| 009 | EWTZ | 0–63 | 31 | Correção trapezoidal |
| 010 | VSLP | 0–63 | 31 | Inclinação vertical |
| 011 | VSIZ | 0–63 | 15 | Amplitude vertical (altura) |
| 012 | SCOR | 0–63 | 14 | S-Correction |
| 013 | VPOS | 0–63 | 31 | Posição vertical |
| 014 | VZOM | 0–63 | 31 | Zoom vertical |
| 015 | HBL | 0–1 | 1 | RGB Blanking Mode |
| 016 | WBF | 0–15 | 7 | Wide Blanking timing (frente) |
| 017 | WBR | 0–15 | 7/14 | Wide Blanking timing (retorno) |
| 018 | SBL | 0–1 | 0 | Service Blanking |
| 019 | COPY | 0–1 | 0 | Copia dados GEO para todos os modos NVM |

---

## WHBL — White Balance (Balanço de Branco)

| Item# | Nome | Range | Init | Função |
|---|---|---|---|---|
| 000 | BKOR | 0–63 | 31 | Black Level Offset R (ou B quando OFB=01) |
| 001 | BKOG | 0–63 | 31 | Black Level Offset G |
| 002 | RDRV | 0–63 | 37 | White Point R (ganho R no branco) |
| 003 | GDRV | 0–63 | 37 | White Point G |
| 004 | BDRV | 0–63 | 37 | White Point B |
| 005 | LPG | 0–1 | 0 | RGB Gain Preset |
| 006 | PGR | 0–127 | 40 | Preset Gain R |
| 007 | PGG | 0–127 | 40 | Preset Gain G |
| 008 | PGB | 0–127 | 40 | Preset Gain B |
| 009 | GNOF | 0–15 | — | Preset Gain Offset |
| 010 | SBRT | 0–63 | 31 | Sub-Brightness |
| 011 | SBRO | 0–3 | 0 | Sub-Brightness Offset (Intelligent Pic) |
| 012 | EGL | — | — | Enable Gain Loop no sistema CCC |
| 013 | SGL | — | — | Selection of High Current no sistema CCC |
| 014 | AKB | 0–1 | 0 | Black Current Stabilization (AKB on/off) |
| 015 | CBS | 0–1 | 0 | Control Sequence Beam Current Limiting |
| 016 | RGBB | 0–3 | 0 | RGB Blanking |
| 017 | BLBG | 0–1 | 0 | Blanking of Blue & Green Output |
| 018 | OFB | 0–1 | 1 | Black Level Offset Blue |
| 019 | NSBR | 0–15 | 0 | Non Standard Brightness Offset |
| 020 | WBP | 0–3 | — | Color Temp Setting (0=High, 1=Normal, 2/3=Low) |

---

## SADJ — Sub-Adjust (Ajuste de Imagem)

| Item# | Nome | Range | Init | Função |
|---|---|---|---|---|
| 000 | PMAX | 0–63 | 63 | Picture Maximum |
| 001 | SHUE | 0–15 | 7 | Sub-Hue |
| 002 | SSHP | 0–63 | 15 | Sub-Sharpness |
| 003 | SSHO | 0–7 | 0 | Sub-Sharpness Offset (Intelligent Pic) |
| 004 | SCOL | 0–63 | 31 | Sub-Color |
| 005 | SCOO | 0–3 | 0 | Sub-Color Offset (Intelligent Pic) |
| 006 | PIC | 0–127 | 42/31 | Picture Control |
| 007 | COL | 0–127 | 40/31 | Color Control |
| 008 | BRT | 0–127 | 40/31 | Brightness Control |
| 009 | HUE | 0–127 | 50/31 | Hue Control |
| 010 | SHP | 0–127 | 50/31 | Sharpness Control |

---

## YC — Chroma / Luma Processing

Parâmetros de processamento de crominância e luminância. Items variam por sistema (PAL/NTSC/SECAM).

---

## SYNC — Sincronismo

Ajustes de sincronismo H/V — frequência, fase, AFC.

---

## PICT — Picture (Imagem)

Parâmetros de processamento de imagem (contraste, brilho, gama, etc.).

---

## SW — Software Options / Switches

Bits de opção de software para habilitar/desabilitar funções por mercado.

---

## VIF — Video IF

Parâmetros do circuito IF de vídeo — ganho AGC, filtros.

---

## VM — Velocity Modulation

| Função | Descrição |
|---|---|
| VM | Controla a modulação de velocidade — nitidez das bordas via bobina VM no yoke |

IC001 pin65 (VM) → bobina VM no deflection yoke.

---

## SDEM — Sound Demodulator

| Item# | Nome | Range | Init | Função |
|---|---|---|---|---|
| 000 | FMWS | 0–3 | 0 | Window Selection for FM Demodulator |
| 001 | QSS | 0–1 | 1 | Quasi Split Sound Amplifier Mode |
| 002 | BPB | 0–1 | 0 | Bypass Sound Bandpass Filter |
| 003 | AMLO | 0–1 | 0 | Audio Output Signal for AM Sound |
| 004 | HPVC | 0–1 | 0 | Head Phone Volume Control |

---

## TXT — Teletext

| Item# | Nome | Range | Init | Função |
|---|---|---|---|---|
| 000 | TXV | 0–63 | 39 | Teletext Vertical Position (Philips) |
| 001 | THD | 0–127 | 10 | Teletext H-sync Active Edge Shift |
| 002 | TBR | 0–31 | 15 | Teletext RGB Brightness |
| 003 | ACQ | — | — | Teletext Acquisition (Auto=0, PAL=1) |

---

## SDSP — Sound Display / DSP de Áudio

| Item# | Nome | Range | Init | Função |
|---|---|---|---|---|
| 000 | BBL | 0–15 | — | BBE Contour |
| 001 | BBH | 0–15 | 0 | BBE Process |
| 002 | BBLW | 0–15 | 6 | BBE Contour Offset |
| 003 | SVOF | 0–15 | — | Surround/Effect Mode Volume Offset |
| 004 | LAD | 0–31 | 5 | Decoder Level Adjust |
| 005 | LAM | 0–31 | 5 | Mono Level Adjust |
| 006 | LAN | 0–31 | 22 | Nicam Level Adjust |
| 007 | LAS | 0–31 | 5 | SAP Level Adjust |
| 008 | LAA | 0–31 | — | ADC Level Adjust |
| 009–010 | SEF | — | — | Incredible Mono/Stereo Effect |
| 011 | TRE | 0–15 | 21 | Main Treble Offset |
| 012 | EQ1 | 0–15 | 20 | Equalizer Main 100Hz Offset |
| 013 | EQ2 | 0–15 | 3 | Equalizer Main 300Hz Offset |
| 014 | EQ3 | 0–15 | 0 | Equalizer Main 1000Hz Offset |
| 015 | EQ4 | 0–15 | 0 | Equalizer Main 3000Hz Offset |
| 016 | EQ5 | 0–15 | 0 | Equalizer Main 8000Hz Offset |
| 017 | BFCT | 0–7 | 0 | DBE, DUB and BBE Control |
| 018 | SCEN | 0–15 | 4 | SRS3D Center Control |
| 019 | SSPA | 0–15 | 1 | SRS3D Space Control |
| 020 | BBHW | 0–15 | 0 | BBE Process Offset in WOW mode |
| 021 | STRE | 0–7 | 1 | Treble Offset for Surround mode |
| 022 | BBHT | 0–15 | 0 | BBE Offset in TV mode |
| 023 | TTRE | 0–7 | 2 | Treble Offset in TV mode |
| 024 | VBAS | 0–3 | 0 | Bass Offset by user volume |
| 025 | VTRE | 0–3 | 0 | Treble Offset by user volume |
| 026 | TBAS | 0–7 | 0 | Bass Offset for TV |
| 010 | BAS | 0–15 | 4 | Main Bass Offset |

---

## SDEC — Sound Decoder

Parâmetros de decodificação de som (NICAM, BTSC, A2, etc.) — ajuste por sistema de transmissão.

---

## SDKC — Sound DKC

Parâmetros DKC (detecção de sistema de som).

---

## PIP — Picture in Picture

Parâmetros de PIP (se disponível no modelo).

---

## HTV — Hotel TV / Hospitality

Configurações para modo hotel (se habilitado via SW).

---

## OPTM — Options Main

Bits de opções principais do sistema.

---

## OPUS / OPVP / OPTB — Options Sub

Opções adicionais de sistema, vídeo e áudio.

### OPB1–OPB6 — Option Bytes

Bytes de opção que definem as características do modelo por destino de mercado (Brasil, Europa, EUA, Japão, etc.). Cada bit controla uma funcionalidade específica.

---

## Diferenças entre variantes — valores de configuração

### Parâmetros que diferem por destino

| Categoria | Item | Nome | rev_brazil (SCC-S80A-A) | rev_s79aa (SCC-S79A-A/B) |
|-----------|------|------|------------------------|--------------------------|
| SYNC | 006 | FORF | 00 (Brazil) | 01 (Latin) |
| OPTM | 007 | LANG | 02 (Português) | 01 (Latin) |
| OPUS | 001 | SPCH | 05 (Brazil) | 06 (Latin) |

### Option Bytes — valores por variante

| Byte | rev_brazil | rev_s79aa | Diferença |
|------|-----------|-----------|-----------|
| OPB1 | 72 | 72 | Igual |
| OPB2 | 43 | 43 | **Interpretação diferente:** Brazil = PAL/NTSC multi; S79AA = NTSC only |
| OPB3 | 4 | 4 | Igual (US Stereo habilitado) |
| OPB4 | 0 | 0 | Igual |
| OPB5 | 3 | 3 | Igual |
| OPB6 | 5 | 5 | Igual |

> OPB2 DEC=43 representa bits diferentes nos dois modelos porque o mapa de bits de sistema de cor difere entre versões de firmware Brazil vs Latin. O valor decimal é o mesmo mas o comportamento efetivo é diferente — Brazil aceita PAL; S79AA só decodifica NTSC.

## Notas gerais

- Dados após "/" na tabela oficial referem-se a modelos NTSC. Sem "/" = comum a todos.
- Itens marcados `*` ou `**`: consultar tabela na página 25 do manual.
- Itens sombreados na tabela oficial: sem dados para este modelo.
- Inicializar NVM (COPY / inicialização geral) exige reajuste completo de todos os parâmetros.
- Versão firmware: NTSC v6.16N | Release: SUS01 v0.69U
