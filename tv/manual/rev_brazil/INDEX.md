# KV-21FS140 Service Manual — Index

**Model:** Sony Trinitron KV-21FS140  
**Chassis:** BX1S  
**Commander:** RM-YA005  
**Part No.:** 9-872-877-01 (Rev 1, 2005/12)  
**Destinos:** Brazil (SCC-S80A-A), E variants (SCC-S79A-A, SCC-S79B-A)

---

## Sumário por Seção

### Páginas 1–3 — Capa e Índice
- Histórico de revisão, modelos/destinos/chassis, tabela de conteúdo completa
- Aviso de segurança: curto-circuitar anodo do tubo antes de remover

---

### Páginas 4–5 — Função de Auto-diagnóstico

**Códigos de erro (flashes do LED STANDBY):**

| Flashes | Código | Causa provável |
|---------|--------|----------------|
| Sem energia | — | Cabo desligado ou fusível F600 (A board) |
| 2x | OCP (2:0–2:255) | Q805 ou IC751 em curto |
| 4x | V-Protect/OVP (4:0–4:255) | +13V ausente ou IC804 defeituoso |
| 5x | IK/AKB (5:0–5:255) | IC1545 ou IC001 defeituoso; G2 mal ajustado |
| 8x | Power NG +5V (8:0–8:255) | IC604 ou IC602 defeituoso |

**Como acessar diagnóstico:**
- Entrar: `[DISPLAY] → [5] → [VOL+] → [POWER]` (em standby)
- Limpar resultado: `[CH 8]`
- Sair: desligar TV

**Circuito diagnóstico:**
- OCP: detectado no pino 32 do IC001 (>4V → standby)
- V-Protect: detectado no pino 13 do IC001 (ausência de pulso vertical)
- IK/AKB: IC001 detecta desbalanço RGB >15s
- Power NG: IC001 detecta HV anormal por falha em IC602/IC604

---

### Páginas 6–7 — Seção 1: Desmontagem

**Sequência:**
1. Tampa traseira — 7 parafusos (+BVTP 4×16)
2. Remoção do alto-falante — 2 parafusos (washer head +P4×16)
3. Remoção do Chassis Assy
4. Posição de serviço
5. Remoção da A Board
6. Remoção do tubo de imagem (CRT)

**Remoção do CRT:**
- Desconectar: Deflection Yoke, Neck Assy, DGC, strap de aterramento
- Deitar TV com face do CRT para baixo em almofada
- Remover: cap de anodo, C Board, mola de tensão, suportes CRT, DY, Neck Assy, DGC
- **ATENÇÃO:** Curto-circuitar anodo após remoção

---

### Páginas 8–10 — Seção 2: Ajustes Físicos (Setup Adjustments)

**Equipamentos necessários:**
- Gerador de padrões, degaussing, osciloscópio, multímetro digital, XCV Adjuster, Landing Checker, fonte DC

**Sequência obrigatória de ajuste:**
1. Beam Landing (purity)
2. Convergência
3. Focus
4. G2 (Screen)
5. White Balance

**2-1 Beam Landing:**
- Sinal verde, mover DY para trás, ajustar purity control (centro = verde, lados = vermelho/azul)
- Avançar DY até tela inteira verde
- Verificar vermelho e azul; usar discos magnéticos nos cantos

**2-2 Convergência:**
- Estático vertical: ímã 4 polos — alinhar R, G, B no centro
- Estático horizontal: ímã 6 polos — alinhar azul com R/G
- Grosso: TLH (H-conv R/B), YCH (balanço Y), TLV (V-conv R/B), XCV (balanço X)
- Cantos: Piece A(90) Permaloy nos cantos com misconvergência

**2-3 Focus:**
- Padrão monoscópio digital, modo DYNAMIC
- Ajustar VR de focus no centro; verificar anel magenta com padrão azul

**2-4 G2 (Screen):**
- Condição: Picture/Brightness STANDARD, TV em Video mode, WHBL 016 "RGBB" = 01
- Catodo R/G/B a 165 ±2 VDC
- Ajustar Screen VR no FBT até linha de varredura desaparecer
- Restaurar RGBB = 00

**2-5 White Balance:**
- Modo serviço, sinal branco raster, Picture DYNAMIC, PICT 006 "WTS" = 00
- Highlight: ajustar WHBL 03 "GDRV" e 04 "BDRV" (botões 1/4 e 3/6)
- Cutoff: ajustar WHBL 000 "BKOR" e 001 "BKOG"
- Gravar: `[MUTING] → [-]`
- Restaurar WTS ao dado original

