# Block 003 — Power Supply SMPS (A Board)

**Schematic:** page 35 | **Manual:** pages 36–37

## Visão geral

Fonte chaveada principal (SMPS). Converte 110–220V AC em todas as tensões DC necessárias.

## Entrada AC

| Componente | Valor / Tipo | Função |
|---|---|---|
| CN600 | 2P | Conector entrada AC |
| THP600 | Termistor PTC | Proteção inrush e sobrecarga térmica |
| C660 | 0.22 µF 275V PP | Filtro EMC |
| D604 | D3SB60F3 | Ponte retificadora AC |
| RY600 | Relé | Relé de entrada AC (também comuta bobina DGC) |

## Controlador e transformador principal

| Ref | Tipo | Função |
|---|---|---|
| IC601 | 175519811 | SWITCHING REGULATOR — controlador PWM do SMPS |
| T600 | MTZJ-T-77-15 | **TRANSFORMADOR PRINCIPAL SMPS** — componente crítico de segurança. Substituir SOMENTE com part number Sony |

## Saídas secundárias

| Tensão | IC regulador | Tipo | Tensão medida | Destinos |
|---|---|---|---|---|
| +B 135V | — | Deflexão horizontal | — | Block 004 Q805, L802; Block 005 tuner |
| 11V | — | Input para reguladores lineares | — | IC602 input |
| 9V | IC602 (KIA78R09API) | Regulado | 8.8 V | Blocks 001, 002, 004, 005, 006 |
| 5V | IC604 (KIA7805API) | Regulado | 4.8 V | Blocks 001, 002, 004, 005, 006 |
| 3.3V | IC606 (KIA78D33P1) | Regulado | 3.2 V | Block 001 IC001, Block 004 |
| 1.8V main | IC607 (BA18BC0FP-E2) | Core digital IC001 | — | Block 001 IC001 |
| 1.8V áudio | IC603 (PQ018EF01SSH) | Áudio | — | Block 001 seção áudio, Block 002 |
| 30V | — | RF Amp / Tuner | — | Block 005 tuner LNA |

## Tensões medidas nos reguladores

| Ref | Tipo | Pin I (V) | Pin G (V) | Pin O (V) |
|---|---|---|---|---|
| IC602 | KIA78R09API | 10.4 | 0 | 8.8 |
| IC604 | KIA7805API | 8.8 | 0 | 4.8 |
| IC606 | KIA78D33P1 | 4.8 | 0 | 3.2 |
| IC605 | SE135N-LF38 | 134.4 | 0 | 21.2 (error amp) |

## Proteções

| Ref | Tipo / Valor | Função |
|---|---|---|
| F600 | Fusível | **FUSÍVEL PRINCIPAL** — primeira coisa a verificar em sem-energia |
| THP600 | PTC | Proteção inrush e sobrecarga térmica |
| VDR600 | Varistor | Proteção contra surtos na linha AC |
| PS602–PS605 | 5A 90V PTCR | Varistores PTCR de proteção |
| T603 | — | Transformador auxiliar |
| T604 | — | Transformador de isolação |
| T605 | — | Transformador de isolação |

## Circuito de Degaussing

| Componente | Função |
|---|---|
| RY600 | RELAY AC POWER — comuta bobina DGC |
| DGC coil | 1-453-329-41 (Brasil) — bobina de degaussing em volta do CRT |
| Q606 | RELAY SW — controlado por IC001 pino 115 |

## Diagnóstico de falhas

| Sintoma | Verificar | Componentes |
|---|---|---|
| Sem energia, fusível ok | IC601 (PWM), T600 (transformador), Q606 (relay) | IC601, T600, Q606 |
| Fusível queima repetidamente | Curto na linha +B (Q805, IC751) ou no primário SMPS | F600, Q805, IC751 |
| LED pisca 8x (Power NG +5V) | IC604 (5V reg) ou IC602 (9V reg) | IC604, IC602 |
| Tensão +B incorreta | IC601, IC605 (error amp), R636 (feedback) | IC601, IC605 |
| Zumbido na imagem (ripple 100/120Hz) | Capacitores eletrolíticos na saída da ponte retificadora | C623, C624, C628, C632 |
