# Block 004 — Deflection (A Board)

**Schematic:** páginas 36–37 | **Manual:** páginas 38–39

## Alimentações do estágio

| Tensão | Valor | Fonte |
|---|---|---|
| +B | 135V DC | SMPS (Block 003) — alimentação principal estágio H |
| VCC +13V | 13.9V | FBT T801 → IC804 |
| VSS −13V | −13.5V | FBT T801 → IC804 |
| 9V / 5V | 9V / 5V | Reguladores Block 003 |

---

## Subcircuito 1 — Driver Horizontal

```
IC001 (HOUT pin67) → Q807 (PIN DRIVE) → T800 (driver transformer) → Q805 (H-OUT) → T801 (FBT)
```

| Ref | Tipo | Função | Tensões medidas |
|---|---|---|---|
| Q807 | 2SA1235-F | PIN DRIVE — pré-driver PNP | E=0.1V, B=1.1V, C=0V |
| Q803 | 2SC3209LK | PIN AMP / H-DRIVE — amplificador pincushion | C=70.6V, E=0V, B=133.4V |
| T800 | 143793622 | Transformador driver horizontal | — |
| Q805 | 2SC5885 | **H-OUT** — transistor de saída horizontal principal NPN alta tensão | **Coletor: >500Vpp — NÃO medir com multímetro** |
| Q804 | KTA1279 | STOPPER — limita pico de tensão no coletor de Q805 | — |
| Q814 | 2SC1623-L5L6 | Transistor auxiliar horizontal | — |

---

## Subcircuito 2 — Correção EW / Pincushion

**Função:** Modula a amplitude de varredura horizontal com uma parábola a 50/60Hz, corrigindo distorção pincushion (efeito almofada).

### Fluxo do sinal EW

```
IC001 pin21 (EWD) → IC802 (op-amp TJM4558CDT) → Q806 (MIXER 2SC1623) → L802 (22mH) → +B → Q805 (H-OUT) → DY800 (yoke H)
```

A corrente através de L802 é modulada pelo circuito EW, variando a tensão disponível para Q805 a cada linha horizontal — resultando em varredura mais estreita no topo/base (onde a parábola é menor) e mais larga no centro.

### Componentes

| Ref | Tipo / Valor | Função | Tensões medidas |
|---|---|---|---|
| IC802 | TJM4558CDT | Dual op-amp — amplifica e formata sinal EWD | pin1=3.3V, pin2=2.2V, pin3=6.0V, pin4=8.8V, pin5=2.4V, pin6=3.1V, pin7=3.0V |
| Q806 | 2SC1623-L5L6 | MIXER EW — combina parábola com corrente +B | E=9.3V (9.9V NTSC), B=0V, C=4.9V |
| Q809 | 2SC3209LK | Transistor auxiliar EW drive | — |
| Q810 | 2SC3209LK | Transistor auxiliar EW | — |
| L802 | 22 mH | **BOBINA EW** — em série na linha +B para Q805. Crítica para correção pincushion | — |
| C857 | 220 µF 25V | Filtro/reservatório EW | — |
| C861 | 220 µF 25V | Filtro/reservatório EW | — |
| C867 | 33 µF 160V | Capacitor de ressonância principal H — junto com L805 define freq. ressonância | — |
| D818, D819 | 10ERB20-TB3 | Retificadores EW | — |
| D821 | 10ERB20-TB3 | H-CENT1 — referência posição horizontal | — |
| D823, D824 | PG104R | RECTIFIER EW | — |
| R888 | 47k | Divisor de sinal EW | — |

### Forma de onda EW (ref 16)
- Amplitude: **9.2Vpp** no mixer Q806 (condição NTSC)

### Parâmetros de serviço (GEOM) que controlam este circuito

| Parâmetro | Item# | Range | Init | Efeito |
|---|---|---|---|---|
| HSIZ | 005 | 0–63 | 31 | Largura geral (amplitude EWD) |
| EWPW | 006 | 0–63 | 31 | Curvatura da parábola EW — **principal pincushion** |
| UCOP | 007 | 0–63 | 17 | Pincushion canto superior |
| LCOP | 008 | 0–63 | 17 | Pincushion canto inferior |
| EWTZ | 009 | 0–63 | 31 | Correção trapezoidal |

---

## Subcircuito 3 — S-Correction

**Função:** Compensa distorção em S na varredura horizontal (trajetória do feixe vs tela plana no eixo X).

| Ref | Tipo / Valor | Função | Tensões medidas |
|---|---|---|---|
| Q808 | IRF614-037 | **S-CORRECTION MOSFET** N-ch de potência | S=1.8V, G=0.1V, D=0V |
| C825 | 0.022 µF 200V PP | Capacitor de S-correction | — |
| C842 | 0.022 µF 400V PP | Capacitor de S-correction | — |
| D801 | — | STOPPER S-correction | — |

**Parâmetro de serviço:** SCOR (item 012), range 0–63, init 14.

---

## Subcircuito 4 — Saída Horizontal e FBT

**Função:** Gera o pulso de retrace e todas as altas tensões para o CRT.

