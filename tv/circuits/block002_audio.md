# Block 002 — Audio Amplifier (A Board)

**Schematic:** página 34 | **Manual:** páginas 34–35

## IC Principal: IC200 AN5276T / AN17804A

> **Diferença entre variantes:**  
> - **rev_brazil:** documenta AN5276T  
> - **rev_s79aa:** documenta AN5276T **ou** AN17804A como alternativas — ambas podem estar instaladas dependendo da revisão da placa

| Campo | Valor |
|---|---|
| Tipo | AN5276T (rev_brazil) / AN5276T ou AN17804A (rev_s79aa) |
| Função | AUDIO AMP — amplificador de áudio estéreo de saída para alto-falantes |
| Alimentação | 9V |
| Socket | J200 (177078631) |

## Entradas de áudio (← A Board IC001)

| Sinal | Origem | Descrição |
|---|---|---|
| OUTL | IC001 pin36 via AUDIO_1 | Áudio esquerdo |
| OUTR | IC001 pin37 | Áudio direito |
| MONO_OUTL | IC001 pin39 | Saída mono |
| SCARTHPL | IC001 pin (SCART) | Áudio SCART |
| LSL-AUDIO | IC001 pin (via 001:12A) | Left Surround |
| LSR-AUDIO | IC001 pin (via 001:12A) | Right Surround |

## Saídas para alto-falantes

| Sinal | Conector | Destino |
|---|---|---|
| SPL / SP | CN200 (4P) | Alto-falante esquerdo |
| SPR | CN200 (4P) | Alto-falante direito |
| SP GND | CN200 | Terra dos alto-falantes |

Conector adicional para J Board: CN201 (via W062).

## Controles de mute

| Sinal | Origem | Função |
|---|---|---|
| AUDIO-MUTE | IC001 pin (001:4L) | Mute geral do áudio |
| MOMUTE-AUDIO | IC001 pin (001:7A) | Mute de monitor |
| MON-MUTE-AUDIO | Block 006 | Mute do monitor out |
| AUDIO-STDBY | IC001 pin (001:1F) | Mute em standby |
| PWR-OFF-MUTE | IC001 pin (001:5A) | Mute ao desligar |

## Transistores de mute e buffer

| Ref | Tipo | Função |
|---|---|---|
| Q200 | UN2211 | BUFFER |
| Q201 | 2SA1235-F | BUFFER |
| Q202 | 2SA1235-F | AC MUTE |
| Q204 | — | BUFFER |
| Q205 | — | BUFFER |
| Q206 | UN2211 | MUTE CCT |

## Diodos de proteção e switch

| Ref | Tipo | Função |
|---|---|---|
| D200 | 1PS226-115 | PROTECT |
| D201 | MMDL914T1 | SWITCH |
| D202 | MMDL914T1 | SWITCH |
| D203 | MMDL914T1 | SWITCH |
| D204 | MMDL914T1 | SWITCH |
| D205–D215 | MMDL914T1 | STOPPER / SWITCH |
| D211 | 1PS226-115 | PROTECT (linha 9V) |

## Componentes passivos notáveis

| Ref | Valor | Função |
|---|---|---|
| R234, R235 | 47Ω FPRD | **Resistores fusíveis** de saída de áudio |
| C215 | 2200µF | Capacitor de acoplamento saída L |
| C217, C214 | 1000µF 25V | Capacitor de acoplamento saída R |
| L201 | — | Filtro de saída |
| FB2602 | — | Ferrite bead EMI |
| L2601 | 10µH | Indutor filtro |
| R2646 | 1Ω FPRD | Resistor fusível |
| R2647 | 10kΩ FPRD | Resistor fusível |

## Conectores

| Ref | Destino | Pinos | Sinais |
|---|---|---|---|
| CN200 | Alto-falantes | 4P | SP L, GND, GND, SP R |
| CN201 | J Board CN3400 | — | Saída alto-falante auxiliar |
| CN202 | — | — | Auxiliar (WHT) |
| CN203 | — | — | Auxiliar |

## Alimentação

- 9V: de Block 003 (IC602) — distribuída via 001:6A; 002:2E; 003:10B; 004:2C; 005:2E; 006:7B
- 1.8V: de IC603 (PQ018EF01SSH) — seção de áudio

## Diagnóstico de falhas

| Sintoma | Verificar | Componentes |
|---|---|---|
| Sem áudio (ambos canais) | Sinal AUDIO-MUTE ativo, IC200 defeituoso | IC200, Q202, D201 |
| Sem áudio (um canal) | R234 ou R235 aberto (FPRD fusível) | R234, R235 |
| Distorção no áudio | C215/C214/C217 secos | C215, C214, C217 |
| Zumbido no áudio | Problema na alimentação 9V, L2601 | IC602, L2601 |
