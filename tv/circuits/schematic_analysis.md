# KV-21FS140 — Análise Completa dos Esquemáticos

## Estrutura da A Board (7 Blocos)

A placa principal (A Board) está dividida em 7 blocos funcionais. Cada bloco é uma seção do esquemático com nome e número de referência de grade (letras A–L, números 1–17).

Conexões entre blocos são indicadas como `XXX:YZ` → bloco:coluna/linha.

---

## BLOCK 001 — Processador Central (IC001)

**Função:** Núcleo do sistema. Contém o IC one-chip que faz tudo: controle de sistema, processamento de vídeo, processamento de áudio, demodulação, geometria.

### IC principal
| Ref | Tipo | Função |
|-----|------|--------|
| IC001 | TDA12009H (ou variante) | One-chip: System Controller + Video Processor + Audio Processor |
| IC003 | CAT24WC16WI-TE13 | NVM — EEPROM 16kbit (armazena dados de serviço) |
| IC002 | RPM7240-H5 | IC Receiver (controle remoto SIRCS) |

### Transistores de interface e proteção
| Ref | Tipo | Função |
|-----|------|--------|
| Q001 | UN2211 | RGB-MUTE SPOT — mute dos sinais RGB no CRT |
| Q006 | UN2216 | G LED SW — switch do LED verde (standby) |
| Q007 | UN2216 | R LED SW — switch do LED vermelho |
| Q010 | 2SA1235-F | Buffer geral |
| Q013 | (XX) | S2 switch |
| Q016 | UN2211 | PROTECTOR |

### Componentes passivos notáveis
| Ref | Valor | Função |
|-----|-------|--------|
| X001 | 181331121 | Cristal de referência 24.576MHz (clock principal IC001) |
| L036 | 22µH | Filtro de alimentação 3.3V |
| L040 | 10µH | Filtro alimentação |
| D914 | SPB-25MVWF | LED bicolor (standby/ativo) |
| D002 | MMDL914T1 | Diodo fornecimento 3.3V |
| D003 | MMDL914T1 | Diodo fornecimento 5V |
| D057/D058/D059 | MMDL914T1 | R-MUTE / G-MUTE / B-MUTE (mute individual de canhões RGB) |

### Pinos chave do IC001 (por função)
| Pino | Sinal | Destino/Origem |
|------|-------|----------------|
| 21 | EWD | EWD-DEFL → Block 004 grid 5A (sinal de correção pincushion) |
| 32 | EHTO | OCP (detecção overcurrent do +B) |
| 65 | VM | VM OUT — Velocity Modulation (saída para VM coil) |
| 66 | AFC | AFC-DEFL → Block 004 (AFC horizontal) |
| 67 | HOUT | HOUT-DEFL → Block 004 grid 6A (pulso de drive horizontal) |
| 83 | ABL | ABL → Block 004 (Automatic Beam Limiter) |
| 13 | VGUARD | VGUARD-DEFL → Block 004 (proteção vertical) |
| 14/15 | PH2LF/PH1LF | Horizontal PLL phase → Block 004 |
| 22/23 | VD+/VD- | Vertical drive → Block 004 |
| 84 | IK | AKB (Auto Black Level) feedback do C Board |
| 85/86/87 | B/G/R OUT | Saída RGB → C Board via CN004/CN701 |
| 108/109 | SCL0/SDA0 | I²C bus para NVM e dispositivos auxiliares |
| 110 | VDDP(3.3V) | Alimentação digital 3.3V IC001 |

### Conectores do Block 001
| Conector | Pinos | Destino |
|----------|-------|---------|
| CN004 | 7P | → C Board CN701 (R/G/B/IK/GND/9V) |
| CN005 | 3P | Botões frontais (KEY) |
| CN007 | (XX) | → Block 006 CN905 |

### Tensões IC001 (medidas representativas)
- Pin 4: 2.6V, Pin 5: 3.2V, Pin 21: 3.2V (EWD)
- Pin 45 (VCC8V): 8.3V, Pin 84 (IK): 1.5V
- Pin 110 (VDDP 3.3V): 3.2V

---

## BLOCK 002 — Amplificador de Áudio

**Função:** Amplificação final de áudio, circuito de mute, proteção de saída.

### IC principal
| Ref | Tipo | Função |
|-----|------|--------|
| IC200 | AN5276T | Audio Amplifier — 2× 10W |

