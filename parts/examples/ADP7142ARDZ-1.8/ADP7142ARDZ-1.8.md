# 40 V, 200 mA, Low Noise, CMOS LDO Linear Regulator 

## FEATURES

- Low noise: $11 \mu \mathrm{~V}$ rms independent of fixed output voltage
- PSRR of 88 dB at $10 \mathrm{kHz}, 68 \mathrm{~dB}$ at $100 \mathrm{kHz}, 50 \mathrm{~dB}$ at 1 MHz , $\mathrm{V}_{\text {OUT }} \leq 5 \mathrm{~V}, \mathrm{~V}_{\mathrm{IN}}=7 \mathrm{~V}$
- Input voltage range: 2.7 V to 40 V
- Maximum output current: 200 mA
- Initial accuracy: $\pm 0.8 \%$
- Accuracy over line, load, and temperature
- $-1.2 \%$ to $+1.5 \%, T_{J}=-40^{\circ} \mathrm{C}$ to $+85^{\circ} \mathrm{C}$
- $\pm 1.8 \%, T_{J}=-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$
- Low dropout voltage: 200 mV (typical) at a 200 mA load, $\mathrm{V}_{\text {OUT }}=$ 5 V
- User programmable soft start (LFCSP and SOIC only)
- Low quiescent current, $\mathrm{I}_{\mathrm{GND}}=50 \mu \mathrm{~A}$ (typical) with no load
- Low shutdown current: $1.8 \mu \mathrm{~A}$ at $\mathrm{V}_{\mathrm{IN}}=6 \mathrm{~V}, 3.0 \mu \mathrm{~A}$ at $\mathrm{V}_{\mathrm{IN}}=40 \mathrm{~V}$
- Stable with a small $2.2 \mu \mathrm{~F}$ ceramic output capacitor
- Fixed output voltage options: $1.8 \mathrm{~V}, 2.5 \mathrm{~V}, 3.3 \mathrm{~V}, 3.8 \mathrm{~V}$, and 5.0 V
- 15 standard voltages between 1.2 V and 5.0 V are available
- Adjustable output from 1.2 V to $\mathrm{V}_{\mathrm{IN}}-\mathrm{V}_{\mathrm{DO}}$, output can be adjusted above initial set point
- Precision enable
- $2 \mathrm{~mm} \times 2 \mathrm{~mm}, 6$-lead LFCSP, 8-Lead SOIC, 5-Lead TSOT
- AEC-Q100 qualified for automotive applications


## APPLICATIONS

- Regulation to noise sensitive applications
- ADC, DAC circuits, precision amplifiers, power for VCO V $V_{\text {TUNE }}$ control
- Communications and infrastructure
- Medical and healthcare
- Industrial and instrumentation
- Automotive


## TYPICAL APPLICATION CIRCUITS

![img-0.jpeg](img-0.jpeg)

Figure 1. ADP7142 with Fixed Output Voltage, 5 V
![img-1.jpeg](img-1.jpeg)

Figure 2. ADP7142 with 5 V Output Adjusted to 6 V

## GENERAL DESCRIPTION

The ADP7142 is a CMOS, low dropout (LDO) linear regulator that operates from 2.7 V to 40 V and provides up to 200 mA of output current. This high input voltage LDO is ideal for the regulation of high performance analog and mixed signal circuits operating from 39 V down to 1.2 V rails. Using an advanced proprietary architecture, the device provides high power supply rejection, low noise, and achieves excellent line and load transient response with a small $2.2 \mu \mathrm{~F}$ ceramic output capacitor. The ADP7142 regulator output noise is $11 \mu \mathrm{~V}$ rms independent of the output voltage for the fixed options of 5 V or less.

The ADP7142 is available in 15 fixed output voltage options. The following voltages are available from stock: 1.2 V (adjustable), 1.8 $\mathrm{V}, 2.5 \mathrm{~V}, 3.3 \mathrm{~V}, 3.8 \mathrm{~V}$, and 5.0 V . Additional voltages available by special order are $1.5 \mathrm{~V}, 1.85 \mathrm{~V}, 2.0 \mathrm{~V}, 2.2 \mathrm{~V}, 2.75 \mathrm{~V}, 2.8 \mathrm{~V}, 2.85 \mathrm{~V}$, $3.0 \mathrm{~V}, 4.2 \mathrm{~V}$, and 4.6 V .

Each fixed output voltage can be adjusted above the initial set point with an external feedback divider. This allows the ADP7142 to provide an output voltage from 1.2 V to $\mathrm{V}_{\mathrm{IN}}-\mathrm{V}_{\mathrm{DO}}$ with high PSRR and low noise.

User programmable soft start with an external capacitor is available in the LFCSP and SOIC packages.

The ADP7142 is available in a 6-lead, $2 \mathrm{~mm} \times 2 \mathrm{~mm}$ LFCSP making it not only a very compact solution, but it also provides excellent thermal performance for applications requiring up to 200 mA of output current in a small, low profile footprint. The ADP7142 is also available in a 5-lead TSOT and an 8-lead SOIC.TABLE OF CONTENTS

Features ..... 1
Applications ..... 1
Typical Application Circuits ..... 1
General Description ..... 1
Specifications ..... 3
Input and Output Capacitance, Recommended Specifications ..... 4
Absolute Maximum Ratings ..... 5
Thermal Data ..... 5
Thermal Resistance ..... 5
ESD Caution ..... 5
Pin Configurations and Function Descriptions ..... 6
Typical Performance Characteristics ..... 7
Theory of Operation ..... 13
Applications Information ..... 14
Design Tools ..... 14
Capacitor Selection ..... 14
Programmable Precision Enable ..... 15
Soft Start ..... 15
Noise Reduction of the ADP7142 in Adjustable Mode ..... 16
Effect of Noise Reduction on Start-Up Time ..... 16
Current-Limit and Thermal Overload Protection ..... 17
Thermal Considerations ..... 17
Printed Circuit Board Layout Considerations ..... 20
Outline Dimensions ..... 22
Ordering Guide ..... 23
Output Voltage Options ..... 24
Evaluation Boards ..... 24
Automotive Products ..... 24
REVISION HISTORY
7/2024-Rev. I to Rev. J
Changes to Figure 54 and Figure 55 ..... 18
3/2022-Rev. H to Rev. I
Changes to Features Section ..... 1
Change to Applications Section ..... 1
Change to General Description Section ..... 1
Change to Specifications Section ..... 3
Changes to Table 3 ..... 5
Changes to Figure 6 Caption, Figure 9 Caption, Figure 10 Caption, and Figure 11 Caption ..... 7
Changes to Figure 12 Caption, Figure 13 Caption, Figure 15 Caption, and Figure 16 Caption ..... 8
Changes to Figure 19 Caption to Figure 22 Caption ..... 9
Changes to Figure 24 Caption and Figure 25 Caption ..... 10
Changed ADISIMPower Design Tool Section to Design Tools Section ..... 14
Changes to Design Tools Section ..... 14
Changes to Input and Output Capacitor Properties Section ..... 14
Changes to Soft Start Section ..... 15
Changes to Figure 48 ..... 15
Change to Effect of Noise Reduction on Start-Up Time Section ..... 16
Changes to Thermal Considerations Section ..... 17
Changes to Ordering Guide ..... 23
Added Voltage Output Options Section ..... 24
Added Automotive Products Section ..... 24# SPECIFICATIONS

$\mathrm{V}*{\mathrm{IN}}=\mathrm{V}*{\text {OUT }}+1 \mathrm{~V}$ or 2.7 V , whichever is greater, $\mathrm{V}*{\text {OUT }}=5 \mathrm{~V}, \mathrm{~V}*{\mathrm{EN}}=\mathrm{V}*{\mathrm{IN}}, \mathrm{I}*{\text {OUT }}=10 \mathrm{~mA}, \mathrm{C}*{\mathrm{IN}}=\mathrm{C}*{\text {OUT }}=2.2 \mu \mathrm{~F}, \mathrm{C}_{\mathrm{SS}}=0 \mathrm{pF}, \mathrm{T}_{\mathrm{A}}=25^{\circ} \mathrm{C}$ for typical specifications, $\mathrm{T}*{\mathrm{J}}=-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ for minimum/maximum specifications, unless otherwise noted.

Table 1.

