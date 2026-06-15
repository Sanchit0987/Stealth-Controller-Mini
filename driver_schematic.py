# ======================================================================
# SKiDL schematic : Driver Board (DRV8316 + ESP32 + MA702 + TWAI)
# Company          : Gadget Workbench
# Rev              : 0.2
# Source           : /mnt/user-data/uploads/Driver.net
# ======================================================================

import os

# ── Library path setup ───────────────────────────────────────────────
# Library.kicad_sym must be in the same folder as this script
_lib_dir = os.path.dirname(os.path.abspath(__file__))

# Set fp-lib-table for footprint resolution BEFORE importing skidl
for _fp in [
    os.path.expanduser("~/Library/Preferences/kicad/9.0/fp-lib-table"),
    os.path.expanduser("~/Library/Preferences/kicad/8.0/fp-lib-table"),
    os.path.expanduser("~/.config/kicad/9.0/fp-lib-table"),
    os.path.expanduser("~/.config/kicad/fp-lib-table"),
]:
    if os.path.isfile(_fp):
        os.environ["KICAD_FP_LIB_TABLE"] = _fp
        print(f"fp-lib  : {_fp}")
        break

from skidl import *

# Add project library folder to ALL KiCad search paths
# (must be done AFTER importing skidl)
for _key in lib_search_paths:
    if _key.startswith("kicad"):
        lib_search_paths[_key].append(_lib_dir)

print(f"sym-lib : {_lib_dir}/Library.kicad_sym")

# ── POWER RAILS ──────────────────────────────────────────────────────
gnd = Net('GND'); gnd.drive = POWER
vm = Net('VM'); vm.drive = POWER

# ── SIGNAL NETS ──────────────────────────────────────────────────────
net_3_3v = Net('3.3v')
boot_sw = Net('BOOT_SW')
can_rx = Net('CAN_RX')
can_tx = Net('CAN_TX')
drv_clk = Net('DRV_CLK')
drv_cs = Net('DRV_CS')
drv_csa = Net('DRV_CSA')
drv_csb = Net('DRV_CSB')
drv_csc = Net('DRV_CSC')
drv_off = Net('DRV_OFF')
drv_sdi = Net('DRV_SDI')
drv_sdo = Net('DRV_SDO')
en = Net('EN')
enc_clk = Net('ENC_CLK')
enc_cs = Net('ENC_CS')
enc_miso = Net('ENC_MISO')
enc_mosi = Net('ENC_MOSI')
enc_nd = Net('ENC_ND')
fault = Net('FAULT')
inha = Net('INHA')
inhb = Net('INHB')
inhc = Net('INHC')
inla = Net('INLA')
inlb = Net('INLB')
inlc = Net('INLC')
net_ic2_boot = Net('Net-(IC2-BOOT)')
net_ic2_rt = Net('Net-(IC2-RT)')
net_ic2_sw = Net('Net-(IC2-SW)')
net_ic3_pwm_dv = Net('Net-(IC3-PWM{slash}DV)')
net_ic3_ssck_en = Net('Net-(IC3-SSCK{slash}EN)')
net_ic3_ssd_nd = Net('Net-(IC3-SSD{slash}ND)')
net_ic4_canh = Net('Net-(IC4-CANH)')
net_ic4_canl = Net('Net-(IC4-CANL)')
net_ic4_rs = Net('Net-(IC4-RS)')
net_jp1_a = Net('Net-(JP1-A)')
net_u1_avdd = Net('Net-(U1-AVDD)')
net_u1_cp = Net('Net-(U1-CP)')
net_u1_cph = Net('Net-(U1-CPH)')
net_u1_cpl = Net('Net-(U1-CPL)')
net_u1_sw_bk = Net('Net-(U1-SW_BK)')
outa = Net('OUTA')
outb = Net('OUTB')
outc = Net('OUTC')
uart1 = Net('UART1')
uart2 = Net('UART2')
vref_ilim = Net('VREF_ILIM')
v_buck_out = Net('V_BUCK_OUT')

# ── PARTS ────────────────────────────────────────────────────────────
# Parts are loaded from Library.kicad_sym in the same folder as this script
Boot1 = Part('Library', 'SW_Push_Dual_XKB_Connectivity_TS-1177-B-B-B',  # Push button switch, generic, symbol, four pins
        footprint='DriverParts:XKB_Connectivity_TS-1177-B-B-B',
        tag='Boot1')
Boot1.ref   = 'Boot1'
Boot1.value = 'SW_Push_Dual'

C1 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C1')
C1.ref   = 'C1'
C1.value = '22uF'

