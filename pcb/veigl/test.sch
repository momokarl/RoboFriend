EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:switches
LIBS:relays
LIBS:motors
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:teensy
LIBS:test-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "a schaas"
Date "2018-02-25"
Rev ""
Comp "Seppls Platinenservice"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L +5V #PWR01
U 1 1 5A92A711
P 4900 4650
F 0 "#PWR01" H 4900 4500 50  0001 C CNN
F 1 "+5V" H 4900 4790 50  0000 C CNN
F 2 "" H 4900 4650 50  0001 C CNN
F 3 "" H 4900 4650 50  0001 C CNN
	1    4900 4650
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 5A92A72F
P 4850 5600
F 0 "#PWR02" H 4850 5350 50  0001 C CNN
F 1 "GND" H 4850 5450 50  0000 C CNN
F 2 "" H 4850 5600 50  0001 C CNN
F 3 "" H 4850 5600 50  0001 C CNN
	1    4850 5600
	1    0    0    -1  
$EndComp
$Comp
L Conn_02x03_Counter_Clockwise J2
U 1 1 5A92A7CF
P 3200 1800
F 0 "J2" H 3250 2000 50  0000 C CNN
F 1 "PowerConn" H 3250 1600 39  0000 C CNN
F 2 "Connectors_Molex:Molex_MiniFit-JR-5556-06B_2x03x4.20mm_Straight" H 3200 1800 50  0001 C CNN
F 3 "" H 3200 1800 50  0001 C CNN
	1    3200 1800
	1    0    0    -1  
$EndComp
$Comp
L Teensy++2.0 U1
U 1 1 5A92B088
P 5850 3900
F 0 "U1" H 5850 5250 60  0000 C CNN
F 1 "Teensy++2.0" H 5850 2350 60  0000 C CNN
F 2 "footprints:Teensy2.0++" H 5950 3050 60  0001 C CNN
F 3 "" H 5950 3050 60  0000 C CNN
	1    5850 3900
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR03
U 1 1 5A92B301
P 4900 2800
F 0 "#PWR03" H 4900 2550 50  0001 C CNN
F 1 "GND" H 4900 2650 50  0000 C CNN
F 2 "" H 4900 2800 50  0001 C CNN
F 3 "" H 4900 2800 50  0001 C CNN
	1    4900 2800
	1    0    0    -1  
$EndComp
$Comp
L Conn_02x05_Odd_Even J1
U 1 1 5A92B523
P 7800 1900
F 0 "J1" H 7850 2200 50  0000 C CNN
F 1 "MLeftConn" H 7850 1600 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x05_Pitch2.54mm" H 7800 1900 50  0001 C CNN
F 3 "" H 7800 1900 50  0001 C CNN
	1    7800 1900
	1    0    0    -1  
$EndComp
$Comp
L Conn_02x05_Odd_Even J3
U 1 1 5A92B589
P 9950 1900
F 0 "J3" H 10000 2200 50  0000 C CNN
F 1 "MRightConn" H 10000 1600 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x05_Pitch2.54mm" H 9950 1900 50  0001 C CNN
F 3 "" H 9950 1900 50  0001 C CNN
	1    9950 1900
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR04
U 1 1 5A92B90B
P 7450 1550
F 0 "#PWR04" H 7450 1400 50  0001 C CNN
F 1 "+5V" H 7450 1690 50  0000 C CNN
F 2 "" H 7450 1550 50  0001 C CNN
F 3 "" H 7450 1550 50  0001 C CNN
	1    7450 1550
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR05
U 1 1 5A92B922
P 9550 1550
F 0 "#PWR05" H 9550 1400 50  0001 C CNN
F 1 "+5V" H 9550 1690 50  0000 C CNN
F 2 "" H 9550 1550 50  0001 C CNN
F 3 "" H 9550 1550 50  0001 C CNN
	1    9550 1550
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR06
U 1 1 5A92B939
P 8250 2300
F 0 "#PWR06" H 8250 2050 50  0001 C CNN
F 1 "GND" H 8250 2150 50  0000 C CNN
F 2 "" H 8250 2300 50  0001 C CNN
F 3 "" H 8250 2300 50  0001 C CNN
	1    8250 2300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR07