### Transistores
| Ref | Tipo | Função |
|-----|------|--------|
| Q200 | UN2211 | BUFFER |
| Q201 | 2SA1235-F | BUFFER |
| Q202 | 2SA1235-F | AC MUTE |
| Q204, Q205 | (XX) | BUFFER (não montados neste modelo) |
| Q206 | UN2211 | MUTE CCT |

### Passivos notáveis
| Ref | Valor | Função |
|-----|-------|--------|
| C214/C215/C216/C217 | 1000/2200µF 25V | Capacitores de saída do amp |
| C218/C219 | 22µF | Filtros de feedback |
| R234, R235 | 47Ω FPRD | Resistores fusíveis de proteção (saída do amp) |
| R2646, R2647 | 1Ω / 10k FPRD | Resistores de sensing de saída |
| J200 | 177078631 | Conector de entrada de áudio |
| CN200 | 4P WHT | Conector de saída para alto-falantes |

### Sinais de controle
- `AUDIO-STDBY` ← 001:1F (standby de áudio)
- `AUDIO-MUTE` ← 001:4L (mute geral)
- `MOMUTE-AUDIO` ← 001:7A (mute de monitor out)
- `PWR-OFF-MUTE` ← 001:5A

### Tensões
- IC200: alimentado por 9V
- Q201: B=82.3V, C=0V, E=0V (em standby)

---

## BLOCK 003 — Fonte de Alimentação (SMPS)

**Função:** Conversora chaveada principal. Gera todas as tensões secundárias a partir de 110–220V AC.

### ICs e reguladores
| Ref | Tipo | Função |
|-----|------|--------|
| IC601 | (175519811) | SWITCHING REGULATOR IC principal do SMPS |
| IC602 | KIA78R09API | Regulador linear 9V (entrada 11V) |
| IC603 | PQ018EF01SSH | Regulador 1.8V (para áudio) |
| IC604 | KIA7805API | Regulador linear 5V |
| IC605 | SE135N-LF38 | ERROR AMP / REG auxiliar |
| IC606 | KIA78D33P1 | Regulador linear 3.3V |
| IC607 | BA18BC0FP-E2 | Regulador 1.8V principal (digital) |

### Transistores de potência
| Ref | Tipo | Função |
|-----|------|--------|
| Q601 | (não listado explicitamente) | RELAY SW — chave do relé principal |
| Q605 | (XX) | BUFFER regulador |
| Q606 | (componente crítico !) | Transistor principal de chaveamento |
| Q608 | 2SC1623-L5L6 | SW auxiliar |
| Q609 | 2SC1623-L5L6 | SW auxiliar |

### Componentes críticos de segurança (marcados !)
| Ref | Valor/Tipo | Função |
|-----|-----------|--------|
| THP600 | TERMISTOR PTC | Proteção térmica / limitação de inrush |
| C660 | 0.22µF 275V PP | Filtro EMI fase/neutro |
| T600 | MTZJ-T-77-15 | Transformador principal SMPS (!!) |
| T603 | — | Transformador auxiliar |
| T604, T605 | — | Transformadores de isolação |
| PS602, PS603, PS604, PS605 | 5A 90V | Varistores PTC de proteção |
| F600 | FUSÍVEL | Fusível principal da A Board |
| S600 | — | Varistor de proteção (VDR600) |
| VDR600 | — | Varistor de surto |
| D604 | D3SB60F3 | Ponte retificadora AC |
| RY600 | RELAY AC POWER | Relé de entrada AC |

### Tensões produzidas
| Linha | Tensão | Observação |
|-------|--------|------------|
| +B | ~135V | Linha principal para deflexão H |
| 11V | 11V | Input para IC602 |
| 9V | 9V | IC602 output; para áudio, tuner, etc. |
| 5V | 5V | IC604; para digital |
| 3.3V | 3.3V | IC606; para digital |
| 1.8V | 1.8V | IC607 e IC603 |
| 30V | 30V | Para RF Amp/Tuner |

### Proteções
- OCP: detectado por IC001 pin 32 ← feedback de Q816 collector (Block 004)
- OVP: detectado por IC001 pin 13 (V-GUARD) ← pulso vertical ausente
- Relé DGC: acionado por DGC-RELAY signal de IC001 (desmagnetização)

---

## BLOCK 004 — Deflexão (DEFLECTION)

**Função:** Geração e amplificação dos sinais de deflexão horizontal e vertical, incluindo circuitos de pincushion EW, S-correction, ABL, proteções OCP/OVP.

Este bloco é o mais crítico para geometria da imagem.

