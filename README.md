[PICTURE]

# Introduction

I have developed this open-source rover platform over the last few years as a means of expanding my students' understanding of physics concepts by applying them to an engineering challenge. The engineering challenge has changed over the years, but most recently it has resulted in the development of the companion repository to this repository - the rover challenges arena. Students try to complete up to 10 different challenges with the use of a rover. The present repository covers the construction and coding of the rover.

# Rover Materials

The materials used for this project are broken down into the following components.

## Custom-PCB

[PICTURE]

This custom PCB is designed for an ESP32 to connect to two small motor drivers. It has pins for up to eight motors. However, because each motor driver can only control two motors, this is achieved by making parallel connections to each of the exisiting connections. This means that only four motors can be individually controlled.

This PCB was created using [EasyEDA](https://easyeda.com/). To order a copy of this PCB, uploead the Gerber file from the PCB folder and upload it to [JLCPCB](https://jlcpcb.com/?href=easyeda-home), which is one of many websites that can manufacture PCBs for consumers. They are generally really cheap. As an example, a batch of 50 PCBs costs $19. The only real expensive part is the shipping, usually around $17-50.

The PCB schematic is on the left and the PCB layout is on the right in the images below.  for reference:

<p align="center">
  <img src="media/screenshots/pcb_schematic.png" alt="PCB Schematic" width="600"/>
  <img src="media/screenshots/pcb_layout.svg" alt="PCB Layout" width="250"/>
</p>

## Microcontroller, Motors, and Motor Drivers

The following materials need to be purchased for this rover (links included):

* [USB-C ESP32 (X1, $8.99 ea.)](https://www.amazon.com/AITRIP-ESP-WROOM-32-Development-Microcontroller-Integrated/dp/B0DF2YJSHN/ref=sr_1_3?crid=1G6IDOYNKPKX9&dib=eyJ2IjoiMSJ9.J8fl2PuZsBFTQRqqz9O9mLtmR5c3g4T6QqdGo-D0eTjT6x-RNRspTE-T1cENww24dOzuOXNMWdfDVSyXLg11Bf9geRDMJQTGeN8fDzUZQdUuu6ql33jUCzh54aLePB23ZYlcQnI6kKamfVrkVmBWImiDyPM2_cfJRQ31eAQTGoVGCAZvd5FDOsKMtfXPDIBeboR9r5_mAR9PJ2iZAl1XFMpgxN3lRmXGAhl4d1pkhEw.R_NzTn628-SylaJJRwnYczlZxkceZnzVgDT5ZIbxqGE&dib_tag=se&keywords=esp32%2Busb%2Bc&qid=1747615119&sprefix=esp32%2Busb%2Bc%2Caps%2C127&sr=8-3&th=1)
* [Motor Driver (X2, $6.95 ea.)](https://www.adafruit.com/product/2448)
* [Batteries (X2, $19.99 total)](https://www.amazon.com/dp/B0C5CDZ7HS?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_3)
* [Battery adapter cables (X2, $1.17 ea.)](https://www.amazon.com/dp/B08SC3D3SQ?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_1&th=1)
* [DC Motors (X4-X8, $3.50 ea.)](https://www.adafruit.com/product/2941)
* [Wheels (X4-X8, $2.50 ea.)](https://www.adafruit.com/product/2744)
* [Male Header Pins (X16, ~$0.20 total)](https://www.amazon.com/MCIGICM-Header-2-45mm-Arduino-Connector/dp/B07PKKY8BX/ref=sr_1_3?crid=1UOTCLVLP8NBF&dib=eyJ2IjoiMSJ9.3vFjmsH10W3-0I49M7i2SLer6N2w76n3suAL41lNyWbCktqeX2xUwJKGOw1Unq-mAp24IQL2WQ-Ev7Umi65YURue2SRQPZGjTOn-chwyhK-M_IjeCaW5rokSMnyMAVVnZTc5CzgG8dEONU-uutB7UxnSnLH0U2Croee-BUiI-JDEPxRCRiiMCBSRJgNAdIBv6GiGNRgSYq-3P6zK5nOuW5kb43uDa-oWIACeoFh99JM.nKbcZqvC_hNR6ES6f7s5o9FuPlfrFeEAsgNfd5lOjas&dib_tag=se&keywords=male+header+pin&qid=1747615696&sprefix=male+header+pin%2Caps%2C160&sr=8-3)
* Female JST Connectors
* M3 x 10mm Hex Screw
* M3 Nut

Based on XYZ ...

# Rover Body

[PICTURE]


The most efficient way of making the body for the rover is to lasercut most of it. This is because lasercutting is much quicker than 3D printing and can be great for rapid prototyping. I usually have students lasercut cardboard designs first to ensure their dimensions are correct and then final designs are made on 3mm/6mm plywood.

## OnShape

Designs are made on [OnShape](https://cad.onshape.com/).

This is a free online CAD tool, available on all devices and can run even on the most limited of hardware machines.

### OnShape Tutorial

I ask my students to follow the OnShape Tutorial first, creating a skateboard to familiarize themselves with the tools of OnShape. Most useful are the sketch, extrude, mirror, and dimension tools.

### OnShape CAD Model

### Videos for Support

## Lasercutting and 3D Printing

### 3D Printer

### Lasercutter

## Assembly

# Programming

## Thonny

## Programming Basics

# Tips