|  Parameter | Symbol | Test Conditions/Comments | Min | Typ | Max | Unit  |
| --- | --- | --- | --- | --- | --- | --- |
|  INPUT VOLTAGE RANGE | $\mathrm{V}_{\text {IN }}$ |  | 2.7 |  | 40 | V  |
|  OPERATING SUPPLY CURRENT | $\mathrm{I}_{\text {GND }}$ | $\mathrm{I}_{\text {OUT }}=0 \mu \mathrm{~A}$ |  | 50 | 140 | $\mu \mathrm{A}$  |
|   |  | $\mathrm{I}_{\text {OUT }}=10 \mathrm{~mA}$ |  | 80 | 190 | $\mu \mathrm{A}$  |
|   |  | $\mathrm{I}_{\text {OUT }}=200 \mathrm{~mA}$ |  | 180 | 320 | $\mu \mathrm{A}$  |
|  SHUTDOWN CURRENT | $\mathrm{I}_{\text {GND-SD }}$ | $\mathrm{EN}=\mathrm{GND}$ |  | 1.8 |  | $\mu \mathrm{A}$  |
|   |  | $\mathrm{EN}=\mathrm{GND}, \mathrm{V}_{\mathrm{IN}}=40 \mathrm{~V}$ |  | 3.0 | 10 | $\mu \mathrm{A}$  |
|  OUTPUT VOLTAGE ACCURACY |  |  |  |  |  |   |
|  Output Voltage Accuracy | $\mathrm{V}_{\text {OUT }}$ | $\mathrm{I}_{\text {OUT }}=10 \mathrm{~mA}, \mathrm{~T}_{\mathrm{J}}=25^{\circ} \mathrm{C}$ | $-0.8$ |  | $+0.8$ | $\%$  |
|   |  | $100 \mu \mathrm{~A}<\mathrm{I}*{\text {OUT }}<200 \mathrm{~mA}, \mathrm{~V}*{\mathrm{IN}}=\left(\mathrm{V}*{\text {OUT }}+1 \mathrm{~V}\right)$ to $40 \mathrm{~V}, \mathrm{~T}*{\mathrm{J}}=-40^{\circ} \mathrm{C}$ | $-1.2$ |  | $+1.5$ | $\%$  |
|   |  | to $+85^{\circ} \mathrm{C}$ |  |  |  |   |
|   |  | $100 \mu \mathrm{~A}<\mathrm{I}*{\text {OUT }}<200 \mathrm{~mA}, \mathrm{~V}*{\mathrm{IN}}=\left(\mathrm{V}*{\text {OUT }}+1 \mathrm{~V}\right)$ to 40 V | $-1.8$ |  | $+1.8$ | $\%$  |
|  LINE REGULATION | $\Delta \mathrm{V}_{\text {OUT }} / \Delta \mathrm{V}_{\text {IN }}$ | $\mathrm{V}_{\mathrm{IN}}=\left(\mathrm{V}_{\text {OUT }}+1 \mathrm{~V}\right)$ to 40 V | $-0.01$ |  | $+0.01$ | $\% / \mathrm{V}$  |
|  LOAD REGULATION ${ }^{1}$ | $\Delta \mathrm{V}_{\text {OUT }} / \Delta \mathrm{I}_{\text {OUT }}$ | $\mathrm{I}_{\text {OUT }}=100 \mu \mathrm{~A}$ to 200 mA |  | 0.002 | 0.004 | $\% / \mathrm{mA}$  |
|  SENSE INPUT BIAS CURRENT | SENSE $_{\text {LBIAS }}$ | $100 \mu \mathrm{~A}<\mathrm{I}*{\text {OUT }}<200 \mathrm{~mA}, \mathrm{~V}*{\mathrm{IN}}=\left(\mathrm{V}*{\text {OUT }}+1 \mathrm{~V}\right)$ to 40 V |  | 10 | 1000 | nA  |
|  DROPOUT VOLTAGE ${ }^{2}$ | $\mathrm{V}_{\text {DROPOUT }}$ | $\mathrm{I}_{\text {OUT }}=10 \mathrm{~mA}$ |  | 30 | 60 | mV  |
|   |  | $\mathrm{I}_{\text {OUT }}=200 \mathrm{~mA}$ |  | 200 | 420 | mV  |
|  START-UP TIME ${ }^{3}$ | $\mathrm{t}_{\text {START-UP }}$ | $\mathrm{V}_{\text {OUT }}=5 \mathrm{~V}$ |  | 380 |  | $\mu \mathrm{s}$  |
|  SOFT START SOURCE CURRENT | $\mathrm{SS}_{\text {LSOURCE }}$ | $\mathrm{SS}=\mathrm{GND}$ |  | 1.15 |  | $\mu \mathrm{A}$  |
|  CURRENT-LIMIT THRESHOLD ${ }^{4}$ | $\mathrm{I}_{\text {LIMIT }}$ |  | 250 | 360 | 460 | mA  |
|  THERMAL SHUTDOWN |  |  |  |  |  |   |
|  Thermal Shutdown Threshold | $\mathrm{TS}_{\text {SD }}$ | $\mathrm{T}_{\mathrm{J}}$ rising |  |  |  |   |
|  Thermal Shutdown Hysteresis | $\mathrm{TS}_{\text {SD-HYS }}$ |  |  | 150 |  | ${ }^{\circ} \mathrm{C}$  |
|  UNDERVOLTAGE THRESHOLDS |  |  |  | 15 |  | ${ }^{\circ} \mathrm{C}$  |
|  Input Voltage Rising | $\mathrm{UVLO}_{\text {RISE }}$ |  |  |  |  |   |
|  Input Voltage Falling | $\mathrm{UVLO}_{\text {FALL }}$ |  | 2.2 |  | 2.69 | V  |
|  Hysteresis | $\mathrm{UVLO}_{\text {HYS }}$ |  |  | 230 |  | V  |
|  PRECISION EN INPUT |  | $2.7 \mathrm{~V} \leq \mathrm{V}_{\mathrm{IN}} \leq 40 \mathrm{~V}$ |  |  |  |   |
|  Logic High | $\mathrm{EN}_{\text {HIGH }}$ |  | 1.15 | 1.22 | 1.30 | V  |
|  Logic Low | $\mathrm{EN}_{\text {LOW }}$ |  | 1.06 | 1.12 | 1.18 | V  |
|  Logic Hysteresis | $\mathrm{EN}_{\text {HYS }}$ |  |  | 100 |  | mV  |
|  Leakage Current | $\mathrm{I}_{\text {EN-LKG }}$ | $\mathrm{EN}=\mathrm{V}_{\mathrm{IN}}$ or GND |  | 0.04 | 1 | $\mu \mathrm{A}$  |
|  Delay Time | $\mathrm{t}_{\text {EN-DLY }}$ | From EN rising from 0 V to $\mathrm{V}*{\mathrm{IN}}$ to $0.1 \times \mathrm{V}*{\text {OUT }}$ |  | 80 |  | $\mu \mathrm{s}$  |
|  OUTPUT NOISE | OUT ${ }_{\text {NOISE }}$ | 10 Hz to 100 kHz , all output voltage options |  | 11 |  | $\mu \mathrm{V} \mathrm{rms}$  |
|  POWER SUPPLY REJECTION RATIO | PSRR | $1 \mathrm{MHz}, \mathrm{V}_{\mathrm{IN}}=7 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=5 \mathrm{~V}$ |  | 50 |  | dB  |
|   |  | $100 \mathrm{kHz}, \mathrm{V}_{\mathrm{IN}}=7 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=5 \mathrm{~V}$ |  | 68 |  | dB  |
|   |  | $10 \mathrm{kHz}, \mathrm{V}_{\mathrm{IN}}=7 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=5 \mathrm{~V}$ |  | 88 |  | dB  |

[^0] [^0]: 1 Based on an endpoint calculation using $100 \mu \mathrm{~A}$ and 200 mA loads. See Figure 7 for typical load regulation performance for loads less than 1 mA . 2 Dropout voltage is defined as the input-to-output voltage differential when the input voltage is set to the nominal output voltage. Dropout applies only for output voltages above 2.7 V . 3 Start-up time is defined as the time between the rising edge of EN to OUT being at $90 \%$ of its nominal value. 4 Current-limit threshold is defined as the current at which the output voltage drops to $90 \%$ of the specified typical value. For example, the current limit for a 5.0 V output voltage is defined as the current that causes the output voltage to drop to $90 \%$ of 5.0 V or 4.5 V .# SPECIFICATIONS

## INPUT AND OUTPUT CAPACITANCE, RECOMMENDED SPECIFICATIONS

Table 2.

|  Parameter | Symbol | Test Conditions/Comments | Min | Typ | Max | Unit  |
| --- | --- | --- | --- | --- | --- | --- |
|  INPUT AND OUTPUT CAPACITANCE |  |  |  |  |  |   |
|  Minimum Capacitance ${ }^{1}$ | $\mathrm{C}_{\text {MIN }}$ | $\mathrm{T}_{\mathrm{A}}=-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 1.5 |  |  | $\mu \mathrm{F}$  |
|  Capacitor Effective Series Resistance (ESR) | $\mathrm{R}_{\text {ESR }}$ | $\mathrm{T}_{\mathrm{A}}=-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 0.001 |  | 0.3 | $\Omega$  |

1 The minimum input and output capacitance must be greater than $1.5 \mu \mathrm{~F}$ over the full range of operating conditions. The full range of operating conditions in the application must be considered during device selection to ensure that the minimum capacitance specification is met. XTR and XSR type capacitors are recommended, while YSV and ZSU capacitors are not recommended for use with any LDO.# ABSOLUTE MAXIMUM RATINGS 

