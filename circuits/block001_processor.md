# Block 001 — Processor (A Board)

**Schematic:** page 33 | **Manual:** pages 32–33

## IC Principal: IC001 TDA12009H

| Campo | Valor |
|---|---|
| Tipo | TDA12009H (variantes: TDA12017H / 12019H / 12027H / 12067H / 12077H) |
| Função | One-chip System Controller + Video Processor + Audio Processor |
| Total de pinos | 128 |
| Clock | 24.576 MHz — cristal X001 (181331121) |

## ICs de Suporte

| Ref | Tipo | Função |
|---|---|---|
| IC003 | CAT24WC16WI-TE13 | NVM EEPROM 16kbit — armazena todos os parâmetros de serviço (GEOM, WHBL, SADJ, etc.) via I²C |
| IC002 | RPM7240-H5 | IC Receiver — decodifica sinal SIRCS do controle remoto RM-YA005 |

## Mapa de Pinos IC001 (selecionados)

### Entradas de vídeo

| Pino | Sinal | Descrição |
|---|---|---|
| 58 | CVBS1/Y1 | AV1 vídeo composto / luminância Y |
| 59 | C1 | AV1 Chroma |
| 51 | CVBS2/Y2 | AV2 |
| 52 | C2 | AV2 Chroma |
| 55 | CVBS3 | AV3 |
| 64 | CVBS0 | Entrada monitor SCART |

### Saídas RGB → C Board

| Pino | Sinal | Destino |
|---|---|---|
| 85 | B OUT | → C Board (cátodo Azul do CRT) |
| 86 | G OUT | → C Board (cátodo Verde) |
| 87 | R OUT | → C Board (cátodo Vermelho) |
| 84 | IK | ← C Board — feedback AKB (sensing cátodo) |

### Sinais de deflexão → Block 004

| Pino | Sinal | Descrição |
|---|---|---|
| 21 | EWD | Drive parabólico East-West → Block 004 |
| 67 | HOUT | Pulso drive horizontal → Block 004 |
| 66 | AFC | Horizontal AFC → Block 004 |
| 65 | VM | Velocity Modulation output (para bobina VM no yoke) |
| 22 | VD+ | Vertical drive + → Block 004 |
| 23 | VD− | Vertical drive − → Block 004 |
| 13 | VGUARD | ← Block 004 — detecção V-Protect (OVP) |
| 32 | EHTO | ← Q816 coletor — detecção OCP |
| 83 | ABL | ← FBT — Automatic Beam Limiter |
| 14 | PH2LF | H phase lock |
| 15 | PH1LF | H phase lock |

### Sinais de áudio

| Pino | Sinal | Destino |
|---|---|---|
| 36 | OUTL | → Block 002 amp (áudio L) |
| 37 | OUTR | → Block 002 amp (áudio R) |
| 39 | MONO_OUTL | → Block 005/006 |

### Sinais IF

| Pino | Sinal | Origem |
|---|---|---|
| 24, 25 | VIFIN1/2 | ← Block 005 IF vídeo |
| 29, 30 | SIFIN1/2 | ← Block 005 IF áudio |
| 41 | PLLIF | ← Block 005 tuner PLL |
| 31 | AGCOUT | → tuner AGC |

### Controle de sistema

| Pino | Sinal | Função |
|---|---|---|
| 108 | SCL0 | I²C clock (NVM, dispositivos) |
| 109 | SDA0 | I²C data |
| 119 | KEY | Botões frontais |
| 114 | STBY_SW | Switch de standby |
| 115 | DGC RELAY | Controla relé de degaussing |
| 122 | RED LED | LED vermelho (via Q007) |
| 123 | GREEN LED | LED verde standby (via Q006) |

### Alimentação IC001

| Pino | Sinal | Tensão medida |
|---|---|---|
| 45 | VCC8V | 8.3 V |
| 110 | VDDP (3.3V) | 3.2 V |
| 100 | VDDC2 (1.8V) | 1.8 V |
| 117 | VDDC1 (1.8V) | 1.8 V |
| 124 | VDDC3 (1.8V) | 1.8 V |

## Tensões medidas IC001 (seleção)

| Pino | Sinal | Tensão (V) |
|---|---|---|
| 4 | — | 2.6 |
| 5 | — | 3.2 |
| 21 | EWD | 3.2 |
| 32 | EHTO | 0.7 |
| 45 | VCC8V | 8.3 |
| 65 | VM | 0.2 |
| 83 | ABL | 1.5 |
| 84 | IK | 1.5 |
| 85 | B OUT | 1.5 |
| 86 | G OUT | 1.4 |
| 87 | R OUT | 1.5 |
| 110 | VDDP | 3.2 |

## Transistores

| Ref | Tipo | Função |
|---|---|---|
| Q001 | UN2211 | RGB-MUTE SPOT — curto nos cátodos durante mute |
| Q006 | UN2216 | G LED SW — switch LED verde standby |
| Q007 | UN2216 | R LED SW — switch LED vermelho |
| Q010 | 2SA1235-F | Buffer auxiliar |
| Q016 | UN2211 | PROTECTOR |

## Componentes-chave

| Ref | Tipo / Valor | Função |
|---|---|---|
| X001 | 24.576 MHz (181331121) | Cristal de clock principal do IC001 |
| D914 | SPB-25MVWF | LED bicolor (verde standby / vermelho erro) |
| D057 | MMDL914T1 | R-MUTE — mute cátodo Vermelho |
| D058 | MMDL914T1 | G-MUTE — mute cátodo Verde |
| D059 | MMDL914T1 | B-MUTE — mute cátodo Azul |
| D002 | MMDL914T1 | Diodo proteção linha 3.3V |
| D003 | MMDL914T1 | Diodo proteção linha 5V |
| L036 | 22 µH | Filtro alimentação 3.3V |
| L040 | 10 µH | Filtro alimentação |
| L044 | 10 µH | Filtro 1.8V |

## Conectores

| Ref | Destino | Pinos | Sinais |
|---|---|---|---|
| CN004 | C Board CN701 | 7 | GND, B OUT, G OUT, R OUT, GND, IK, 9V |
| CN005 | — | 3 | Botões frontais (KEY) |
| CN007 | Block 006 CN905 | — | AV/Monitor out |