U 1 1 5A92B950
P 10450 2300
F 0 "#PWR07" H 10450 2050 50  0001 C CNN
F 1 "GND" H 10450 2150 50  0000 C CNN
F 2 "" H 10450 2300 50  0001 C CNN
F 3 "" H 10450 2300 50  0001 C CNN
	1    10450 2300
	1    0    0    -1  
$EndComp
Wire Wire Line
	5150 4750 4900 4750
Wire Wire Line
	4900 4750 4900 4650
Wire Wire Line
	5150 2750 4900 2750
Wire Wire Line
	4900 2750 4900 2800
Wire Wire Line
	7600 1700 7450 1700
Wire Wire Line
	7450 1700 7450 1550
Wire Wire Line
	9750 1700 9550 1700
Wire Wire Line
	9550 1700 9550 1550
Wire Wire Line
	8100 1700 8250 1700
Wire Wire Line
	8250 1700 8250 2300
Wire Wire Line
	10250 1700 10450 1700
Wire Wire Line
	10450 1700 10450 2300
Wire Wire Line
	8100 1800 8400 1800
Wire Wire Line
	8100 1900 8400 1900
Wire Wire Line
	8100 2000 8400 2000
Wire Wire Line
	8100 2100 8400 2100
Wire Wire Line
	7600 2100 7350 2100
Wire Wire Line
	10250 1800 10600 1800
Wire Wire Line
	10250 1900 10600 1900
Wire Wire Line
	10250 2000 10600 2000
Wire Wire Line
	10250 2100 10600 2100
Text Label 8400 1800 0    60   ~ 0
MLeftSig1
Text Label 8400 1900 0    60   ~ 0
MLeftSig2
Text Label 10600 1800 0    60   ~ 0
MRightSig1
Text Label 10600 1900 0    60   ~ 0
MRightSig2
Text Label 8400 2000 0    60   ~ 0
MLeftFwd
Text Label 8400 2100 0    60   ~ 0
MLeftBck
Text Label 7350 2100 2    60   ~ 0
MLeftPWM
Text Label 10600 2000 0    60   ~ 0
MRightFwd
Text Label 10600 2100 0    60   ~ 0
MRightBck
Wire Wire Line
	9750 2100 9550 2100
Text Label 9550 2100 2    60   ~ 0
MRightPWM
Wire Wire Line
	5150 4350 4600 4350
Text Label 4600 4350 2    60   ~ 0
MRightPWM
Wire Wire Line
	5150 4450 4600 4450
Text Label 4600 4450 2    60   ~ 0
MLeftPWM
Wire Wire Line
	5150 4150 4600 4150
Wire Wire Line
	5150 4250 4600 4250
Text Label 4600 4150 2    60   ~ 0
MLeftFwd
Text Label 4600 4250 2    60   ~ 0
MLeftBck
Wire Wire Line
	5150 3950 4600 3950
Wire Wire Line
	5150 4050 4600 4050
Text Label 4600 3950 2    60   ~ 0
MRightFwd
Text Label 4600 4050 2    60   ~ 0
MRightBck
Wire Wire Line
	6550 4350 6950 4350
Wire Wire Line
	6550 4250 6950 4250
Wire Wire Line
	6550 4150 6950 4150
Wire Wire Line
	6550 4050 6950 4050
Text Label 6950 4350 0    60   ~ 0
MLeftSig1
Text Label 6950 4250 0    60   ~ 0
MLeftSig2
Text Label 6950 4150 0    60   ~ 0
MRightSig1
Text Label 6950 4050 0    60   ~ 0
MRightSig2
Wire Wire Line
	5150 4850 4850 4850
Wire Wire Line
	4850 4850 4850 5600
$EndSCHEMATC
