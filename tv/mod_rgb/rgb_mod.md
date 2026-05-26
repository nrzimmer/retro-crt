# RGB Mod — KV-21FS140 (Chassis BX1S)

**Status:** Documentado, não executado  
**Dificuldade:** Média — sem mexer em HV se seguir procedimento correto

---

## Contexto

IC001 (TDA12009H) **não tem** pinos de entrada RGB analógico externo para SCART.  
Sinais SCART presentes no IC001 são apenas:
- `SCARTFBL/A16` — fast-blanking (detecta presença de SCART)
- `CVBSO` — composto do SCART (não RGB)
- `SCARTHPR/L` — áudio do SCART

O conector J901 (11P, borda direita da placa, D13/14) carrega **vídeo componente (Y/Pb/Pr)** + áudio, não RGB.

**Único ponto de injeção RGB viável: CN004 (A Board) / CN701 (C Board).**

---

## Caminho do sinal RGB atual

```
IC001 pin87(R) / pin86(G) / pin85(B)
    → CN004 (A Board, 7 pinos)
    → [cabo]
    → CN701 (C Board, 7 pinos)
    → IC751 (TDA6108AJF)
    → Cátodos R/G/B do CRT
```

### Pinagem CN701 (C Board) / CN004 (A Board)

| Pin | Sinal |
|-----|-------|
| 1 | GND |
| 2 | B OUT |
| 3 | G OUT |
| 4 | R OUT |
| 5 | GND |
| 6 | IK (AKB sensing) |
| 7 | 9V |

### Resistores de entrada na C Board (antes do IC751)

| Ref | Valor | Canal |
|-----|-------|-------|
| R757 | 1kΩ | R |
| R756 | 1kΩ | G |
| R758 | 1kΩ | B |
| R752 | 680Ω | R (da A Board) |
| R753 | 680Ω | G |
| R754 | 680Ω | B (não montado neste modelo) |

---

## Esquema do mod

```
                    ┌─────────────────────────────┐
                    │        MOD BOARD            │
                    │                             │
 Fonte RGB          │  75Ω    100µF   R_bias      │
 R (0–0.7V) ───────┤──┤├──┤├──────┤>─────────────┼──┐
 G (0–0.7V) ───────┤──┤├──┤├──────┤>─────────────┼──┤  74HCT4053 ──> CN004
 B (0–0.7V) ───────┤──┤├──┤├──────┤>─────────────┼──┘     │
                    │                             │         │
 Enable (5V=RGB) ──┼─────────────────────────────┼─── pino S (controle)
 Enable (0V=TV)    │                             │
                    │                             │
 IC001 RGB out ────┼─────────────────────────────┼──> CN004 (passthrough quando S=0)
                    └─────────────────────────────┘
```

### Chip de chaveamento: opções

#### 74HCT4053 — recomendado

- 3× mux analógico 2:1, single supply 5V
- Um pino de controle (S) chave os 3 canais simultaneamente
- S = LOW (0V) → passa sinal IC001 (TV normal)
- S = HIGH (5V) → passa RGB externo
- Ron ~80–120Ω, BW ~100MHz, DIP-16 disponível
- Entrada de controle compatível com TTL (threshold ~1.4V) — FB de console aciona direto

#### Alternativas drop-in (mesmo pinout DIP-16)

| Chip | Diferença | Quando usar |
|------|-----------|-------------|
| **74HC4053** | Threshold de controle CMOS (~2.5V) em vez de TTL | Se sinal de controle for 3.3V ou CMOS |
| **CD4053** | CMOS 4000 original — Ron ~300Ω a 5V, BW menor | Só se não achar HCT/HC — Ron mais alto mas aceitável no trecho curto |
| **MAX4053** | Ron ~30Ω, melhor crosstalk, mesmo pinout | Melhor performance, mesma montagem |

#### Alternativas SMD (performance superior, mais difícil de soldar)

| Chip | Package | Ron | Vantagem |
|------|---------|-----|----------|
| TS3A5017 (TI) | SOT-23-8 | ~3Ω | Ron muito baixo, single supply |
| ADG712 (AD) | SOIC-16 | ~5Ω | Baixo distorção, precisão |
| TS5A3159 (TI) | SOT-23-6 | ~1Ω | Single channel — precisa 3x |

