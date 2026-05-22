# NES / Famicom — Mods RGB e Áudio

---

## RGB — NES não tem saída nativa

NES padrão (front-loader e top-loader USA) só tem saída **RF e composite**.  
RGB requer mod interno obrigatório.

| Modelo | RGB nativo | Notas |
|--------|-----------|-------|
| NES front-loader (USA) | ✗ | Mod obrigatório |
| NES top-loader (USA) | ✗ | Mod obrigatório |
| Famicom original (JP) | ✗ | Composite + RF apenas |
| AV Famicom (HVC-101) | ✗ RGB nativo | Composite + S-Video; sem RGB sem mod |
| Famicom Titler | ✓ | Raríssimo — saída RGB/S-Video nativa |

---

## Mods RGB disponíveis

| Mod | Saída | Conector instalado | Notas |
|-----|-------|-------------------|-------|
| **NESRGB** (Tim Worthington) | RGB analógico | Multi-out estilo SNES | Melhor opção — usa PPU original |
| PC-10 (Playchoice-10) | RGB analógico | Depende da instalação | Original Nintendo, difícil de encontrar |
| Hi-Def NES | HDMI digital | HDMI | Não usa SCART |
| UltraHDMI | HDMI digital | HDMI | Não usa SCART |

---

## PPU-LITE — alternativa open source ao NESRGB

**PPU-LITE** (andkorzh) — substituto FPGA do PPU, open source, custo reduzido.

| Aspecto | NESRGB (original) | PPU-LITE (open source) |
|---------|------------------|----------------------|
| Licença | Proprietário (Tim Worthington) | Open source — GitHub |
| PCB | 4 camadas | **2 camadas** — mais barato |
| FPGA | — | Cyclone I EP1C3T100C8N (Altera) ou Lattice LCMXO2 |
| Forma/tamanho | Referência | **Idêntico ao NESRGB** — mesmos adaptadores |
| Paletas (Cyclone) | — | 4: NES Classic, SONY CXA, Smooth, Natural Nestopia YUV |
| Paletas (Lattice) | — | 8: + CDIRECT, PC-10, PVM Style, WaveBeam |
| Seleção paleta | — | Jumpers J3/J4 (Cyclone) ou J3/J4/J5 (Lattice) |
| DAC | ADV7125 | R2R discreto com arrays de resistores |
| Venda | Tim Worthington / revendedores | Ninguém vendendo ainda — fabricar próprio |
| Instalação | Igual ao NESRGB | Igual ao NESRGB |

**Repositório:** https://github.com/andkorzh/PPU-LITE  
**Gerbers:** inclusos no repo — mandar fabricar JLCPCB/PCBWay  
**Upload FPGA:** somente arquivo `.jic` (Cyclone) ou equivalente Lattice — NÃO usar `.pof`

> PPU-LITE foi intencionalmente dimensionado igual ao NESRGB para reaproveitar todos os métodos de instalação e adaptadores existentes.

---

## Onde comprar

### Conector Multi-out para cabo DIY

