# rickrollpi
Use your Raspberry Pi for Rick Rolling

This project is using AIY google kit: https://aiyprojects.withgoogle.com/voice-v1/

## 1. Follow these instructions to build the device and setup software

https://aiyprojects.withgoogle.com/voice-v1/

## 2. Clone this repo
Connect to Pi by SSH'ing into it

```
git clone https://github.com/martyweb/rickrollpi.git
cd rickrollpi
chmod +x rick.*
```
## 3. Test the script
This should run the script and enable you to push the button and hear the sound
```
./rick.sh
```

## 4. Setup autostart
### 4a. Raspiconfig
```sudo raspi-config```

Select this option: System Options -> Boot / Auto Login -> Desktop Auto Login

### 4b. Add command to autostart (example file is in the "autostart" in repo)
Run: 
```nano /home/pi/.config/lxsession/LXDE-pi/autostart```

Add line: 
```@bash /home/pi/rickroll/rick.sh```