---

### 4A. Estágio de Driver Horizontal + Pincushion (EW)

#### Cadeia de sinal horizontal:
```
IC001 pin HOUT → [HOUT-DEFL] → Q807 (PIN DRIVE) → T800 → Q805 (H-OUT) → T801 (FBT)
```

| Ref | Tipo | Função | Tensões medidas |
|-----|------|--------|----------------|
| Q807 | 2SA1235-F | PIN DRIVE — transistor PNP de pré-drive do horizontal + pincushion | E=0.1V, B=1.1V, C=0V |
| Q803 | 2SC3209LK | PIN AMP / H-DRIVE — amplificador do sinal de pincushion | C≈70V, E=0V, B≈133V |
| T800 | 143793622 | Transformador driver horizontal — acopla o drive para Q805 | — |
| Q805 | 2SC5885 | H-OUT — transistor de saída horizontal principal (NPN alta tensão) | Coletor: pulso >500Vp-p |
| D807 | BY228GP | DAMPER — diodo amortecedor horizontal (essencial para forma de onda) | — |
| D817 | PG156R | DAMPER secundário | — |

#### Componentes do circuito de pincushion EW (East-West):

O pincushion (efeito almofada) resulta do fato de que a tela plana ou levemente curvada precisa de maior amplitude de varredura nas linhas do centro (onde a distância ao canhão é maior) e menor nos extremos verticais. O circuito EW modula a amplitude do sinal horizontal com uma forma de onda parabólica sincronizada com a frequência vertical.

**Fluxo de sinal EW:**
```
IC001 pin EWD → [EWD-DEFL → Block 004 grid 5A]
    → IC802 (op-amp TJM4558CDT) → amplifica/formata sinal parabólico
    → Q806 (MIXER 2SC1623) → combina com sinal H
    → L802 (22mH) → bobina EW em série com yoke H
    → DY800 → Deflection Yoke (bobinas horizontais)
```

| Ref | Valor/Tipo | Função |
|-----|-----------|--------|
| IC802 | TJM4558CDT | Op-amp duplo — formata/amplifica sinal EWD da IC001 |
| Q806 | 2SC1623-L5L6 | MIXER — mistura sinal EW na corrente horizontal |
| Q809 | 2SC3209LK | Transistor auxiliar EW/drive |
| Q810 | 2SC3209LK | Transistor auxiliar EW |
| L802 | 22mH | **Bobina EW** — em série na alimentação do yoke horizontal, modula amplitude H |
| C857 | 220µF 25V | Filtro/reservatório EW |
| C861 | 220µF 25V | Filtro/reservatório EW |
| C867 | 33µF 160V | Capacitor ressonante do estágio H-OUT (junto com L805) |
| C878 | 0.01µF 25V | Bypass EW |
| D818 | 10ERB20-TB3 | Retificador EW |
| D819 | 10ERB20-TB3 | Retificador EW |
| D821 | 10ERB20-TB3 | H-CENT1 — circuito de posição horizontal |
| D823 | PG104R | RECTIFIER EW |
| D824 | PG104R | RECTIFIER EW |
| D827 | PG104R | RECT |
| D828 | — | circuito auxiliar |
| R890 | — | Resistor de ajuste EW |
| R888 | 47kΩ | Divisor de sinal EW |
| C860 | 1000p 500V | Filtro HV EW |

**Tensões medidas IC802 (TJM4558CDT):**
| Pino | V | Função |
|------|---|--------|
| 1 | 3.3V | OUT1 (saída do 1º amp) |
| 2 | 2.2V | IN1- |
| 3 | 6.0V | IN1+ (recebe EWD de IC001) |
| 4 | 8.8V | V+ (alimentação positiva) |
| 5 | 2.4V | IN2+ |
| 6 | 3.1V | IN2- |
| 7 | 3.0V | OUT2 |
| 8 | 0V | V- (GND) |

#### Circuito de S-Correction:

A S-correction compensa a distorção em S na varredura horizontal (causada pela diferença entre a trajetória do feixe e a tela plana ao longo do eixo X).

| Ref | Tipo | Função |
|-----|------|--------|
| Q808 | IRF614-037 | **S-CORRECTION** — MOSFET de potência, controla a modulação de largura horizontal para compensar distorção em S |
| C825 | 0.022µF 200V PP | Capacitor de S-correction |
| C842 | 0.022µF 400V PP | Capacitor de S-correction |
| R406 | XX | Resistor de S-correction |
| D801 | — | STOPPER do S-correction |

