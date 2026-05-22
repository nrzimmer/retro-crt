# Autodiagnóstico — Códigos de LED e Procedimentos

**Chassis:** BX1S | **Modelo:** KV-21FS140

## Códigos de pisca do LED

O LED bicolor (D914 SPB-25MVWF, controlado por Q006/Q007) exibe códigos de erro piscando em vermelho.

| Código | Pisca | Significado | Verificar primeiro | Componentes suspeitos |
|---|---|---|---|---|
| 2x | ██ ██ | **OCP — Over Current Protection** | Q805 em curto C-E; IC751 C Board em curto; +B curto | Q805, IC751, F600 |
| 4x | ██ ██ ██ ██ | **V-Protect — sem deflexão vertical** | +13V ausente do FBT; IC804 defeituoso | IC804, T801, R891, R895 |
| 5x | ██ ██ ██ ██ ██ | **IK/AKB — Auto Kinescope Biasing** | G2 (SCREEN) mal ajustado; IC751 defeituoso; tensão 200V ausente | IC751, T801, R774, D780 |
| 8x | ██ ██ ██ ██ ██ ██ ██ ██ | **Power NG — falha +5V** | IC604 (5V reg) ou IC602 (9V reg) defeituosos | IC604, IC602, F600 |

## Procedimento geral de diagnóstico

1. Anotar o número de piscadas do LED ao ligar
2. Desligar da tomada — aguardar descarga do HV (~1 min)
3. Verificar F600 (fusível principal) na A Board
4. Medir tensões de alimentação (+B, 9V, 5V, 3.3V) com multímetro
5. Proceder por código conforme tabela acima

## Diagnóstico por sintoma visual

| Sintoma | Causa provável | Verificar |
|---|---|---|
| Tela preta, LED verde aceso | IC751, mute travado (D057/D058/D059), G2 baixo | IC751, G2 screen pot no FBT |
| Tela preta, LED vermelho piscando | Ver código de piscadas acima | — |
| Linha horizontal no centro | Sem deflexão vertical — IC804 ou R891/R895 | IC804, R891, R895 |
| Faixa vertical (sem deflexão H) | Q805 defeituoso, T800 driver, Q807 | Q805, T800, Q807 |
| Imagem muito escura | G2 (SCREEN) muito baixo, AKB fora de ajuste | Pot SCREEN no FBT |
| Uma cor ausente | IC751 canal defeituoso, mute diodo (D057/058/059) | IC751, D057, D058, D059 |
| Pincushion excessivo | L802 (22mH) aberta, Q806 MIXER | L802, Q806, IC802 |
| Sem áudio | IC200 defeituoso, R234/R235 FPRD abertos | IC200, R234, R235 |
| Sem recepção de canal | TU101, tensão 30V ausente | TU101, D103 |
| Zumbido na imagem (ripple) | Capacitores eletrolíticos SMPS | C623, C624, C628, C632 |
| TV liga e desliga imediatamente | Q805 em curto, OCP disparando | Q805, Q804, F600 |
| Fusível F600 queima repetidamente | Curto em Q805 (H-OUT) ou IC751 | Q805, IC751 |

## Pinos de proteção no IC001

| Pino | Sinal | Função de proteção |
|---|---|---|
| 13 | VGUARD | Detecção V-Protect (OVP) — monitora pulso vertical |
| 32 | EHTO | Detecção OCP — Q816 coletor |
| 83 | ABL | Automatic Beam Limiter — feedback do FBT |
| 84 | IK | AKB sensing — feedback cátodos |

## Sequência de verificação de tensões (sem energia)

```
1. F600 (fusível A Board) — visual + continuidade
2. +B 135V no coletor Q805 → se 0V, SMPS não parte
3. 9V em IC602 saída → se baixo, verificar IC602
4. 5V em IC604 saída → se baixo, LED 8x
5. 3.3V em IC606 saída → alimentação IC001
6. 200V no C Board (HV menor do FBT) → alimentação IC751
7. ~25kV no ânodo do CRT → FBT T801 funcionando
```

## Componentes críticos de segurança

> **ATENÇÃO:** Os componentes abaixo devem ser substituídos **exclusivamente** com o part number Sony especificado. Nunca use substitutos genéricos.

| Ref | Tipo | Part number |
|---|---|---|
| T600 | Transformador SMPS | MTZJ-T-77-15 |
| T801 | FBT Flyback | NX-4751//M3A4 |
| IC804 | Vertical IC | STV9302A (part Sony) |

## Resistores fusíveis (FPRD) — verificar antes de substituir outros componentes

| Ref | Valor | Localização | Função |
|---|---|---|---|
| R400, R401 | 0.47Ω 1/2W | Block 004 — yoke H | Sensing corrente yoke H |
| R891 | 100Ω | Block 004 — IC804 out | Fusível saída vertical |
| R895 | 2.2Ω | Block 004 — IC804 | Sensing corrente vertical |
| R234, R235 | 47Ω | Block 002 — IC200 | Fusível saída áudio |
| R774 | 150Ω 3W | C Board | Sensing IK/AKB |
| R795 | 100kΩ | C Board | Descarga HV — fusível |
| R2646 | 1Ω | Block 002 | Fusível |
| R2647 | 10kΩ | Block 002 | Fusível |
