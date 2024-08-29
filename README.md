Knock Script
This script automates the process of knocking on a door in a virtual environment by holding down the e key, moving the mouse to the left side of the screen, and clicking repeatedly. The script can be toggled on and off using hotkeys and can be stopped at any time.

Features
Automated Knocking: Simulates knocking by holding the e key, moving the mouse, and clicking.
Hotkey Controls:
Press F2 to start or pause the knocking action.
Press End to stop the knocking action completely.
Press Esc to exit the program.
Customizable Knocking Delay: Set the delay between knocks by adjusting the knocking_delay variable.
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/knock-script.git
cd knock-script
Install Dependencies Ensure you have Python installed. Then, install the required packages:

bash
Copy code
pip install keyboard pyautogui
Usage
Run the Script

bash
Copy code
python knock_script.py
Controls

Press F2 to start or pause knocking.
Press End to stop the knocking completely.
Press Esc to terminate the script.
Adjust Knocking Delay

Open the script file (knock_script.py).
Modify the knocking_delay variable (in seconds) to change the delay between knocks.