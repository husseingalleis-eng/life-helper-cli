import time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  # Overwrite the line each second
        time.sleep(1)
        t -= 1
        
        

def reminder_time():
    print("\nWelcome to Reminder / Timer\n")
    reminder = input("What do you want to remember:")
    time_type = input("Do you want the reminder in minutes or seconds: ")
    time_type = time_type.lower().strip()
    while True:
        if time_type in ('minutes', 'm'):
            while True:
                try:
                    t = float(input("Enter the time in minutes: "))
                    break
                except ValueError:
                    print("You must enter a number")
   
            if t > 0:
                t *= 60
                countdown(int(t))
                print(f"Reminder: it is time to {reminder}")
                break
            else:
                print("Wrong input, or time is negative")
        elif time_type in ('seconds', 's'):
            while True:
                try:
                    t = float(input("Enter the time in seconds: "))
                    break
                except ValueError:
                    print("You must enter a number")
            if t > 0:
                countdown(int(t))
                print(f"\nReminder: it is time to {reminder}")
                break
            else:
                print("Wrong input, or time is negative")
        else:
            print("We don't have this kind of reminders yet")
            break