**Para este projeto:** 74HCT4053 DIP é suficiente. Ron de 100Ω no trecho curto interno introduz atenuação de ~0.06% com carga de 1kΩ+680Ω — imperceptível.

---

## Detecção automática + chave manual

### Detecção automática via Fast Blanking (SCART pino 16)

Cabos SCART RGB enviam 1–3V no pino FB (fast blanking) quando console está ativo.
Esse sinal controla o pino S do 74HCT4053 automaticamente via transistor NPN.

```
Pino FB (SCART p16)
    │
    R1 (10kΩ)
    │
    Base ── Q1 (BC547 / 2N2222)
    Emissor ── GND
    Coletor ── pino S do 74HCT4053
              └── R2 (10kΩ pull-down para GND)
```

- FB alto (console ativo) → Q1 conduz → S=HIGH → RGB ativo
- FB baixo / cabo desconectado → Q1 corta → S=LOW → TV normal

**Requisito:** cabo SCART deve conectar pino 16 (FB). Verificar no cabo utilizado.

---

### Chave manual de 3 posições

Permite forçar modo independente do FB — útil para debug, consoles sem FB, ou forçar TV normal sem desconectar cabo.

| Posição | Comportamento | Conexão do pino S |
|---------|--------------|-------------------|
| AUTO | FB controla via Q1 | Saída do coletor de Q1 |
| RGB | Força RGB sempre | VCC 5V fixo |
| TV | Força TV normal sempre | GND fixo |

```
                    ┌─── AUTO: coletor Q1 (saída FB)
Pino S (74HCT4053) ─┤─── RGB:  VCC 5V
                    └─── TV:   GND
```

Chave: rotativa 3 posições ou alavanca ON-OFF-ON (SP3T). Custo ~R$5–10.

### Alimentação 5V para o mod

**Ponto de coleta:** IC604 (KIA7805API) pino 3 — saída regulada 4.8V.

IC604 fica na PSU board (Block 003), fora do RF shield do IC001. TO-220, pino 3 = saída 5V. Solda fio direto no pino ou no capacitor de filtro de saída adjacente.

Não usar CN004 pino 7 (9V) para alimentar o mod board 5V — exigiria regulador adicional.  
**Opção B (LM1203N):** CN004 pino 7 (9V) pode alimentar o LM1203N diretamente (margem reduzida) ou via módulo boost MT3608 para 12V.

### Componentes adicionais

| Componente | Qtd | Observação |
|-----------|-----|------------|
| Transistor NPN BC547 ou 2N2222 | 1x | Driver FB |
| Resistor 10kΩ 1/4W | 2x | Base (R1) e pull-down (R2) |
| Chave SP3T (3 posições) | 1x | AUTO / RGB / TV |

### Nível de sinal e acoplamento

| Parâmetro | IC001 out | Fonte externa | IC751 espera |
|-----------|-----------|---------------|--------------|
| DC offset | ~1.5V | ~0V | ~0.7V |
| Swing | ~0.7Vpp | ~0.7Vpp | ~0.7Vpp |

Fonte externa tem DC em 0V e swing de ~0.35Vpp no ponto de terminação (divisor 75Ω+75Ω). Precisa de ganho ×2 + acoplamento + bias antes do mux.

Duas opções de implementação:

---

### Opção A — Op-amp (TLV2374) + componentes discretos

**Alimentação:** 5V do IC604. Componentes comuns, fáceis de encontrar.

#### Cadeia de sinal por canal