C2 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C2')
C2.ref   = 'C2'
C2.value = '100nF'

C3 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0805_2012Metric',
        tag='C3')
C3.ref   = 'C3'
C3.value = '22uF'

C4 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C4')
C4.ref   = 'C4'
C4.value = '1uF'

C5 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C5')
C5.ref   = 'C5'
C5.value = '10nF'

C6 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C6')
C6.ref   = 'C6'
C6.value = '1uF'

C7 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C7')
C7.ref   = 'C7'
C7.value = '100nF'

C8 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C8')
C8.ref   = 'C8'
C8.value = '100nF'

C9 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C9')
C9.ref   = 'C9'
C9.value = '10uF'

C10 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C10')
C10.ref   = 'C10'
C10.value = '1uF'

C11 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C11')
C11.ref   = 'C11'
C11.value = '2.2uF'

C12 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C12')
C12.ref   = 'C12'
C12.value = '100nF'

C13 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C13')
C13.ref   = 'C13'
C13.value = '1uF'

C14 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C14')
C14.ref   = 'C14'
C14.value = '100nF'

C15 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C15')
C15.ref   = 'C15'
C15.value = '22uF'

C16 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C16')
C16.ref   = 'C16'
C16.value = '22uF'

C17 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C17')
C17.ref   = 'C17'
C17.value = '100nF'

C18 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C18')
C18.ref   = 'C18'
C18.value = '10uF'

C19 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C19')
C19.ref   = 'C19'
C19.value = '100nF'

C20 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0603_1608Metric',
        tag='C20')
C20.ref   = 'C20'
C20.value = '10uF'

C21 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0805_2012Metric',
        tag='C21')
C21.ref   = 'C21'
C21.value = '22uF 25v'

C22 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0805_2012Metric',
        tag='C22')
C22.ref   = 'C22'
C22.value = '22uF 25v'

C23 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0805_2012Metric',
        tag='C23')
C23.ref   = 'C23'
C23.value = '22uF 25v'

C24 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0805_2012Metric',
        tag='C24')
C24.ref   = 'C24'
C24.value = '22uF 25v'

C25 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0805_2012Metric',
        tag='C25')
C25.ref   = 'C25'
C25.value = '22uF 25v'

C26 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0805_2012Metric',
        tag='C26')
C26.ref   = 'C26'
C26.value = '22uF 25v'

C29 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0805_2012Metric',
        tag='C29')
C29.ref   = 'C29'
C29.value = '22uF 25v'

C30 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0805_2012Metric',
        tag='C30')
C30.ref   = 'C30'
C30.value = '22uF 25v'

C31 = Part('Library', 'C',  # Unpolarized capacitor
        footprint='Capacitor_SMD:C_0805_2012Metric',
        tag='C31')
C31.ref   = 'C31'
C31.value = '22uF 25v'

IC1 = Part('Library', 'ESP32-PICO-V3',  # RF System on a Chip - SoC Module WiFi LGA Dual Core BT Combo
        footprint='DriverParts:ESP32PICOV3',
        tag='IC1')
IC1.ref   = 'IC1'
IC1.value = 'ESP32-PICO-V3'

IC2 = Part('Library', 'LMR36506',
        footprint='DriverParts:LMR36506',
        tag='IC2')
IC2.ref   = 'IC2'
IC2.value = 'LMR36506'

IC3 = Part('Library', 'MA702GQ-P',  # Board Mount Hall Effect / Magnetic Sensors 12-bit, digital, contactless angle sensor with ABZ incremental & PWM outputs
        footprint='DriverParts:MA702',
        tag='IC3')
IC3.ref   = 'IC3'
IC3.value = 'MA702GQ-P'

IC4 = Part('Library', 'SN65HVD230QDRG4',  # 3.3-V CAN Transceiver with Standby Mode
        footprint='DriverParts:SN65HVD230QDR',
        tag='IC4')
IC4.ref   = 'IC4'
IC4.value = 'SN65HVD230QDRG4'

J1 = Part('Library', 'XT30PB',  # Mini XT30 Connector
        footprint='DriverParts:XT30PB',
        tag='J1')
J1.ref   = 'J1'
J1.value = 'XT30PB'

JP1 = Part('Library', 'SolderJumper_2_Open',  # Solder Jumper, 2-pole, open
        footprint='Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm',
        tag='JP1')
JP1.ref   = 'JP1'
JP1.value = 'SolderJumper_2_Open'

JP2 = Part('Library', 'SolderJumper_3_Bridged12',  # 3-pole Solder Jumper, pins 1+2 closed/bridged
        footprint='Jumper:SolderJumper-3_P1.3mm_Open_RoundedPad1.0x1.5mm_NumberLabels',
        tag='JP2')
