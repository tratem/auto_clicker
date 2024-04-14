#auto clicker 
#For recording the clicing sequence in the first prompt input "N"
#
#For running a prerecored sequence in the first prompt input "R"
#Use Ctrl + C to end the recording
#Use Shift + F5 to stop the script

import pyautogui
import time
import mouse
import keyboard
import csv

x_array = []
y_array = []
timing_array = []

#Chose number of repetitions
repetitions = 1 

#Deleys in seconds
#Initial delay
init_delay = 5

#Click delay
click_delay = 0.2

#Record new imputs sequence
def new_recording():
    print(f"New position is going to be recorded in {init_delay}s. Move the mouse to desired position. To terminate and save the recording press Ctrl + C")
    time.sleep(init_delay)
    print("Started")
    start_time = time.time()
    while not(keyboard.is_pressed("Ctrl + C")):
        if(mouse.is_pressed()):
            end_time = time.time()
            x, y = pyautogui.position()
            x_array.append(x)
            y_array.append(y)
            timing_array.append(end_time - start_time)
            start_time = time.time()
            time.sleep(click_delay)

    #Generation on csv to store the imputs
    with open("positions.csv", "w", newline="") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(["X", "Y", "Time"])
                writer.writerows(zip(x_array, y_array, timing_array))


def run_recorded():
    with open("positions.csv", "r", newline="") as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)           
        for row in reader:
            x, y, time_delay = map(float, row)
            pyautogui.moveTo(x , y)
            pyautogui.click()
            time.sleep(time_delay)

def main():
    user = (input("Do you want to generate [N]ew sequence or [R]un one already prerecorded sequence? ")).upper()
    while user != 'R' and user != 'N':
        user = (input("Insert [N]ew sequence or [R]un prerecorded? ")).upper()

    if (user == 'N'):
        new_recording()
    else:
        for i in range(repetitions):
            run_recorded()

if __name__ == "__main__":
    main()