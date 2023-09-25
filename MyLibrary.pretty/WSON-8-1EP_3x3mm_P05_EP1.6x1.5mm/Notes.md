# KiCad Daughter Card Modifications
## Goals
- [x] Check the footprints on the 2 FDAs HGAIN/LGAIN
- [x] Create new footprints in my user library for them
- [x] Replace the footprints on the PCB design
- [x] adjust component placement
- [ ] check 3d render and gerber files

Mid Height of Area is y: 181.15mm

cap vertical offset:
178.64-181.15 = 2.51
178.54-181.15 = 2.61

Had to adjust wire widths for clearance errors on DRC

LMH6550_SOIC Footprint
-  Larger than previous footpring

## Building Daughter Card Needed PartList
- 10nF 0402
- 6.7$\mu$F 0402
- Substituted 59$\Omega$ for 49.9$\Omega$ resistors
- 

## Analog Shorting Baseline
 - R12 close to input pin
 - Transistor is U6 on daughtercard
 - Add LTC6752 to design
 - Voltage Divide 5V to ~0.5-1V
 - Branch it off of LGAIN since noise is not an issue for LGAIN
 - Google inverting comparator circuit, check recommended layouts
 - 