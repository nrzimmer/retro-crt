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

### Chip de chaveamento: 74HCT4053

- 3× mux analógico 2:1, single supply 5V
- Um pino de controle (S) chave os 3 canais simultaneamente
- S = LOW (0V) → passa sinal IC001 (TV normal)
- S = HIGH (5V) → passa RGB externo

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

Não usar CN004 pino 7 (9V) — exigiria regulador adicional.

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

Solução: cap de acoplamento (100µF) remove DC da fonte + resistor para referência de ~0.7V via divisor resistivo (ex: 1kΩ para 1.5V, 680Ω para GND → ~0.8V de bias).

---

## Conexões completas do mod

| Sinal da fonte | Conecta em | Observação |
|---------------|-----------|------------|
| CSYNC (ou composite com sync) | J901 pin 1 (V1) | IC001 trava deflexão aqui |
| R (0–0.7V, 75Ω) | CN004 pin 4 via 74HCT4053 | Com cap + bias |
| G (0–0.7V, 75Ω) | CN004 pin 3 via 74HCT4053 | Com cap + bias |
| B (0–0.7V, 75Ω) | CN004 pin 2 via 74HCT4053 | Com cap + bias |
| Audio L | J901 pin 5 (L1) | AV1 áudio esquerdo |
| Audio R | J901 pin 4 (R1) | AV1 áudio direito |
| Enable/FB | 74HCT4053 pino S | LOW=TV, HIGH=RGB |
| GND | Chassis / CN004 pin 1 ou 5 | Referência comum |

**TV deve estar no modo AV1** para receber sync e áudio da fonte externa.

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

| Componente | Qtd | Observação |
|-----------|-----|------------|
| 74HCT4053 (DIP ou SMD) | 1x | Mux analógico 3× 2:1 |
| Resistor 75Ω 1/4W | 3x | Terminação RGB |
| Capacitor eletrolítico 100µF 16V | 3x | Acoplamento AC |
| Resistor bias ~1kΩ 1/4W | 3x | Bias para IC751 |
| Resistor bias ~680Ω 1/4W | 3x | Divisor de bias |
| Conector compatível CN004/CN701 | 1x | Verificar passo e tipo in situ |
| Cabo para sinais RGB | — | Blindado |
| Chave ou transistor de controle | 1x | Para pino S do 74HCT4053 |

---

## Referências internas

- `circuits/cboard_rgb_amp.md` — IC751, CN701, resistores de entrada R/G/B
- `circuits/block006_av_inputs.md` — J901 pinagem, entradas AV1/SCART
- `circuits/voltage_waveform_table.md` — IC001 pinos 85/86/87 tensões
- `circuits/block001_processor.md` — IC001 TDA12009H visão geral
