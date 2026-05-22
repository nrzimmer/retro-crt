# GEOM — Parâmetros de Geometria (Service Mode)

**Categoria:** GEOM | **Dispositivo:** TV-Processor (IC001) | **NVM:** IC003 EEPROM

## Acesso ao Service Mode

```
[DISPLAY] → [5] → [VOL+] → [POWER]  (com TV em standby)
```

- **Navegação:** [1]/[4] para item, [3]/[6] para valor
- **Gravar:** [MUTING] → [−]
- **4 modos independentes:** PAL 50Hz Normal, PAL 50Hz Wide, NTSC 60Hz Normal, NTSC 60Hz Wide

## Tabela de Parâmetros

| Item# | Nome | Range | Init | Função | Efeito físico / Hardware |
|---|---|---|---|---|---|
| 000 | HPOS | 0–63 | 31 | Horizontal Shift | Move toda a imagem E/O. IC001 modifica timing HOUT |
| 001 | HPAR | 0–63 | 31 | Horizontal Parallelogram | Corrige imagem em paralelogramo (linhas H inclinadas) |
| 002 | HBOW | 0–63 | 31 | Horizontal Bow | Corrige curvatura das linhas H (acima/abaixo do centro) |
| 003 | VLIN | 0–63 | 31 | Vertical Linearity | Equaliza espaçamento das linhas horizontais de cima a baixo |
| 004 | VSCR | 0–63 | 31 | Vertical Scroll | Move toda a imagem cima/baixo. **Não copiar ao mudar de modo** |
| 005 | HSIZ | 0–63 | 31 | EW Width | Largura H — amplitude sinal EWD IC001 pin21 → L802 → Q805 |
| 006 | EWPW | 0–63 | 31 | EW Parabola/Width | **Parâmetro principal de pincushion** — curvatura parábola EW → IC802 → Q806 |
| 007 | UCOP | 0–63 | 17 | EW Upper Corner Parabola | Pincushion cantos superiores — independente de LCOP |
| 008 | LCOP | 0–63 | 17 | EW Lower Corner Parabola | Pincushion cantos inferiores — independente de UCOP |
| 009 | EWTZ | 0–63 | 31 | EW Trapezoid | Corrige quando um lado vertical é maior que o outro |
| 010 | VSLP | 0–63 | 31 | Vertical Slope | Inclinação vertical |
| 011 | VSIZ | 0–63 | 15 | Vertical Amplitude | Altura da imagem |
| 012 | SCOR | 0–63 | 14 | S-Correction | Correção em S da varredura H — relacionado a Q808 (IRF614) |
| 013 | VPOS | 0–63 | 31 | Vertical Shift | Posição vertical da imagem |
| 014 | VZOM | 0–63 | 31 | Vertical Zoom | Zoom vertical |
| 015 | HBL | 0–1 | 1 | RGB Blanking Mode | — |
| 016 | WBF | 0–15 | 7 | Wide Blanking Timing F | Timing do blanking wide (frente) |
| 017 | WBR | 0–15 | varia | Wide Blanking Timing R | Timing do blanking wide (retorno) |
| 018 | SBL | 0–1 | 0 | Service Blanking | — |
| 019 | COPY | 0–1 | 0 | Copy GEO data | Copia dados GEOM de 50Hz para todas as áreas NVM 50/60Hz |

## Alvos de ajuste (HSIZ / VSIZ)

| Parâmetro | SPCB | PAL monoscope | NTSC monoscope |
|---|---|---|---|
| HSIZ (005) — largura | 16.4 cm | 14.6 cm | 15.3 cm |
| VSIZ (011) — altura | 12.4 cm | 11.3 cm | 11.5 cm |

## Sequência de ajuste — PAL 50Hz Normal

1. **VPOS (013)** — posicionar centro vertical
2. **VSIZ (011)** — ajustar altura (alvo 11.3cm PAL mono)
3. **HPOS (000)** — centralizar horizontalmente
4. **EWTZ (009)** — corrigir trapezoide
5. **HSIZ (005)** — ajustar largura (alvo 14.6cm PAL mono)
6. **HBOW (002)** — corrigir curva das linhas H
7. **EWPW (006)** — ajustar parábola EW (pincushion principal)
8. **UCOP (007)** — pincushion canto superior
9. **LCOP (008)** — pincushion canto inferior
10. **HPAR (001)** — corrigir paralelogramo
11. **SCOR (012)** — S-correction
12. **VLIN (003)** — linearidade vertical
13. **VSCR (004)** — scroll vertical (não copiar entre modos)

## Fluxo de trabalho para todos os 4 modos

1. Ajustar PAL 50Hz Normal (Wide=OFF)
2. Ativar Wide Mode ON → copiar todos PAL50 Normal → PAL50 Wide (exceto VSCR)
3. Ajustar NTSC 60Hz Normal (Wide=OFF)
4. Ativar Wide Mode ON → copiar todos NTSC60 Normal → NTSC60 Wide (exceto VSCR)
5. Reconfirmar VSIZ e VPOS em todos os modos
