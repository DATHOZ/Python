def get_controller(wlcVal):
    if wlcVal == "1":
        return "wlc1 10.x.x.1" 
    elif wlcVal == "2":
        return "wlc2 10.x.x.2"
    elif wlcVal == "3":
        return "wlc3 10.x.x.3"
    elif wlcVal == "4":
        return "wlc4 10.x.x.4"
    elif wlcVal == "5":
        return "wlc5 10.x.x.5"
    elif wlcVal == "6":
        return "wlc6 10.x.x.6"

def main():
    # Get input from user
    #primary_controller_name = input("Type the # of the WLC primary : ")
    #primary_controller_ip = input("Please provide the primary controller IP: ")
    #secondary_controller_name = input("Type the # of the WLC: ")
    #secondary_controller_ip = input("Please provide the secondary controller IP: ")

    # Hard coded
    print("""
    WLC Migration options:
    1: wlc1
    2: wlc2
    3: wlc3
    4: wlc4
    5: wlc5
    6: wlc6
    """)
    numpri = input("Type primary WLC # : ")
    numsec = input("Type secondary WLC # : ")
    primary_controller = get_controller(numpri)
    secondary_controller = get_controller(numsec)

    #populate data.txt with "sh ap summary | inc <ap_name>"
    with open("data.txt", 'r') as file:
        data = file.read()
        data = data.splitlines()
        
    commands = []

    for line in data:
        # Cuts line on spaces
        parts = line.split(' ')
        parts_clean = []
        # Cleans out the spaces and use [0] as first word
        for part in parts:
            if part != "":
                parts_clean.append(part)
        print(parts_clean)
        ap_name = parts_clean[0]
        # Generate our commands
        cleansec_command = f"ap name {ap_name} controller secondary tempName2 0.0.0.0"
        cleanpri_command = f"ap name {ap_name} controller primary tempName1 0.0.0.0"   
        primary_command = f"ap name {ap_name} controller primary {primary_controller}"                                  
        secondary_command = f"ap name {ap_name} controller secondary {secondary_controller}"
        #reset_command = f"config ap reset {ap_name} "
        #confirm_command = f"y"
        
        commands.append(cleansec_command)
        commands.append(cleanpri_command)
        commands.append(primary_command)
        commands.append(secondary_command)
        #commands.append(reset_command)
        #commands.append(confirm_command + '\n')

    for command in commands:
            print(command)
            #print('\n')
    with open("output.txt", "w+") as file:
        for command in commands:
            file.write(command + '\n')

if __name__ == "__main__":
    main()