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
How the SKiDL Schematic Was Created

This section explains the full process of how the original KiCad schematic
was studied and recreated as a SKiDL Python file.


Step 1 — Open the schematic in KiCad and identify all components


Open KiCad and load the project
Open the Schematic Editor
Go through every component on the schematic and note down:

Reference (e.g. U1, C1, R1)
Value (e.g. DRV8316TRGFR, 22uF, 10k)
Symbol library it belongs to (shown in component properties)
Footprint assigned to it (e.g. DriverParts:DRV8316)



Click each component → Properties to confirm the exact symbol name
and footprint string



Step 2 — Identify all nets


In the Schematic Editor, go to Inspect → Net Navigator or
Tools → Highlight Net to see all named nets
Note down every net name (e.g. GND, 3.3V, SPI_MOSI, PWM_A)
Power nets (GND, VM, +3V3) are treated separately as power rails
Alternatively export the netlist via File → Export → Netlist and
read the net names directly from the .net file



Step 3 — Add the symbol library to KiCad globally

The Library.kicad_sym file contains all custom symbols used in this project.
Add it to KiCad so symbols resolve correctly:


In KiCad go to Preferences → Manage Symbol Libraries
Click the Global Libraries tab (so it's available to all projects)
Click the + button at the bottom
Fill in:

Nickname: Library
Library Path: full path to Library.kicad_sym on your machine
e.g. /Users/yourname/stealth-controller-mini/Library.kicad_sym
Plugin Type: KiCad



Click OK and save



Step 4 — Add the footprint library to KiCad globally

The DriverParts.pretty/ folder contains all custom footprints:


In KiCad go to Preferences → Manage Footprint Libraries
Click the Global Libraries tab
Click the + button
Fill in:

Nickname: DriverParts
Library Path: full path to DriverParts.pretty/ on your machine
e.g. /Users/yourname/stealth-controller-mini/DriverParts.pretty
Plugin Type: KiCad



Click OK and save



Step 5 — Copy the symbol library into the project folder

For SKiDL to find Library.kicad_sym automatically at runtime, place it
in the same folder as driver_skidl.py:

stealth-controller-mini/
├── driver_skidl.py
├── Library.kicad_sym    ← must be here
└── ...

SKiDL uses this at the top of the script:

python_lib_dir = os.path.dirname(os.path.abspath(__file__))
lib_search_paths['kicad9'].append(_lib_dir)

This tells SKiDL to look in the script's own folder for any .kicad_sym files.


Step 6 — Define components in SKiDL

Each component from the schematic is defined as a Part() call, referencing
the symbol from Library.kicad_sym and the footprint from DriverParts.pretty/:

python# Syntax
ref = Part('LibraryNickname', 'SymbolName',
           footprint='FootprintLib:FootprintName',
           tag='REF')
ref.ref   = 'REF'
ref.value = 'VALUE'

# Example — motor driver IC
U1 = Part('Library', 'DRV8316TRGFR',
          footprint='DriverParts:DRV8316',
          tag='U1')
U1.ref   = 'U1'
U1.value = 'DRV8316R'

# Example — decoupling capacitor
C1 = Part('Library', 'C',
          footprint='DriverParts:C_0402',
          tag='C1')
C1.ref   = 'C1'
C1.value = '100nF'

Repeat this for all 54 components in the schematic.


Step 7 — Define power rails and signal nets

Power rails are defined with drive = POWER so SKiDL treats them correctly:

python# Power rails
gnd = Net('GND'); gnd.drive = POWER
vm  = Net('VM');  vm.drive  = POWER

# Signal nets — one for each named net in the schematic
spi_mosi  = Net('SPI_MOSI')
spi_miso  = Net('SPI_MISO')
spi_clk   = Net('SPI_CLK')
pwm_a     = Net('PWM_A')
can_tx    = Net('CAN_TX')
# ... and so on for all nets


Step 8 — Create connections

Connect component pins to nets using the += operator.
Pin numbers or pin names from the symbol are used inside []:

python# Connect by pin number
gnd += U1['GND'], C1['2'], C2['2']

# Connect by pin name
vm  += U1['VM'], L1['1']

# Signal net connections
spi_mosi += IC1['IO13'], U1['SDI']
spi_miso += IC1['IO12'], U1['SDO']
spi_clk  += IC1['IO14'], U1['SCLK'], IC2['CLK']

Cross-reference each connection against the schematic's wire connections
to make sure every pin is accounted for.


Step 9 — Generate and export the netlist

At the bottom of the script, add the export calls:

python# Generates Driver_skidl.net — import in KiCad PCBnew via File → Import Netlist
generate_netlist(file_='Driver_skidl.net')

# Generates Driver_skidl.xml — KiCad XML format for KiCad 6+
generate_xml(file_='Driver_skidl.xml')

Then run:

bashpython3 driver_skidl.py


Step 10 — Verify the netlist

To confirm the generated netlist matches the original:

bash# Quick structural diff
diff Driver.net Driver_skidl.net

Or import it into KiCad PCBnew and check for any unmatched footprints or
missing connections:


Open PCBnew
File → Import Netlist → Driver_skidl.net
Click Update PCB
KiCad will report any mismatches



About the 3D Files

The Driver.step and Driver.stl files in this repo are the 3D models of
the completed PCB board. They were produced through the following workflow:

KiCad Schematic (.kicad_sch)
        ↓
KiCad PCBnew — component placement + trace routing (.kicad_pcb)
        ↓
KiCad 3D Viewer — verify component 3D models
        ↓
File → Export → STEP  →  Driver.step
File → Export → STL   →  Driver.stl

SKiDL's role in this pipeline is only the first step — generating the
netlist that feeds into KiCad PCBnew. The physical placement of components,
routing of copper traces, and 3D export are all done inside KiCad and are
outside the scope of SKiDL.



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
