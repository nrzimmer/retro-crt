# Switch SCART RGB

**Função:** N consoles conectados simultaneamente → 1 entrada SCART na TV. Troca de fonte sem desconectar cabo.

```
Console 1 ──► [SCART IN 1] ┐
Console 2 ──► [SCART IN 2] ├── Switch ──► [SCART OUT] ──► TV
Console 3 ──► [SCART IN 3] ┘
Console 4 ──► [SCART IN 4]
```

---

## Tipos

### Passivo (chave mecânica)

Chave rotativa conecta pinos diretamente — sem eletrônica. Funciona mas carrega o sinal: cada entrada desconectada cria impedância paralela → atenuação e possível reflexão. Aceitável para 2–3 entradas, problemático com mais.

### Ativo (com amplificação)

Mux eletrônico + buffer de saída. Sinal regenerado — qualidade independente do número de entradas.

---

## Por que 74HC4053 não serve para wired-bus

4053 é SPDT: Y sempre conectado a A ou B, **nunca high-Z**. Se Y de múltiplas unidades em paralelo:

- Selecionado: Y → sinal ✓
- Não selecionados: Y → GND (ou input flutuando) → pull-down no barramento

Resultado: sinal atenuado ou curto. Não funciona para topologia wired-bus.

O 4053 é adequado apenas como **mux em árvore** (2:1 por estágio):

```
4 entradas, 6 sinais (R,G,B,sync,L,R):

Entrada 1 ─┐
Entrada 2 ─┤── 4053_A (2:1, 3ch) ──┐
Entrada 3 ─┤                        ├── 4053_C (2:1, 3ch) ──► R,G,B out
Entrada 4 ─┘── 4053_B (2:1, 3ch) ──┘
(repetir com 4053_D para sync+audio)
```

2 bits de controle → 4 entradas. Sem barramento compartilhado.

---

## Chip correto para wired-bus: SN74CBT3244

FET bus switch octal. Tem pino **OE#** (output enable ativo baixo) que coloca **todas as saídas em high-Z** quando desabilitado — permite barramento compartilhado real.

