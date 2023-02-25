# keyloggerscreenshotter

Keylogger with Screenshotter
This is a simple keylogger that logs all keyboard input and takes screenshots of the user's screen at regular intervals. The keylogger and screenshotter are run as separate threads in the same program.

Getting Started


Prerequisites

This program requires Python 3.x and the following libraries:

pynput
pillow
smtplib


To install the required libraries, run the following command in the terminal:


Copy code

pip install pynput pillow smtplib


Running the Program

To run the program, navigate to the directory where the program is saved and run the following command in the terminal:

Copy code

python pack.py


Customization


The program can be customized to your needs by modifying the following variables:

INTERVAL_KEYLOGGER: The interval in seconds between each report sent by the keylogger.
INTERVAL_SCREENSHOTTER: The interval in seconds between each screenshot taken by the screenshotter.
EMAIL_ADDRESS: The email address used to send the reports.
EMAIL_PASSWORD: The password for the email address used to send the reports.


License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This program was inspired by the following resources:

Python Keylogger by Nikhil Gupta
Python Screenshot Tutorial by Edureka


Regenerate response
