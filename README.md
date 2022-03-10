# rickrollpi
Use your Raspberry Pi for Rick Rolling

THis project is using AIY google kit: https://aiyprojects.withgoogle.com/voice-v1/

1. Follow these instructions to build the device and setup software

https://aiyprojects.withgoogle.com/voice-v1/

2. SSH into Pi 

3. Clone this repo
```
git clone https://github.com/martyweb/rickrollpi.git
cd rickrollpi
chmod +x rick.*
```
3a. Test the script
```
./rick.sh
```

4. Setup autostart
4a. Raspiconfig
```sudo raspi-config```
Select this option: System Options -> Boot / Auto Login -> Desktop Auto Login

4b. Add command to autostart (example file is in the "autostart" in repo)
Run: 
```nano /home/pi/.config/lxsession/LXDE-pi/autostart```

Add line: 
```@bash /home/pi/rickroll/rick.sh```