**Tensões Q808 (IRF614 MOSFET):**
- S: 1.8V, G: 0.1V, D: 0V (em repouso)

#### Circuito de H-Center (posição horizontal):

| Ref | Tipo | Função |
|-----|------|--------|
| IC801 | LM2903DT | COMPARATOR — detecta e controla posição do centro H |
| S800 | 157270711 | Ajuste de centro H (trim) |
| D819 | 10ERB20-TB3 | H-CENT1 |
| R412 | 22kΩ 1/2W | Divisor do comparador |
| R411 | 68kΩ 1/2W | Divisor do comparador |
| R413 | 0.47Ω | Sensing de corrente |
| R405 | 0.47Ω | Sensing de corrente |
| R896 | 10kΩ | Pull-up |

---

### 4B. Estágio de Saída Horizontal (H-OUT) e FBT

| Ref | Tipo | Função |
|-----|------|--------|
| Q805 | 2SC5885 | **H-OUT** — transistor de saída horizontal. Coletor conectado ao FBT (T801). Alta tensão de coletor em operação. |
| Q804 | KTA1279 | STOPPER — limita o pico de tensão no coletor de Q805 |
| Q814 | 2SC1623-L5L6 | Transistor auxiliar H |
| T801 | NX-4751//M3A4 | **FBT (Flyback Transformer)** — gera HV para ânodo do CRT (~25kV), e tensões secundárias (SV, FV, -13V para vertical, etc.) |
| T802 | (XX) | — não montado |
| D807 | BY228GP | DAMPER — absorve a energia de retrace, protege Q805 |
| D816 | — | Diodo auxiliar |
| C841 | 0.1µF 400V PP | Capacitor de ressonância H |
| C846 | — | Capacitor HV |
| C847 | — | Capacitor auxiliar |
| C867 | 33µF 160V | **Capacitor de ressonância principal** — junto com L805, determina frequência de ressonância do estágio H |
| L805 | 2.2mH | **Bobina de linearidade** — em série com yoke H, corrige linearidade |
| L804 | (XX) | — não montado |
| R400, R401 | 0.47Ω 1/2W FPRD | Sensing de corrente do yoke H (resistores fusíveis!) |
| R416 | 4.7kΩ 1/2W | Resistor no circuito FBT |
| JW1840, JW1841 | fios 5mm / 7.5mm | Conexões de ajuste da bobina de linearidade |

#### Tensões do FBT (T801) — saídas secundárias
| Enrolamento | Tensão | Destino |
|-------------|--------|---------|
| HV | ~25kV | Ânodo do CRT (via cabo HV) |
| FV | ~600V | Focus (G3) do CRT |
| SV | ~500V | Screen (G2) do CRT |
| -13V (VSS) | -13V | IC804 (vertical IC) pin 1 |
| +13V (VCC) | +13V | IC804 pin 3 |

#### Pinos do FBT usados no esquemático
| Terminal | Destino |
|----------|---------|
| T801-1 | HV + GND_1 |
| T801-2 | HV + GND_1 |
| T801-4 | HV + GND_1 |
| T801-5 | FV / SV |
| T801-7 | Secondary |
| T801-9 | Secondary |
| T801-11 | Secondary |

---

### 4C. Estágio Vertical (IC804)

| Ref | Tipo | Função |
|-----|------|--------|
| IC804 | STV9302A | **VERTICAL IC** — amplificador de deflexão vertical completo |
| Q009 | (MIXER) | Amplificador auxiliar do vertical |
| C854 | 2.2µF 35V | Capacitor de bootstrap vertical |
| C855, C858 | — | Filtros verticais |
| R326 | 220Ω | Resistor de ganho |
| R327 | 3.3kΩ | Resistor de ganho |
| D820 | PG102R | Retificador auxiliar vertical |
| R891 | 100Ω FPRD | Resistor fusível de saída vertical |
| R895 | 2.2Ω FPRD | Sensing de corrente vertical (fusível) |

**Tensões IC804 (STV9302A):**
| Pino | V | Função |
|------|---|--------|
| 1 | -13.5V | VSS — alimentação negativa |
| 2 | * | (pulso — não mensurável com multímetro) |
| 3 | 13.9V | VCC — alimentação positiva |

**Sinais de entrada no IC804:**
- VD+ e VD-: pulso vertical de IC001 (pinos 22/23)
- PH2LF: sinal de fase horizontal baixo de IC001