Table 3.

| Parameter | Rating |
| :-- | :-- |
| VIN to GND | -0.3 V to +44 V |
| VOUT to GND | -0.3 V to VIN |
| EN to GND | -0.3 V to +44 V |
| SENSE/ADJ to GND | -0.3 V to +6 V |
| SS to GND | -0.3 V to VIN or +6 V |
|  | (whichever is less) |
| Storage Temperature Range | $-65^{\circ} \mathrm{C}$ to $+150^{\circ} \mathrm{C}$ |
| Junction Temperature $\left(T_{J}\right)$ | $150^{\circ} \mathrm{C}$ |
| Operating Ambient Temperature $\left(T_{A}\right)$ | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ |
| Range |  |
| Soldering Conditions | JEDEC J-STD-020 |
| ESD |  |
| 6-Lead LFCSP, 8-Lead SOIC |  |
| Human Body Model (HBM) | $\pm 1000 \mathrm{~V}$ |
| Field Induced Charged Device Model | $\pm 1000 \mathrm{~V}$ |
| (FICDM) |  |
| 5-Lead TSOT |  |
| HBM | $\pm 1000 \mathrm{~V}$ |
| FICDM | $\pm 1250 \mathrm{~V}$ |
| 5-Lead TSOT (W Grade) |  |
| HBM $^{1}$ | $\pm 1000 \mathrm{~V}$ |
| HBM $^{2}$ | $\pm 2000 \mathrm{~V}$ |
| FICDM | $\pm 1250 \mathrm{~V}$ |

${ }^{1}$ All pins passing.
2 All pins passing with elevated output noise. No physical damage to circuitry.
Stresses at or above those listed under Absolute Maximum Ratings may cause permanent damage to the product. This is a stress rating only; functional operation of the product at these or any other conditions above those indicated in the operational section of this specification is not implied. Operation beyond the maximum operating conditions for extended periods may affect product reliability.

## THERMAL DATA

Absolute maximum ratings apply individually only, not in combination. The ADP7142 can be damaged when the junction temperature limits are exceeded. Monitoring ambient temperature does not guarantee that $T_{J}$ is within the specified temperature limits. In applications with high power dissipation and poor thermal resistance, the maximum ambient temperature may have to be derated.

In applications with moderate power dissipation and low printed circuit board (PCB) thermal resistance, the maximum ambient temperature can exceed the maximum limit as long as the junction temperature is within specification limits. The junction temperature of the device is dependent on the ambient temperature, the power dissipation $\left(P_{D}\right)$ of the device, and the junction-to-ambient thermal resistance of the package $\left(\theta_{J A}\right)$.
Maximum $T_{J}$ is calculated from the $T_{A}$ and $P_{D}$ using the formula
$T_{J}=T_{A}+\left(P_{D} \times \theta_{J A}\right)$
$\theta_{\mathrm{JA}}$ of the package is based on modeling and calculation using a 4-layer board. The $\theta_{\mathrm{JA}}$ is highly dependent on the application and board layout. In applications where high maximum power dissipation exists, close attention to thermal board design is required. The value of $\theta_{\mathrm{JA}}$ may vary, depending on PCB material, layout, and environmental conditions. The specified values of $\theta_{\mathrm{JA}}$ are based on a 4-layer, 4 inches $\times 3$ inches circuit board. See JESD51-7 and JESD51-9 for detailed information on the board construction.
$\Psi_{\text {JB }}$ is the junction-to-board thermal characterization parameter with units of ${ }^{\circ} \mathrm{C} / \mathrm{W}$. The $\Psi_{\text {JB }}$ of the package is based on modeling and calculation using a 4-layer board. The JESD51-12, Guidelines for Reporting and Using Electronic Package Thermal Information, states that thermal characterization parameters are not the same as thermal resistances. $\Psi_{\text {JB }}$ measures the component power flowing through multiple thermal paths rather than a single path as in thermal resistance $\left(\theta_{J B}\right)$. Therefore, $\Psi_{\text {JB }}$ thermal paths include convection from the top of the package as well as radiation from the package, factors that make $\Psi_{\text {JB }}$ more useful in real-world applications. Maximum $T_{J}$ is calculated from the board temperature $\left(T_{B}\right)$ and $P_{D}$ using the formula
$T_{J}=T_{B}+\left(P_{D} \times \Psi_{J B}\right)$
See JESD51-8 and JESD51-12 for more detailed information about $\Psi_{\text {JB }}$.

## THERMAL RESISTANCE

$\theta_{\mathrm{JA}}, \theta_{\mathrm{JC}}$, and $\Psi_{\mathrm{JB}}$ are specified for the worst-case conditions, that is, a device soldered in a circuit board for surface-mount packages.

Table 4. Thermal Resistance

| Package Type | $\boldsymbol{\theta}_{\mathbf{J A}}$ | $\boldsymbol{\theta}_{\mathbf{J C}}$ | $\boldsymbol{\Psi}_{\mathbf{J B}}$ | Unit |
| :-- | :-- | :-- | :-- | :-- |
| 6-Lead LFCSP | 72.1 | 42.3 | 47.1 | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |
| 8-Lead SOIC | 52.7 | 41.5 | 32.7 | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |
| 5-Lead TSOT | 170 | $\mathrm{~N} / \mathrm{A}^{1}$ | 43 | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |

${ }^{1} \mathrm{~N} / \mathrm{A}$ means not applicable.

## ESD CAUTION

![img-2.jpeg](img-2.jpeg)

ESD (electrostatic discharge) sensitive device. Charged devices and circuit boards can discharge without detection. Although this product features patented or proprietary protection circuitry, damage may occur on devices subjected to high energy ESD. Therefore, proper ESD precautions should be taken to avoid performance degradation or loss of functionality.# PIN CONFIGURATIONS AND FUNCTION DESCRIPTIONS 

![img-3.jpeg](img-3.jpeg)

Figure 3. 6-Lead LFCSP Pin Configuration
![img-4.jpeg](img-4.jpeg)

Figure 4. 5-Lead TSOT Pin Configuration
Table 5. Pin Function Descriptions

| Pin No. |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
| 6-Lead LFCSP | 8-Lead SOIC | 5-Lead TSOT | Mnemonic | Description |
| 1 | 1,2 | 5 | VOUT | Regulated Output Voltage. Bypass VOUT to GND with a $2.2 \mu \mathrm{~F}$ or greater capacitor. |
| 2 | 3 | 4 | SENSE/ADJ | Sense Input (SENSE). Connect to load. An external resistor divider may also be used to set the output voltage higher than the fixed output voltage (ADJ). |
| 3 | 4 | 2 | GND | Ground. |
| 4 | 5 | 3 | EN | The Enable Pin Controls the Operation of the LDO. Drive EN high to turn on the regulator. Drive EN low to turn off the regulator. For automatic startup, connect EN to VIN. |
| 5 | 6 | Not applicable | SS | Soft Start. An external capacitor connected to this pin determines the soft-start time. Leave this pin open for a typical 380 us start-up time. Do not ground this pin. |
| 6 | 7,8 | 1 | VIN <br> EP | Regulator Input Supply. Bypass VIN to GND with a $2.2 \mu \mathrm{~F}$ or greater capacitor. <br> Exposed Pad. The exposed pad on the bottom of the package enhances thermal performance and is electrically connected to GND inside the package. It is recommended that the exposed pad connect to the ground plane on the board. |# TYPICAL PERFORMANCE CHARACTERISTICS 

$V_{\text {IN }}=V_{\text {OUT }}+1 \mathrm{~V}$ or 2.7 V , whichever is greater, $V_{\text {OUT }}=5 \mathrm{~V}, I_{\text {OUT }}=10 \mathrm{~mA}, C_{\text {IN }}=C_{\text {OUT }}=2.2 \mu \mathrm{~F}, T_{A}=25^{\circ} \mathrm{C}$, unless otherwise noted.
![img-5.jpeg](img-5.jpeg)

Figure 6. Output Voltage $\left(V_{\text {OUT }}\right)$ vs. Junction Temperature $\left(T_{J}\right)$
![img-6.jpeg](img-6.jpeg)

Figure 7. Output Voltage $\left(V_{\text {OUT }}\right)$ vs. Load Current $\left(I_{\text {LOAD }}\right)$
![img-7.jpeg](img-7.jpeg)

Figure 8. Output Voltage $\left(V_{\text {OUT }}\right)$ vs. Input Voltage $\left(V_{\text {IN }}\right)$
![img-8.jpeg](img-8.jpeg)

Figure 9. Ground Current $\left(I_{\text {GND }}\right)$ vs. Junction Temperature $\left(T_{J}\right)$
![img-9.jpeg](img-9.jpeg)

Figure 10. Ground Current $\left(I_{\text {GND }}\right)$ vs. Load Current $\left(I_{\text {LOAD }}\right)$
![img-10.jpeg](img-10.jpeg)