JP2.ref   = 'JP2'
JP2.value = 'SolderJumper_3_Bridged12'

JP3 = Part('Library', 'SolderJumper_2_Bridged',  # Solder Jumper, 2-pole, closed/bridged
        footprint='Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm',
        tag='JP3')
JP3.ref   = 'JP3'
JP3.value = 'SolderJumper_2_Bridged'

JP4 = Part('Library', 'SolderJumper_2_Bridged',  # Solder Jumper, 2-pole, closed/bridged
        footprint='Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm',
        tag='JP4')
JP4.ref   = 'JP4'
JP4.value = 'SolderJumper_2_Bridged'

JP5 = Part('Library', 'SolderJumper_3_Bridged12',  # 3-pole Solder Jumper, pins 1+2 closed/bridged
        footprint='Jumper:SolderJumper-3_P1.3mm_Open_RoundedPad1.0x1.5mm_NumberLabels',
        tag='JP5')
JP5.ref   = 'JP5'
JP5.value = 'SolderJumper_3_Bridged12'

L1 = Part('Library', 'pspice_INDUCTOR',
        footprint='Inductor_SMD:L_1210_3225Metric',
        tag='L1')
L1.ref   = 'L1'
L1.value = '15uH'

OUT_A1 = Part('Library', 'MountingHole_Pad',  # Mounting Hole with connection
        footprint='DriverParts:Motor_Wire_Solder_Pad',
        tag='OUT_A1')
OUT_A1.ref   = 'OUT_A1'
OUT_A1.value = 'MountingHole_Pad'

OUT_B1 = Part('Library', 'MountingHole_Pad',  # Mounting Hole with connection
        footprint='DriverParts:Motor_Wire_Solder_Pad',
        tag='OUT_B1')
OUT_B1.ref   = 'OUT_B1'
OUT_B1.value = 'MountingHole_Pad'

OUT_C1 = Part('Library', 'MountingHole_Pad',  # Mounting Hole with connection
        footprint='DriverParts:Motor_Wire_Solder_Pad',
        tag='OUT_C1')
OUT_C1.ref   = 'OUT_C1'
OUT_C1.value = 'MountingHole_Pad'

R1 = Part('Library', 'R',  # Resistor
        footprint='Resistor_SMD:R_0603_1608Metric',
        tag='R1')
R1.ref   = 'R1'
R1.value = '22'

R2 = Part('Library', 'R',  # Resistor
        footprint='Resistor_SMD:R_0603_1608Metric',
        tag='R2')
R2.ref   = 'R2'
R2.value = '5.1k'

R3 = Part('Library', 'R',  # Resistor
        footprint='Resistor_SMD:R_0603_1608Metric',
        tag='R3')
R3.ref   = 'R3'
R3.value = '10K'

R4 = Part('Library', 'R',  # Resistor
        footprint='Resistor_SMD:R_0603_1608Metric',
        tag='R4')
R4.ref   = 'R4'
R4.value = '10K'

R5 = Part('Library', 'R',  # Resistor
        footprint='Resistor_SMD:R_0603_1608Metric',
        tag='R5')
R5.ref   = 'R5'
R5.value = '120'

Reset1 = Part('Library', 'SW_Push_Dual_XKB_Connectivity_TS-1177-B-B-B',  # Push button switch, generic, symbol, four pins
        footprint='DriverParts:XKB_Connectivity_TS-1177-B-B-B',
        tag='Reset1')
Reset1.ref   = 'Reset1'
Reset1.value = 'SW_Push_Dual'

TWAI1 = Part('Library', 'S3B-ZR-SM4A-TF',
        footprint='DriverParts:SHDR3W50P0X150',
        tag='TWAI1')
TWAI1.ref   = 'TWAI1'
TWAI1.value = 'TWAI'

TWAI2 = Part('Library', 'S3B-ZR-SM4A-TF',
        footprint='DriverParts:SHDR3W50P0X150',
        tag='TWAI2')
TWAI2.ref   = 'TWAI2'
TWAI2.value = 'TWAI'

U1 = Part('Library', 'DRV8316TRGFR',
        footprint='DriverParts:DRV8316',
        tag='U1')
U1.ref   = 'U1'
U1.value = 'DRV8316R'

UART1 = Part('Library', 'S3B-ZR-SM4A-TF',
        footprint='DriverParts:SHDR3W50P0X150',
        tag='UART1')
UART1.ref   = 'UART1'
UART1.value = 'UART'

