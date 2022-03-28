#! python3
# countdown.py - countdown
import time, subprocess

timeLeft = 20
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['see', 'break_is_over.txt'])



















