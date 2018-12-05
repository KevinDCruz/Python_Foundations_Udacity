import webbrowser
import time

breaks = 3
breaks_count = 0

print("Program started at: "+time.ctime())
while (breaks_count < breaks):
    time.sleep(10)
    webbrowser.open("www.youtube.com")
    breaks_count = breaks_count + 1