Figure 11. Ground Current $\left(I_{\text {GND }}\right)$ vs. Input Voltage $\left(V_{\text {IN }}\right)$# TYPICAL PERFORMANCE CHARACTERISTICS 

![img-11.jpeg](img-11.jpeg)

Figure 12. Shutdown Current ( $I_{\text {OND-SO }}$ ) vs. Temperature at Various Input Voltages $\left(V_{I N}\right)$
![img-12.jpeg](img-12.jpeg)

Figure 13. Dropout Voltage ( $V_{\text {DROPOUT }}$ ) vs. Load Current ( $I_{\text {LOAD }}$ ), $V_{\text {OUT }}=5 \mathrm{~V}$
![img-13.jpeg](img-13.jpeg)

Figure 14. Output Voltage $\left(V_{\text {OUT }}\right)$ vs. Input Voltage $\left(V_{\text {IN }}\right)$ in Dropout, $V_{\text {OUT }}=5 \mathrm{~V}$
![img-14.jpeg](img-14.jpeg)

Figure 15. Ground Current ( $I_{G N D}$ ) vs. Input Voltage ( $V_{I N}$ ) in Dropout, $V_{\text {OUT }}=5 \mathrm{~V}$
![img-15.jpeg](img-15.jpeg)

Figure 16. Output Voltage $\left(V_{\text {OUT }}\right)$ vs. Junction Temperature $\left(T_{J}\right), V_{\text {OUT }}=3.3 \mathrm{~V}$
![img-16.jpeg](img-16.jpeg)

Figure 17. Output Voltage $\left(V_{\text {OUT }}\right)$ vs. Load Current $\left(I_{\text {LOAD }}\right), V_{\text {OUT }}=3.3 \mathrm{~V}$# TYPICAL PERFORMANCE CHARACTERISTICS 

![img-17.jpeg](img-17.jpeg)

Figure 18. Output Voltage $\left(V_{\text {OUT }}\right)$ vs. Input Voltage $\left(V_{\text {IN }}\right), V_{\text {OUT }}=3.3 \mathrm{~V}$
![img-18.jpeg](img-18.jpeg)

Figure 19. Ground Current $\left(I_{\text {GND }}\right)$ vs. Junction Temperature $\left(T_{J}\right), V_{\text {OUT }}=3.3 \mathrm{~V}$
![img-19.jpeg](img-19.jpeg)

Figure 20. Ground Current $\left(I_{\text {GND }}\right)$ vs. Load Current $\left(I_{\text {LOAD }}\right), V_{\text {OUT }}=3.3 \mathrm{~V}$
![img-20.jpeg](img-20.jpeg)

Figure 21. Ground Current $\left(I_{\text {GND }}\right)$ vs. Input Voltage $\left(V_{\text {IN }}\right), V_{\text {OUT }}=3.3 \mathrm{~V}$
![img-21.jpeg](img-21.jpeg)

Figure 22. Dropout Voltage $\left(V_{\text {DROPOUT }}\right)$ vs. Load Current $\left(I_{\text {LOAD }}\right), V_{\text {OUT }}=3.3 \mathrm{~V}$
![img-22.jpeg](img-22.jpeg)

Figure 23. Output Voltage $\left(V_{\text {OUT }}\right)$ vs. Input Voltage $\left(V_{\text {IN }}\right)$ in Dropout, $V_{\text {OUT }}=3.3 \mathrm{~V}$# TYPICAL PERFORMANCE CHARACTERISTICS 

![img-23.jpeg](img-23.jpeg)

Figure 24. Ground Current $\left(I_{G N D}\right)$ vs. Input Voltage $\left(V_{I N}\right)$ in Dropout, $V_{\text {OUT }}=3.3 \mathrm{~V}$
![img-24.jpeg](img-24.jpeg)

Figure 25. Soft Start (SS) Current vs. Temperature $\left(T_{J}\right)$, Multiple Input Voltages $\left(V_{I N}\right), V_{\text {OUT }}=5 \mathrm{~V}$
![img-25.jpeg](img-25.jpeg)

Figure 26. Power Supply Rejection Ratio (PSRR) vs. Frequency, $V_{\text {OUT }}=1.8 \mathrm{~V}$, for Various Headroom Voltages
![img-26.jpeg](img-26.jpeg)

Figure 27. Power Supply Rejection Ratio (PSRR) vs. Headroom Voltage, $V_{\text {OUT }}=1.8 \mathrm{~V}$, for Different Frequencies
![img-27.jpeg](img-27.jpeg)

Figure 28. Power Supply Rejection Ratio (PSRR) vs. Frequency, $V_{\text {OUT }}=3.3 \mathrm{~V}$, for Various Headroom Voltages
![img-28.jpeg](img-28.jpeg)

Figure 29. Power Supply Rejection Ratio (PSRR) vs. Headroom Voltage, $V_{\text {OUT }}=3.3 \mathrm{~V}$, for Different Frequencies# TYPICAL PERFORMANCE CHARACTERISTICS 

![img-29.jpeg](img-29.jpeg)

Figure 30. Power Supply Rejection Ratio (PSRR) vs. Frequency, $V_{\text {OUT }} \approx 5 \mathrm{~V}$, for Various Headroom Voltages
![img-30.jpeg](img-30.jpeg)

Figure 31. Power Supply Rejection Ratio (PSRR) vs. Headroom Voltage, $V_{\text {OUT }} \approx 5 \mathrm{~V}$, for Different Frequencies
![img-31.jpeg](img-31.jpeg)

Figure 32. RMS Output Noise vs. Load Current (ILOAD)
![img-32.jpeg](img-32.jpeg)

Figure 33. Output Noise Spectral Density vs. Frequency, $I_{\text {LOAD }} \approx 10 \mathrm{~mA}$
![img-33.jpeg](img-33.jpeg)

Figure 34. Output Noise Spectral Density vs. Frequency, for Different Loads
![img-34.jpeg](img-34.jpeg)

Figure 35. Output Noise Spectral Density vs. Frequency, for Different Output Voltages $\left(V_{\text {OUT }}\right)$# TYPICAL PERFORMANCE CHARACTERISTICS 

![img-35.jpeg](img-35.jpeg)

Figure 36. Load Transient Response, $I_{\text {LOAD }}=1 \mathrm{~mA}$ to $200 \mathrm{~mA}, V_{\text {OUT }}=5 \mathrm{~V}$, $V_{I N}=7 \mathrm{~V}, \mathrm{CH1}$ Load Current $\left(I_{\text {LOAD }}\right), \mathrm{CH} 2 V_{\text {OUT }}$
![img-36.jpeg](img-36.jpeg)

Figure 37. Line Transient Response, $I_{\text {LOAD }}=200 \mathrm{~mA}, V_{\text {OUT }}=5 \mathrm{~V}, \mathrm{CH1} V_{I N}$, $\mathrm{CH} 2 V_{\text {OUT }}$
![img-37.jpeg](img-37.jpeg)

Figure 38. Load Transient Response, $I_{\text {LOAD }}=1 \mathrm{~mA}$ to $200 \mathrm{~mA}, V_{\text {OUT }}=3.3 \mathrm{~V}$, $V_{I N}=5 \mathrm{~V}, \mathrm{CH1}$ Load Current $\left(I_{\text {LOAD }}\right), \mathrm{CH} 2 V_{\text {OUT }}$
![img-38.jpeg](img-38.jpeg)

Figure 39. Line Transient Response, $I_{\text {LOAD }}=200 \mathrm{~mA}, V_{\text {OUT }}=3.3 \mathrm{~V}, \mathrm{CH1} V_{I N}$, $\mathrm{CH} 2 V_{\text {OUT }}$
![img-39.jpeg](img-39.jpeg)

Figure 40. Load Transient Response, $I_{\text {LOAD }}=1 \mathrm{~mA}$ to $200 \mathrm{~mA}, V_{\text {OUT }}=1.8 \mathrm{~V}$, $V_{I N}=3 \mathrm{~V}, \mathrm{CH1}$ Load Current $\left(I_{\text {LOAD }}\right), \mathrm{CH} 2 V_{\text {OUT }}$
![img-40.jpeg](img-40.jpeg)

Figure 41. Line Transient Response, $I_{\text {LOAD }}=200 \mathrm{~mA}, V_{\text {OUT }}=1.8 \mathrm{~V}, \mathrm{CH1} V_{I N}$, $\mathrm{CH} 2 V_{\text {OUT }}$# THEORY OF OPERATION 

The ADP7142 is a low quiescent current, LDO linear regulator that operates from 2.7 V to 40 V and provides up to 200 mA of output current. Drawing a low $180 \mu \mathrm{~A}$ of quiescent current (typical) at full load makes the ADP7142 ideal for portable equipment. Typical shutdown current consumption is less than $3 \mu \mathrm{~A}$ at room temperature.

