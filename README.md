# Digital-Picture-Frame
1. Make sure to cd into the directory with the images and then run this command:
command: `feh -F -d -z -Y --slideshow-delay 10 --action1 "python3 /home/pi/Desktop/Digital-Picture-Frame/feh_image_deletion.py -d echo '$PWD/'%n %n"`
command for DPF: `feh -F -d -z -Y --slideshow-delay 10 --action1 "python3 /home/dpf/Desktop/Digital-Picture-Frame/DPF_Scripts/feh_image_deletion.py -d echo '$PWD/'%n %n"`
2. To check what python script is running on Raspberry pi, run this command:
command: ps aux | grep keyboard_command.py
3. All startup scripts are ran from /etc/profile. The code added to this file is:
    sleep 5 && export DISPLAY=:0.0 && cd /media/pi/'Samsung USB'/'Slideshow Images' && `feh -F -Y -d -z --slideshow-delay 10 --action1 "python3 /home/pi/Desktop/Digital-Picture-Frame/feh_image_deletion.py -d echo '$PWD/'%n %n"` &
    python3 /home/pi/Desktop/Digital-Picture-Frame/keyboard_command.py &
4. Shutdown command: sudo rtcwake -m mem -l -t $(date +%s -d 'tomorrow 09:00')

# To Do
- Backup the whole raspberry pi
- Write better documentation
- Use a config file for scripts so it can avoid using hardcoded filepaths/directories.