---

### Página 11 — Seção 3: Ajustes de Circuito — Modo Serviço

**Entrada no Service Mode:**
`[DISPLAY] → [5] → [VOL+] → [POWER]` (em standby)

**Saída:** `[POWER]` → standby → `[POWER]` novamente

**Navegação:**
- `[1]/[4]` ou `[2]/[5]` — selecionar item
- `[3]/[6]` — ajustar valor
- `[MUTING]` → `[-]` — gravar

**Display do Service Mode:**
`categoria | nº item | nome | dado decimal | SERVICE | freq | canal`

---

### Páginas 12–28 — Tabelas de Ajuste (Service Mode Items)

**Categorias disponíveis:**

| Categoria | Descrição | Páginas |
|-----------|-----------|---------|
| GEOM | Geometria (posição H/V, tamanho, correções EW) | 12–13 |
| WHBL | White Balance (offset preto R/G/B, drive branco, sub-brilho) | 13–14 |
| SADJ | Sub-ajustes (PMAX/contraste, hue, color, bright) | 14 |
| YC | Processamento Y/C (frequência peaking, delay, matriz) | 15 |
| SYNC | Sincronismo (modo sync, PLL, identificação vídeo) | 15 |
| PICT | Qualidade de imagem (cathode drive, comb filter, gamma, coring) | 16 |
| SW | Seleção de sinal (CVBS2, SVO, proteção flash) | 16 |
| VIF | FI de vídeo (offset demodulador, AGC, modo de busca) | 17 |
| VM | Velocity Modulation (delay, amplitude, modo) | 17 |
| SDEM | Demodulador FM (janela FM, QSS, filtro bandpass) | 18 |
| TXT | Teletext (posição vertical, brilho RGB, aquisição) | 18 |
| SDSP | Display de som (BBE, surround, equalizer, treble, bass) | 19 |
| SDEC | Decoder de som (SAP, FM A2, NICAM, DCXO) | 20 |
| SDKC | Decoder Korean (apenas modelos NTSC Korean) | 20 |
| PIP | Picture-in-Picture (posição H/V, AGC, delay) | 21 |
| HTV | Home TV (volume máximo/inicial, standby, prog inicial) | 22 |
| OPTM | Opções (timer auto-off, OSD, mute sem sinal) | 22 |
| OPUS | Opções de sistema (stay-off, canal inicial, CC) | 23 |
| OPVP | Opções vídeo/processamento (bandpass, burst key) | 23 |
| OPTB | Option bytes OPB1–OPB6 (bits de configuração) | 24 |

**Dados variáveis por modelo (pág. 25):**
- SYNC/FORF: Latin=01, Brazil=00, Argentina=03
- OPTM/LANG: Brazil=02, Argentina=01
- OPUS/SPCH: Latin=06, Brazil=05, Argentina=01

**OPB1 — KV-21FS140 Brazil:** DEC=72 (Home Theatre habilitado, B/G system)  
**OPB2 — Brazil:** DEC=43 (Component YCbCr disponível, 2 composites, PAL/NTSC multi)  
**OPB3 — Brazil:** DEC=4 (US Stereo habilitado, monaural=0)  
**OPB4 — Brazil:** DEC=0 (sem VM, sem surround, sem teletext)  
**OPB5 — Brazil:** DEC=3 (IP habilitado, Wide habilitado)  
**OPB6 — Brazil:** DEC=5 (sem PiP, OSD language=Portuguese)

---

### Páginas 29–30 — Ajustes de Qualidade e Geometria