| Ref | Tipo | Função |
|---|---|---|
| T801 | NX-4751//M3A4 | **FLYBACK TRANSFORMER** — componente crítico de segurança. Substituir SOMENTE com part Sony |
| D807 | BY228GP | DAMPER — absorve energia de retrace, protege Q805 |
| D817 | PG156R | DAMPER secundário |
| C841 | 0.1 µF 400V PP | Capacitor de ressonância H |
| L805 | 2.2 mH | Bobina de linearidade — em série com yoke H |
| R400, R401 | 0.47Ω 1/2W FPRD | Sensing de corrente yoke H — **RESISTORES FUSÍVEIS** |
| R416 | 4.7k 1/2W | Resistor no circuito FBT |
| JW1840 | fio 5mm | Jumper ajuste linearidade H |
| JW1841 | fio 7.5mm | Jumper ajuste linearidade H |

### Saídas do FBT T801

| Saída | Tensão | Destino |
|---|---|---|
| HV | ~25kV | Ânodo do CRT |
| FV | ~600V | Focus (G3/G4 do CRT) |
| SV | ~500V | Screen (G2 do CRT) |
| +13V | 13.9V | VCC para IC804 (vertical) |
| −13V | −13.5V | VSS para IC804 |

### Formas de onda
- DY800 yoke H: **28.8Vpp** (condição NTSC) — ref 15
- Estágio H: **132.0Vpp** — ref 12

---

## Subcircuito 5 — Deflexão Vertical

| Ref | Tipo | Função | Tensões medidas |
|---|---|---|---|
| IC804 | **STV9302A** | VERTICAL IC — amplificador deflexão vertical integrado. **Componente crítico — substituir só com p/n Sony** | pin1(VSS)=−13.5V, pin2(IN)=pulso, pin3(VCC)=13.9V |
| C854 | 2.2 µF 35V | Capacitor de bootstrap vertical | — |
| R891 | 100Ω FPRD | Resistor fusível de saída vertical — **FUSÍVEL** | — |
| R895 | 2.2Ω FPRD | Sensing corrente vertical — **FUSÍVEL** | — |
| D820 | PG102R | Retificador auxiliar vertical | — |

**Entradas IC804:** VD+ (IC001 pin22), VD− (IC001 pin23), PH2LF (IC001)

### Formas de onda vertical
- V out ref 14: **1.40Vpp**
- V out ref 17: **1.34Vpp**

---

## Subcircuito 6 — Centro Horizontal

| Ref | Tipo | Função |
|---|---|---|
| IC801 | LM2903DT | COMPARATOR — detecta e controla posição centro H |
| S800 | 157270711 | Trim de ajuste centro H |
| R412 | 22k 1/2W RN | Divisor comparador |
| R411 | 68k 1/2W RN | Divisor comparador |

---

## Subcircuito 7 — Proteções

### OCP (Over Current Protection)

- **Detecção:** Q816 coletor → IC001 pin32 (EHTO)
- **Ação:** IC001 entra em standby se >4V no pin32
- **LED:** pisca 2x

### OVP (Over Voltage Protection / V-Protect)

- **Detecção:** IC001 pin13 (VGUARD) — monitora pulso vertical
- **Ação:** LED pisca 4x, entra em standby

### ABL (Automatic Beam Limiter)

- **Detecção:** Feedback do FBT → IC001 pin83
- **Ação:** Reduz brilho/contraste quando corrente do feixe excede limite

| Ref | Tipo | Função |
|---|---|---|
| D812 | RD5.1ESB2 | PROTECTOR |
| D816 | RD5.6SB-T1 | CLAMP REG |
| D832, D833 | MMDL914T1 | STOPPER proteção CN801 |
| TH800 | Termistor | Proteção térmica estágio H |

---

## Conector Deflection Yoke

| Ref | Pinos | Sinais |
|---|---|---|
| DY800 | 6P | H.DY (2 pinos horizontais) + V.DY (2 pinos verticais) |
| CN801 | 5P | → C Board CN703: 200V, NC, GND, H1, NC |

---

## Diagnóstico de falhas

| Sintoma | Verificar | Componentes |
|---|---|---|
| LED pisca 2x (OCP) | Q805 em curto C-E, IC751 em curto | Q805, IC751 |
| LED pisca 4x (V-Protect) | +13V ausente, IC804 defeituoso | IC804, T801 |
| Raster estreito ou largo | Ajustar GEOM 005 HSIZ via service mode | — |
| Pincushion não corrige | L802 aberta ou Q806 defeituoso | L802, Q806, IC802 |
| Pincushion só no topo ou só na base | Ajustar GEOM 007 UCOP ou 008 LCOP | — |
| Imagem trapezoidal | Ajustar GEOM 009 EWTZ | — |
| Distorção em S horizontal | Q808 (IRF614) defeituoso ou C825/C842 secos | Q808, C825, C842 |
| Falta linearidade H | L805 (2.2mH) com valor alterado | L805 |
| Scan width instável | C867 seco (33µF 160V) | C867 |
| Sem varredura vertical (linha H no centro) | IC804 defeituoso, R891/R895 abertos | IC804, R891, R895 |
| Imagem inclinada | Ajustar GEOM 001 HPAR | — |
| TV liga e desliga imediatamente | Q805 ou Q804 em curto | Q805, Q804 |