**Sinais de saída do IC804:**
- V+ e V- → Yoke vertical via DY800
- H+ → parte do estágio H (feedback)

---

### 4D. Conectores e Proteções do Block 004

| Ref | Pinos | Função |
|-----|-------|--------|
| DY800 | 6P | **Deflection Yoke** — pinos H.DY (2 pinos H) e V.DY (2 pinos V) |
| CN801 | (XX) → CN703 | Conector → C Board (sinal H1 para yoke de foco) |

**Proteções:**
| Sinal | Detectado por | Ação |
|-------|--------------|------|
| OVP-DEFL | IC001 pin 13 (VGUARD) | Standby se deflexão V parar |
| OCP-PROTECT | IC001 pin 32 (EHTO) ← Q816 | Standby se +B tiver overcurrent |
| HOLD_DOWN | ← Block 003 (fonte) | Mantém transistores desligados |
| ABL | IC001 pin 83 ← FBT | Limita corrente do feixe |

**Componentes de proteção adicionais:**
| Ref | Tipo | Função |
|-----|------|--------|
| D829 | (FPRD) | Clamp |
| D812 | RD5.1ESB2 | PROTECTOR |
| D816 | RD5.6SB-T1 | CLAMP REG |
| D832, D833 | MMDL914T1 | STOPPER — proteção do CN801 |
| D804, D805, D808, D809 | 1SS133T-77 | STOPPER |
| TH800 | — | Termistor — proteção térmica do estágio H |
| R421, R422, R423 | — | Resistores de proteção |

---

### 4E. Circuito de Rotation (Rotação de Imagem)

| Ref | Função |
|-----|--------|
| IC800 | (XX) ROTATION AMP — não montado neste modelo |
| CN800 | (XX) — não montado |
| R800–R817 | (todos XX) — não montados |

Sinal ROT_CTRL e ROT_SW vêm de IC001 mas o circuito de rotação não está populado.

---

## BLOCK 005 — IF / Tuner

**Função:** Recepção e demodulação do sinal de RF. Inclui tuner, filtros SAW, circuito IF de vídeo e áudio.

### Componentes principais
| Ref | Tipo | Função |
|-----|------|--------|
| TU101 | 169369411 | **Tuner principal** |
| TU102 | (XX) | Tuner secundário — não montado |
| SWF100 | 179592911 | SAW filter — filtro IF de vídeo (44MHz) |
| SWF101 | 181339111 | SAW filter — filtro IF de som |
| SWF103 | (XX) | SAW auxiliar — não montado |
| CF101 | (XX) | Filtro cerâmico — não montado |
| CT131 | (XX) | Capacitor trim — não montado |
| CT139 | 178152621 | Capacitor trim do PLL |
| L100 | 100µH | Indutor filtro do tuner |
| L101 | 0.33µH | Indutor IF |
| L102 | (XX) | Não montado |
| L103, L107 | 0Ω (short) | Jumpers de roteamento |
| L105 | (XX) | Não montado |
| L106 | 100µH | Indutor de filtro |

### Transistores
| Ref | Tipo | Função |
|-----|------|--------|
| Q100 | 2SC1623-L5L6 | BUFFER — buffer de saída IF |
| Q102 | 2SC3779C,D-AA | BUFFER — buffer de sinal IF |
| Q103, Q104 | (XX) | SWITCH — não montados |
| Q111 | (XX) | BUFFER — não montado |

### Reguladores auxiliares
| Ref | Tipo | Função |
|-----|------|--------|
| D103 | MTZJ-33B | Regulador 33V para o tuner |
| D106 | RD3.3B | Regulador 3.3V auxiliar |

### Sinais de saída do Block 005
| Sinal | Destino |
|-------|---------|
| VIFIN1, VIFIN2 | → IC001 pins (entrada IF de vídeo) |
| SIFIN1, SIFIN2 | → IC001 pins (entrada IF de som) |
| PLLIF | → IC001 (PLL do tuner) |
| IFVO/IF_MON_OUT | → IC001 e Block 006 (monitor out de IF) |
| TU-AGC | → Block 006 (AGC do tuner) |
| 2SIF | → IC001 (2nd IF de som) |

---

## BLOCK 006 — Entradas AV / SCART / Monitor Out

**Função:** Gerencia todas as entradas e saídas de A/V: AV1, AV2, AV3, SCART, DVD/RGB, monitor out.