**P MAX / Contraste (SADJ 000):**
- Video mode, Picture CUSTOM
- PAL 100% CB; PICTURE 100%, COLOR 0%, BRIGHT 50%
- Osciloscópio no pino 4 (R Output) de CN004
- Alvo: 1.46 ±0.03 Vp-p (21" sem VM) ou 1.10 Vp-p (NTSC sem VM)

**Sub Color (SADJ 004):**
- PAL: VB2=VB3=VB4; NTSC: VB1=VB4 (diff ≤70mV)
- Osciloscópio no pino 2 (B Output) de CN004

**Sub Hue (SADJ 001):**
- NTSC 3.58 CB; ajustar VB1=VB2=VB3=VB4 (diff ≤80mV)

**Sub Bright (WHBL 010 SBRT):**
- RF mode, PAL monoscópio, Brightness 50%, Picture MINIMUM
- Cutoff = 10 IRE; levemente iluminado = 20 IRE

**Geometria — 4 modos obrigatórios:**
1. PAL 50Hz Normal
2. PAL 50Hz Wide
3. NTSC 60Hz Normal
4. NTSC 60Hz Wide

**Items GEOM em ordem de ajuste (PAL 50Hz Normal):**
VPOS → VSIZ → HPOS → EWTZ → HSIZ → HBOW → EWPW → UCOP → LCOP → HPAR → SCOR → VLIN → VSCR

Alvos VSIZ: 12.4 (SPCB), 11.3 (PAL mono), 11.5 (NTSC mono)  
Alvos HSIZ: 16.4 (SPCB), 14.6 (PAL mono), 15.3 (NTSC mono)

---

### Páginas 31–46 — Seção 4: Diagramas

**Página 31 — Diagrama de Blocos:**
- One-chip IC001 (System/Video/Audio Processor) central
- Seções: RF Amp/Tuner → VIF/SIF → Color Decoder → YUV Processor → RGB Amp → CRT
- Audio: ADC → DAP/Stereo → Audio Amp IC (AN5276T) → 2× 10W speakers
- Power: AC 110–220V → CISPR/PFC → SMPS → +B(135V), 30V, 11V, 9V, 5V, 3.3V, 1.8V

**Página 32 — Localização das Placas:**
- **A Board** — placa principal (processamento, deflexão, fonte)
- **C Board** (C/CV Board) — CRT neck board (RGB output para cátodos do tubo)

**Páginas 33–44 — Esquemáticos A Board (7 Blocos):**

| Bloco | Função principal |
|-------|-----------------|
| Block 001 | IC001 One-Chip (System Controller + Video + Audio), NVM IC003, LEDs, conectores |
| Block 002 | Audio Amp IC200 (AN5276T), circuito de mute, fonte 9V para áudio |
| Block 003 | Power Supply (SMPS): transformador T600, reguladores 9V/5V/3.3V/1.8V, DGC relay |
| Block 004 | Deflexão: H-Out Q805 (2SC5885), V-Out IC804 (STV9302A), FBT T801, EW |
| Block 005 | IF: tuner, VIF SAW, SIF, AGC, RF Amp LNA |
| Block 006 | Entradas AV (AV1/AV2/AV3), SCART, DVD/RGB, saídas monitor |
| Block 007 | (referenciado em HS-A007) |

**Página 45 — C Board Schematic:**
- IC751 (TDA6108AJF) — RGB output amp para cátodos do CRT
- CN701 conecta ao CN004 da A Board (R/G/B/IK/9V/GND)
- CN703 conecta ao CN801 da A Board (deflexão)

**Página 46 — Tensões e Formas de Onda** (pág. 47 no manual)

**Página 47 — ICs com vista superior (IC package drawings):**
- IC001: TDA12009H, TDA12017H, TDA12019H, TDA12027H, TDA12067H, TDA12077H
- IC602: KIA78R09API (9V reg)
- IC605: SE135N-LF38
- IC603: PQ018EF01SSH (1.8V reg)

---

### Páginas 48–49 — Seção 5: Vista Explodida

**Componentes principais com part numbers:**

| Ref | Part No. | Descrição |
|-----|----------|-----------|
| 3 | 8-738-823-05 | Tubo de imagem A51LPT50X(SDS) — exceto SV-13105(E) |
| 3 | 8-738-822-05 | Tubo de imagem A51LPT50X — SV-13105(E) |
| 4 | 1-452-032-00 | Disco magnético |
| 5 | 2-658-334-11 | Tampa traseira |
| 6 | 4-084-918-01 | Holder cabo HV |
| 7 | 4-031-319-01 | Espaçador DY (Brazil) |
| 8 | 4-057-714-01 | Peça TLH correction |
| 9 | 8-451-505-71 | Deflection Yoke Y21RSA-V |
| 10 | A-1116-728-A | C Board montada (VAR) |
| 19 | 1-453-329-41 | Bobina de degaussing — exceto SV-13105(E) |
| 19 | 1-456-153-11 | Bobina de degaussing — SV-13105(E) |

**A Board completa por variante:**
- KV-21FS140 Brazil: A-1151-078-A
- KV-21FS140 SV-13105(E): A-1152-116-A
- KV-21FS140 SV-13106(E): A-1152-122-A

---

### Páginas 50–57 — Seção 6: Lista de Peças Elétricas

**Conteúdo:** Part numbers individuais para todos os componentes das placas A e C:
- Capacitores (C001–C2xxx)
- Resistores (R001–R2647, incluindo chips, metal film, fusíveis)
- Diodos (D002–D833)
- Transistores (Q001–Q816)
- ICs (IC001, IC200, IC602–IC607, IC751, IC800–IC804)
- Bobinas/Indutores (L001–L806)
- Conectores, jumpers (JR, JW, CN, J)
- Transformadores (T600–T605, T800–T802)
- Fusível: F600 (A board)

**Componentes críticos de segurança (marcados !):**
- Todos os itens sombreados nos esquemáticos devem ser substituídos SOMENTE com part numbers Sony especificados

---

### Página 58 — C Board: Peças e Acessórios

**C Board (CN701/CN703):**
- IC751: TDA6108AJF/N1 (RGB amp) — Part 6-703-482-01
- J751: Socket CRT — Part 1-451-544-11
- L780: Indutor 22uH — Part 1-414-742-21

**Acessórios/Embalagem:**
- Manual Brazil: 2-666-991-51
- Manual outros: 2-666-990-41
- Transformador de antena (modelos E): 1-417-182-11

---

## Referência Rápida — Tensões Nominais

| Linha | Tensão | Notas |
|-------|--------|-------|
| +B | 135V | Principal; OCP monitora esta linha |
| HV (anodo CRT) | ~25kV | Via FBT T801 |
| VCC Audio | 30V | Para amp áudio |
| 11V | 11V | IC602 input |
| 9V | 9V | IC602 (KIA78R09API) |
| 5V | 5V | IC604 (KIA7805API) |
| 3.3V | 3.3V | IC606 (KIA78D33P1) |
| 1.8V | 1.8V | IC607 (BA18BC0FP) e IC603 (PQ018EF01SSH) |
| -13V (VSS) | -13V | Para IC804 (vertical) |
| Catodo CRT | 165 ±2 VDC | Ajuste G2; medido no catodo R/G/B |

---

## Referência Rápida — ICs Principais

| Referência | Tipo/Part | Função |
|------------|-----------|--------|
| IC001 | TDA12009H (ou variantes) | One-chip: System + Video + Audio Processor |
| IC003 | CAT24WC16WI-TE13 | NVM (memória EEPROM) |
| IC200 | AN5276T | Audio Amp |
| IC602 | KIA78R09API | Regulador 9V |
| IC603 | PQ018EF01SSH | Regulador 1.8V |
| IC604 | KIA7805API | Regulador 5V |
| IC605 | SE135N-LF38 | Regulador auxiliar |
| IC606 | KIA78D33P1 | Regulador 3.3V |
| IC607 | BA18BC0FP-E2 | Regulador 1.8V (áudio) |
| IC751 | TDA6108AJF/N1 | RGB Output Amp (C Board) |
| IC801 | LM2903DT | Comparador |
| IC802 | TJM4558CDT | Op-Amp |
| IC804 | STV9302A | Vertical Deflection IC |
| Q805 | 2SC5885 | H-Output transistor |

---

## Referência Rápida — Conectores Inter-boards

| Conector A Board | Conector C Board | Sinal |
|-----------------|-----------------|-------|
| CN004 (7P) | CN701 | R/G/B out, IK, GND, 9V |
| CN801 | CN703 | H1, deflexão |
| CN005 (3P) | — | Key buttons |

---

## Referência Rápida — Diagnóstico de Falhas Comuns

| Sintoma | Verificar primeiro |
|---------|-------------------|
| Sem energia, fusível ok | Q805 (H-Out), IC751 (C Board), +B line |
| LED pisca 2x | Q805 ou IC751 em curto |
| LED pisca 4x | +13V ausente, IC804 (STV9302A) |
| LED pisca 5x | IC001, IC1545 (Video OUT), ajuste G2 |
| LED pisca 8x | IC604 (5V reg), IC602 (9V reg) |
| Sem varredura vertical | IC804 (STV9302A), V-Out stage |
| Sem imagem, raster ok | IC001, ajuste White Balance, G2 |
| Misconvergência cantos | Piece A(90) Permaloy, magnetos |
| Sem cor | IC001 (color decoder), ajuste SCOL/SHUE |
