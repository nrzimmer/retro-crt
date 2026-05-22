# KV-21FS140 Service Manual — Index (Edição LATIN NORTH/SOUTH)

**Modelo:** Sony Trinitron KV-21FS140  
**Chassis:** BX1S  
**Commander:** RM-YA005  
**Part No.:** 9-965-997-01 (Rev 1, 2/2006)  
**Destinos:** LATIN NORTH (SCC-S79A-A), LATIN SOUTH (SCC-S79B-A)

> Este manual cobre modelos **NTSC apenas** — sem suporte PAL/NTSC multi.  
> Comparar com `../rev_brazil/INDEX.md` para diferenças vs modelo Brazil.

---

## Sumário por Seção

### Páginas 1–3 — Capa e Índice

- Histórico de revisão, modelos/destinos/chassis, tabela de conteúdo completa
- Aviso de segurança: curto-circuitar anodo do tubo antes de remover

---

### Páginas 4–8 — Especificações e Diagnóstico

**Especificações (Página 4):**
- Sistema de TV: NTSC (American standard)
- Canais: VHF 2–13 / UHF 14–69 / CATV 1–125
- Antena: 75-ohm externa VHF/UHF
- Tubo: FD Trinitron — 21" diagonal (20" visível)
- Acessórios: Commander RM-YA005, 2× pilhas AA

**Avisos e Precauções (Página 5):**
- Transformador de isolação obrigatório durante serviço
- Chassis conectado diretamente à linha AC (live chassis)
- Componentes críticos marcados com ! — substituir apenas com part numbers Sony

**Verificação de Segurança (Página 6):**
- Verificar soldas, bridges, fios pressionados
- Teste de vazamento AC: máximo 0.5 mA
- Métodos de medição documentados

**Função Auto-diagnóstico (Páginas 7–8):**

| Flashes | Código | Causa provável |
|---------|--------|----------------|
| Sem energia | — | Cabo desligado ou fusível F600 queimado |
| 2x | OCP (2:0–2:255) | Q805 ou IC751 em curto |
| 4x | V-Protect/OVP (4:0–4:255) | +13V ausente ou IC804 defeituoso |
| 5x | IK/AKB (5:0–5:255) | IC1545 ou IC001 defeituoso; G2 mal ajustado |
| 8x | Power NG +5V (8:0–8:255) | IC604 ou IC602 defeituoso |

**Como acessar diagnóstico:**
- Entrar: `[DISPLAY] → [5] → [VOL-] → [POWER]` (em standby)
- ⚠️ **Diferente do Brasil:** este manual usa **VOL-** para diagnóstico e **VOL+** para service mode
- Limpar resultado: `[CH 8]`
- Sair: desligar TV

---

### Páginas 9–11 — Seção 1: Desmontagem

**Sequência:**
1. Tampa traseira — 7 parafusos (+BVTP 4×16)
2. Soltar A Board catch tab
3. Posição de serviço — desconectar CN200
4. Remoção do tubo de imagem (CRT)

**Remoção do CRT:**
- Descarregar anodo (tensão residual alta — atenção)
- Desconectar: Deflection Yoke, Neck Assy, DGC, strap de aterramento
- Remover: C Board, chassis, neck assembly, deflection yoke, bobina de degaussing
- Remover CRT com suportes de mola
- **ATENÇÃO:** Curto-circuitar anodo após remoção

---

### Páginas 12–15 — Seção 2: Ajustes Físicos (Setup Adjustments)

**Equipamentos necessários:**
- Gerador de padrões, degaussing, osciloscópio, multímetro digital, XCV Adjuster, Landing Checker, fonte DC

**Sequência obrigatória de ajuste:**
1. Beam Landing (purity)
2. Convergência
3. Focus
4. G2 (Screen)
5. White Balance

**2-1 Beam Landing:**
- Sinal verde, mover DY para trás, ajustar purity control
- Centro = verde, lados = vermelho/azul
- Avançar DY até tela inteira verde
- Verificar vermelho e azul; ajustar discos magnéticos nos cantos

**2-2 Convergência:**
- Estático vertical: ímã 4 polos — alinhar R, G, B no centro
- Estático horizontal: ímã 6 polos — alinhar azul com R/G
- Grosso: TLH (H-conv R/B), YCH (balanço Y), TLV (V-conv R/B), XCV (balanço X)
- Cantos: Piece A(90) Permaloy ou Convergence Correct Assy