```
Fonte RGB
(0–0.7V, 75Ω)
     │
     ├──[R_term 75Ω]── GND               ← termina linha → ~0.35Vpp no nó
     │
     ├──[C_in 47µF 16V]                  ← remove DC da fonte
     │         │
     │    [R_a 33kΩ]── 5V  ┐
     │         │            ├── virtual GND ~1.16V (compartilhado R/G/B)
     │    [R_b 10kΩ]── GND ┘
     │         │ (+ C_vgnd 10µF em paralelo com R_b)
     │
     [TLV2374 — não-inversor, alimentado a 5V]
          (+) = ~1.16V + sinal AC
          (−) conectado à saída via R_f (10kΩ) e ao GND via R_g:
          R_g = R_gmin(5kΩ) + R_wb(trimpot 0–1kΩ) + R_contraste(0–10kΩ, seção pot 3-gang)
          Ganho = 1 + 10k / (5k + R_wb + R_contraste)
          Nominal (R_wb=0, R_contraste=5kΩ): ganho = 2.0 → 0.35×2 = 0.70Vpp ✓
          DC saída = 1.16V × ganho (máx 3.48V a ganho=3 — dentro do rail 5V ✓)
     │
     ├──[C_out 47µF 16V]                 ← remove DC do op-amp (~1.16V×ganho)
     │
     ├──[R_top 10kΩ]── 5V    ┐
     │                        ├── divisor de bias de brilho
     ├──[R_bmin 470Ω]─┐       │
     │         [pot_brightness 2kΩ lin]── GND
     │                 │
     │          bias DC ~0.22–0.99V (compartilhado R/G/B)
     │
     └──── entrada do 74HCT4053 (canal externo)

IC001 RGB out ──────────── entrada do 74HCT4053 (canal TV)
74HCT4053 saída ────────────────────────────────────────> CN004 pin R/G/B
```

#### Contraste — ganho do op-amp

`Ganho = 1 + R_f / (R_gmin + R_wb + R_contraste)`

| R_contraste | R_wb | Ganho | Swing saída | DC saída op-amp | Headroom (5V) |
|-------------|------|-------|-------------|-----------------|---------------|
| 0Ω (máx) | 0Ω | 3.00× | 1.05Vpp | 3.48V → pico 4.0V | 1.0V ✓ |
| 5kΩ (meio) | 0Ω | 2.00× | 0.70Vpp ✓ | 2.32V → pico 2.67V | 2.33V ✓ |
| 10kΩ (mín) | 0Ω | 1.67× | 0.58Vpp | 1.94V → pico 2.23V | 2.77V ✓ |
| 5kΩ | 1kΩ | 1.83× | 0.64Vpp | 2.13V → pico 2.45V | 2.55V ✓ |

Ponto nominal: R_contraste ≈ 5kΩ (meio do pot). White balance trim ajusta ganho ±8% por canal.

> **Erro anterior corrigido:** virtual GND em 2×10kΩ (2.5V) colocaria DC de saída em 5V exatos a ganho=2 — clipping garantido. Correto é 33kΩ+10kΩ → ~1.16V.

#### Brilho — bias compartilhado

`V_bias = 5V × (R_bmin + pot) / (R_top + R_bmin + pot)`

| pot_brightness | V_bias | Efeito |
|----------------|--------|--------|
| 0Ω | ~0.22V | Imagem escura, pretos esmagados |
| ~900Ω | ~0.59V | Neutro — equivale ao IC001 nominal |
| 2kΩ | ~0.99V | Imagem clara, pretos elevados |

R_bmin=470Ω evita bias=0V. Um pot, 3 canais simultâneos — sem desvio de cor.

#### Polaridade dos capacitores eletrolíticos

| Cap | Polo + | Polo − | Tensão típica |
|-----|--------|--------|---------------|
| C_in | lado op-amp (1.16V) | lado fonte (~0V) | ~1.16V |
| C_out | lado op-amp (2.3V–3.5V) | lado bias (0.2V–1.0V) | ~1.3V–3.3V |

#### Componentes Opção A — por canal (×3)

| Componente | Valor | Função |
|-----------|-------|--------|
| R_term | 75Ω 1/4W | Terminação 75Ω da fonte |
| C_in | 47µF 16V eletrolítico | Acoplamento — remove DC da fonte |
| C_out | 47µF 16V eletrolítico | Acoplamento — remove DC do op-amp |
| R_gmin | 5kΩ 1/4W | Define ganho máximo (×3 com pot=0) |
| R_f | 10kΩ 1/4W | Resistor de realimentação |
| R_wb | trimpot 1kΩ multivolta | White balance por canal (ajuste único) |
| R_top | 10kΩ 1/4W | Divisor de bias, lado 5V |
| R_bmin | 470Ω 1/4W | Bias mínimo |

