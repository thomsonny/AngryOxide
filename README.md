# Raspberry Pi Zero 2 W e-Paper Display Project w/ Angry Oxide 

## Overview
This project uses a Waveshare 2.13 inch e-Paper HAT v4 with a Raspberry Pi Zero 2 W to display process statuses of Angry Oxide running headless at boot

## Setup

### Hardware
- Waveshare 2.13 inch e-Paper HAT v4
- Raspberry Pi Zero 2 W
- Sd Card 

### Software
- Raspbian OS lite
- Python 3
- Required Python libraries: `spidev`, `RPi.GPIO`, `Pillow`, `waveshare_epd`

### Display Installation

1. Follow the steps to install Angry Oxide on your pi [here](https://github.com/ScriptTactics/AngryOxide-Scripts).
   
2. Download the epaper_display.py file from this page and put it onto the root of your sd card

3. run 
   > sudo python3 epaper_display.py

this will check the script is working with your display

### Angry Oxide auto boot setup

Open a New Terminal Session

1. SSH into your Raspberry Pi:
2. Run the e-Paper display script if it's not already running:
> sudo python3 epaper_display.py
3. 
















