# Block 006 — AV Inputs / SCART / Monitor Out (A Board)

**Schematic:** página 38 | **Manual:** páginas 42–43

## Visão geral

Bloco de entradas externas de vídeo e áudio: AV1, AV2, AV3, SCART (monitor), e saídas monitor. Roteia sinais para IC001 e para Block 002 (áudio).

## Conectores de entrada/saída externos

| Ref | Tipo | Função |
|---|---|---|
| J900 | — | AV1 — entrada vídeo/áudio (principal) |
| J901 | 11P | Conector multi-pino (SCART ou AV) |
| J903 | 3P | Conector auxiliar |
| J904 | — | Saída MON OUT |
| J905 | — | Saída L OUT (áudio L) |
| J906 | — | Saída R OUT (áudio R) / VIDEO IN 1 |
| J907 | — | S IN / VIDEO IN 1 (entrada S-Video) |
| J908 | — | L OUT / MON OUT |
| J909 | — | Conector auxiliar |

## Entradas de vídeo e áudio roteadas para IC001

| Sinal | Pinos IC001 | Descrição |
|---|---|---|
| CVBS1/Y1 | pin58 | AV1 vídeo composto / Y |
| C1 | pin59 | AV1 Chroma |
| CVBS2/Y2 | pin51 | AV2 |
| INL2, INR2 | — | AV2 áudio L/R |
| CVBS3 | pin55 | AV3 |
| INL3, INR3 | — | AV3 áudio L/R |
| CVBSO | pin64 | SCART monitor entrada de vídeo |
| SCARTHPR | pin (001:13E) | SCART áudio R |
| SCARTHPL | pin (001:13E); Block002 | SCART áudio L |
| SCARTFBL/A16 | pin (001:13D) | SCART Fast Blank / A16 |
| INL1, INR1 | pin (001:13F) | AV1 áudio L/R |
| S1/VC | pin111 | Seleção de fonte |

## Saídas monitor

| Sinal | Origem | Destino |
|---|---|---|
| MON-OUT | IC001 pin (001:13F) | → J904 / J908 monitor out |
| OUTL | IC001 pin36 (001:13G) | → áudio L out |
| OUTR | IC001 pin37 (001:13G) | → áudio R out |
| MON-MUTE-AUDIO | — | → Block 002 (002:5D) |
| IFVO | Block 005 (005:6D) | → monitor IF out |

## Transistores de buffer

| Ref | Tipo | Função |
|---|---|---|
| Q900 | 2SA1235-F | MONITOR OUT BUFFER |
| Q901 | UN2216 | Buffer auxiliar |
| Q902 | UN2216 | Buffer auxiliar |
| Q910 | XX | Buffer |
| Q911 | XX | AUDIO MONO BUFFER |
| Q912 | XX | AMP GAIN ADJUST |

## Diodos de proteção (numerosos — todos para proteção de entrada)

| Refs | Tipo | Função |
|---|---|---|
| D900–D918 | XX / PDZ3.6B / RD5.6SB | PROTECTION — proteção de entradas externas |
| D931, D932 | PDZ3.6B-115 | PROTECTION |
| D915, D916 | RD5.6SB-T1 | PROTECTION |

## Resistores de terminação (75Ω)

Entradas de vídeo terminadas com 75Ω — padrão de vídeo composto:

| Refs | Valor | Função |
|---|---|---|
| R917, R928, R929, R930 | 75Ω | Terminação 75Ω sinais vídeo |
| R9053 | 75Ω | Terminação auxiliar |

## Indutores e ferrites

| Ref | Valor | Função |
|---|---|---|
| L902 | 47µH | Filtro de alimentação Block 006 |
| FB902, FB903 | XX | Ferrite beads EMI |

## Componentes passivos notáveis

| Ref | Valor | Função |
|---|---|---|
| C901, C900 | 2.2µF 16V | Acoplamento de áudio |
| C955 | 47µF 35V | Filtro de alimentação |
| C967 | 2.2µF 16V | Acoplamento |
| R902 | 1kΩ | Resistor de polarização |
| R914, R913 | 470kΩ | Divisor de tensão |

## Conector para Block 002

| Ref | Destino | Pinos | Descrição |
|---|---|---|---|
| CN905 | A Board Block002 CN007 | — | Saída áudio mono / monitor |

## Alimentações

| Tensão | Uso |
|---|---|
| 9V | Buffers de vídeo e áudio |
| 5V | Circuitos digitais / switches |

## Sinais de controle

| Sinal | Origem | Função |
|---|---|---|
| D1_JP/MODE1_EU | IC001 (001:7L) | Seleção modo Japan/Europa |
| D1_JP/MODE2_EU/MONSW-MONO | IC001 (001:7A) | Switch monitor mono |
| AGC | → CN904 | AGC para tuner (via Block 005) |

## Diagnóstico de falhas

| Sintoma | Verificar | Componentes |
|---|---|---|
| Sem imagem em AV1 | J900 / J901, Q900 buffer, D900–D903 | Q900, D900–D903 |
| Sem áudio em AV | SCARTHPL/R rota, Q911 buffer | Q911, D900, D905 |
| Sem monitor out | Q900 defeituoso, MON-MUTE-AUDIO ativo | Q900, Q901 |
| Entrada S-Video sem imagem | J907, rota Y/C para IC001 | J907, resistores 75Ω |
