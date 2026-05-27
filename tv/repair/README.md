# Lista de Componentes — Reparo Pincushion KV-21FS140

**Sintoma:** Bordas curvadas para dentro, com spikes de largura normal intermitentes. Aparece em poucos segundos após ligar.
**Causa provável:** Componente ativo instável no circuito EW — C857/C861/C867 trocados sem resolver.

---

## Ordem de reparo

### Etapa 1 — Capacitores eletrolíticos (causa mais provável)

Trocar primeiro. Se resolver, não precisa continuar.

| Componente a comprar | Qtd | Ref na placa | Valor original | Local no circuito |
|---|---|---|---|---|
| ~~220µF 25V 105°C electrolytic~~ | ~~3x~~ | ~~C857, C861~~ | ~~220µF 25V~~ | ~~Trocados — não resolveu~~ |
| ~~33µF 160V 105°C electrolytic~~ | ~~2x~~ | ~~C867~~ | ~~33µF 160V~~ | ~~Trocado — não resolveu~~ |
| 100µF 35V 105°C electrolytic | 2x | C854 (+ 1 reserva) | 100µF 35V | Bootstrap vertical IC804 |

> **Atenção:** usar obrigatoriamente capacitores **105°C**. Não usar 85°C — área quente, falharão novamente rápido.
> C867: tensão mínima 160V — não substituir por tensão menor.

---

### Etapa 2 — Transistores e op-amp do circuito EW

Se etapa 1 não resolver completamente.

| Componente a comprar | Qtd | Ref na placa | Valor original | Função |
|---|---|---|---|---|
| 2SC1815 ou BC547 (NPN) | 2x | Q806, Q814 | 2SC1623-L5L6 | MIXER EW e auxiliares |
| KTA1279 (PNP) | 1x | Q809 | KTA1279 | Auxiliar EW (PNP — substituto diferente de Q806!) |
| 2SC3209LK | 2x | Q803, Q810 | 2SC3209LK | PIN AMP / H-DRIVE (original preferível) |
| JRC4558 ou NE5532 DIP-8 | 1x | IC802 | TJM4558CDT | Dual op-amp — processa sinal EWD |
| IRF614 | 1x | Q808 | IRF614-037 | S-CORRECTION MOSFET (difícil achar — pedir junto) |

> **Atenção pinout transistores japoneses:** 2SC1623 e 2SC1815 têm pinagem diferente de BC547 europeu.
> Confirmar EBC antes de soldar. Medir com multímetro no modo diodo antes de instalar.
>
> **Q809 é PNP (KTA1279)** — NÃO substituir com 2SC1815/BC547.
>
> **Q803 (PIN AMP):** opera em tensões mais altas. Preferir 2SC3209LK original ou equivalente de mesma classe.

---

### Etapa 3 — Diodos do circuito EW

Se etapa 1 e 2 não resolverem.

| Componente a comprar | Qtd | Ref na placa | Valor original | Função |
|---|---|---|---|---|
| UF4007 (fast recovery 1A 1000V) | 9x | D819, D821, D823, D824, D827 (+ reservas) | 10ERB20-TB3 / PG104R | Retificadores fast recovery EW |
| RD5.1ESB2 (Zener 5.1V) | 1x | D818 | RD5.1ESB2 | Referência Zener — NÃO substituir com UF4007 |

> UF4007 substitui apenas os fast recovery (10ERB20 / PG104R).
> D818 é Zener 5.1V — componente diferente, substituto diferente.

---

### Etapa 4 — Resistores fusíveis (FPRD)

Verificar visualmente antes de pedir. Trocar se houver sinal de queima ou se medição indicar valor incorreto.

| Componente a comprar | Qtd | Ref na placa | Valor | Função |
|---|---|---|---|---|
| 0.47Ω 1/2W | 2x | R400, R401 | 0.47Ω | Sensing corrente yoke H — fusíveis |
| 2.2Ω 1/4W | 1x | R891 | 2.2Ω | Fusível saída vertical IC804 |
| 3.3kΩ 1/10W | 1x | R895 | 3.3kΩ | Sensing corrente vertical |
| 47kΩ 1/4W | 1x | R888 | 47k | Divisor sinal EW |

---

## Lista de compra consolidada

```
CAPACITORES:
  3x  220µF 25V 105°C electrolytic
  2x  33µF 160V 105°C electrolytic
  2x  100µF 35V 105°C electrolytic

TRANSISTORES:
  2x  2SC1815 ou BC547 (NPN) — Q806, Q814
  1x  KTA1279 (PNP) — Q809
  2x  2SC3209LK — Q803, Q810
  1x  IRF614 — Q808

OP-AMP:
  1x  JRC4558 ou NE5532 DIP-8 — IC802

DIODOS:
  9x  UF4007 (fast recovery) — D819, D821, D823, D824, D827
  1x  RD5.1ESB2 (Zener 5.1V) — D818

RESISTORES:
  2x  0.47Ω 1/2W — R400, R401
  1x  2.2Ω 1/4W — R891
  1x  3.3kΩ 1/10W — R895
  1x  47kΩ 1/4W — R888
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