### Transistores
| Ref | Tipo | Função |
|-----|------|--------|
| Q900 | 2SA1235-F | MONITOR OUT BUFFER |
| Q901 | UN2216 | Chave auxiliar |
| Q902 | UN2216 | Chave de vídeo |
| Q910, Q911 | (XX) | Não montados |
| Q912 | (XX) | AMP GAIN ADJUST — não montado |

### Passivos notáveis
| Ref | Valor | Função |
|-----|-------|--------|
| C901, C900 | 2.2µF 16V | Acoplamento AV |
| C955 | 47µF 35V | Filtro de alimentação |
| L902 | 47µH | Filtro de áudio |
| R9028, R9030 | 100Ω | Terminadores de entrada de vídeo |
| R928, R929, R930 | 75Ω | Terminadores de saída de vídeo (75Ω standard) |

### Conectores
| Ref | Pinos | Função |
|-----|-------|--------|
| J900 | (XX) | AV1 (não montado neste modelo) |
| J901 | 11P | SCART / AV |
| J903 | 3P | Conector auxiliar |
| J904 | (XX) | Não montado |
| J905–J909 | (XX) | Não montados |
| CN903, CN904 | — | I²C bus do tuner / conector auxiliar |
| CN905 | (XX) | → Block 001/002 |

---

## BLOCK 007 — (Referenciado como HS-A007)

Referenciado no Block 003 como "HS-A007:1B". Provavelmente circuito de soft-start ou Horizontal-Sync auxiliary. Detalhes não extraídos nos TXTs disponíveis.

---

## C BOARD (C/CV Board) — Amplificador RGB para o CRT

**Função:** Recebe os sinais RGB processados da A Board e os amplifica para o nível necessário para pilotar os cátodos do tubo (tipicamente 100–200V de excursão).

### IC principal
| Ref | Tipo | Função |
|-----|------|--------|
| IC751 | TDA6108AJF/N1 | **RGB Output Amplifier** — 3 canais de alta tensão para cátodos R, G, B |

### Componentes de alta tensão
| Ref | Valor | Função |
|-----|-------|--------|
| C752 | 4700p 2kV | Desacoplamento de HV |
| C754 | 4.7µF 250V | Filtro 250V |
| C751 | 10µF 250V | Filtro HV |
| L780 | 22µH | Indutor de suavização HV |
| R781 | 0.56Ω 2W | Resistor de sensing |
| R795 | 100kΩ 1/2W FPRD | Divisor de HV (resistor de descarga!) |
| R757, R756, R758 | 1kΩ 1/2W | Resistores de entrada RGB |
| R774 | 150Ω 3W RS | Resistor de sensing de corrente (IK) |
| RV750 | 110MΩ | Resistor de descarga do ânodo (!) |
| D750 | PG102R | PROTECTOR |
| D780 | 1SS133T-77 | STOPPER |
| D781 | 1SS133T-77 | STOPPER |
| D754, D755, D756 | HSS82-TJ | PROTECTOR — proteção de HV |
| J751 | 145154411 | **Socket do CRT** — encaixa no neck do tubo |

### Pino IK (AKB)
- R774 (150Ω 3W) faz sensing da corrente de cátodo
- Sinal IK vai via CN701 → CN004 → IC001 pin 84 (feedback de auto black level)

### Conectores da C Board
| Conector | Pinos | Destino |
|----------|-------|---------|
| CN701 | 7P WHT | ← A Board CN004 (R/G/B/IK/GND/9V) |
| CN703 | 5P WHT | ← A Board CN801 (H1/GND/NC) |
| CN704 | 1P | GND do CRT |
| CN705 | 1P | Aterramento |

### Ajuste de convergência estática
- RV750 (H.STAT) — ajuste horizontal de convergência estática (potenciômetro de 110MΩ... na verdade este valor parece ser da C Board, é um resistor de descarga. O potenciômetro H.STAT é mecânico na placa.)

---

## Resumo dos Sinais de Interface Entre Blocos