#### Componentes Opção A — globais (×1)

| Componente | Valor | Função |
|-----------|-------|--------|
| TLV2374 ou LMV324 | DIP-14 ou SOP-14 | Quad op-amp single-supply 5V |
| R_a virtual GND | 33kΩ 1/4W | Divisor virtual GND (lado 5V) |
| R_b virtual GND | 10kΩ 1/4W | Divisor virtual GND (lado GND) → ~1.16V |
| C_vgnd | 10µF 16V eletrolítico | Filtra ruído no nó virtual GND |
| pot_brightness | 2kΩ linear | Brilho — 1 pot, 3 canais |
| pot_contraste | 10kΩ linear 3-gang | Contraste — 3 seções, mesmo eixo |
| C_bypass VCC 74HCT4053 | 100nF cerâmico | Desacoplamento próximo ao chip |
| C_bypass VCC op-amp | 100nF cerâmico | Desacoplamento próximo ao TLV2374 |
| C_bulk VCC | 10µF eletrolítico | Bulk decoupling 5V |

---

### Opção B — LM1203N (chip dedicado de vídeo RGB)

**Chip:** National Semiconductor LM1203N, 28-pin DIP.  
**Alimentação:** 12V (preferencial) ou 9V do CN004 pino 7 (margem reduzida).  
Projetado especificamente para pré-amplificação RGB de monitores CRT — contraste e white balance nativos no chip.

#### Arquitetura interna relevante

| Função | Pinos | Método |
|--------|-------|--------|
| Entradas RGB | 4 (R), 6 (G), 9 (B) | Entrada diferencial com clamp |
| Saídas RGB | 25 (R), 20 (G), 16 (B) | Corrente para driver de saída |
| Contraste | 12 | Tensão 0V–V_ref → atenuador resistivo interno igualado |
| Brilho (black level) | 14 (CLAMP GATE) | Pulso de blanking trava o nível de preto |
| White balance (drive) | 27 (R), 22 (G), 18 (B) | Trimpot por canal — ajusta ganho individual |
| White balance (cutoff) | 26 (R), 21 (G), 17 (B) | Ajusta ponto de corte de preto por canal |
| Clamp caps | 5 (R), 8 (G), 10 (B) | Cap externo 0.1µF — segura DC de preto |
| VREF saída | 11 | Referência interna (~1.2V) — usar para divisor de contraste |
| VCC | 1, 13, 23, 28 | Alimentação — todos conectar ao 12V |
| GND | 7 | Ground |

#### Cadeia de sinal (Opção B)

```
Fonte RGB
(0–0.7V, 75Ω)
     │
     ├──[R_term 75Ω]── GND          ← ~0.35Vpp após terminação
     │
     ├──[C_in 100nF film]            ← acoplamento AC (chip espera sinal sem DC)
     │
     [LM1203N pino R/G/B in]
          Ganho interno ajustado pelos pinos DRIVE (trimpots)
          Contraste via pino 12 (0V = mín, VREF = máx)
          Brilho via CLAMP GATE (pino 14) + CSYNC
     │
     [LM1203N pinos R/G/B out → 25/20/16]
     │
     ├──[R_out 1kΩ]                  ← adapta saída de corrente para tensão
     │
     └──── entrada do 74HCT4053 (canal externo)
```

> **Nota nível de saída:** LM1203N saída é corrente. Com 1kΩ de carga → tensão. Ajustar R_out ou trimpot DRIVE para obter ~0.7Vpp na entrada do 74HCT4053. Verificar com osciloscópio na primeira calibração.

#### Contraste (Opção B)

Pino 12 (CONTRAST): tensão de 0V (mínimo contraste) até V_ref/pino 11 (máximo).  
Pot simples de 10kΩ entre GND e VREF (pino 11), wiper no pino 12.  
**Um pot, 3 canais igualmente — atenuadores internos são igualados pelo fabricante.**

