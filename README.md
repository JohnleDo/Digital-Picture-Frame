# Digital-Picture-Frame
1. Make sure to cd into the directory with the images and then run this command:
command: `feh -F -d -z --slideshow-delay 10 --action1 "python3 /home/pi/Desktop/'Digital Picture Frame'/feh_image_deletion.py -d echo '$PWD/'%n %n"`
command for DPF: `feh -F -d -z --slideshow-delay 10 --action1 "python3 /home/dpf/Desktop/Digital-Picture-Frame/DPF_Scripts/feh_image_deletion.py -d echo '$PWD/'%n %n"`
command for sleep: sudo rtcwake -m mem -l -t $(date +%s -d 'tomorrow 09:00')