| Parâmetro | 74HC4053 | SN74CBT3244 |
|-----------|----------|-------------|
| Tipo | Mux CMOS SPDT | FET bus switch |
| Ron típico | 100–200Ω | <5Ω |
| High-Z disponível | ✗ | ✓ (via OE#) |
| Canais | 3× 2:1 | 8× SPST |
| Uso em vídeo | Sofrível | Transparente |

**Topologia com CBT3244:**

- Um IC por entrada SCART (habilita/desabilita todos os sinais daquela entrada)
- Todas as entradas no mesmo barramento
- MCU controla OE# de cada IC — só um habilitado por vez
- Barramento → buffer de vídeo → saída

---

## Arquitetura típica de switch ativo completo

```
Console 1 ──► CBT3244 (OE# = LOW  → ativo) ──┐
Console 2 ──► CBT3244 (OE# = HIGH → high-Z) ──┤── barramento RGB+sync+audio
Console 3 ──► CBT3244 (OE# = HIGH → high-Z) ──┤         │
Console N ──► CBT3244 (OE# = HIGH → high-Z) ──┘         ▼
                                                     THS7374 (buffer 4ch)
                    MCU ──► OE# de cada IC               │
                    ▲                                     ▼
              IR remote /                          LM1881 (sync stripper)
              botões /                                    │
              fast blanking                               ▼
              detector                              SCART OUT → TV
```

### Chips de buffer e sync

| Chip | Função | Notas |
|------|--------|-------|
| THS7374 | Buffer vídeo 4ch + LPF | Regenera sinal após mux, filtro selecionável |
| THS7314/THS7316 | Buffer vídeo 3ch | Alternativa mais simples |
| LM1881 | Sync stripper | Extrai csync de composite ou luma |
| LMH1980 | Sync stripper alternativo | Auto-detecta tipo de sync |

### Auto-switch por fast blanking (pin 16 SCART)

Console ligado → pin 16 vai para 1–3V → comparador detecta → MCU comuta para essa entrada. Sem apertar botão.

Implementação simples: comparador LM393 ou transistor NPN em cada entrada monitorando pin 16.

---

## Projetos open source

### OSSW — Open SCART SWitch ⭐ ativo

**Repositório:** https://github.com/BinaryS010/ossw  
**Status:** alpha/protótipo funcional. Autor não vende kit, gerbers disponíveis para fabricação própria.

**Especificações:**
- 8 entradas SCART, 2 saídas SCART simultâneas (não testado)
- Euro SCART apenas (sem JP-21)
- Switching manual (auto-switch planejado, não implementado)
- Saída de áudio stereo via RCA

**Hardware principal:**
| Chip | Função |
|------|--------|
| SN74CBT3244 | FET bus switch octal (mux das entradas) |
| THS7374 | Amp vídeo 4ch + LPF selecionável |
| LM1881 | Sync stripper + seleção csync/composite/luma |
| ATSAMD21J18A | ARM Cortex-M0 (controle, UI, IR) |
| 24LC64 | EEPROM 64Kb (salva configuração) |
| TSOP38238 | Receptor IR 38kHz |
| SN74HC14 | Debounce hardware dos botões |

**PCB:** 4 camadas (~400×130mm) + placa filha LCD 2 camadas. Case acrílico cortado a laser.  
**Alimentação:** 7.5V DC 1A, conector 2.5mm barrel jack centro-positivo.

**Limitações:**
- Switching somente manual (auto por blanking não implementado)
- Sync TTL pode danificar dispositivos upstream — usar apenas cabos com sync 75Ω atenuado
- Firmware: upgrade requer programador Atmel ICE

---

### Osmagtor/8-to-4-scart-switch ⭐ ativo (atualizado abr/2026)

**Repositório:** https://github.com/Osmagtor/8-to-4-scart-switch  
**Status:** passivo, funcional, PCB KiCAD disponível. Sem eletrônica ativa.

**Especificações:**
- 8 entradas, 4 saídas simultâneas — diferencial raro
- Passivo: spring-loaded push buttons mecânicos (mesmo mecanismo de switches baratos de hardware store)
- Seleção RGB via botão dedicado (controla pin 16)
- Diodos 1N4148 em pin 8 (aspect ratio) e pin 16 (blanking) para evitar feedback entre entradas
- Entradas RCA: injeção de áudio estéreo (ex: Mega Drive headphone jack) e lightgun
- Saídas RCA: para captura ou monitor externo

**Como funciona internamente:**
```
Cada spring-loaded button commuta 6 sinais de uma entrada:
  SCART pins: 2 (R audio), 6 (L audio), 7 (B), 11 (G), 15 (R), 20 (composite/sync)
Pin 8 e pin 16: roteados via traces separados com diodos 1N4148
  → impede que uma entrada "alimente" outra quando múltiplos botões pressionados
```

**Limitações:**
- Passivo: sem buffer → alguma degradação com muitas entradas
- Sem auto-switch por blanking
- STL para case não incluído

---

### mrehkopf/WuetendesSeil — firmware para Hydra SCART

**Repositório:** https://github.com/mrehkopf/WuetendesSeil  
**Status:** ativo (last commit 2025-09). Firmware replacement para o Hydra SCART switch v1 (produto comercial).

**Melhorias sobre firmware original:**
- Seleção manual de input (botão do meio alterna auto/manual)
- Busca rápida de input — sem running light animation
- PWM dos LEDs desabilitado (eliminava buzzing no áudio)
- Tolerância de 2s para perda de sinal (evita troca acidental no reset do console)

> Hydra é produto comercial com hardware fechado. Firmware open source apenas.

---

### gbrown128/SCARTer — crosspoint matrix (abandonado)

**Repositório:** https://github.com/gbrown128/SCARTer  
**Status:** abandonado desde 2018. Interessante pelo chip usado.

12 entradas × 3 saídas com **FMS6501** — crosspoint matrix de vídeo 12×9. Permite qualquer entrada para qualquer saída simultaneamente. ATMEGA328 como controlador. Não chegou a ser finalizado.

---

### Numbski/open-source-scart-switch (2017, inativo)

**Repositório:** https://github.com/Numbski/open-source-scart-switch  
3 entradas, manual. Chips: CBT3244 + LMH1980. Sem firmware documentado. Não recomendado — desatualizado.

---

## Como switch passivo barato funciona (dissecado)

O projeto Osmagtor documenta o mecanismo dos switches de R$20–50 vendidos em hardwares stores e AliExpress:

- Spring-loaded push buttons de 18 pinos (2×9): cada botão commuta 6 sinais da sua entrada
- Mecanismo físico garante só um botão pressionado por vez (como botões de rádio vintage)
- Todas as saídas dos botões conectadas em barramento comum → saída SCART
- Pin 8 e pin 16 em traces separados com diodos 1N4148 (sem passar pelos botões) — evita feedback
- Botão RGB adicional corta/passa o sinal RGB (controla pin 16)

**Degradação:** sem high-Z real no barramento — entradas não selecionadas ficam "penduradas". Aceitável para 3–4 entradas, perceptível com 8+.

---

## Aplicação: NES/SNES/N64/PS1/PS2 na KV-21FS140

5 consoles → 1 entrada SCART (via mod CN004 da TV).

OSSW cobre com folga (8 entradas). Opção mais simples: switch de 4–5 entradas com CBT3244 + THS7374 + LM1881.

| Console | RGB nativo | Obs |
|---------|-----------|-----|
| SNES | ✓ | Direto, caps 220µF no cabo |
| PS1 | ✓ | Direto, caps 220µF no cabo |
| PS2 | ✓ | Direto, sem caps no cabo |
| N64 | ✗ | Requer mod RGB interno |
| NES | ✗ | Requer NESRGB ou PPU-LITE |

Todos operam em 240p/480i — 100% compatíveis com 15kHz do KV-21FS140.

---

## Opções comerciais — AliExpress e lojas retro

### AliExpress — switches passivos baratos

Switches mecânicos passivos vendidos em AliExpress por ~$5–25. Funcionam, qualidade variável.

**Links de busca diretos:**

| Busca | Link |
|-------|------|
| SCART switch geral | [aliexpress.com/w/wholesale-scart-switch.html](https://www.aliexpress.com/w/wholesale-scart-switch.html) |
| SCART switcher 4 port | [aliexpress.com — "scart switcher 4 port"](https://www.aliexpress.com/wholesale?SearchText=scart+switcher+4+port) |
| Euro SCART selector | [aliexpress.com — "euro scart selector"](https://www.aliexpress.com/wholesale?SearchText=euro+scart+selector) |
| SCART switch RGB | [aliexpress.com — "scart switch rgb"](https://www.aliexpress.com/wholesale?SearchText=scart+switch+rgb) |

> AliExpress bloqueia scraping automatizado — links de busca são mais confiáveis que links diretos de produto (expiram ou mudam de vendedor).

**O que esperar:**
- Spring-loaded push buttons mecânicos (mesmo mecanismo do Osmagtor acima)
- Sem buffer ativo — sinal pode degradar com muitas entradas
- Sem auto-switch
- Qualidade aceitável para 2–3 consoles, problemática para 5+
- Muitos não comutam todos os 21 pinos — verificar se comuta R/G/B/sync e não só composite+audio

> ⚠️ Switches baratos de AliExpress frequentemente **omitem pin 16 (blanking)** do barramento — TV pode não ativar modo RGB automaticamente. Testar antes de comprar.

### gSCARTsw — Lotharek (comercial, ativo, recomendado)

**Loja:** https://lotharek.pl (buscar "gSCARTsw")  
Produto polonês, enviado para o Brasil via correios. Referência da comunidade retro.

- 8 entradas, 2 saídas
- Ativo com buffer — sinal limpo independente do número de entradas
- **Auto-switch por fast blanking** (pin 16) — troca automático ao ligar console
- Suporta todos os 21 pinos SCART incluindo pin 8 e pin 16
- Firmware: closed source, hardware fechado (firmware replacement open source: WuetendesSeil acima)

**Custo:** ~€60–80 + frete internacional (~€15–25 para Brasil).

### Hydra SCART Switch (comercial)

Produto da comunidade retro europeia. Auto-switch por blanking, 8 entradas. Hardware fechado, firmware substituível pelo WuetendesSeil (ver acima).

### Keene Electronics SCART Switch (comercial UK)

Switches SCART ativos de qualidade, 4–8 entradas. Difícil de encontrar fora da Europa.

---

## Recomendação para o setup NES/SNES/N64/PS1/PS2

| Opção | Custo | Auto-switch | Buffer | DIY |
|-------|-------|-------------|--------|-----|
| Switch passivo AliExpress | ~$10 | ✗ | ✗ | ✗ |
| Osmagtor PCB (fabricar) | ~$5 PCB + ~$10 componentes | ✗ | ✗ | ✓ |
| OSSW (fabricar, 4 camadas) | ~$40 PCB + ~$50 componentes | ✗ (planejado) | ✓ THS7374 | ✓ |
| gSCARTsw Lotharek | ~$90 com frete | ✓ | ✓ | ✗ |

Para 5 consoles sem auto-switch: switch passivo de AliExpress funciona. Para uso confortável com auto-switch: gSCARTsw é o mais maduro e testado pela comunidade, mas caro. OSSW é a melhor alternativa DIY ativa.

---

## Referências

- [OSSW — GitHub BinaryS010](https://github.com/BinaryS010/ossw)
- [Osmagtor/8-to-4-scart-switch — GitHub](https://github.com/Osmagtor/8-to-4-scart-switch)
- [WuetendesSeil firmware Hydra — GitHub mrehkopf](https://github.com/mrehkopf/WuetendesSeil)
- [SN74CBT3244 datasheet — TI](https://www.ti.com/product/SN74CBT3244)
- [THS7374 datasheet — TI](https://www.ti.com/product/THS7374)
- [LM1881 datasheet — TI](https://www.ti.com/product/LM1881)
- [gSCARTsw — Lotharek](https://lotharek.pl) — referência comercial de qualidade
- [SCART Switches — RetroRGB](https://retrorgb.com/scartswitches.html)