#### Brilho (Opção B)

CLAMP GATE (pino 14) requer pulso de blanking para travar o nível de preto.  
Conectar ao sinal de blanking do console (SCART pino 16 / FB) ou ao CSYNC via circuito de detecção.  
Sem esse pulso: brilho fixo no valor de inicialização dos caps de clamp (funciona mas sem controle dinâmico).

Alternativa simples sem blanking: deixar pino 14 em 5V fixo (clampa continuamente) — funciona mas pode introduzir distorção no preto em alguns sinais.

#### White balance (Opção B)

- Pinos DRIVE (27/22/18): trimpot de 1kΩ por canal entre GND e VCC — ajusta ganho
- Pinos CLAMP− (26/21/17): trimpot de 1kΩ por canal — ajusta ponto de corte de preto

Calibração em duas etapas: primeiro DRIVE (ajusta branco), depois CLAMP− (ajusta preto).

#### Alimentação Opção B

| Opção | Tensão | Como obter | Observação |
|-------|--------|-----------|------------|
| Ideal | 12V | Rail 12V interno da TV (verificar no PSU board) | Headroom máximo |
| Aceitável | 9V | CN004 pino 7 | Headroom reduzido, testar estabilidade |
| Alternativa | 12V boost | Módulo boost MT3608 a partir do 9V | ~R$5, simples |

Não usar 5V do IC604 — tensão insuficiente para LM1203N.

#### Componentes Opção B — por canal (×3)

| Componente | Valor | Função |
|-----------|-------|--------|
| R_term | 75Ω 1/4W | Terminação 75Ω da fonte |
| C_in | 100nF film (MKT/MKP) | Acoplamento AC — film preferível a eletrolítico em HF |
| C_clamp | 100nF film | Clamp cap por canal (pinos 5/8/10) |
| R_out | 1kΩ 1/4W | Converte saída de corrente em tensão |
| trimpot DRIVE | 1kΩ multivolta | White balance ganho por canal |
| trimpot CUTOFF | 1kΩ multivolta | White balance corte de preto por canal |

#### Componentes Opção B — globais (×1)

| Componente | Valor | Função |
|-----------|-------|--------|
| LM1203N | DIP-28 | Chip pré-amp RGB dedicado |
| pot_contraste | 10kΩ linear | Contraste — 1 pot, 3 canais (atenuador interno) |
| Fonte 12V (se necessário) | MT3608 ou rail TV | Alimentação do LM1203N |
| C_bypass VCC | 100nF cerâmico ×4 | Bypass em cada pino VCC (1, 13, 23, 28) |
| C_bulk VCC | 10µF eletrolítico | Bulk decoupling 12V |

> **Brilho na Opção B:** controlado pelo circuito de clamp — não há pot externo de brilho como na Opção A. O brilho ajusta-se automaticamente pelo nível de preto do sinal se CLAMP GATE estiver conectado ao blanking. Se precisar de ajuste manual, interpor trimpot no VREF (pino 11).

---

#### Comparativo das opções

| Critério | Opção A (TLV2374) | Opção B (LM1203N) |
|----------|-------------------|-------------------|
| Tensão supply | 5V (já disponível) | 12V (pode precisar de boost) |
| Disponibilidade | Alta — op-amp genérico | Média — chip legacy, achar em estoque |
| Complexidade | Média | Maior (28 pinos, clamp, blanking) |
| Contraste | Pot 3-gang (3 seções) | Pot simples (atenuador interno) |
| Brilho | Pot externo direto | Clamp automático ou VREF trimpot |
| White balance | 3 trimpots (ganho) | 6 trimpots (ganho + cutoff por canal) |
| Qualidade de sinal | Boa (op-amp genérico) | Melhor (igualamento interno, projetado p/ vídeo) |
| **Recomendação** | Primeira opção — menor risco | Se achar o chip e quiser qualidade extra |

---

## Conexões completas do mod

