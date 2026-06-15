# Stealth Controller Mini

A fully code-defined motor driver board featuring **DRV8316**, **ESP32**, **MA702**, and **TWAI/CAN**, implemented entirely in **SKiDL**.

---

## Features

* Fully generated schematic using SKiDL
* DRV8316 3-phase motor driver
* ESP32-PICO-V3 microcontroller
* MA702 magnetic angle sensor
* CAN/TWAI communication interface
* Custom KiCad symbols and footprints
* Generates KiCad-compatible netlists directly from Python

---

## Repository Structure

```text
stealth-controller-mini/
│
├── driver_skidl.py              # Main SKiDL schematic source
├── Library.kicad_sym            # Custom symbol library
├── DriverParts.pretty/          # Custom footprint library
├── Driver_skidl.net             # Generated netlist
├── Driver_skidl.xml             # Generated XML netlist
│
├── convert_netlist.py           # KiCad netlist → SKiDL utility
├── requirements.txt             # Python dependencies
├── README.md
└── .gitignore
```

---

## Main Components

| Reference | Part            |
| --------- | --------------- |
| IC1       | ESP32-PICO-V3   |
| U1        | DRV8316TRGFR    |
| IC2       | MA702GQ-P       |
| IC3       | LMR36506        |
| IC4       | SN65HVD230QDRG4 |
| Boot1     | SW_Push_Dual    |
| J1        | XT30PB          |
| L1        | Inductor        |
| C1-C31    | Capacitors      |
| R1-R5     | Resistors       |
| JP1-JP5   | Solder Jumpers  |

---

## Requirements

* Python 3.9+
* KiCad 9+
* SKiDL 2.2.3+

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<username>/stealth-controller-mini.git
cd stealth-controller-mini
```

### Install Dependencies

```bash
pip install skidl
```

---

## Configure KiCad Libraries

### Symbol Library

Add `Library.kicad_sym`:

1. Preferences → Manage Symbol Libraries
2. Project Libraries → Add
3. Configure:

```text
Nickname: Library
Path: ${KIPRJMOD}/Library.kicad_sym
```

### Footprint Library

Add `DriverParts.pretty`:

1. Preferences → Manage Footprint Libraries
2. Project Libraries → Add
3. Configure:

```text
Nickname: DriverParts
Path: ${KIPRJMOD}/DriverParts.pretty
```

---

## Generate Netlists

Ensure `Library.kicad_sym` is located beside `driver_skidl.py`.

```bash
python3 driver_skidl.py
```

Generated outputs:

```text
Driver_skidl.net
Driver_skidl.xml
```

---

## Import into PCBnew

1. Open PCBnew
2. File → Import Netlist
3. Select `Driver_skidl.net`
4. Update PCB

---

## SKiDL Workflow

The schematic was recreated from KiCad using the following process:

1. Identify all components and footprints
2. Extract and verify schematic nets
3. Define all parts in SKiDL
4. Create power and signal nets
5. Connect pins to nets
6. Generate netlist and XML outputs
7. Verify against the original schematic

Example:

```python
U1 = Part(
    "Library",
    "DRV8316TRGFR",
    footprint="DriverParts:DRV8316",
    tag="U1"
)

vm = Net("VM")
gnd = Net("GND")

vm += U1["VM"]
gnd += U1["GND"]
```

---

## 3D Model Workflow

```text
SKiDL
   ↓
KiCad Netlist
   ↓
PCBnew Layout
   ↓
3D Viewer
   ↓
STEP / STL Export
```

Generated files:

```text
Driver.step
Driver.stl
```

---

## Notes

* `Library.kicad_sym` is required for SKiDL netlist generation.
* `DriverParts.pretty` is required when importing into KiCad PCBnew.
* PCB placement, routing, and 3D exports are performed in KiCad.
* SKiDL is used only for schematic generation and netlist creation.

---

## License

Add your preferred license information here.
