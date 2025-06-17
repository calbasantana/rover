<p align="center">
  <img src="media/photos/rover.jpg" alt="PCB Front" width="500"/>
</p>

# Introduction

The purpose of this repository is to provide access to an open-source platform that I have created and developed for students over the last few years as a means of expanding their understanding of physics concepts by applying physics concepts to engineering challenges. This engineering challenge entails the create of a rover - a four- to eight-wheeled vehicle - using an ESP32 microcontroller on a custom PCB.

The engineering challenge has changed over the years, but most recently it has resulted in the development of the companion repository to this repository - the rover challenges arena. Students try to complete up to 10 different challenges with the use of a rover. The present repository covers the construction and coding of the rover.

# Rover Materials

The materials used for this project are broken down into the following components.

## Custom-PCB

<p align="center">
  <img src="media/photos/pcb_front.jpg" alt="PCB Front" width="400"/>
  <img src="media/photos/pcb_back.jpg" alt="PCB Back" width="400"/>
</p>

This custom PCB is designed for an ESP32 to connect to two small motor drivers. It has pins for up to eight motors. However, because each motor driver can only control two motors, this is achieved by making parallel connections to each of the exisiting connections. This means that only four motors can be individually controlled.

This PCB was created using [EasyEDA](https://easyeda.com/). To order a copy of this PCB, uploead the Gerber file from the PCB folder and upload it to [JLCPCB](https://jlcpcb.com/?href=easyeda-home), which is one of many websites that can manufacture PCBs for consumers. They are generally really cheap. As an example, a batch of 50 PCBs costs $19. The only real expensive part is the shipping, usually around $17-50.

The PCB schematic is on the left and the PCB layout is on the right in the images below.

<p align="center">
  <img src="media/screenshots/pcb_schematic.png" alt="PCB Schematic" width="500"/>
  <img src="media/screenshots/pcb_layout.svg" alt="PCB Layout" width="200"/>
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
* [Female Header Pins (X62, ~0.95 total)](https://www.amazon.com/HiLetgo-Single-Female-2-54mm-Vertical/dp/B00VVI1L1W/ref=sr_1_3_pp?crid=NPNPOKB91D29&dib=eyJ2IjoiMSJ9.9vMG7GqiAFYneYPy2v9wQx7lT2hcQ21uJ3e7QXKd_EpeJU6i4XD_6IQeQc9utVA1-admOWsRZY8n1KRUA5fB8FU6J1WYhzvevCKz7TDfNkUMr8vHz4yNH4MuzlXgmvm73Sh_UjgRwEPRol1EbqMn6DA71yFwVrXtCO42eYcRAyAbe0Jmh2ia_QMplpS08nGHomcU6_ZsW1rTJIa2oyH3JiYsLgm-X5SW7Ce0QAfSFRY.NFfpzE2d00qUkSDoAWciaKczEzbB0I4n1xxrOmx6gXo&dib_tag=se&keywords=female+header+pins&qid=1749999579&sprefix=female+header+pin%2Caps%2C156&sr=8-3)
* [Female JST Connectors (X2, ~$0.70 total)](https://www.amazon.com/JST-PH-Connector-Silicone-Cables-Female/dp/B0D7Q9HJLQ/ref=sr_1_6?crid=1OY008FZLL536&dib=eyJ2IjoiMSJ9.4aRmf4dmQKSs9h_unlhZ_TgC8WKbhZY8RALcwZqi1RJsGpiDVvwwjpCrT4n0gMqLo1yuU8t-5NAq3znRMLu7aD6gjDpXYebLzliudYr6stwDojt8r4pEUoLxPhwmeTG3fAjsFNm7kbAROLlhk5SFx6iwu-nLGKs4lNizYMZlD0OdhFTR8XtegeO5o9HZ-fizsNefvIvn86OZqmizFdhWUN6F7_IAZVKl1c2gG709zG7FF_3uOQ2je62cglIUAwJO0cWTP38_-sOKsTn8sV8lprWvCuxEu70HfiI0O_-FXPE.BD_9UebhgyUL0OsyTiWHE1vSSe1FSmDZ6Pfw9cERLc4&dib_tag=se&keywords=PH+2.0+female&qid=1749999041&s=electronics&sprefix=ph+2.0+female%2Celectronics%2C110&sr=1-6)*
* [Switch (X1, ~$0.40 total)](https://www.amazon.com/dp/B07FVM3XYR?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_14)
* [M3 x 12mm Socket Screw (X10, ~$0.90 total)](https://www.amazon.com/Socket-Screws-Metric-Stainless-Machine/dp/B07KRRNDGC/ref=sr_1_1_pp?crid=181TL0KV8WMZI&dib=eyJ2IjoiMSJ9.qFKcM0_hOHsuDVnbysODHM9XFF-_A7_uLYXTW4WCNCpoM_k8vr51OMGSw6TwAykqneJ55IARZPzY82BU8el1Eb3YGrV60S8IzDGbxCJ-s00cydmgddsyUVyTwMX-SvRT9F4360SLhiZ4ohbTgS9Pfa2T1zNszpvQZeTTyWG1MVFGcq4BRzXAJU9JoK2RTOMzRVn_0Vz13PuqKfrIFJnmyAr9zIVGNiuL1U62YW33UBU.dQt5aficSLVgpOmchhikaIVgcZDt6ddoisIbHYLGrrI&dib_tag=se&keywords=m3%2Bscrews&qid=1749999877&sprefix=m3%2Bscrew%2Caps%2C176&sr=8-1&th=1)
* [M3 Nut (X2, ~$0.15 total)
](https://www.amazon.com/BinifiMux-100Pcs-0-5mm-Lock-Nuts/dp/B075ZZW7VL/ref=sr_1_3_pp?crid=181TL0KV8WMZI&dib=eyJ2IjoiMSJ9.qFKcM0_hOHsuDVnbysODHM9XFF-_A7_uLYXTW4WCNCpoM_k8vr51OMGSw6TwAykqneJ55IARZPzY82BU8el1Eb3YGrV60S8IzDGbxCJ-s00cydmgddsyUVyTwMX-SvRT9F4360SLhiZ4ohbTgS9Pfa2T1zNszpvQZeTTyWG1MVFGcq4BRzXAJU9JoK2RTOMzRVn_0Vz13PuqKfrIFJnmyAr9zIVGNiuL1U62YW33UBU.dQt5aficSLVgpOmchhikaIVgcZDt6ddoisIbHYLGrrI&dib_tag=se&keywords=m3+screws&qid=1749999877&sprefix=m3+screw%2Caps%2C176&sr=8-3)
* [Male-to-Female cable jumpers (Optional, X4-X8, ~$0.35 ea.)
](https://www.amazon.com/Elegoo-EL-CP-004-Multicolored-Breadboard-arduino/dp/B01EV70C78/ref=sr_1_3?crid=2ZR1BQEZH4IW2&dib=eyJ2IjoiMSJ9.5rAMJ78BD0lhbGZWyHYck31fdM2Hh3UJkHfOnVIjk5gtzulkosZnUVRL9dNsoh9dsgBt7WY6honTqPFFwXvYh8Qa3zZAAt8P-GjIpCxT51RMMRnm0ZGDlVXjY5zuz7Ey_RcQ37DMdvXtgZkPs-nTEVUu9sVfYKFk-kkbtNQfh9Pqx7QdvDnXENwrJKClrhgIUUwY6l_rrxWWe9RkkMJxY4pZy-Lec4Mc3pU0vFAsRjs.Kr2Grj1a15xKc42zvtqmRBMftRLNJHvuzMyTCJ2BXoM&dib_tag=se&keywords=male+to+female+cable&qid=1750012097&sprefix=male+to+female+cable%2Caps%2C165&sr=8-3)

*: I was not able to find the 2-pin female JST connectors by themselves, so I just used the ones from this bundle.

The above prices are an estimate and does not take into account that if you were to just build one rover, the price would be much higher. However, if you were to assume that you bought enough materials for a class to create somewhere between 5 to 6 rovers, the estimated cost above might make sense on a per rover basis. On average, each rover should cost around **$72.52** (not including the optional cable jumpers, which can allow the rover to be significantly larger). Now, that certainly isn't cheap, but all of these materials can be reused over and over again and if some parts are broken, then they are easy to replace for a few dollars, unlike other platforms that cost upwards of $300 (see [PASCObot](https://www.pasco.com/products/stem-sense/sense-and-control/ps-2994) as an example).

# Rover Body

The rover body needs to be able to hold the most critical parts of the rover, specifically the PCB and batteries. It is also usually the largest single piece of the rover. For this reason, lasercutting is particularly useful. You can not only make large parts without warping, as would occur with 3D printing such a large piece, but you can also make them fast, allowing room for rapid prototyping and fixing of mistakes (because things seldom go right the first time).

## OnShape

To make the body and other parts of the rover, I use [OnShape](https://cad.onshape.com/) and recommend that my students do the same. This is a free online CAD tool, available on all devices and can run even on the most limited of hardware machines.

### OnShape Tutorial

I ask my students to follow an [OnShape Tutorial](https://learn.onshape.com/courses/unit-2-designing-a-skateboard) first, creating a skateboard to familiarize themselves with the tools of OnShape. Most useful are the sketch, extrude, mirror, and dimension tools.

After students have become familiar with OnShape, it is then recommended that they create their own OnShape document and share it out with their group members. While one person will be primarily taking the responsibility of the document, they should all be involved with determining measurements and making design decisions. There will also be days where the lead the designer may be out, so others need to step in their place to continue progress.

### OnShape CAD Model

Below you will see an example of what a rover could look like. This is a very basic design and students can - and should - deviate from it to suit their needs.

<p align="center">
  <img src="media/screenshots/rover_CAD.png" alt="Rover CAD Model" width="500"/>
</p>

Most notable about this design are the following features:

* **Vertical Battery Placement**: The batteries are placed vertically so the rover remains compact.
* **Vertical PCB**: The PCB is placed vertically such that accessing the USB-C port is easier. Additionally, this makes it so that the overall footprint of the base is smaller.
* **Four Motors**: I decided on four motors for simplicity. Having a few additional motors may have been helpful to increase friction for challenges like Challenge 6: Welcome to Seattle, but I decided against it. Should students wish to attempt this challenge, it may be wise to increase the number of motors/wheels.

### Videos for Support

Below you will find videos pertaining to each section of the base design and how they were created. It may be helpful to view them, but students should deviate from this design as needed. Please note these videos are available under media/videos.

**Base and PCB Holder**

https://github.com/user-attachments/assets/f6f469bb-e396-4308-9e46-521faad81ced

**Battery Holders**

https://github.com/user-attachments/assets/219071bb-fc81-4022-aa20-69a2cab3a099

**Motor Mounts**

https://github.com/user-attachments/assets/837b10f8-ceb4-4dcb-96e3-d2f189cb6fed

## Lasercutting and 3D Printing

Most of the rover will be - or at least should be - lasercut. This will make prototyping easier. Out of the previously demonstrated parts, the base, PCB holder, and battery holders components will be lasercut. Motor mounts, due to both their small size and irregular shape, are best 3D printed. Below you will find specifications of the lasercutter and 3D printer used.

### Materials
* [4-Pack 12" x 16" x 1/8" Walnut Plywood Sheets ($23.99)](https://www.amazon.com/ROBOTIME-16-Pack-Walnut-Plywood-Sheets/dp/B0D4QTZWJW/ref=sr_1_5?crid=5N28N9MA546C&dib=eyJ2IjoiMSJ9.k-VTc77EEiA7iWVr4SBXFp1fa-s328xiTw0COCg3Xb3MTlrC8jpyruFXeUAeiiCiWeqd_bGG2jZyUaQwydheF_9vHEUdJ36aQLL7ZHE5pD8w4FC9Gp49ls-iut2qMNPMHNQ82mpEpoqCAWkl8qQQYMF5L2UaZzDGzs6tHkzidyan0-cBc8F1ldLTGhLnjbjEgGYdoTjovSiQekXt7Qi3dmsm8Edp9dEApYT0CpZSLDZV_hyY13bmmnv_ypCVnFxkAoH8YGcZmUlBg8sBuiU4P-10BCj7j6n8NnpZB6GvpBw.S8gtR7mVVgHNEFjv2BN-OQO5X2sNbt_du2D0Gg0-LNU&dib_tag=se&keywords=robotime%2B8%2Bpack%2Bwalnut%2Bplywood%2Bsheets%2B12%2Bx%2B16&qid=1746033927&sprefix=robotime%2B8%2Bpack%2Bwalnut%2Bplywood%2Bsheets%2B12%2Bx%2B16%2Caps%2C70&sr=8-5&th=1)
* [Navy Blue ELEGOO 1kg, 1.75mm Filament ($18.69)](https://www.amazon.com/ELEGOO-Filament-Dimensional-Accuracy-Carboard/dp/B0CFV4WLY6/ref=sr_1_1?dib=eyJ2IjoiMSJ9.0zBpEpW4jNbq1P5QCaHqCDY1p09Dfbw3Amhrep2wDUAoP2OhINhw7hHcC1wH-1VgctB92Ci-VHMd2DsSIe3xQaMOLhpzDRa-ui6xJ0zy1eKPvdz4Tl1GfT9mzRmei9OSNcotDHvOwjmG1bahxUusv1efDrZm5Zcp2qnXroiV6WCIBQMEZ7esqvav3zGEm5NzIS_VPlqaA3rYNav5nIaTwUfFZmpOaOG9pfS6o4Kng8w.LMNtaL9GyxCNgsTN4-3rez2hmy-NqedElxaa92ErEtA&dib_tag=se&keywords=ELEGOO+Matte+PLA+Filament+Navy+Blue+1KG%2C+1.75mm+3D+Printer+Filament+Dimensional+Accuracy+%2B%2F-+0.02mm%2C+1kg+Carboard+Spool+%282.2lbs%29+for+Most+FDM+3D+Printers&qid=1750015709&sr=8-1)

### Lasercutter
XTool D1 Pro \
**Software** \
XTool Creative Studio (XCS) \
**Settings (for cutting)** \
Power (%): 100 \
Speed (mm/s): 5 \
Pass: 1

### 3D Printer
Original Prusa Mini+ \
**Software** \
PrusaSlicer \
**Settings** \
Layer Height: .2mm \
Infill: 50% \
Supports: Everywhere \
Estimated Printing Time: ~ 2hours.

## Assembly

Once all parts have been lasercut and 3D printed, it is time for assembly. I highly suggest starting off with hot gluing all parts that need to be hot glued and waiting for a bit for them to dry. After doing this, it is recommended to assemble in the following order:

* Place and screw the PCB. Make sure the ESP32 and motor drivers are on it.
* Screw the motor mounts to the board.
* Place the DC motors inside the motor mounts and screw them in, being very careful with their cables. I recommend placing the motors such that the cables coming out of them face towards the center of the rover (this way they won't get caught on stuff).
* Screw the wheels onto the DC motors.
* Connect the motors in the desired locations, using cable jumpers if necessary. **Black goes on GND and red on VCC**. It is recommended to have one motor in each of the numbered slots (like 1A, 2A, 3A, and 4A).
* Connect the battery adapter cables.
* Connect the batteries to test that all components work. **IMPORTANT**: If running the default code, it will have all motors moving forward, so if some wheels are spinning backwards, you can change the orientation of the motor connections such that the black cable is on VCC and red is on GND; **this only works to reverse the drive of motors, do not try this with the batteries**. Remove once you've confirmed all components seem to be working OK. Report any issues.

# Programming

Thonny is used as the programming platform. Students can install this application on their own non-chromebook devices using the instructions below.

Go to the official [Thonny](https://thonny.org/) website and download the application. Then, depending on your operating system, continue as follows:

**For Windows**: Install the 64-bit version. Then, go to this [website](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) to install a driver, which will allow USB access to Thonny so it can connect to the ESP32 via USB. Go to Downloads, then click CP210x VCP Windows. Once downloaded, use the x64 .exe file to install the driver. \
**For Mac**: Install using the first option with .pkg. Then, go to this [website](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) to install a driver, which will allow USB access to Thonny so it can connect to the ESP32 via USB. Go to Downloads, then click CP210x VCP Mac OSX Driver. Then click on the .dmg file to install; **it will ask you to give access at some point in the settings, make sure to allow it access otherwise it won’t work**. \
**For Linux**: It is recommended that you use the flatpak installation method if you already have flatpak in your system. If you do not have flatpak in your system, you may install it from the terminal via your default package manager; see this [website](https://flatpak.org/setup/) for specific directions if you are unsure. You may need to use “sudo chmod a+rw /dev/ttyUSB0” to open up the USB connection each time you connect the ESP32.

Rovers are programmed in microPython. Below you will find some instructions on how to program the rover, which requires that both .py files in this repostory (main.py and rover.py) are uploaded to the ESP32.

## Programming Your Rover

To program your rover, first open up the Thonny application. Then, follow the instructions below.

1. Remove your ESP32 from your rover. Trying to connect to it while it is connected to the rover might damage the ESP32, so it is best to remove it and then connect to it.

2. Press the STOP/Start button. At the bottom of the screen, you should see ">>>". This should indicate the ESP32 is connected.

3. Go to File -> Open. Select from micropython device. Here, you should be able to open up the main.py file.

4. You should also be able to open rover.py file to see available functions. Essentially, the most important three pieces of code are the following:

  * **rover.move_motor(motor_num, direction, speed)**: You should input the motor number, the direction (forward or backward), and speed (100 - 1000). For example, rover.move_motor(1, forward, 300) moves motor 1 at a speed of 300 forward. You can have multiple motors move at the same time by having them on separate, but sequential lines like so:
    * rover.move_motor(1, forward, 300)
    * rover.move_motor(2, forward, 300)
  These two lines of code move motors 1 and 2 forward at a speed of 300.
  * **sleep(time)**: This piece of code decides how long the previous piece of code runs for before moving to the next. If placed right after the two pieces of code from the last bullet point, it will move those two motors forward at a speed of 300 for 10 seconds before moving to the next piece of code. Decimals are allowed.
  * **gradual_stop_all(direction="forward", initial_speed=700)**: This piece of code gradually stops all motors. No edits are necessary. However, if you would like to match the speed with the speed from previous line of code, you may do so.

# Tips

Since I have been doing this for a while, there are a lot of issues I've learned how to troubleshoot.
