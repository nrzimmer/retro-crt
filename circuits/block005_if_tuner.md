# Block 005 — IF / Tuner (A Board)

**Schematic:** página 37 | **Manual:** páginas 40–41

## Componentes principais

| Ref | Tipo | Função |
|---|---|---|
| TU101 | 169369411 | **Tuner principal** — sintonia RF, converte canal para IF |
| TU102 | XX | Tuner auxiliar (variante de modelo) |
| SWF100 | 179592911 | Surface Acoustic Wave Filter — filtro SAW vídeo IF |
| SWF101 | 181339111 | Surface Acoustic Wave Filter — filtro SAW áudio IF |
| SWF103 | XX | Filtro SAW auxiliar |
| CF101 | XX | Filtro de cerâmica IF |
| CT131, CT139 | XX / 178152621 | Transformadores de IF |

## Fluxo do sinal

```
Antena → TU101 (tuner) → IF → SWF100 (filtro vídeo) → VIFIN1/2 → IC001 pin24/25
                               ↓
                         SWF101 (filtro áudio) → SIFIN1/2 → IC001 pin29/30
                               ↓
                         CF101 → Q102 (buffer) → L101/L103 → processamento IF
```

## Transistores e buffers IF

| Ref | Tipo | Função |
|---|---|---|
| Q100 | 2SC1623-L5L6 | BUFFER IF |
| Q102 | 2SC3779C,D-AA | BUFFER — pré-amplificador IF |
| Q103 | XX | SWITCH |
| Q104 | XX | SWITCH |
| Q111 | XX | BUFFER |

## Indutores e filtros

| Ref | Valor | Função |
|---|---|---|
| L100 | 100µH | Filtro de alimentação IF |
| L101 | 0.33µH | Bobina ressonância IF |
| L102 | XX | Bobina IF |
| L103 | 0Ω | Jumper |
| L105 | XX | Filtro |
| L106 | 100µH | Filtro |
| L107 | 0Ω | Jumper |
| FB001 | XX | Ferrite bead |
| FB101 | 0µH | Ferrite bead |

## Diodos reguladores IF

| Ref | Tipo | Função |
|---|---|---|
| D103 | MTZJ-33B | REGULATOR — 33V zener para tuner |
| D106 | RD3.3B | REGULATOR — 3.3V para circuito IF |
| D100 | XX | STOPPER |
| D102 | XX | — |
| D105 | MMDL914T1 | STOPPER |
| D107–D111 | XX / RD5.6SB | PROTECT |
| D108, D109 | RD5.6SB-T1 | PROTECT |

## Sinais para IC001

| Sinal | Pino IC001 | Descrição |
|---|---|---|
| VIFIN1-IF | pin24 | Vídeo IF input 1 |
| VIFIN2-IF | pin25 | Vídeo IF input 2 |
| SIFIN1-IF | pin29 | Áudio SIF input 1 |
| SIFIN2-IF | pin30 | Áudio SIF input 2 |
| PLLIF | pin41 | PLL do tuner |
| IFVO/IF_MON_OUT | pin43 | IF monitor output → Block 006 |
| TU-AGC | — | AGC do tuner ← Block 006 |
| TUAGC-IF | pin (001:11L) | AGC output para tuner |
| STBY_SW | pin (001:6L) | Sinal de standby |
| M-SYS-IF | pin (001:6L) | Seleção do sistema de modulação |
| SECAM-L-L | pin (001:6L) | Seleção SECAM |
| 2SIF | pin (001:11L) | — |

## Saídas para outros blocos

| Sinal | Destino | Descrição |
|---|---|---|
| IFVO | Block 006 (006:8H) | Monitor IF output |
| MONO_OUTL | IC001 pin (001:13G); Block 006 | Saída áudio mono |

## Alimentações

| Tensão | Origem | Uso |
|---|---|---|
| 30V | Block 003 | Tuner LNA |
| 9V | IC602 (Block 003) | Circuitos IF |
| 5V | IC604 (Block 003) | Digital / tuner |
| I²C (SCL0, SDA0) | IC001 pins 108/109 | Comunicação com tuner |

## Interface I²C com tuner

Tuner TU101 é controlado via I²C (SCL/SDA) pelo IC001. Sinais também acessíveis via CN904 (5P) para AGC.

| Ref | Pinos | Sinais |
|---|---|---|
| CN904 | 5P | AGC, GND, B INT, B DAT, B CLK |
| CN903 | 4P XX | GND, B INT, B DAT, B CLK |

## Diagnóstico de falhas

| Sintoma | Verificar | Componentes |
|---|---|---|
| Sem recepção de canal | TU101 defeituoso, 30V ausente | TU101, D103 |
| Imagem ruidosa / neve | AGC incorreto, SWF100/SWF101 defeituosos | SWF100, SWF101, Q111 |
| Sem áudio em canais RF | SWF101, SIFIN incorreto | SWF101, CF101 |
| IF instável | L100/L106 abertos, alimentação 9V | L100, L106, IC602 |
