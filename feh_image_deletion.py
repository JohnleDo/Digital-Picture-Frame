import argparse, os, json
from datetime import datetime
from pynput.keyboard import Key, Controller


"""
    We take a list of strings as an argument because when we will be using Feh we bind this script to a key. To do that
    we run it as this command:
        "feh -F --action1 "python3 /path_to_python_script/feh_image_deletion.py -d echo $PWD/%n %n"
    When looking at this command we include a bash command and the reason for that is because we need to get the name
    of the image being deleted so we can record it and store it into a json file.
    
    - args.d[0] = echo command
    - args.d[1] = image file path
    - args.d[2] = image file name
"""

def WriteToLog(logFilePath, message):
    if (os.path.exists(logFilePath)):
        with open(logFilePath, "a") as file:
            file.write(datetime.today().strftime("%d-%b-%Y (%H:%M:%S)") + ": " + message + "\n")
            file.close()
    
    else:
        with open(logFilePath, "w") as file:
            file.write(datetime.today().strftime("%d-%b-%Y (%H:%M:%S)") + ": " + message + "\n")
            file.close()

if __name__ == '__main__':
    try:
        logFilePath = os.getcwd() + "/Logs/Image_Deletion_Log.txt"
        WriteToLog(logFilePath, "Began Program")

        keyboard = Controller()

        parser = argparse.ArgumentParser(description='used to capture Feh image filenames before deletion.')
        parser.add_argument('-d', nargs='+', help='Name of file to be deleted. Takes a list to deal with bash command.')
        args = parser.parse_args()
        feh_dir = args.d[1].replace(args.d[2], "")
        print("Feh Image Filename to be deleted: " + args.d[2])

        if os.path.exists(feh_dir + "removed_images.json"):
            with open(feh_dir + "removed_images.json", "a") as file:
                json.dump({"filename": args.d[2],
                        "date of deletion": datetime.today().strftime('%Y-%m-%d')}, file)
                file.write(os.linesep)
                file.close()
        else:
            with open(feh_dir + "removed_images.json", "w") as file:
                json.dump({"filename": args.d[2],
                        "date of deletion": datetime.today().strftime('%Y-%m-%d')}, file)
                file.write(os.linesep)
                file.close()

        os.remove(args.d[1])

    except Exception as e:
        WriteToLog(logFilePath,"[ERROR]: " + e.args[0])