| Sinal da fonte | Conecta em | Observação |
|---------------|-----------|------------|
| CSYNC (ou composite com sync) | AV2 VIDEO RCA (frontal) | IC001 trava deflexão aqui |
| R (0–0.7V, 75Ω) | CN004 pin 4 via 74HCT4053 | Com cap + bias |
| G (0–0.7V, 75Ω) | CN004 pin 3 via 74HCT4053 | Com cap + bias |
| B (0–0.7V, 75Ω) | CN004 pin 2 via 74HCT4053 | Com cap + bias |
| Audio L | AV2 AUDIO L RCA (frontal) | AV2 áudio esquerdo |
| Audio R | AV2 AUDIO R RCA (frontal) | AV2 áudio direito |
| Enable/FB | 74HCT4053 pino S | LOW=TV, HIGH=RGB |
| GND | Chassis / CN004 pin 1 ou 5 | Referência comum |

**TV deve estar no modo AV2** — sync e áudio entram pelos RCAs frontais do AV2, deixando AV1 e componente livres para outros dispositivos.

### Por que AV2 e não AV1

AV2 usa os RCAs frontais da TV (borda oposta a J901). Sync e áudio entram por lá. RGB bypass via CN004 é independente da entrada selecionada — IC001 trava deflexão em AV2, mas RGB vai direto para IC751.

Resultado: AV1 (J901) e componente continuam disponíveis normalmente.

---

## Compatibilidade com videogames

### Funciona nativamente (saída 15kHz)

| Console | Resolução típica | Observação |
|---------|-----------------|------------|
| SNES / Super Famicom | 224p / 240p / 448i | RGB nativo, perfeito |
| Mega Drive / Genesis | 224p / 240p | RGB nativo, perfeito |
| Master System | 192p / 224p | RGB nativo |
| Neo Geo (AES/MVS) | 240p | RGB nativo |
| PlayStation 1 | 240p / 480i | Ambos 15kHz, troca transparente |
| Saturn | 240p / 480i | Ambos 15kHz |
| N64 | 240p / 480i | Requer mod RGB interno |
| GameCube | 480i | Modo 480i = 15kHz |
| Dreamcast | 240p / 480i | Via SCART, não VGA |

### Problemático

| Console | Problema |
|---------|----------|
| PS2 | Muitos jogos forçam 480p (31kHz) — imagem some nesses momentos |
| GameCube | 480p mode = 31kHz, não funciona |
| Dreamcast VGA | 31kHz, não funciona |
| Xbox / PS3+ | 31kHz+, incompatível sem upscaler |

### Mudança de resolução em tempo real

- **Mesma freq H (ex: PS1 trocando 240p ↔ 480i):** IC001 re-trava automaticamente. Sem problema.
- **Muda freq H (15kHz → 31kHz):** IC001 perde sync. Imagem some até voltar a 15kHz. Sem dano.
- **Muda largura de pixels (ex: MD 256↔320):** Mesma freq H, só muda pixels ativos. IC001 fica travado. Funciona.

### Solução para fontes 31kHz

Interpor um **RetroTINK 2x-Mini** ou similar entre console e TV:
```
Console → RetroTINK 2x-Mini → [480p → 480i 15kHz] → TV
```
Adiciona ~1 frame de latência. Permite qualquer console independente de resolução.

---

## Segurança

### Para a TV

| Risco | Mitigação |
|-------|-----------|
| Overdrive do CRT por nível alto | 75Ω terminação + cap acoplamento corretos |
| AKB ler nível errado durante bypass | Causa variação de brilho por alguns frames — sem dano |
| Mod reversível | CN004/CN701 é conector físico — desconecta e volta ao original |

### Para você — PERIGOS DO CRT

> **ATENÇÃO: A TV mantém tensões letais após desligar da tomada.**

| Tensão | Local | Tempo de descarga |
|--------|-------|------------------|
| ~25kV | Ânodo do CRT (capa vermelha) | **horas a dias** |
| ~200V | C Board — alimentação IC751 | minutos |
| ~135V | B+ na A Board | minutos |

**Procedimento obrigatório antes de abrir a TV:**

