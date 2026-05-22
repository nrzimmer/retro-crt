# Cabo SCART RGB — PlayStation 2
---

## Conector AV — mesmo do PS1

Conector proprietário Sony 12 pinos — **idêntico ao PS1 e PSone**.  
Pinagem igual ao PS1 (ver [`ps1.md`](ps1.md)).

---

## Diferença crítica em relação ao PS1: capacitores

| Console | Caps 220µF nas linhas RGB | Onde estão os caps |
|---------|--------------------------|-------------------|
| PS1 | ✗ Não tem internamente | **Devem estar no cabo** |
| PS2 | ✓ Já tem internamente | Cabo não precisa |

**Consequência:** cabo PS1 e cabo PS2 **não são intercambiáveis**.

- Usar cabo PS2 (sem caps) no PS1 → imagem com DC offset, possível dano ao display
- Usar cabo PS1 (com caps) no PS2 → double-cap na linha → atenuação e distorção de sinal

---

## Fiação PS2 → SCART

```
PS2 AV                   Componentes              SCART
──────                   ───────────              ─────
Pin 11 (R) ──────────────────────────────────►  Pin 15 (Red In)
Pin 12 (G) ──────────────────────────────────►  Pin 11 (Green In)
Pin 9  (B) ──────────────────────────────────►  Pin 7  (Blue In)
Pin 6  (CSync) ──────────────────────────────►  Pin 20 (Sync In)
Pin 10 (+5V) ── R1 (820Ω) ─┬─ R2 (1kΩ) ─ GND ► Pin 16 (Blanking)
Pin 4  (Audio L) ────────────────────────────►  Pin 6  (Audio In L)
Pin 2  (Audio R) ────────────────────────────►  Pin 2  (Audio In R)
Pin 1,3,8 (GND) ─────────────────────────────►  Pins GND
```

Sem caps nas linhas RGB (PS2 já tem internamente).

---

## Resoluções e compatibilidade com KV-21FS140

| Modo | Freq H | Compatível |
|------|--------|-----------|
| 240p | 15.7 kHz | ✓ |
| 480i | 15.7 kHz | ✓ |
| 480p | 31.5 kHz | ✗ — muitos jogos forçam este modo |
| 1080i | 33.75 kHz | ✗ |

**Problema PS2:** grande parte dos jogos força 480p automaticamente → imagem some no KV-21FS140.  
Solução: forçar 480i via menu do PS2 (configurações de vídeo) ou usar adaptador (RetroTINK 2x-Mini).

---

## Contexto histórico — como o PS2 era usado na época

Na época do lançamento (2000–2006), **99% dos jogadores usavam cabo composite** (RCA amarelo/branco/vermelho) incluído na caixa, em CRTs consumer comuns — exatamente o tipo da KV-21FS140.

**O problema do 480p não existia na prática porque:**
- Cabo composite na caixa → PS2 detecta composite → força 480i automaticamente
- 480p só ativa quando PS2 detecta **cabo componente conectado**
- TVs com entrada componente eram raras até 2003–2004

**Conclusão:** usar composite ou RGB SCART na KV-21FS140 reproduz fielmente a experiência original. O "problema do 480p" é autoinfligido pelo uso de cabo componente.

---

## Opções de vídeo para PS2 na KV-21FS140

| Cabo | Entrada TV | Qualidade | 480p | Notas |
|------|-----------|-----------|------|-------|
| Composite (RCA) | AV frontal | Baixa | ✗ (força 480i) | Como na época — sem problema |
| RGB SCART | Mod CN004 | **Alta** | ✗ (imagem some) | Melhor qualidade, problema nos jogos 480p |
| Componente (Y/Pb/Pr) | J901 | Alta | ✗ (imagem some) | Qualidade similar ao SCART |

> **J901** (entrada componente da KV-21FS140) aceita PS2 via cabo componente para conteúdo 480i — sem mod adicional necessário.

### Solução para jogos 480p

Jogos que forçam 480p mesmo com SCART/componente: forçar 480i nas configurações do PS2:
`Browser → Config do Sistema → Saída por Componente → desativar`

Alguns jogos ignoram essa configuração e forçam 480p de qualquer forma — nesses casos não há solução no CRT 15kHz sem upscaler externo.

### Upscalers — se quiser jogar 480p

| Dispositivo | Entrada | Saída | 480p | Custo |
|------------|---------|-------|------|-------|
| OSSC | SCART / Componente | HDMI | ✓ | ~U$150 |
| RetroTINK 5X Pro | SCART / Componente | HDMI | ✓ | ~U$250 |
| RetroTINK 2x-Mini | Composite / S-Video | HDMI | ✗ (só 15kHz) | ~U$60 |

Todos saem em HDMI — requerem TV moderna. Não existe upscaler que converta 480p de volta para sinal analógico 15kHz para usar no CRT.

---

## Referências

- [Differences PS1 vs PS2 cable — ASSEMblergames archive](https://assemblergames.org/viewtopic.php?t=9085)
- [Game Console SCART Diagrams — arcadecontrols mirror](https://mirrors.arcadecontrols.com/eviltim/eviltim/gamescart/gamescart.htm)
