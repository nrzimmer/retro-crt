# Cabo SCART RGB — Super Nintendo / Super Famicom


## Conector MultiAV do SNES

Conector proprietário 12 pinos card-edge (macho no console).

| Pin | Sinal | Notas |
|-----|-------|-------|
| 1 | Red | RGB vermelho |
| 2 | Green | RGB verde |
| 3 | **CSYNC** (NTSC) / **+12V** (PAL) | ⚠️ DIFERENTE POR REGIÃO |
| 4 | Blue | RGB azul |
| 5 | GND | |
| 6 | GND | |
| 7 | Y (Luma) | S-Video Y — pode usar como sync alternativo |
| 8 | C (Chroma) | S-Video C |
| 9 | CVBS | Composite video |
| 10 | +5V | Alimentação — usar para blanking |
| 11 | Audio L | |
| 12 | Audio R | |

> **ATENÇÃO PAL:** Pin 3 = +12V no SNES PAL. Usar cabo NTSC em SNES PAL **danifica equipamentos**.

---

## Diagrama de fiação — SNES NTSC

```
MultiAV                  Componentes              SCART
────────                 ───────────              ─────
Pin 1  (R)  ──── C1+ ─ 220µF ─ C1- ────────────► Pin 15 (Red In)
Pin 2  (G)  ──── C2+ ─ 220µF ─ C2- ────────────► Pin 11 (Green In)
Pin 4  (B)  ──── C3+ ─ 220µF ─ C3- ────────────► Pin 7  (Blue In)
Pin 3  (CSYNC) ─────────────────────────────────► Pin 20 (Sync/CVBS In)
Pin 10 (+5V) ── R1 (820Ω) ─┬─ R2 (1kΩ) ─ GND  ► Pin 16 (Fast Blanking ~2.6V)
Pin 11 (Audio L) ──────────────────────────────► Pin 6  (Audio In L)
Pin 12 (Audio R) ──────────────────────────────► Pin 2  (Audio In R)
Pin 5/6 (GND) ─────────────────────────────────► Pins 4,5,9,13,17,18,21 (GNDs)
```

### Componentes

| Ref | Valor | Função |
|-----|-------|--------|
| C1, C2, C3 | 220µF 6.3V (ou 16V) eletrolítico | Remove DC offset (~1V) das linhas RGB |
| R1 | 820Ω | Divisor blanking (lado 5V) |
| R2 | 1kΩ | Divisor blanking (lado GND) → ~2.6V |

**Polaridade dos caps:** polo `+` para o console (pin MultiAV), polo `−` para o SCART.

---

## Diagrama de fiação — SNES PAL

```
MultiAV                  Componentes              SCART
────────                 ───────────              ─────
Pin 1  (R)  ──┬── R_term (75Ω) ── GND           ► Pin 15 (Red In)
Pin 2  (G)  ──┼── R_term (75Ω) ── GND           ► Pin 11 (Green In)
Pin 4  (B)  ──┴── R_term (75Ω) ── GND           ► Pin 7  (Blue In)
Pin 9  (CVBS) ─── 75Ω ─ GND  ──────────────────► Pin 20 (Sync/CVBS In)
Pin 7  (Luma) ──────────────────────────────────► Pin 20 (alternativa sync)
Pin 10 (+5V) ── divisor ────────────────────────► Pin 16 (Fast Blanking)
Pin 11 (Audio L) ──────────────────────────────► Pin 6  (Audio In L)
Pin 12 (Audio R) ──────────────────────────────► Pin 2  (Audio In R)
Pin 5/6 (GND) ─────────────────────────────────► GNDs
```

> PAL usa resistores 75Ω para terra (em vez de caps) para reduzir nível de contraste ao correto.  
> Pin 3 (+12V) **não conectar** ao SCART.

---

## Sync — opções para SNES NTSC

| Opção | Pino MultiAV | Qualidade | Notas |
|-------|-------------|-----------|-------|
| csync | Pin 3 | ✓✓ Melhor | Disponível em todos exceto 1CHIP-03 |
| Luma | Pin 7 | ✓ Boa | Funciona em todos; mais ruído HF |
| CVBS | Pin 9 | ✓ Aceitável | Sync embutido no composite |

**1CHIP-03 (raro):** não tem csync no MultiAV. Usar luma, ou restaurar csync com kit de componentes.

---

## Modelos SNES — compatibilidade

| Modelo | csync disponível | Notas |
|--------|-----------------|-------|
| SNES 1 original (NTSC) | ✓ (exceto 1CHIP-03) | Melhor qualidade RGB |
| SNES 1CHIP (1 e 2) | ✓ | Melhor qualidade de imagem |
| SNES 1CHIP-03 | ✗ | Faltam componentes; usar luma ou restaurar |
| SNES Mini (Super Famicom Jr.) | [Requer mod](../../consoles/snes/) | csync em pin 18 do chip S-RGB |
| SNES PAL | Pin 3 = +12V | Cabo diferente — ver seção PAL |

---

## Uso com mod RGB KV-21FS140

Para usar com o mod descrito em [`tv/mod_rgb/rgb_mod.md`](../../tv/mod_rgb/rgb_mod.md):

- Sync (csync) → AV2 VIDEO RCA (frontal) da TV
- RGB (R/G/B) → entrada do mod board (via 74HCT4053)
- Audio L/R → AV2 AUDIO RCA (frontal)
- Blanking (+5V via divisor) → pino S do 74HCT4053 (via BC547)

O mod já tem resistência de terminação (75Ω) e cap de acoplamento (47µF) — **não duplicar** esses componentes no cabo se usar com este mod específico.

---

## Referências

- [SNES RGB Cables / csync — RetroRGB](https://retrorgb.com/snescsync.html)
- [Nintendo MultiAV — GameSX](https://gamesx.com/wiki/doku.php?id=av:nintendomultiav)
- [Game Console SCART Diagrams — arcadecontrols mirror](https://mirrors.arcadecontrols.com/eviltim/eviltim/gamescart/gamescart.htm)
- [SNES DIY SCART Cable — sector.sunthar.com](https://sector.sunthar.com/guides/nintendo/snes/snes-diy-scart-cable.html)