**2-3 Focus:**
- Padrão monoscópio digital, modo DYNAMIC
- Ajustar VR de focus no centro; verificar anel magenta com padrão azul

**2-4 G2 (Screen):**
- Condição: Picture/Brightness STANDARD, TV em Video mode, WHBL 016 "RGBB" = 01
- Catodo R/G/B a 165 ±2 VDC
- Ajustar Screen VR no FBT até linha de varredura desaparecer
- Restaurar RGBB = 00

---

### Página 16 — Seção 3: Modo Serviço

**Entrada no Service Mode:**
`[DISPLAY] → [5] → [VOL+] → [POWER]` (em standby)

**Saída:** `[POWER]` → standby → `[POWER]` novamente

**Navegação:**
- `[1]/[4]` — selecionar item
- `[3]/[6]` — ajustar valor
- `[MUTING] → [−]` — gravar

**Display:** `categoria | nº item | nome | dado decimal | SERVICE | freq | canal`

---

### Páginas 17–30 — Tabelas de Ajuste (Service Mode Items)

| Categoria | Descrição |
|-----------|-----------|
| GEOM | Geometria (posição H/V, tamanho, correções EW) |
| WHBL | White Balance (offset preto R/G/B, drive branco, sub-brilho) |
| SADJ | Sub-ajustes (PMAX/contraste, hue, color, bright) |
| YC | Processamento Y/C (frequência peaking, delay, matriz) |
| SYNC | Sincronismo (modo sync, PLL, identificação vídeo) |
| PICT | Qualidade de imagem (cathode drive, comb filter, gamma, coring) |
| SW | Seleção de sinal (CVBS2, SVO, proteção flash) |
| VIF | FI de vídeo (offset demodulador, AGC, modo de busca) |
| VM | Velocity Modulation (delay, amplitude, modo) |
| SDEM | Demodulador FM (janela FM, QSS, filtro bandpass) |
| TXT | Teletext |
| SDSP | Display de som (BBE, surround, equalizer, treble, bass) |
| SDEC | Decoder de som (SAP, FM A2, NICAM, DCXO) |
| HTV | Home TV (volume máximo/inicial, standby, prog inicial) |
| OPTM | Opções (timer auto-off, OSD, mute sem sinal) |
| OPUS | Opções de sistema (stay-off, canal inicial, CC) |
| OPVP | Opções vídeo/processamento |
| OPTB | Option bytes OPB1–OPB6 |

**Dados variáveis por modelo:**

| Item | LATIN (S79AA) | Brazil (S80A) |
|------|---------------|---------------|
| SYNC/FORF | 01 | 00 |
| OPTM/LANG | 01 | 02 |
| OPUS/SPCH | 06 | 05 |

**Option Bytes — LATIN:**

| Byte | DEC | Diferença vs Brazil |
|------|-----|---------------------|
| OPB1 | 72 | Igual |
| OPB2 | 43 | Brazil = PAL/NTSC multi; LATIN = NTSC only |
| OPB3 | 4 | Igual (US Stereo) |
| OPB4 | 0 | Igual |
| OPB5 | 3 | Igual |
| OPB6 | 5 | Igual |

---

### Páginas 18–19 — Ajustes de Qualidade e Geometria

