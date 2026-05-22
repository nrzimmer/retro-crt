# Lista de Componentes — Reparo Pincushion KV-21FS140

**Sintoma:** Efeito pincushion crescente após aquecimento, com spikes de largura correta intermitentes.
**Causa provável:** Capacitores eletrolíticos secos (alto ESR) no circuito EW — Block 004.

---

## Ordem de reparo

### Etapa 1 — Capacitores eletrolíticos (causa mais provável)

Trocar primeiro. Se resolver, não precisa continuar.

| Componente a comprar | Qtd | Ref na placa | Valor original | Local no circuito |
|---|---|---|---|---|
| 220µF 25V 105°C electrolytic | 3x | C857, C861 (+ 1 reserva) | 220µF 25V | Reservatório EW — causa principal |
| 33µF 160V 105°C electrolytic | 2x | C867 (+ 1 reserva) | 33µF 160V | Ressonância H — scan width instável |
| 2.2µF 35V 105°C electrolytic | 2x | C854 (+ 1 reserva) | 2.2µF 35V | Bootstrap vertical IC804 |

> **Atenção:** usar obrigatoriamente capacitores **105°C**. Não usar 85°C — área quente, falharão novamente rápido.
> C867: tensão mínima 160V — não substituir por tensão menor.

---

### Etapa 2 — Transistores e op-amp do circuito EW

Se etapa 1 não resolver completamente.

| Componente a comprar | Qtd | Ref na placa | Valor original | Função |
|---|---|---|---|---|
| 2SC1815 ou BC547 (NPN) | 3x | Q806, Q809, Q810 | 2SC1623-L5L6 | MIXER EW e auxiliares |
| 2SC3209LK | 2x | Q803, Q810 | 2SC3209LK | PIN AMP / H-DRIVE (original preferível) |
| JRC4558 ou NE5532 DIP-8 | 1x | IC802 | TJM4558CDT | Dual op-amp — processa sinal EWD |
| IRF614 | 1x | Q808 | IRF614-037 | S-CORRECTION MOSFET (difícil achar — pedir junto) |

> **Atenção pinout transistores japoneses:** 2SC1623 e 2SC1815 têm pinagem diferente de BC547 europeu.
> Confirmar EBC antes de soldar. Medir com multímetro no modo diodo antes de instalar.
>
> **Q803 (PIN AMP):** opera em tensões mais altas. Preferir 2SC3209LK original ou equivalente de mesma classe.
> BC547 serve apenas para Q806, Q809, Q810.

---

### Etapa 3 — Diodos do circuito EW

Se etapa 1 e 2 não resolverem.

| Componente a comprar | Qtd | Ref na placa | Valor original | Função |
|---|---|---|---|---|
| UF4007 (fast recovery 1A 1000V) | 10x | D818, D819, D821, D823, D824, D827 (+ reservas) | 10ERB20-TB3 / PG104R | Retificadores e referências EW |

> UF4007 substitui todos os fast recovery do circuito EW.
> Comprar pacote de 10 — barato e cobre todos com reserva.

---

### Etapa 4 — Resistores fusíveis (FPRD)

Verificar visualmente antes de pedir. Trocar se houver sinal de queima ou se medição indicar valor incorreto.

| Componente a comprar | Qtd | Ref na placa | Valor | Função |
|---|---|---|---|---|
| 0.47Ω 1/2W | 2x | R400, R401 | 0.47Ω | Sensing corrente yoke H — fusíveis |
| 100Ω 1/2W | 1x | R891 | 100Ω | Fusível saída vertical IC804 |
| 2.2Ω 1/2W | 1x | R895 | 2.2Ω | Sensing corrente vertical — fusível |
| 47kΩ 1/4W | 1x | R888 | 47k | Divisor sinal EW |

---

## Lista de compra consolidada

```
CAPACITORES:
  3x  220µF 25V 105°C electrolytic
  2x  33µF 160V 105°C electrolytic
  2x  2.2µF 35V 105°C electrolytic

TRANSISTORES:
  3x  2SC1815 ou BC547
  2x  2SC3209LK
  1x  IRF614

OP-AMP:
  1x  JRC4558 ou NE5532 DIP-8

DIODOS:
  10x UF4007

RESISTORES:
  2x  0.47Ω 1/2W
  1x  100Ω 1/2W
  1x  2.2Ω 1/2W
  1x  47kΩ 1/4W
```

---

## Verificação gratuita — fazer ANTES de comprar qualquer coisa

### Parâmetros GEOM via service mode

NVM corrompida pode causar pincushion permanente sem relação com temperatura. Verificar antes de pedir peças.

**Entrar no service mode:**
```
[DISPLAY] → [5] → [VOL+] → [POWER]  (com TV em standby)
```

**Verificar e corrigir se necessário:**

| Item# | Nome | Valor correto |
|---|---|---|
| 006 | EWPW | 31 |
| 007 | UCOP | 17 |
| 008 | LCOP | 17 |
| 009 | EWTZ | 31 |
| 005 | HSIZ | 31 |

Se algum valor estiver errado: corrigir com [3]/[6], gravar com [MUTING] → [−].
Se corrigir o problema → NVM estava corrompida, não precisa trocar componentes.

### Juntas frias (cold solder joints)

Inspecionar visualmente com lupa ou luz rasante os pontos de solda em:
- Q806 (MIXER)
- IC802 (op-amp)
- L802 (bobina 22mH)
- Conectores CN801

Junta fria aparece como solda fosca, rachada ou com anel ao redor do componente.
Resolver com retoque de solda — sem custo.

### L802 — bobina EW (medir antes de pedir)

Medir resistência DC com multímetro nos terminais de L802 (bobina 22mH).
Deve ser poucos ohms (tipicamente 2–5Ω).
Leitura aberta (OL) = bobina rompida → causa pincushion independente de temperatura.
L802 é peça especializada — difícil de achar, pedir só se confirmado defeituoso.

---

## Diagnóstico rápido antes de trocar

Se tiver **spray de gelo (freeze spray):**
Ligar TV, aguardar pincushion aparecer, borrifar em C857/C861.
Se imagem corrigir momentaneamente → caps confirmados, etapa 1 resolve.

Se tiver **medidor de ESR:**
Medir C857/C861 com TV quente. ESR > 1Ω em 220µF 25V = cap ruim.
