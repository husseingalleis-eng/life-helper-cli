import os 
from pathlib import Path

folder = 'tools'
path = Path(folder)

try:
    path.mkdir()
    print(f"Directory  '{path}' created successfully")
except FileExistsError:
    print(f"Directory  '{path}' is already exist")
except PermissionError:
    print(f"Permission denied: Unable to create '{path}'")
except Exception as e:
    print(f"An error occurred: {e}")



selecting = True
while selecting:
    while True:
        print("\nWelcome to Life Helper Multi-Tool CLI\n")
        print("-----------------------THE MENU--------------------------")
        print("1 - Random Decision Maker            2 - Password Generator")
        print("3 - Unit Converter                   4 - System Info Tool")
        print("5 - URL Cleaner & Validator          6 - Reminder / Timer")
        print("7 - Website Status Checker           8 - File Downloader")
        print("9 - JSON Data Manager                10 - Weather Checker (API)\n0 - Exit\n")
        break
    while True:  
        try:
            selection = int(input("Please select one option: "))
            break
        except ValueError:
            print("You must enter a number? ")
        
    while True:
        match selection:
            case 0:
                selection = 'Exit'
                print("See u next time")
                selecting = False
                break
            case 1:
                selection = 'Random Decision Maker'
                from tools import random_decision_make
                random_decision_make.random_decision_maker()
                break
            case 2:
                selection = 'Password Generator'
                from tools import password_generator
                password_generator.password_generator()
                break
            case 3:
                selection = 'Unit Converter'
                from tools import unit_converter
                unit_converter.unit_converter()
                break
            case 4:
                selection = 'System Info Tool'
                from tools import system_info_tool
                system_info_tool.system_info_tool()
                break
            case 5:
                selection = 'URL Cleaner & Validator'
                from tools import url_cleaner_validator
                url_cleaner_validator.url_cleaner_validator()
                break
            case 6:
                selection = 'Reminder / Timer'
                from tools import reminder_timer
                reminder_timer.reminder_time()
                break
            case 7:
                selection = 'Website Status Checker'
                from tools import website_status_checker
                website_status_checker.website_status_checker()
                break
            case 8:
                selection = 'File Downloader'
                from tools import file_downloader
                file_downloader.file_downloader()
                break
            case 9:
                selection = 'JSON Data Manager'
                from tools import json_data_manager
                json_data_manager.json_data_manager()
                break
            case 10:
                selection = 'Weather Checker (API)'
                from tools import weather_checker
                weather_checker.weather_checker()
                break
            case _:
                print("You must enter a number between 0 and 10")
                break
    os.system('pause')
        
    
