# Circuits — Análise de Circuitos KV-21FS140

Análise dos blocos de circuito da A Board e C Board, parâmetros de service mode e diagnóstico.  
Baseado em ambos os manuais — diferenças entre rev_brazil e rev_s79aa são anotadas em cada arquivo.

## Arquivos

### Blocos de circuito (A Board)

| Arquivo | Bloco | Conteúdo |
|---------|-------|----------|
| [block001_processor.md](block001_processor.md) | Block 001 | IC001 One-Chip — System/Video/Audio Processor |
| [block002_audio.md](block002_audio.md) | Block 002 | IC200 Audio Amp (AN5276T / AN17804A) |
| [block003_psu.md](block003_psu.md) | Block 003 | SMPS — transformador T600, reguladores |
| [block004_deflection.md](block004_deflection.md) | Block 004 | Deflexão H/V — Q805, IC804, FBT T801, EW |
| [block005_if_tuner.md](block005_if_tuner.md) | Block 005 | IF — tuner, VIF SAW, SIF, AGC |
| [block006_av_inputs.md](block006_av_inputs.md) | Block 006 | Entradas AV, SCART, RGB |
| [cboard_rgb_amp.md](cboard_rgb_amp.md) | C Board | IC751 TDA6108AJF — RGB amp para cátodos do CRT |

### Service Mode e Diagnóstico

| Arquivo | Conteúdo |
|---------|----------|
| [self_diagnostic.md](self_diagnostic.md) | Códigos LED, diagnóstico por sintoma, proteções |
| [service_mode_categories.md](service_mode_categories.md) | Todas as categorias GEOM/WHBL/SADJ/etc. com valores por variante |
| [geom_service_params.md](geom_service_params.md) | Parâmetros GEOM detalhados, sequência de ajuste |
| [voltage_waveform_table.md](voltage_waveform_table.md) | Tensões nominais e formas de onda |

### Análise geral

| Arquivo | Conteúdo |
|---------|----------|
| [SCHEMATIC_ANALYSIS.md](SCHEMATIC_ANALYSIS.md) | Análise completa de todos os blocos do esquemático |
