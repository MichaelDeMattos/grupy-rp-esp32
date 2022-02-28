# grupy-rp-esp32
Esp32 - Micropython (Pylestra - 2022)

###### Install pependences to Debian or Derivates
...
apt update
sudo apt install python3-pip python3-venv libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0 
...


###### Write MircroPython - Firmware


If you are putting MicroPython on your board for the first time then you should first erase the entire flash using:

...
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
...

From then on program the firmware starting at address 0x1000:

...
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 115200 write_flash -z 0x1000 <Firmware>
...