```
IC001 (Block 001)
  │
  ├─ EWD ──────────────────────────→ Block 004 (pincushion/EW)
  ├─ HOUT ─────────────────────────→ Block 004 (drive horizontal)
  ├─ AFC ──────────────────────────→ Block 004 (AFC horizontal)
  ├─ VD+/VD- ──────────────────────→ Block 004 (drive vertical)
  ├─ VGUARD ───────────────────────→ Block 004 (proteção V)
  ├─ ABL ──────────────────────────→ Block 004 ← (FBT feedback)
  │
  ├─ R/G/B OUT ────────────────────→ C Board (cátodos do CRT)
  ├─ IK ───────────────────────────← C Board (auto black level)
  │
  ├─ VIFIN1/2 ─────────────────────← Block 005 (IF vídeo)
  ├─ SIFIN1/2 ─────────────────────← Block 005 (IF áudio)
  │
  ├─ OUTL/OUTR ────────────────────→ Block 002 (áudio para amp)
  └─ I²C (SCL0/SDA0) ─────────────→ IC003 (NVM) + Tuner

Block 003 (SMPS)
  ├─ +B (135V) ────────────────────→ Block 004, Block 005, Block 001
  ├─ 9V ───────────────────────────→ Block 001, 002, 004, 005, 006
  ├─ 5V ───────────────────────────→ Block 001, 002, 004, 005, 006
  ├─ 3.3V ─────────────────────────→ Block 001, 004
  └─ 1.8V ─────────────────────────→ Block 001

Block 004 (Deflexão)
  ├─ FBT (T801) → HV (25kV) ───────→ C Board (ânodo CRT)
  ├─ FBT → FV/SV ──────────────────→ C Board (focus/screen CRT)
  ├─ FBT → -13V/+13V ──────────────→ IC804 alimentação
  ├─ OCP-PROTECT ──────────────────→ Block 001 (IC001 proteção)
  ├─ OVP-DEFL ─────────────────────→ Block 001 (IC001 proteção)
  └─ DY800 ─────────────────────────→ Deflection Yoke (externo)
```

---

## ANÁLISE DETALHADA: Circuito Horizontal / Pincushion (EW)

### Visão Geral do Problema

O efeito almofada (pincushion) é uma distorção geométrica onde os lados verticais da imagem se curvam para dentro. Acontece porque:
- O CRT tem geometria cônica/esférica
- A tela é plana (ou quase)
- As linhas horizontais do centro têm maior amplitude que as dos extremos verticais (top/bottom)

A correção EW modula a **amplitude do sinal horizontal** com uma onda **parabólica na frequência vertical** (50Hz/60Hz): nas linhas do centro da tela a amplitude H é maior, nos extremos é menor.

### Cadeia Completa do Sinal EW neste TV

```
[Dados GEOM no NVM (IC003)]
        │
        ▼
[IC001 — calcula forma de onda EWD digital]
  pino EWD (pin 21) → sinal analógico parabólico a 50/60Hz
        │
        │ EWD-DEFL (001:10L → 004:5A)
        ▼
[IC802 — TJM4558CDT — Dual Op-Amp]
  Amplifica e formata o sinal EWD
  Pin 3 (IN1+): recebe EWD da IC001
  Pin 1 (OUT1): sinal EW amplificado → 3.3V medido
  Pin 7 (OUT2): saída para próximo estágio → 3.0V medido
        │
        ▼
[Q806 — 2SC1623-L5L6 — MIXER]
  Combina o sinal parabólico EW com a corrente DC de alimentação
  E=(9.3)V, B=0V (ou próximo), C=4.9V
        │
        ▼
[L802 — 22mH — Bobina EW]
  ← Ponto crítico! Esta bobina fica em série com o fornecimento de +B
     para o estágio horizontal. A corrente através dela modula a 
     tensão disponível para Q805 (H-OUT), alterando a amplitude
     de varredura horizontal proporcionalmente.
        │
        ▼
[Q805 — 2SC5885 — H-OUT]
  Transistor de saída horizontal. Sua amplitude de operação varia
  conforme a tensão de alimentação modulada por L802.
        │
        ▼
[T801 — FBT — Flyback]
        │
        ▼
[DY800 — Deflection Yoke]
  Bobinas horizontais com amplitude variável → corrige pincushion
```

### Parâmetros de Serviço que Controlam o Pincushion EW

Todos estes parâmetros são programados digitalmente via IC001 e afetam o sinal EWD:

| Código GEOM | Nome | Efeito no pincushion |
|-------------|------|---------------------|
| GEOM 005 | HSIZ (EW Width) | Amplitude geral do pincushion — aumentar = ampliar todos os lados |
| GEOM 006 | EWPW (EW Parabola/Width) | Curvatura da parábola EW — ajusta quanto os lados curvam |
| GEOM 007 | UCOP (EW Upper Corner Parabola) | Correção de pincushion no canto superior |
| GEOM 008 | LCOP (EW Lower Corner Parabola) | Correção de pincushion no canto inferior |
| GEOM 009 | EWTZ (EW Trapezoid) | Correção trapezoidal — corrige se um lado é maior que o outro |
| GEOM 000 | HPOS | Posição horizontal (não afeta pincushion, só shift) |
| GEOM 001 | HPAR | Horizontal Parallelogram (inclinação das linhas H) |
| GEOM 002 | HBOW | Horizontal Bow (curvatura em arco das linhas horizontais) |

