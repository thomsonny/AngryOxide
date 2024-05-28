# AngryOxide

# Raspberry Pi Zero 2 W e-Paper Display Project

## Overview
This project uses a Waveshare 2.13 inch e-Paper HAT v4 with a Raspberry Pi Zero 2 W to display process statuses.

## Setup

### Hardware
- Waveshare 2.13 inch e-Paper HAT v4
- Raspberry Pi Zero 2 W
- Sd Card 

### Software
- Raspbian OS lite
- Python 3
- Required Python libraries: `spidev`, `RPi.GPIO`, `Pillow`, `waveshare_epd`

### Installation
1. **Install necessary libraries**:
   ```sh
   sudo apt-get update
   sudo apt-get install python3-pil python3-spidev python3-rpi.gpio