**P MAX / Contraste (SADJ 000):**
- NTSC 75% CB; PICTURE 100%, COLOR 0%, BRIGHTNESS 50%
- Osciloscópio no pino 4 (R Output) de CN004
- Alvo: **1.10 ±0.03 Vp-p** (NTSC 21" sem VM)

**Sub Color (SADJ 004):**
- NTSC: VB1=VB4 (diff ≤70mV)

**Sub Hue (SADJ 001):**
- NTSC 3.58 CB; ajustar VB1=VB2=VB3=VB4 (diff ≤80mV)

**Sub Bright (WHBL 010 SBRT):**
- RF mode, monoscópio NTSC, Brightness 50%, Picture MINIMUM
- Cutoff = 10 IRE; levemente iluminado = 20 IRE

**Geometria — 2 modos (NTSC apenas, sem PAL):**
1. NTSC 60Hz Normal
2. NTSC 60Hz Wide

**Items GEOM em ordem de ajuste:**
VPOS → VSIZ → HPOS → EWTZ → HSIZ → HBOW → EWPW → UCOP → LCOP → HPAR → SCOR → VLIN → VSCR

Alvos VSIZ: 11.5 (NTSC mono)  
Alvos HSIZ: 15.3 (NTSC mono)

---

### Páginas 35–46 — Seção 4: Diagramas

**Página 35 — Localização das Placas:**
- **A Board** — placa principal
- **C Board** — CRT neck board

**Página 36 — Diagrama de Blocos:**
- IC001 One-Chip central (System + Video + Audio)
- RF Amp/Tuner → VIF/SIF → Color Decoder → YUV → RGB Amp → CRT
- Audio Amp: AN5276T **ou** AN17804A (alternativas documentadas neste manual)
- Power: AC → SMPS → +B(135V), 30V, 11V, 9V, 5V, 3.3V, 1.8V

**Páginas 37–44 — Esquemáticos A Board (6 blocos):**

| Bloco | Função |
|-------|--------|
| Block 001 | IC001, NVM IC003, LEDs, conectores |
| Block 002 | Audio Amp (AN5276T/AN17804A), mute, fonte 9V |
| Block 003 | SMPS: T600, reguladores |
| Block 004 | Deflexão: Q805, IC804, FBT T801, EW |
| Block 005 | IF: tuner, VIF SAW, SIF, AGC |
| Block 006 | Entradas AV (AV1/AV2/AV3), SCART, DVD/RGB |

**Página 44 — C Board Schematic:**
- IC751 (TDA6108AJF) — RGB amp para cátodos do CRT
- CN701 → CN004 da A Board (R/G/B/IK/9V/GND)
- CN703 → CN801 da A Board (deflexão)

**Páginas 46–47 — ICs com vista superior (package drawings)** — idêntico ao Brazil

---

### Páginas 47–48 — Seção 5: Vista Explodida

**Componentes principais:**

| Ref | Part No. | Descrição |
|-----|----------|-----------|
| 3 | 8-738-822-05 | CRT (LATIN NORTH) |
| 3 | 8-738-823-05 | CRT (LATIN SOUTH) |
| 55 | 8-451-505-71 | Deflection Yoke Y21RSA-V |
| 56 | A-1179-571-A | C Board montada |
| 61 | 1-456-153-11 | Bobina de degaussing (LATIN NORTH) |
| 61 | 1-419-287-21 | Bobina de degaussing (LATIN SOUTH) |

**A Board completa:**

| Variante | Part No. |
|----------|----------|
| LATIN NORTH | A-1152-116-A |
| LATIN SOUTH | A-1152-122-A |

---

### Páginas 49+ — Seção 6: Lista de Peças Elétricas

Part numbers individuais para todos componentes das placas A e C. Estrutura idêntica ao Brazil — conferir valores específicos quando substituir componentes, pois part numbers de alguns itens diferem.

---

## Referência Rápida — Tensões Nominais

| Linha | Tensão | Notas |
|-------|--------|-------|
| +B | 135V | Principal; OCP monitora |
| HV (anodo CRT) | ~25kV | Via FBT T801 |
| VCC Audio | 30V | Para amp áudio |
| 11V | 11V | IC602 input |
| 9V | 9V | IC602 (KIA78R09API) |
| 5V | 5V | IC604 (KIA7805API) |
| 3.3V | 3.3V | IC606 (KIA78D33P1) |
| 1.8V | 1.8V | IC603 (PQ018EF01SSH) e IC607 (BA18BC0FP-E2) |
| -13V (VSS) | -13V | Para IC804 (vertical) |
| Catodo CRT | 165 ±2 VDC | Ajuste G2 |

## Referência Rápida — ICs Principais

| Ref | Part | Função |
|-----|------|--------|
| IC001 | TDA12009H (variantes) | One-chip: System + Video + Audio |
| IC003 | CAT24WC16WI-TE13 | NVM EEPROM |
| IC200 | AN5276T **ou AN17804A** | Audio Amp |
| IC602 | KIA78R09API | Regulador 9V |
| IC603 | PQ018EF01SSH | Regulador 1.8V |
| IC604 | KIA7805API | Regulador 5V |
| IC605 | SE135N-LF38 | Regulador auxiliar |
| IC606 | KIA78D33P1 | Regulador 3.3V |
| IC607 | BA18BC0FP-E2 | Regulador 1.8V (áudio) |
| IC751 | TDA6108AJF/N1 | RGB Output Amp (C Board) |
| IC801 | LM2903DT | Comparador |
| IC802 | TJM4558CDT | Op-Amp (EW) |
| IC804 | STV9302A | Vertical Deflection |
| Q805 | 2SC5885 | H-Output transistor |