1. Desligar da tomada
2. Aguardar 5 minutos mínimo
3. Descarregar ânodo do CRT:
   - Resistor **10MΩ 2W** em série com fio isolado
   - Inserir ponta sob a capa vermelha do ânodo
   - Outra ponta no chassis metálico da TV
   - Segurar pelo cabo, nunca pelo resistor
   - Aguardar até parar faíscas/som de descarga
4. Só então trabalhar

**Este mod específico (CN004/CN701)** fica na A Board, longe do FBT e ânodo. Com TV desligada e ânodo descarregado, área segura para trabalhar. Não é necessário mexer perto do HV.

---

## Lista de materiais

### Chaveamento e controle

| Componente | Qtd | Observação |
|-----------|-----|------------|
| 74HCT4053 (DIP ou SMD) | 1× | Mux analógico 3× 2:1 |
| Transistor NPN BC547 ou 2N2222 | 1× | Driver FB |
| Resistor 10kΩ 1/4W | 2× | Base (R1) e pull-down (R2) do transistor FB |
| Chave SP3T (3 posições) | 1× | AUTO / RGB / TV |

### Ganho e controles de imagem — Opção A (TLV2374)

| Componente | Qtd | Observação |
|-----------|-----|------------|
| TLV2374 ou LMV324 (quad op-amp) | 1× | Single-supply 5V, DIP-14 ou SOP-14 |
| Resistor 75Ω 1/4W | 3× | R_term — terminação RGB por canal |
| Resistor 5kΩ 1/4W | 3× | R_gmin — ganho mínimo por canal |
| Resistor 10kΩ 1/4W | 3× | R_f — realimentação por canal |
| Resistor 33kΩ 1/4W | 1× | R_a virtual GND (lado 5V) |
| Resistor 10kΩ 1/4W | 1× | R_b virtual GND (lado GND) → ~1.16V |
| Resistor 10kΩ 1/4W | 3× | R_top bias brilho por canal |
| Resistor 470Ω 1/4W | 1× | R_bmin — bias mínimo brilho |
| Capacitor eletrolítico 47µF 16V | 6× | C_in + C_out por canal (polo + para lado de maior tensão) |
| Capacitor eletrolítico 10µF 16V | 2× | C_vgnd (virtual GND) + bulk VCC |
| Capacitor cerâmico 100nF | 2× | Bypass VCC 74HCT4053 + TLV2374 |
| Trimpot 1kΩ multivolta | 3× | White balance R, G, B |
| Pot linear 2kΩ | 1× | Brilho |
| Pot linear 10kΩ 3-gang | 1× | Contraste — 3 seções, mesmo eixo |

### Ganho e controles de imagem — Opção B (LM1203N)

| Componente | Qtd | Observação |
|-----------|-----|------------|
| LM1203N | 1× | DIP-28 — verificar disponibilidade antes de escolher esta opção |
| Resistor 75Ω 1/4W | 3× | R_term — terminação RGB por canal |
| Resistor 1kΩ 1/4W | 3× | R_out — converte saída corrente em tensão |
| Capacitor film 100nF (MKT) | 6× | C_in (×3) + C_clamp (×3) por canal |
| Capacitor cerâmico 100nF | 5× | Bypass VCC pinos 1, 13, 23, 28 + 74HCT4053 |
| Capacitor eletrolítico 10µF | 1× | Bulk VCC 12V |
| Trimpot 1kΩ multivolta | 6× | White balance: DRIVE ×3 + CUTOFF ×3 |
| Pot linear 10kΩ | 1× | Contraste (wiper no pino 12, entre GND e VREF pino 11) |
| Fonte 12V | 1× | Rail 12V interno da TV ou módulo boost MT3608 do 9V |

### Conectores e cabeamento

| Componente | Qtd | Observação |
|-----------|-----|------------|
| Conector compatível CN004/CN701 | 1× | Verificar passo e tipo in situ |
| Cabo fino blindado (tipo áudio) | — | Sync + áudio AV2 — pode ser longo |
| Cabo fino simples (flat ou 0.1mm) | — | RGB interno (curto, mod board ao lado do CN004) |

---

## Cabeamento interno

### RGB (curto — mod board ao lado do CN004)

