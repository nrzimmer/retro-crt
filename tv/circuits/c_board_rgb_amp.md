# C Board (C/CV Board) — RGB Output Amplifier

**Schematic:** página 40 | **Manual:** página 45

## Visão geral

Placa de saída RGB de alta tensão para o CRT. Recebe sinais RGB (~1V) da A Board e os amplifica para os cátodos do tubo (~100–200V de excursão).

## IC Principal: IC751 TDA6108AJF/N1

| Campo | Valor |
|---|---|
| Tipo | TDA6108AJF/N1 |
| Função | RGB Output Amplifier — 3 canais de alta tensão para os cátodos R, G, B do CRT |
| Alimentação | 200V (de T801 via H1/CN703) |

### Entradas (← A Board via CN701)

| Canal | Pino A Board | Sinal |
|---|---|---|
| R IN | IC001 pin87 (R OUT) → CN004 | — |
| G IN | IC001 pin86 (G OUT) → CN004 | — |
| B IN | IC001 pin85 (B OUT) → CN004 | — |

### Saídas (→ CRT via J751)

| Canal | Destino |
|---|---|
| R OUT | Cátodo Vermelho do CRT |
| G OUT | Cátodo Verde do CRT |
| B OUT | Cátodo Azul do CRT |

## Socket do CRT: J751

| Ref | Tipo | Função |
|---|---|---|
| J751 | 145154411 | Socket do CRT — encaixa no pescoço do tubo de imagem |

### Pinos do socket

| Pino | Sinal | Descrição |
|---|---|---|
| R | Cátodo Vermelho | Saída IC751 R |
| G | Cátodo Verde | Saída IC751 G |
| B | Cátodo Azul | Saída IC751 B |
| G1 | Grade de controle | Terra ou pequena tensão negativa |
| G2 | Screen grid | Ajuste SCREEN no FBT |
| G3/G4 | Focus | Ajuste FOCUS no FBT |
| HV | Ânodo | ~25kV do FBT T801 |
| CV | Convergência estática | — |

## Componentes de Alta Tensão

| Ref | Valor | Função |
|---|---|---|
| C752 | 4700pF 2kV | Desacoplamento de alta tensão |
| C754 | 4.7µF 250V | Filtro linha 200V |
| C751 | 10µF 250V | Filtro HV |
| L780 | 22µH | Indutor suavização HV |
| R781 | 0.56Ω 2W | Sensing de corrente |
| R795 | 100kΩ 1/2W FPRD | **Resistor de descarga HV — RESISTOR FUSÍVEL** |
| RV750 | ~110MΩ | Resistor de descarga do ânodo — segurança |

## Componentes de Entrada

| Ref | Valor | Função |
|---|---|---|
| R757 | 1kΩ 1/2W | Resistor de entrada R |
| R756 | 1kΩ 1/2W | Resistor de entrada G |
| R758 | 1kΩ 1/2W | Resistor de entrada B |
| R752 | 680Ω | Resistor de entrada R (da A Board) |
| R753 | 680Ω | Resistor de entrada G |
| R754 | 680Ω | Resistor de entrada B (XX — não montado neste modelo) |

## Circuito AKB (Auto Kinescope Biasing / IK)

**Função:** Sensing automático do nível de preto dos cátodos. IC001 lê nível de preto a cada campo e ajusta o bias do IC751 automaticamente.

```
Corrente cátodo → R774 → tensão proporcional → CN701 pin IK → A Board CN004 → IC001 pin84 (IK)
```

| Ref | Tipo / Valor | Função |
|---|---|---|
| R774 | 150Ω 3W RS | Resistor sensing de corrente de cátodo (IK) |
| D780 | 1SS133T-77 | STOPPER circuito IK |
| D781 | 1SS133T-77 | STOPPER circuito IK |

## Proteções

| Ref | Tipo | Função |
|---|---|---|
| D750 | PG102R | PROTECTOR linha de alta tensão |
| D754 | HSS82-TJ | PROTECTOR HV |
| D755 | HSS82-TJ | PROTECTOR HV |
| D756 | HSS82-TJ | PROTECTOR HV |
| D782 | RD5.6SB-T1 | CLAMP |

## Conectores

| Ref | Destino | Pinos | Sinais (em ordem) |
|---|---|---|---|
| CN701 | A Board CN004 | 7 | GND, B OUT, G OUT, R OUT, GND, IK, 9V |
| CN703 | A Board CN801 | 5 | 200V, NC, GND, H1, NC — H1 = pulso H para timing AKB |
| CN704 | — | 1 | GND do CRT |
| CN705 | — | 1 | Aterramento adicional |

## Modelo do CRT

| Destino | Modelo | Part number |
|---|---|---|
| Brasil | A51LPT50X(SDS) | 8-738-823-05 |
| SV13105E | A51LPT50X | 8-738-822-05 |

Tubo de 21 polegadas tipo Trinitron.

## Diagnóstico de falhas

| Sintoma | Verificar | Componentes |
|---|---|---|
| LED pisca 5x (IK/AKB) | IC751 defeituoso, tensão 200V ausente, G2 mal ajustado | IC751, T801, RV_SCREEN |
| Raster sem brilho (RGB cortados) | IC751, D057/D058/D059 mute travado | IC751, D057, D058, D059 |
| Uma cor ausente (ex: sem vermelho) | R OUT aberto, IC751 canal defeituoso, D057 (R-MUTE) travado | IC751, R757, D057 |
| Imagem muito escura ou muito brilhante | Ajuste G2 (SCREEN) no FBT, White Balance WHBL | — |
| Sem imagem mas HV ok (tela cinza) | G2 muito baixo, AKB/IK fora de ajuste | — |
