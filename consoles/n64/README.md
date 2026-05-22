# Nintendo 64 — Mod RGB

---

## ⚠️ N64 NTSC não tem saída RGB nativa

N64 NTSC **não envia RGB pelo MultiAV** sem modificação interna.  
Os pinos físicos R/G/B existem no MultiAV mas não estão conectados internamente.

| Região | RGB nativo | Notas |
|--------|-----------|-------|
| NTSC (USA/JP) | ✗ — mod obrigatório | Pinos RGB presentes mas não conectados |
| PAL (EUR) | Alguns modelos sim | Verificar revisão da placa |
| NUS-CPU-01/02 (NTSC) | Partial | csync presente no pin 3, mas RGB ainda precisa de mod |

---

## Mods RGB disponíveis

| Mod | Saída | Notas |
|-----|-------|-------|
| UltraHDMI | Digital HDMI | Não usa MultiAV RGB |
| N64Digital | Digital HDMI | Não usa MultiAV RGB |
| RGB amp (THS7314/THS7316) | Analógico MultiAV | Habilita saída RGB para cabo SCART |
| Tim Worthington N64 RGB | Analógico MultiAV | Habilita csync limpo |

Para usar cabo SCART, instalar mod analógico (THS7316 ou equivalente).

---

## Referências

- [N64 RGB Mod — RetroRGB](https://retrorgb.com/n64rgbmod.html)
- [N64 RGB Cable / csync — RetroRGB](https://retrorgb.com/n64cablecsync.html)
