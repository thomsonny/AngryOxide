# File path: epaper_display.py

import os
import subprocess
import time
import spidev
import RPi.GPIO as GPIO
from waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont

# Initialize GPIO and SPI
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define pin configuration
RST_PIN = 17
DC_PIN = 25
CS_PIN = 8
BUSY_PIN = 24

# Initialize e-Paper display
epd = epd2in13_V2.EPD()
epd.init()

# Clear the display
epd.Clear(0xFF)

# Create a new image with white background
width, height = epd.height, epd.width  # Swap width and height
image = Image.new('1', (width, height), 255)  # 255: clear the frame
draw = ImageDraw.Draw(image)

# Define font
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 14)

# Function to update display
def update_display(process_status):
    draw.rectangle((0, 0, width, height), fill=255)  # Clear image
    draw.text((10, 10), "Process Status:", font=font, fill=0)
    y_offset = 30
    for line in process_status:
        draw.text((10, y_offset), line, font=font, fill=0)
        y_offset += 20
        if y_offset > height - 20:  # Ensure text fits within display
            break

    # Rotate the image for correct orientation
    rotated_image = image.rotate(180)  # Rotate 180 degrees if necessary
    epd.display(epd.getbuffer(rotated_image))

# Function to check if a process is running
def check_process(process_name):
    try:
        result = subprocess.run(['pgrep', '-f', process_name], stdout=subprocess.PIPE, text=True)
        return f"{process_name}: Running" if result.stdout else f"{process_name}: Not Running"
    except Exception as e:
        return f"Error: {e}"

# Main function
def main():
    processes_to_check = ["angryoxide", "other_process"]  # Add other processes if needed
    try:
        while True:
            process_status = [check_process(proc) for proc in processes_to_check]
            update_display(process_status)
            time.sleep(10)
    except KeyboardInterrupt:
        print("Exiting...")
        epd.sleep()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
