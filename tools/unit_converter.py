def unit_converter():
    print("\nWelcome to Unit Converter\n")
    unit = {
        
       'length' : ['km', 'm', 'cm'],
       'weight' : ['kg', 'g'],
       'temperature' : ['c', 'f']   
    }
    print("The Categories units you can use are: ")
    print("'length' : ['km', 'm', 'cm']\n'weight' : ['kg', 'g']\n'temperature' : ['c', 'f'] \n")
    while True:
        try:
            unit_type = input("Enter the category of the unit you want to use:")
            unit_type = unit_type.lower().strip()
            if not unit_type:
                raise ValueError("Empty input try again!")
            break
        except ValueError as e:
            print(e)
    if unit_type in unit:
        while True:
            try:
                convert_unit = input("Enter the unit you want to convert: ")
                convert_unit = convert_unit.lower().strip()
                if not convert_unit:
                    raise ValueError("Empty input try again!")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                amount = float(input("Enter the amount you want to convert: "))
                break
            except ValueError:
                print("You must enter a number")
        while True:
            try:
                converted_unit = input("Enter the unit you want to convert to it: ")
                converted_unit = converted_unit.lower().strip()
                if not converted_unit:
                    raise ValueError("Empty input try again!")
                break
            except ValueError as e:
                print(e)
        if unit_type == 'length':
            if convert_unit == 'km' and converted_unit == 'm':
                m = amount * 1000
                print(f"{amount} km is = {m} m")
            elif convert_unit == 'km' and converted_unit == 'cm':
                cm = amount * 100000
                print(f"{amount} km is = {cm} cm")
            elif convert_unit == 'm' and converted_unit == 'cm':
                cm = amount * 100
                print(f"{amount} m is = {cm} cm")
            
            elif convert_unit == 'm' and converted_unit == 'km':
                km = amount / 1000
                print(f"{amount} m is = {km} km")
            elif convert_unit == 'cm' and converted_unit == 'm':
                m = amount / 100
                print(f"{amount} cm is = {m} m ")
            elif convert_unit == 'cm' and converted_unit == 'km':
                km = amount / 100000
                print(f"{amount} cm is = {km} km")
            elif convert_unit == converted_unit:
                print(f"The units are same {amount} {convert_unit} is = {amount}  {converted_unit} ")
            else:
                print("\nYou must choose from the menu units only!\n ")
        elif unit_type == 'weight':
            if convert_unit == 'kg' and converted_unit == 'g':
                g = amount * 1000
                print(f"{amount} kg is = {g} g")
            elif convert_unit == 'g' and converted_unit == 'kg':
                kg = amount / 1000
                print(f"{amount} g is = {kg} kg")
            elif convert_unit == converted_unit:
                print(f"The units are same {amount} {convert_unit} is = {amount} {converted_unit} ")
            else:
                print("\nYou must choose from the menu units only!\n ")
        elif unit_type == 'temperature':
            if convert_unit == 'c' and converted_unit == 'f':
                f = (amount * 1.8) + 32 
                print(f"{amount} c is = {f} f")
            elif convert_unit == 'f' and converted_unit == 'c':
                c = (amount - 32) / 1.8
                print(f"{amount} f is = {c} c")
            elif convert_unit == converted_unit:
                print(f"The units are same {amount} {convert_unit} is = {amount}  {converted_unit} ")
            else:
                print("\nYou must choose from the menu units only!\n ")
        else:
            print("This is wrong units !")
    else:
        print("The unit is not avaliable!")