Optimized for use with small $2.2 \mu \mathrm{~F}$ ceramic capacitors, the ADP7142 provides excellent transient performance.
![img-41.jpeg](img-41.jpeg)

Figure 42. Internal Block Diagram
Internally, the ADP7142 consists of a reference, an error amplifier, and a PMOS pass transistor. Output current is delivered via the PMOS pass device, which is controlled by the error amplifier. The error amplifier compares the reference voltage with the feedback voltage from the output and amplifies the difference. If the feedback voltage is lower than the reference voltage, the gate of the PMOS device is pulled lower, allowing more current to pass and increasing the output voltage. If the feedback voltage is higher than the reference voltage, the gate of the PMOS device is pulled higher, allowing less current to pass and decreasing the output voltage.
The ADP7142 is available in 15 fixed output voltage options, ranging from 1.2 V to 5.0 V . The ADP7142 architecture allows any fixed output voltage to be set to a higher voltage with an external voltage
divider. For example, a fixed 5 V output can be set to a 6 V output according to the following equation:
$V_{\text {OUT }}=5 \mathrm{~V}(1+R 1 / R 2)$
where $R 1$ and $R 2$ are the resistors in the output voltage divider shown in Figure 43.

To set the output voltage of the adjustable ADP7142, replace 5 V in Equation 3 with 1.2 V .
![img-42.jpeg](img-42.jpeg)

Figure 43. Typical Adjustable Output Voltage Application Schematic
It is recommended that the R2 value be less than $200 \mathrm{k} \Omega$ to minimize errors in the output voltage caused by the SENSE/ADJ pin input current. For example, when R1 and R2 each equal $200 \mathrm{k} \Omega$ and the default output voltage is 1.2 V , the adjusted output voltage is 2.4 V . The output voltage error introduced by the SENSE/ADJ pin input current is 1 mV or $0.04 \%$, assuming a typical SENSE/ ADJ pin input current of 10 nA at $25^{\circ} \mathrm{C}$.
The ADP7142 uses the EN pin to enable and disable the VOUT pin under normal operating conditions. When EN is high, VOUT turns on, and when EN is low, VOUT turns off. For automatic startup, EN can be tied to VIN.APPLICATIONS INFORMATION

## DESIGN TOOLS

The ADP7142 is supported by the ADIsimPower ${ }^{\text {TM }}$, LTpowerCAD ${ }^{\circledR}$, and LTspice ${ }^{\circledR}$ design tools to produce complete power designs and simulations. For more information on design tools, visit the ADP7142 product page, www.analog.com/adp7142.

## CAPACITOR SELECTION

## Output Capacitor

The ADP7142 is designed for operation with small, space-saving ceramic capacitors, but functions with general-purpose capacitors as long as care is taken with regard to the effective series resistance (ESR) value. The ESR of the output capacitor affects the stability of the LDO control loop. A minimum of $2.2 \mu \mathrm{~F}$ capacitance with an ESR of $0.3 \Omega$ or less is recommended to ensure the stability of the ADP7142. Transient response to changes in load current is also affected by output capacitance. Using a larger value of output capacitance improves the transient response of the ADP7142 to large changes in load current. Figure 44 shows the transient responses for an output capacitance value of $2.2 \mu \mathrm{~F}$.
![img-43.jpeg](img-43.jpeg)

Figure 44. Output Transient Response, $V_{\text {OUT }}=5 \mathrm{~V}, C_{\text {OUT }}=2.2 \mu \mathrm{~F}, \mathrm{CH1}$ Load Current, $\mathrm{CH} 2 \mathrm{~V}_{\text {OUT }}$

## Input Bypass Capacitor

Connecting a $2.2 \mu \mathrm{~F}$ capacitor from VIN to GND reduces the circuit sensitivity to the PCB layout, especially when long input traces or high source impedance is encountered. If greater than $2.2 \mu \mathrm{~F}$ of output capacitance is required, increase the input capacitor to match it.

## Input and Output Capacitor Properties

Any good quality ceramic capacitors can be used with the ADP7142, as long as they meet the minimum capacitance and maximum ESR requirements. Ceramic capacitors are manufactured with a variety of dielectrics, each with different behavior over temperature and applied voltage. Capacitors must have a dielectric adequate to ensure the minimum capacitance over the necessary
temperature range and dc bias conditions. X5R or X7R dielectrics with a voltage rating of 6.3 V to 100 V are recommended. Y5V and Z5U dielectrics are not recommended, due to their poor temperature and dc bias characteristics.
Figure 45 depicts the capacitance vs. voltage bias characteristic of an $0805,2.2 \mu \mathrm{~F}, 10 \mathrm{~V}, \mathrm{X} 5 \mathrm{R}$ capacitor. The voltage stability of a capacitor is strongly influenced by the capacitor size and voltage rating. In general, a capacitor in a larger package or higher voltage rating exhibits better stability. The temperature variation of the X5R dielectric is $\sim \pm 15 \%$ over the $-40^{\circ} \mathrm{C}$ to $+85^{\circ} \mathrm{C}$ temperature range and is not a function of package or voltage rating.
![img-44.jpeg](img-44.jpeg)

Figure 45. Capacitance vs. Voltage Characteristic
Use Equation 4 to determine the worst-case capacitance accounting for capacitor variation over temperature, component tolerance, and voltage.
$C_{E F F}=C_{B I A S}(1-T E M P C O) \times(1-T O L)$
where:
$C_{B I A S}$ is the effective capacitance at the operating voltage. TEMPCO is the worst-case capacitor temperature coefficient. TOL is the worst-case component tolerance.

In this example, the worst-case temperature coefficient (TEMPCO) over $-40^{\circ} \mathrm{C}$ to $+85^{\circ} \mathrm{C}$ is assumed to be $15 \%$ for an X5R dielectric. The tolerance of the capacitor (TOL) is assumed to be $10 \%$, and $\mathrm{C}_{\text {BIAS }}$ is $2.09 \mu \mathrm{~F}$ at 5 V , as shown in Figure 45.
These values in Equation 4 yield
$C_{E F F}=2.09 \mu \mathrm{~F} \times(1-0.15) \times(1-0.1)=$ $1.59 \mu \mathrm{~F}$

Therefore, the capacitor chosen in this example meets the minimum capacitance requirement of the LDO over temperature and tolerance at the chosen output voltage.

To guarantee the performance of the ADP7142, it is imperative that the effects of dc bias, temperature, and tolerances on the behavior of the capacitors be evaluated for each application.## APPLICATIONS INFORMATION

## PROGRAMMABLE PRECISION ENABLE

The ADP7142 uses the EN pin to enable and disable the VOUT pin under normal operating conditions. As shown in Figure 46, when a rising voltage on EN crosses the upper threshold, nominally 1.2 V , VOUT turns on. When a falling voltage on EN crosses the lower threshold, nominally 1.1 V , VOUT turns off. The hysteresis of the EN threshold is approximately 100 mV .
![img-45.jpeg](img-45.jpeg)

Figure 46. Typical VOUT Response to EN Pin Operation
The upper and lower thresholds are user programmable and can be set higher than the nominal 1.2 V threshold by using two resistors. The resistance values, $R_{E N 1}$ and $R_{E N 2}$, can be determined from
$R_{E N 2}=$ nominally $10 \mathrm{k} \Omega$ to $100 \mathrm{k} \Omega$
$R_{E N 1}=R_{E N 2} \times\left(V_{I N}-1.2 \mathrm{~V}\right) / 1.2 \mathrm{~V}$
where $V_{I N}$ is the desired turn-on voltage.
The hysteresis voltage increases by the factor $\left(R_{E N 1}+R_{E N 2}\right) / R_{E N 2}$. For the example shown in Figure 47, the enable threshold is 3.6 V with a hysteresis of 300 mV .
![img-46.jpeg](img-46.jpeg)

Figure 47. Typical EN Pin Voltage Divider
Figure 46 shows the typical hysteresis of the EN pin. This prevents on/off oscillations that can occur due to noise on the EN pin as it passes through the threshold points.

## SOFT START

The ADP7142 uses an internal soft start (when the SS pin is left open) to limit the inrush current when the output is enabled. The start-up time for the 3.3 V option is approximately $380 \mu \mathrm{~s}$ from the time the EN active threshold is crossed to when the output reaches $90 \%$ of its final value. As shown in Figure 48, the start-up time is independent of the output voltage setting.
![img-47.jpeg](img-47.jpeg)

Figure 48. Typical Start-Up Behavior
An external capacitor connected to the SS pin determines the soft start time. The SS pin can be left open for a typical $380 \mu \mathrm{~s}$ start-up time. Do not ground this pin. When an external soft start capacitor ( $\mathrm{C}_{\mathrm{SS}}$ ) is used, the soft start time is determined by the following equation:
$S S_{\text {TIME }}(\mathrm{sec})=t_{\text {STARTUP }(0 p F)}+\left(0.6 \times C_{S S}\right) / I_{S S}$
where:
$t_{\text {STARTUP (at } 0 \mathrm{pF})}$ is the start-up time at $\mathrm{C}_{\mathrm{SS}}=0 \mathrm{pF}$ (typically $380 \mu \mathrm{~s}$ ). $C_{S S}$ is the soft start capacitor ( $F$ ).
$I_{S S}$ is the soft start current (typically $1.15 \mu \mathrm{~A}$ ).
![img-48.jpeg](img-48.jpeg)