**Como ajustar via service mode:**
1. Entrar: `[DISPLAY] → [5] → [VOL+] → [POWER]` (standby)
2. Navegar: `[1]/[4]` para selecionar GEOM
3. Selecionar item: `[2]/[5]` para navegar nos números
4. Ajustar: `[3]/[6]` para mudar valor
5. Gravar: `[MUTING] → [-]`

**Padrão recomendado para ajuste de geometria:** SPCB (Special Color Bar) ou Monoscópio

### Pinos do STV9302A (IC804) — Vertical IC

| Pino | Sinal | V medido |
|------|-------|---------|
| 1 | VSS (-13V) | -13.5V |
| 2 | Input (pulso V) | * |
| 3 | VCC (+13V) | 13.9V |
| 4,5 | Saídas V | Para yoke vertical via DY800 |

### Componentes da Bobina de Deflexão (DY800 — 6 pinos)
| Pino DY800 | Sinal | Origem |
|------------|-------|--------|
| H.DY (2 pinos) | Bobinas horizontais | Q805 ← T801 + L805 + C867 |
| V.DY (2 pinos) | Bobinas verticais | IC804 (STV9302A) |

### Falhas Comuns no Circuito Horizontal/Pincushion

| Sintoma | Causa provável | Componente |
|---------|---------------|------------|
| Sem imagem, TV liga e desliga (OCP) | Q805 em curto | Q805 (2SC5885) |
| LED pisca 2x | Q805 ou IC751 em curto | Q805 / IC751 |
| Raster muito estreito / largo | Valor errado em HSIZ | Ajuste GEOM 005 |
| Pincushion não corrige | L802 aberta ou Q806 defeituoso | L802 (22mH) / Q806 |
| Pincushion só em cima ou só embaixo | UCOP ou LCOP incorreto | Ajuste GEOM 007/008 |
| Imagem trapezoidal | EWTZ incorreto | Ajuste GEOM 009 |
| Imagem em S (largura varia verticalmente) | Q808 (IRF614) defeituoso | Q808 |
| Falta de linearidade H | L805 com valor alterado | L805 (2.2mH) |
| Posição H incorreta | HPOS errado | Ajuste GEOM 000 |
| Imagem inclinada | HPAR incorreto | Ajuste GEOM 001 |
| Scan width instável | C867 seco | C867 (33µF 160V) |
| LED pisca 4x (V-Protect) | IC804 (STV9302A) | IC804 |
| Sem varredura vertical (raster horizontal único) | IC804 defeituoso | IC804 (STV9302A) |
| Deflexão vertical pequena | R891 ou R895 abertos (fusíveis) | R891/R895 FPRD |

### Tensões de Referência no Circuito H

| Ponto | V esperado | Observação |
|-------|-----------|------------|
| +B linha principal | 135V DC | Alimenta Q805 via L802 |
| Coletor Q805 (em operação) | Pulso >500Vp-p | Nunca medir com multímetro comum |
| IC804 VCC | +13.9V | Saída do FBT |
| IC804 VSS | -13.5V | Saída do FBT (negativa) |
| IC802 pin 4 | 8.8V | Alimentação op-amp EW |
| IC802 pin 3 | 6.0V | Entrada do sinal EWD |
| Q806 emitter | ~9.3V (PAL) / 9.9V (NTSC) | Ponto de operação EW |
| DY800 H | Pulso ~28Vp-p (na yoke) | Waveform 15 NTSC: 28.80Vp-p |

---

## Formas de Onda Chave (da tabela de medições, pág. 47–48)

| Ref | Waveform | Amplitude | Observação |
|-----|----------|-----------|------------|
| 15 | DY800 H (yoke horizontal) | 28.80Vp-p | Medida na bobina H do yoke |
| 16 | Q806 (EW MIXER) | 9.20Vp-p | Sinal EW no transistor mixer |
| 12 | Estágio H | 132.0Vp-p | Pulso horizontal no circuito |
| 14 | IC804 saída V | 1.40Vp-p | Saída vertical |
| 17 | IC804 saída V | 1.34Vp-p | Saída vertical |
