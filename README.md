# rickrollpi
Use your Raspberry Pi for Rick Rolling

THis project is using AIY google kit: https://aiyprojects.withgoogle.com/voice-v1/

1. Follow these instructions to build the device and setup software

https://aiyprojects.withgoogle.com/voice-v1/

2. Setup rickroll software 
    Aquire a rickroll.wav file
3. Clone repo


4. Setup autostart
4a. Raspiconfig
```sudo raspi-config```
Select this option: System Options -> Boot / Auto Login -> Desktop Auto Login

4b. Add command to autostart (example file is in the "autostart" in repo)
Run: 
```nano /home/pi/.config/lxsession/LXDE-pi/autostart```

Add line: @bash /home/pi/Desktop/rick.sh