Figure 49. Typical Soft Start Behavior, Different $\mathrm{C}_{\mathrm{SS}}$## APPLICATIONS INFORMATION

## NOISE REDUCTION OF THE ADP7142 IN ADJUSTABLE MODE

The ultralow output noise of the ADP7142 is achieved by keeping the LDO error amplifier in unity gain and setting the reference voltage equal to the output voltage. This architecture does not work for an adjustable output voltage LDO in the conventional sense. However, the ADP7142 architecture allows any fixed output voltage to be set to a higher voltage with an external voltage divider. For example, a fixed 5 V output can be set to a 10 V output according to Equation 3 (see Figure 50):

$$
V_{O U T}=5 \mathrm{~V}(1+R 1 / R 2)
$$

The disadvantage in using the ADP7142 in this manner is that the output voltage noise is proportional to the output voltage. Therefore, it is best to choose a fixed output voltage that is close to the target voltage to minimize the increase in output noise.
The adjustable LDO circuit can be modified to reduce the output voltage noise to levels close to that of the fixed output ADP7142. The circuit shown in Figure 50 adds two additional components to the output voltage setting resistor divider. $C_{N R}$ and $R_{N R}$ are added in parallel with R1 to reduce the ac gain of the error amplifier. $R_{N R}$ is chosen to be small with respect to R2. If $R_{N R}$ is $1 \%$ to $10 \%$ of the value of R2, the minimum ac gain of the error amplifier is approximately 0.1 dB to 0.8 dB . The actual gain is determined by the parallel combination of $R_{N R}$ and $R 1$. This gain ensures that the error amplifier always operates at slightly greater than unity gain.
$C_{N R}$ is chosen by setting the reactance of $C_{N R}$ equal to $R 1-R_{N R}$ at a frequency between 1 Hz and 50 Hz . This setting places the frequency where the ac gain of the error amplifier is 3 dB down from its dc gain.
![img-49.jpeg](img-49.jpeg)

Figure 50. Noise Reduction Modification
The noise of the adjustable LDO is found by using the following formula, assuming the noise of a fixed output LDO is approximately $11 \mu \mathrm{~V}$.
Noise $=11 \mu \mathrm{~V} \times\left(R_{P A R}+R 2\right) / R 2$
where $R_{P A R}$ is a parallel combination of $R 1$ and $R_{N R}$.
Based on the component values shown in Figure 50, the ADP7142 has the following characteristics:

- DC gain of $10(20 \mathrm{~dB})$
- 3 dB roll-off frequency of 1.75 Hz
- High frequency ac gain of $1.099(0.82 \mathrm{~dB})$
- Theoretical noise reduction factor of $9.1(19.2 \mathrm{~dB})$
- Measured rms noise of the adjustable LDO without noise reduction is $70 \mu \mathrm{~V} \mathrm{rms}$
- Measured rms noise of the adjustable LDO with noise reduction is $12 \mu \mathrm{~V} \mathrm{rms}$
- Measured noise reduction of approximately 15.3 dB

Note that the measured noise reduction is less than the theoretical noise reduction. Figure 51 shows the noise spectral density of an adjustable ADP7142 set to 6 V and 12 V with and without the noise reduction network. The output noise with the noise reduction network is approximately the same for both voltages, especially beyond 100 Hz . The noise of the 6 V and 12 V outputs without the noise reduction network differs by a factor of 2 up to approximately 20 kHz . Above 40 kHz , the closed loop gain of the error amplifier is limited by its open loop gain characteristic. Therefore, the noise contribution from 20 kHz to 100 kHz is less than what it would be if the error amplifier had infinite bandwidth. This is also the reason why the noise is less than what might be expected simply based on the dc gain, that is, $70 \mu \mathrm{~V}$ rms vs. $110 \mu \mathrm{~V}$ rms.
![img-50.jpeg](img-50.jpeg)

Figure 51. 6 V and 12 V Output Voltage with and Without Noise Reduction Network

## EFFECT OF NOISE REDUCTION ON START-UP TIME

The start-up time of the ADP7142 is affected by the noise reduction network and must be considered in applications where power supply sequencing is critical.

The noise reduction circuit adds a pole in the feedback loop, slowing down the start-up time. The start-up time for an adjustable model with a noise reduction network can be approximated using the following equation:
$S S N R_{T I M E}(\sec )=5.5 \times C_{N R} \times\left(R_{N R}+R 1\right)$
For a $C_{N R}, R_{N R}$, and $R 1$ combination of $1 \mu \mathrm{~F}, 1 \mathrm{k} \Omega$, and $91 \mathrm{k} \Omega$ as shown in Figure 50, the start-up time is approximately 0.5 sec .# APPLICATIONS INFORMATION 

When $\operatorname{SSNR}_{\text {TIME }}$ is greater than $\mathrm{SS}_{\text {TIME }}$, $\operatorname{SSNR}_{\text {TIME }}$ dictates the length of the start-up time instead of the soft start capacitor.

## CURRENT-LIMIT AND THERMAL OVERLOAD PROTECTION

The ADP7142 is protected against damage due to excessive power dissipation by current and thermal overload protection circuits. The ADP7142 is designed to current limit when the output load reaches 360 mA (typical). When the output load exceeds 360 mA , the output voltage is reduced to maintain a constant current limit.

Thermal overload protection is included, which limits the junction temperature to a maximum of $150^{\circ} \mathrm{C}$ (typical). Under extreme conditions (that is, high ambient temperature and/or high power dissipation) when the junction temperature starts to rise above $150^{\circ} \mathrm{C}$, the output is turned off, reducing the output current to zero. When the junction temperature drops below $135^{\circ} \mathrm{C}$, the output is turned on again, and output current is restored to its operating value.

Consider the case where a hard short from VOUT to ground occurs. At first, the ADP7142 current limits, so that only 360 mA is conducted into the short. If self heating of the junction is great enough to cause its temperature to rise above $150^{\circ} \mathrm{C}$, thermal shutdown activates, turning off the output and reducing the output current to zero. As the junction temperature cools and drops below $135^{\circ} \mathrm{C}$, the output turns on and conducts 360 mA into the short, again causing the junction temperature to rise above $150^{\circ} \mathrm{C}$. This thermal oscillation between $135^{\circ} \mathrm{C}$ and $150^{\circ} \mathrm{C}$ causes a current oscillation between 360 mA and 0 mA that continues as long as the short remains at the output.

Current and thermal limit protections protect the device against accidental overload conditions. For reliable operation, device power dissipation must be externally limited so that the junction temperature does not exceed $125^{\circ} \mathrm{C}$.

## THERMAL CONSIDERATIONS

In applications with a low input-to-output voltage differential, the ADP7142 does not dissipate much heat. However, in applications with high ambient temperature and/or high input voltage, the heat dissipated in the package may become large enough to cause the junction temperature of the die to exceed the maximum junction temperature of $125^{\circ} \mathrm{C}$.

When the junction temperature exceeds $150^{\circ} \mathrm{C}$, the converter enters thermal shutdown. It recovers only after the junction temperature has decreased below $135^{\circ} \mathrm{C}$ to prevent any permanent damage. Therefore, thermal analysis for the chosen application is very important to guarantee reliable performance over all conditions. The junction temperature of the die is the sum of the ambient temperature of the environment and the temperature rise of the package due to the power dissipation, as shown in Equation 2.

To guarantee reliable operation, the junction temperature of the ADP7142 must not exceed $125^{\circ} \mathrm{C}$. To ensure that the junction
temperature stays below this maximum value, the user must be aware of the parameters that contribute to junction temperature changes. These parameters include ambient temperature, power dissipation in the power device, and thermal resistances between the junction and ambient air $\left(\theta_{J A}\right)$. The $\theta_{J A}$ number is dependent on the package assembly compounds that are used and the amount of copper used to solder the package GND pins to the PCB.

Table 6 shows typical $\theta_{\text {JA }}$ values of the 8-lead SOIC, 6-lead LFCSP, and 5-Lead TSOT packages for various PCB copper sizes. Table 7 shows the typical $\Psi_{J B}$ values of the 8-lead SOIC, 6-lead LFCSP, and 5-lead TSOT.

Table 6. Typical $\theta_{J A}$ Values