# ── CONNECTIONS ──────────────────────────────────────────────────────
net_3_3v += C15['1'], C16['1'], C17['1'], C18['1'], C19['1'], C20['1'], C8['1'], C9['1'], IC1['1'], IC1['19'], IC1['26'], IC1['3'], IC1['37'], IC1['4'], IC1['43'], IC1['46'], IC2['8'], IC3['13'], IC4['3'], JP2['3'], L1['2'], R2['1'], R3['1'], U1['23']
boot_sw += Boot1['3'], Boot1['4'], IC1['23']
can_rx += IC1['10'], IC4['4']
can_tx += IC1['32'], IC4['1']
drv_clk += IC1['38'], U1['35']
drv_cs += IC1['34'], U1['36']
drv_csa += IC1['5'], U1['40']
drv_csb += IC1['6'], U1['39']
drv_csc += IC1['7'], U1['38']
drv_off += IC1['33'], U1['21']
drv_sdi += IC1['39'], U1['34']
drv_sdo += IC1['42'], U1['33']
en += C10['1'], IC1['9'], R3['2'], Reset1['3'], Reset1['4']
enc_clk += IC1['20'], IC3['12']
enc_cs += IC1['24'], IC3['5']
enc_miso += IC1['21'], IC3['7']
enc_mosi += IC1['27'], IC3['4']
enc_nd += IC1['8'], JP5['2']
fault += IC1['11'], R2['2'], U1['22']
gnd += Boot1['1'], Boot1['2'], C1['2'], C10['2'], C11['2'], C12['2'], C13['2'], C15['2'], C16['2'], C17['2'], C18['2'], C19['2'], C2['2'], C20['2'], C21['2'], C22['2'], C23['2'], C24['2'], C25['2'], C26['2'], C29['2'], C3['2'], C30['2'], C31['2'], C6['1'], C7['1'], C8['2'], C9['2'], IC1['49'], IC2['9'], IC3['10'], IC3['17'], IC3['8'], IC4['2'], J1['1'], JP2['1'], JP3['2'], R4['2'], Reset1['1'], Reset1['2'], TWAI1['1'], TWAI2['1'], U1['12'], U1['15'], U1['18'], U1['2'], U1['26'], U1['4'], U1['41'], UART1['1']
inha += IC1['18'], U1['27']
inhb += IC1['16'], U1['29']
inhc += IC1['13'], U1['31']
inla += IC1['17'], U1['28']
inlb += IC1['15'], U1['30']
inlc += IC1['12'], U1['32']
net_ic2_boot += C14['1'], IC2['6']
net_ic2_rt += C13['1'], IC2['1'], IC2['7']
net_ic2_sw += C14['2'], IC2['5'], L1['1']
net_ic3_pwm_dv += IC3['9'], JP5['3']
net_ic3_ssck_en += IC3['15'], JP2['2']
net_ic3_ssd_nd += IC3['1'], JP5['1']
net_ic4_canh += IC4['7'], R5['1'], TWAI1['3'], TWAI2['3']
net_ic4_canl += IC4['6'], JP1['2'], TWAI1['2'], TWAI2['2']
net_ic4_rs += IC4['8'], R4['1']
net_jp1_a += JP1['1'], R5['2']
net_u1_avdd += C6['2'], U1['25']
net_u1_cp += C4['1'], U1['8']
net_u1_cph += C5['1'], U1['7']
net_u1_cpl += C5['2'], U1['6']
net_u1_sw_bk += R1['1'], U1['5']
outa += OUT_A1['1'], U1['13'], U1['14']
outb += OUT_B1['1'], U1['16'], U1['17']
outc += OUT_C1['1'], U1['19'], U1['20']
uart1 += IC1['41'], UART1['3']
uart2 += IC1['40'], UART1['2']
vm += C11['1'], C12['1'], C2['1'], C21['1'], C22['1'], C23['1'], C24['1'], C25['1'], C26['1'], C29['1'], C3['1'], C30['1'], C31['1'], C4['2'], IC2['3'], IC2['4'], J1['2'], U1['10'], U1['11'], U1['9']
vref_ilim += C7['2'], IC1['14'], U1['37']
v_buck_out += C1['1'], R1['2'], U1['3']

# ── EXPORT ───────────────────────────────────────────────────────────
# KiCad netlist — import in PCBnew via File → Import Netlist
generate_netlist(file_='Driver_skidl.net')

# KiCad XML netlist — for KiCad 6+
generate_xml(file_='Driver_skidl.xml')

print("✓ Exported: Driver_skidl.net")
print("✓ Exported: Driver_skidl.xml")