# Stealth Controller Mini — SKiDL Schematic

A fully code-defined motor driver board featuring DRV8316 + ESP32 + MA702 + TWAI, written in SKiDL.

## Repository Structure

```
stealth-controller-mini/
│
├── driver_skidl.py              # SKiDL schematic source — run this to generate netlists
├── Library.kicad_sym            # Custom KiCad symbol library
├── DriverParts.pretty/          # Custom KiCad footprint library
├── Driver_skidl.net             # Generated netlist (output)
├── Driver_skidl.xml             # Generated XML netlist (output)
│
├── convert_netlist.py           # Utility: converts any KiCad .net to SKiDL
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── .gitignore                   # Files excluded from version control
```

---

## Components

| Reference | Part | Description |
|-----------|------|-------------|
| IC1 | ESP32-PICO-V3 | Main microcontroller |
| U1 | DRV8316TRGFR | 3-phase motor driver |
| IC2 | MA702GQ-P | Magnetic angle sensor |
| IC4 | SN65HVD230QDRG4 | CAN/TWAI transceiver |
| IC3 | LMR36506 | Power regulator |
| Boot1 | SW_Push_Dual | Boot/reset button |
| J1 | XT30PB | Power connector |
| L1 | Inductor | Power inductor |
| C1–C31 | Capacitors | Decoupling/filter caps |
| R1–R5 | Resistors | Pull-up/down resistors |
| JP1–JP5 | SolderJumpers | Configuration jumpers |
| OUT_A1/B1/C1 | S3B-ZR-SM4A-TF | Motor phase output connectors |
| TWAI1/2 | S3B-ZR-SM4A-TF | CAN bus connectors |
| UART1 | S3B-ZR-SM4A-TF | UART connector |

---

## Requirements

- Python 3.9+
- KiCad 9 installed on your machine
- SKiDL 2.2.3+

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/stealth-controller-mini.git
cd stealth-controller-mini
```

### 2. Install dependencies
```bash
pip install skidl
```

### 3. Add the footprint library to KiCad

The `DriverParts.pretty/` folder contains all custom footprints used in this board.
You need to register it in KiCad so PCBnew can find the footprints when importing the netlist.

**In KiCad:**
1. Go to **Preferences → Manage Footprint Libraries**
2. Click the **Project Libraries** tab
3. Click the **+** button
4. Set:
   - **Nickname:** `DriverParts`
   - **Library Path:** `${KIPRJMOD}/DriverParts.pretty`
   - **Plugin Type:** `KiCad`
5. Click **OK**

### 4. Add the symbol library to KiCad

The `Library.kicad_sym` file contains all custom schematic symbols.

**In KiCad:**
1. Go to **Preferences → Manage Symbol Libraries**
2. Click the **Project Libraries** tab
3. Click the **+** button
4. Set:
   - **Nickname:** `Library`
   - **Library Path:** `${KIPRJMOD}/Library.kicad_sym`
5. Click **OK**

---

## Generate Netlist

Make sure `Library.kicad_sym` is in the same folder as `driver_skidl.py`, then run:

```bash
python3 driver_skidl.py
```

This generates:
- `Driver_skidl.net` — KiCad netlist, import via **PCBnew → File → Import Netlist**
- `Driver_skidl.xml` — KiCad XML netlist for KiCad 6+

---

## Import into KiCad PCBnew

1. Open KiCad → open your project
2. Launch **PCBnew**
3. Go to **File → Import Netlist**
4. Select `Driver_skidl.net`
5. Click **Update PCB**

---

## Notes

- `Library.kicad_sym` and `DriverParts.pretty/` must be present for full KiCad integration
- SKiDL only requires `Library.kicad_sym` to generate the netlist — `DriverParts.pretty/` is only needed when opening in KiCad PCBnew
- The `fp-lib-table` warnings on first run are resolved once KiCad is installed and the footprint library is registered

---