| Copper Size $\left(\mathbf{m m}^{1}\right)$ | $\theta_{\text {JA }}\left({ }^{\circ} \mathrm{C} / \mathrm{W}\right)$ |  |  |
| :--: | :--: | :--: | :--: |
|  | LFCSP | SOIC | TSOT |
| $25^{2}$ | 182.8 | N/A ${ }^{1}$ | N/A ${ }^{1}$ |
| 50 | N/A ${ }^{1}$ | 181.4 | 152 |
| 100 | 142.6 | 145.4 | 146 |
| 500 | 83.9 | 89.3 | 131 |
| 1000 | 71.7 | 77.5 | N/A ${ }^{1}$ |
| 6400 | 57.4 | 63.2 | N/A ${ }^{1}$ |

1 N/A means not applicable.
2 Device soldered to minimum size pin traces.
Table 7. Typical $\Psi_{J B}$ Values

| Model | $\Psi_{J B}\left({ }^{\circ} \mathrm{C} / \mathrm{W}\right)$ |
| :-- | :-- |
| 6-Lead LFCSP | 24 |
| 8-Lead SOIC | 38.8 |
| 5-Lead TSOT | 43 |

To calculate the junction temperature of the ADP7142, use Equation 1:
$T_{J}=T_{A}+\left(P_{D} \times \theta_{J A}\right)$
where:
$T_{A}$ is the ambient temperature.
$P_{D}$ is the power dissipation in the die, given by
$P_{D}=\left(\left(V_{I N}-V_{O U T}\right) \times I_{L O A D}\right)+\left(V_{I N} \times I_{G N D}\right)$
where:
$V_{I N}$ and $V_{O U T}$ are input and output voltages, respectively.
$I_{L O A D}$ is the load current.
$I_{G N D}$ is the ground current.
Power dissipation due to ground current is quite small and can be ignored. Therefore, the junction temperature equation simplifies to the following:
$T_{J}=T_{A}+\left(\left(\left(V_{I N}-V_{O U T}\right) \times I_{L O A D}\right) \times \theta_{J A}\right)$
As shown in Equation 12, for a given ambient temperature, input-to-output voltage differential, and continuous load current, there exists a minimum copper size requirement for the PCB to ensure that the junction temperature does not rise above $125^{\circ} \mathrm{C}$. Figure# APPLICATIONS INFORMATION 

52 to Figure 60 show junction temperature calculations for different ambient temperatures, power dissipation, and areas of PCB copper.
![img-51.jpeg](img-51.jpeg)

Figure 52. LFCSP, $T_{A}=25^{\circ} \mathrm{C}$
![img-52.jpeg](img-52.jpeg)

Figure 53. LFCSP, $T_{A}=50^{\circ} \mathrm{C}$
![img-53.jpeg](img-53.jpeg)

Figure 54. LFCSP, $T_{A}=85^{\circ} \mathrm{C}$
![img-54.jpeg](img-54.jpeg)

Figure 55. SOIC, $T_{A}=25^{\circ} \mathrm{C}$
![img-55.jpeg](img-55.jpeg)

Figure 56. SOIC, $T_{A}=50^{\circ} \mathrm{C}$
![img-56.jpeg](img-56.jpeg)

Figure 57. SOIC, $T_{A}=85^{\circ} \mathrm{C}$APPLICATIONS INFORMATION
![img-57.jpeg](img-57.jpeg)

Figure 58. TSOT, $T_{A}=25^{\circ} \mathrm{C}$
![img-58.jpeg](img-58.jpeg)

Figure 59. TSOT, $T_{A}=50^{\circ} \mathrm{C}$
![img-59.jpeg](img-59.jpeg)

Figure 60. TSOT, $T_{A}=85^{\circ} \mathrm{C}$
In the case where the board temperature is known, use the thermal characterization parameter, $\Psi_{J B}$, to estimate the junction temperature rise (see Figure 61, Figure 62, and Figure 63). Calculate the maximum junction temperature by using Equation 2.
$T_{J}=T_{B}+\left(P_{D} \times \Psi_{J B}\right)$
The typical value of $\Psi_{J B}$ is $24^{\circ} \mathrm{C} / \mathrm{W}$ for the 8 -lead LFCSP package, $38.8^{\circ} \mathrm{C} / \mathrm{W}$ for the 8 -lead SOIC package, and $43^{\circ} \mathrm{C} / \mathrm{W}$ for the 5-lead TSOT package.
![img-60.jpeg](img-60.jpeg)

Figure 61. LFCSP Junction Temperature Rise, Different Board Temperatures
![img-61.jpeg](img-61.jpeg)

Figure 62. SOIC Junction Temperature Rise, Different Board Temperatures
![img-62.jpeg](img-62.jpeg)

Figure 63. TSOT Junction Temperature Rise, Different Board Temperatures# PRINTED CIRCUIT BOARD LAYOUT CONSIDERATIONS 

Heat dissipation from the package can be improved by increasing the amount of copper attached to the pins of the ADP7142. However, as listed in Table 6, a point of diminishing returns is eventually reached, beyond which an increase in the copper size does not yield significant heat dissipation benefits.

Place the input capacitor as close as possible to the VIN pin and GND pin. Place the output capacitor as close as possible to the VOUT and GND pins. Use of 0805 or 1206 size capacitors and resistors achieves the smallest possible footprint solution on boards where area is limited.
![img-63.jpeg](img-63.jpeg)

Figure 64. Example LFCSP PCB Layout
![img-64.jpeg](img-64.jpeg)

Figure 65. Example SOIC PCB Layout
![img-65.jpeg](img-65.jpeg)

Figure 66. Example TSOT PCB Layout# PRINTED CIRCUIT BOARD LAYOUT CONSIDERATIONS

Table 8. Recommended LDOs for Very Low Noise Operation

|  Device
Number | $\mathrm{V}_{\text {IN }}$ Range
(V) | $\mathrm{V}_{\text {OUT }}$
Fixed (V) | $\mathrm{V}_{\text {OUT }}$
Adjust (V) | $\begin{aligned} & \mathrm{I}_{\text {OUT }} \ & (\mathrm{mA}) \end{aligned}$ | $\begin{aligned} & \mathrm{I}_{\mathrm{G}} \text { at } \ & \mathrm{I}_{\text {OUT }} \ & (\mu \mathrm{A}) \end{aligned}$ | $\begin{aligned} & \mathrm{I}_{\text {ONO-80 }} \ & \text { Max } \ & (\mu \mathrm{A}) \end{aligned}$ | Soft
Start | $\mathrm{P}_{\text {GOOD }}$ | Noise
(Fixed)
10 Hz to
100 kHz ( $\mu \mathrm{V}$
rms) | PSRR 100
kHz (dB) | PSRR 1
MHz | Package  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  ADP7102 | 3.3 to 20 | 1.5 to 9 | 1.22 to 19 | 300 | 750 | 75 | No | Yes | 15 | 60 | 40 dB | $3 \mathrm{~mm} \times 3 \mathrm{~mm} 8$ lead LFCSP, 8lead SOIC  |
|  ADP7104 | 3.3 to 20 | 1.5 to 9 | 1.22 to 19 | 500 | 900 | 75 | No | Yes | 15 | 60 | 40 dB | $3 \mathrm{~mm} \times 3 \mathrm{~mm} 8$ lead LFCSP, 8lead SOIC  |
|  ADP7105 | 3.3 to 20 | 1.8, 3.3, 5 | 1.22 to 19 | 500 | 900 | 75 | Yes | Yes | 15 | 60 | 40 dB | $3 \mathrm{~mm} \times 3 \mathrm{~mm} 8$ lead LFCSP, 8lead SOIC  |
|  ADP7112 | 2.7 to 20 | 1.2 to 5 | 1.2 to 19 | 200 | 180 | 10 | Yes | No | 11 | 68 | 50 dB | $1 \mathrm{~mm} \times 1.2 \mathrm{~mm} 6$ ball WLCSP  |
|  ADP7118 | 2.7 to 20 | 1.2 to 5 | 1.2 to 19 | 200 | 180 | 10 | Yes | No | 11 | 68 | 50 dB | $2 \mathrm{~mm} \times 2 \mathrm{~mm} 6$ lead LFCSP, 8lead SOIC, 5-lead TSOT  |
|  ADP7142 | 2.7 to 40 | 1.2 to 5 | 1.2 to 39 | 200 | 180 | 10 | Yes | No | 11 | 68 | 50 dB | $2 \mathrm{~mm} \times 2 \mathrm{~mm} 6$ lead LFCSP, 8lead SOIC, 5-lead TSOT  |
|  ADP7182 | $-2.7$ to -28 | $-1.8$ to -5 | $\begin{aligned} & -1.22 \text { to } \ & -27 \end{aligned}$ | -200 | -650 | -8 | No | No | 18 | 45 | 45 dB | $2 \mathrm{~mm} \times 2 \mathrm{~mm} 6$ lead LFCSP, 3 mm $\times 3 \mathrm{~mm} 8$-lead LFCSP, 5-lead TSOT  |

Table 9. Related Devices

