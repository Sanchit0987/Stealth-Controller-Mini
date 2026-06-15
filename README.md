# Stealth Controller Mini — SKiDL Schematic

Motor driver board (DRV8316 + ESP32 + MA702 + TWAI) defined in SKiDL.

## Files
| File | Description |
|------|-------------|
| `driver_skidl.py` | SKiDL schematic source |
| `Library.kicad_sym` | Custom KiCad symbol library |
| `Driver.net` | Original KiCad netlist (reference) |

## Requirements
- Python 3.9+
- KiCad 9 installed (for symbol/footprint libraries)
- SKiDL

## Setup
```bash
pip install skidl
```

Place `Library.kicad_sym` in the same folder as `driver_skidl.py`.

## Generate Netlist
```bash
python3 driver_skidl.py
```
Outputs:
- `Driver_skidl.net` — import into KiCad PCBnew via File → Import Netlist
- `Driver_skidl.xml` — KiCad XML format for KiCad 6+

## Components
- ESP32-PICO-V3 — main microcontroller
- DRV8316TRGFR — motor driver
- MA702GQ-P — magnetic angle sensor
- SN65HVD230 — CAN transceiver
- LMR36506 — power regulator