Cabo fino simples funciona. Efeitos de linha de transmissão irrelevantes para trecho de ~15cm a 5MHz (comprimento de onda ~40m).

- Cabo tipo flat cable ou fios 0.1mm individuais
- A terminação 75Ω é feita por **resistor no pino de entrada** do mod board, não pelo cabo
- Adicionar blindagem só se aparecer ruído visível após montagem

### Sync + áudio (longo — da mod board/fonte até AV2 frontal)

Sinal de baixa frequência — blindagem básica suficiente.

- Cabo de áudio blindado fino (tipo P2-P2 fino)
- Malha conectada ao GND **em uma ponta apenas** (evita ground loop)
- Pode cruzar a placa sem problema

### Rota dos cabos na A Board

Passar pelos **bordas da placa**, evitar cruzar sobre:
- T801 (FBT) — campo EM forte
- Q805 (H-OUT) — pulsos alta amplitude 15kHz
- Seção EW (L802, Q808)

```
[AV2 frontal]  ←──── sync/áudio (blindado fino, pode ser longo)
       |
   borda da placa
       |
[mod board] ←── RGB curto e simples
       |
    [CN004]
```

---

## Alternativa sem mod — conversor RGB→YPbPr + J901

**Confirmado:** IC001 aceita 240p/15kHz na entrada componente J901. Testado com PS1 (FF8 — troca 240p↔480i em tempo real durante o jogo).

Isso abre uma alternativa sem abrir a TV: usar conversor RGB→YPbPr analógico + J901.

### Requisito crítico: conversor sem upscaling

Conversores com scaler interno (ex: BITFUNX B0FSKMJGXK) convertem 240p→480i internamente — **não servem**. Precisar de conversor de **matriz analógica pura** que só faz conversão de espaço de cor, sem frame buffer.

### Opções confirmadas para 240p nativo

| Produto | Método | 240p | Preço aprox. | Onde |
|---------|--------|------|--------------|------|
| **RetroTINK RGB2COMP** | Matriz analógica | ✅ confirmado | ~$45 USD | retrotink.com |
| **Genérico AliExpress** (LM1881 + BA7230LS) | Matriz analógica | ✅ confirmado com osciloscópio | ~$20 USD | AliExpress |
| **DIY op-amp** | Summing amps + resistores 1% | ✅ (sem frame buffer por definição) | ~$5–10 | componentes |

O genérico do AliExpress usa **LM1881** (separador de sync) + **BA7230LS** (encoder YPbPr) — revisão externa confirmou ausência de conversão de resolução.

### Comparativo com RGB mod direto

| Critério | Conversor + J901 | RGB mod (CN004) |
|----------|-----------------|-----------------|
| Mod na TV | Nenhum | Sim |
| 240p | ✅ | ✅ |
| 480i / 480p | ✅ | ✅ / ❌ (31kHz não passa) |
| Qualidade | Boa (RGB→YPbPr→IC001→RGB) | Melhor (sinal direto) |
| Brilho/contraste | Knobs no adaptador | Pots externos no mod |
| Custo | $20–45 adaptador | $15–25 componentes |
| Reversível | Trivial | Sim (CN004 é conector) |
| AV1 + componente livres | AV1 livre, componente ocupado | Componente + AV1 livres |

### Quando usar cada um

- **Conversor + J901:** uso imediato sem modificação, consoles com SCART RGB, qualidade suficiente para uso casual
- **RGB mod CN004:** melhor qualidade de imagem, libera J901 para outros dispositivos, vale a pena para uso permanente

---

## Referências internas

- [`tv/circuits/c_board_rgb_amp.md`](../circuits/c_board_rgb_amp.md) — IC751, CN701, resistores de entrada R/G/B
- [`tv/circuits/block_006_av_inputs.md`](../circuits/block_006_av_inputs.md) — J901 pinagem, entradas AV1/SCART
- [`tv/circuits/voltage_waveform_table.md`](../circuits/voltage_waveform_table.md) — IC001 pinos 85/86/87 tensões
- [`tv/circuits/block_001_processor.md`](../circuits/block_001_processor.md) — IC001 TDA12009H visão geral