|  Model | Input Voltage (V) | Output Current (mA) | Package  |
| --- | --- | --- | --- |
|  ADP7118CP | 2.7 to 20 | 200 | 6-lead LFCSP  |
|  ADP7118RD | 2.7 to 20 | 200 | 8-lead SOIC  |
|  ADP7118UJ | 2.7 to 20 | 200 | 5-lead TSOT  |
|  ADP7112CB | 2.7 to 20 | 200 | 6-ball WLCSP  |![img-66.jpeg](img-66.jpeg)

Figure 67. 6-Lead Lead Frame Chip Scale Package [LFCSP] $2.00 \mathrm{~mm} \times 2.00 \mathrm{~mm}$ Body and 0.55 mm Package Height (CP-6-3)
Dimensions shown in millimeters
![img-67.jpeg](img-67.jpeg)

Figure 68. 8-Lead Standard Small Outline Package, with Exposed Pad [SOIC_N_EP] Narrow Body
(RD-8-1)
Dimensions shown in millimeters
![img-68.jpeg](img-68.jpeg)

Figure 69. 5-Lead Thin Small Outline Transistor Package [TSOT] (UJ-5)
Dimensions shown in millimeters# OUTLINE DIMENSIONS

## ORDERING GUIDE

|  Model ${ }^{1,2}$ | Temperature Range | Package Description | Packing Quantity | Package
Option | Marking Code  |
| --- | --- | --- | --- | --- | --- |
|  ADP7142ACPZN1.8-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 6-Lead LFCSP ( $2 \mathrm{~mm} \times 2 \mathrm{~mm} \mathrm{w} / \mathrm{EP}$ ) | Reel, 3000 | CP-6-3 | LP5  |
|  ADP7142ACPZN2.5-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 6-Lead LFCSP ( $2 \mathrm{~mm} \times 2 \mathrm{~mm} \mathrm{w} / \mathrm{EP}$ ) | Reel, 3000 | CP-6-3 | LP7  |
|  ADP7142ACPZN3.3-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 6-Lead LFCSP ( $2 \mathrm{~mm} \times 2 \mathrm{~mm} \mathrm{w} / \mathrm{EP}$ ) | Reel, 3000 | CP-6-3 | LP6  |
|  ADP7142ACPZN3.8-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 6-Lead LFCSP ( $2 \mathrm{~mm} \times 2 \mathrm{~mm} \mathrm{w} / \mathrm{EP}$ ) | Reel, 3000 | CP-6-3 | LVK  |
|  ADP7142ACPZN5.0-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 6-Lead LFCSP ( $2 \mathrm{~mm} \times 2 \mathrm{~mm} \mathrm{w} / \mathrm{EP}$ ) | Reel, 3000 | CP-6-3 | LP8  |
|  ADP7142ACPZN-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 6-Lead LFCSP ( $2 \mathrm{~mm} \times 2 \mathrm{~mm} \mathrm{w} / \mathrm{EP}$ ) | Reel, 3000 | CP-6-3 | LP4  |
|  ADP7142ARDZ | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 8-Lead SOIC w/ EP | Tube, 98 | RD-8-1 |   |
|  ADP7142ARDZ-1.8 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 8-Lead SOIC w/ EP | Tube, 98 | RD-8-1 |   |
|  ADP7142ARDZ-1.8-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 8-Lead SOIC w/ EP | Reel, 1000 | RD-8-1 |   |
|  ADP7142ARDZ-2.5 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 8-Lead SOIC w/ EP | Tube, 98 | RD-8-1 |   |
|  ADP7142ARDZ-2.5-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 8-Lead SOIC w/ EP | Reel, 1000 | RD-8-1 |   |
|  ADP7142ARDZ-3.3 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 8-Lead SOIC w/ EP | Tube, 98 | RD-8-1 |   |
|  ADP7142ARDZ-3.3-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 8-Lead SOIC w/ EP | Reel, 1000 | RD-8-1 |   |
|  ADP7142ARDZ-5.0 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 8-Lead SOIC w/ EP | Tube, 98 | RD-8-1 |   |
|  ADP7142ARDZ-5.0-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 8-Lead SOIC w/ EP | Reel, 1000 | RD-8-1 |   |
|  ADP7142ARDZ-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 8-Lead SOIC w/ EP | Reel, 1000 | RD-8-1 |   |
|  ADP7142AUJZ-1.8-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 5-Lead TSOT | Reel, 3000 | UJ-5 | LP5  |
|  ADP7142AUJZ-2.5-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 5-Lead TSOT | Reel, 3000 | UJ-5 | LP7  |
|  ADP7142AUJZ-3.3-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 5-Lead TSOT | Reel, 3000 | UJ-5 | LP6  |
|  ADP7142AUJZ-5.0-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 5-Lead TSOT | Reel, 3000 | UJ-5 | LP8  |
|  ADP7142AUJZ-R2 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 5-Lead TSOT | Reel, 250 | UJ-5 | LP4  |
|  ADP7142AUJZ-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 5-Lead TSOT | Reel, 3000 | UJ-5 | LP4  |
|  ADP7142WAUJZ-1.8-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 5-Lead TSOT | Reel, 3000 | UJ-5 | LVQ  |
|  ADP7142WAUJZ-2.5-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 5-Lead TSOT | Reel, 3000 | UJ-5 | LVR  |
|  ADP7142WAUJZ-3.3-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 5-Lead TSOT | Reel, 3000 | UJ-5 | LVT  |
|  ADP7142WAUJZ-5.0-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 5-Lead TSOT | Reel, 3000 | UJ-5 | LVS  |
|  ADP7142WAUJZ-R7 | $-40^{\circ} \mathrm{C}$ to $+125^{\circ} \mathrm{C}$ | 5-Lead TSOT | Reel, 3000 | UJ-5 | LVU  |

${ }^{1} \mathrm{Z}=$ RoHS Compliant Part. ${ }^{2} \mathrm{~W}=$ Qualified for Automotive Applications.OUTLINE DIMENSIONS

# OUTPUT VOLTAGE OPTIONS

|  Model | Output Voltage (V) ${ }^{1}$  |
| --- | --- |
|  ADP7142ACPZN1.8-R7 | 1.8  |
|  ADP7142ACPZN2.5-R7 | 2.5  |
|  ADP7142ACPZN3.3-R7 | 3.3  |
|  ADP7142ACPZN3.8-R7 | 3.8  |
|  ADP7142ACPZN5.0-R7 | 5  |
|  ADP7142ACPZN-R7 | Adjustable (1.2 V)  |
|  ADP7142ARDZ | Adjustable (1.2 V)  |
|  ADP7142ARDZ-1.8 | 1.8  |
|  ADP7142ARDZ-1.8-R7 | 1.8  |
|  ADP7142ARDZ-2.5 | 2.5  |
|  ADP7142ARDZ-2.5-R7 | 2.5  |
|  ADP7142ARDZ-3.3 | 3.3  |
|  ADP7142ARDZ-3.3-R7 | 3.3  |
|  ADP7142ARDZ-5.0 | 5  |
|  ADP7142ARDZ-5.0-R7 | 5  |
|  ADP7142ARDZ-R7 | Adjustable (1.2 V)  |
|  ADP7142AUJZ-1.8-R7 | 1.8  |
|  ADP7142AUJZ-2.5-R7 | 2.5  |
|  ADP7142AUJZ-3.3-R7 | 3.3  |
|  ADP7142AUJZ-5.0-R7 | 5  |
|  ADP7142AUJZ-R2 | Adjustable (1.2 V)  |
|  ADP7142AUJZ-R7 | Adjustable (1.2 V)  |
|  ADP7142WAUJZ-1.8-R7 | 1.8  |
|  ADP7142WAUJZ-2.5-R7 | 2.5  |
|  ADP7142WAUJZ-3.3-R7 | 3.3  |
|  ADP7142WAUJZ-5.0-R7 | 5  |
|  ADP7142WAUJZ-R7 | Adjustable (1.2 V)  |

${ }^{1}$ For additional voltage options, contact a local Analog Devices, Inc., sales or distribution representative.

## EVALUATION BOARDS

|  Model ${ }^{1,2}$ | Package Description  |
| --- | --- |
|  ADP7142UJ-EVALZ | TSOT Evaluation Board  |
|  ADP7142CP-EVALZ | LFCSP Evaluation Board  |
|  ADP7142RD-EVALZ | SOIC Evaluation Board  |

${ }^{1} \mathrm{Z}=\mathrm{RoHS}$ Compliant Part. ${ }^{2}$ The evaluation boards are preconfigured with an adjustable ADP7142.

## AUTOMOTIVE PRODUCTS

The ADP7142W models are available with controlled manufacturing to support the quality and reliability requirements of automotive applications. Note that these automotive models may have specifications that differ from the commercial models; therefore, designers should review the Specifications section of this data sheet carefully. Only the automotive grade products shown are available for use in automotive applications. Contact your local Analog Devices account representative for specific product ordering information and to obtain the specific Automotive Reliability reports for these models.