| Fornecedor | Link | Notas |
|-----------|------|-------|
| Humble Bazooka | [SNES Multi-Out for NESRGB](https://www.humblebazooka.com/products/snes-style-multi-out-connector-for-nesrgb/) | Conector específico para instalar no NES |
| Console5 | [SNES/N64/GCN AV Multi-Out plug](https://console5.com/store/nintendo-snes-super-famicom-n64-av-multi-out-plug-for-custom-rgb-cables-repair.html) | Conector macho para o cabo (lado do cabo, não do console) |

### Mod NESRGB

| Fornecedor | Link | Notas |
|-----------|------|-------|
| 8BitMods (oficial) | [NESRGB by Tim Worthington](https://8bitmods.com/nesrgb-by-tim-worthington/) | Original — qualidade garantida, frete internacional |
| AliExpress (clone) | [1:1 copy NESRGB kit](https://www.aliexpress.com/item/1005006858950207.html) | Clone — "1:1 copy", funciona mas não é original |
| AliExpress (clone) | [NESRGB kit — busca geral](https://www.aliexpress.com/w/wholesale-nesrgb.html) | Vários vendedores, preços variados |
| AliExpress (clone) | [5× NESRGB PCB board](https://www.aliexpress.com/i/1005003035447719.html) | PCB avulso — precisa soldar componentes |
| **PPU-LITE (open source)** | [GitHub andkorzh/PPU-LITE](https://github.com/andkorzh/PPU-LITE) | Fabricar gerbers no JLCPCB — mais barato |

> **Clone AliExpress vs original:** clones "1:1" geralmente funcionam mas qualidade de fabricação varia. Para uso sério, preferir original da 8BitMods ou fabricar PPU-LITE pelos gerbers.

---

## Alternativas de vídeo ao RGB SCART

NES não tem saída component nativa. Opções além de RGB/SCART:

| Alternativa | Qualidade | Notas |
|------------|-----------|-------|
| NESRGB / PPU-LITE → SCART | ✓✓ Melhor analógico | Mod interno obrigatório |
| Hi-Def NES / UltraHDMI | ✓✓ Digital | HDMI direto, sem SCART |
| Upscaler (RetroTINK 2x) | ✓ Boa | Composite/S-Video → HDMI; sem mod no NES |
| S-Video (NES top-loader) | ✓ Razoável | Top-loader tem saída S-Video melhorada |
| Composite direto | Baixa | Sem mod; funciona com mod RGB da KV-21FS140 via AV2 |

> Não existe mod component para NES. RGB → SCART é o melhor analógico disponível.

---

## Mod Áudio

### Áudio mono (sem mod)

Sem nenhum mod de áudio, simplar o pino mono nos dois canais do SCART:

```
NES Audio (mono) ──┬──► SCART Pin 6  (Audio In L)
                   └──► SCART Pin 2  (Audio In R)
```

TV recebe mesmo sinal nos dois canais — ambos os alto-falantes funcionam.

### Mod "Stereo" (pseudo-stereo)

O NES tem APU com **duas saídas separadas antes do mixer interno**:

| Canal | Conteúdo |
|-------|---------|
| AUX A (canal 1) | Pulso 1 + Pulso 2 (square waves) |
| AUX B (canal 2) | Triângulo + Ruído + DPCM |

Não é stereo real — é separação dos grupos de canais do APU em duas saídas.

**Plain mod:**
- Desconectar AUX A e AUX B do mixer interno
- Adicionar cap 1µF em série em cada canal (polo − para o console)
- Adicionar conector de saída (RCA L/R ou P2 stereo)

**Mixback mod:**
- Tocar AUX A e AUX B sem desconectar do mixer
- Adicionar potenciômetro duplo para misturar o sinal mono de volta (controle de separação)
- Permite ajustar de mono completo a separação máxima

### Expansion Audio (Famicom)

Alguns cartuchos Famicom têm chips de som extras (VRC6, VRC7, MMC5, FDS, etc.) que misturam áudio adicional pelo pino 46 do slot de 60 pinos. No NES (72 pinos) esses pinos não existem — expansão é silenciada.

**O EverDrive N8 suporta expansion audio** — emula os chips de som nos mappers. Mas o NES front-loader precisa de mod para rotear esse áudio até a saída.

#### Mod expansion audio — NES front-loader com EverDrive N8 / flashcart 72 pinos

Soldar **resistor 47kΩ** entre dois pinos da porta de expansão (conector na parte inferior do front-loader):

```
Expansion pin 9  (EXP6) ── 47kΩ ──► Expansion pin 3  (Audio mix input)
```

Opcional mas recomendado para reduzir ruído:
```
Expansion pin 9  (EXP6) ── 1kΩ ──► Expansion pin 2  (GND)
```

> ⚠️ Não confundir **expansion pin 9 (EXP6)** com **expansion pin 6 (EXP9)** — nomes confusos intencionalmente.

**Com NESRGB instalado:** o NESRGB tem ponto de mix dedicado (hole próximo ao jumper J5). Soldar fio blindado 28AWG nesse ponto, passar resistor 47kΩ em série, conectar ao pino de expansão. Guia completo com fotos: [firebrandx.com/edn8tonesrgb.html](http://www.firebrandx.com/edn8tonesrgb.html)

**Volume:** EverDrive N8 firmware controla volume por mapper. Para VRC6, volume level 35 é o mais balanceado. Se necessário, substituir arquivo `EDFC/MAPS/024.RBF` na SD card pela versão fixada em volume 35.

**Adaptador potenciômetro (opcional):** em vez de resistor fixo 47kΩ, usar pot 100kΩ + resistor fixo 20kΩ em série — permite ajustar volume sem abrir o console.

#### Jogos com expansion audio (Famicom)

| Chip | Jogos notáveis |
|------|---------------|
| VRC6 | Castlevania III (JP), Akumajo Densetsu |
| VRC7 | Lagrange Point |
| MMC5 | Castlevania III (USA tem MMC5 — mas sem expansão no NES) |
| FDS | Metroid (JP), Zelda (JP), Gimmick! |
| Sunsoft 5B | Gimmick! |
| N163 | Megami Tensei II |

---

## Referências

- [NES RGB — RetroRGB](https://retrorgb.com/nesrgb.html)
- [NES "Stereo" Audio Mod — ConsoleMods](https://consolemods.org/wiki/NES:%22Stereo%22_Audio_Mod)
- [NES Expansion Audio Mod — ConsoleMods](https://consolemods.org/wiki/NES:Expansion_(EXP)_Audio_Mod)
- [EverDrive N8 + Expansion Audio + NESRGB — firebrandx.com](http://www.firebrandx.com/edn8tonesrgb.html)
