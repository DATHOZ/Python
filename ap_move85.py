def main():
    # Get input from user
    #primary_controller_name = input("Please provide the primary controller name: ")
    #primary_controller_ip = input("Please provide the primary controller IP: ")
    #secondary_controller_name = input("Please provide the secondary controller name: ")
    #secondary_controller_ip = input("Please provide the secondary controller IP: ")

    # Hard coded IP info
    primary_controller_name =  "wlc1"
    primary_controller_ip = "10.x.x.x" 
    secondary_controller_name = "wlc2"
    secondary_controller_ip = "10.x.x.x"

    with open("data.txt", 'r') as file:
        data = file.read()
        data = data.splitlines()
        
    commands = []
    client_command = ""

    for line in data:
        # Cuts line on spaces
        parts = line.split(' ')
        parts_clean = []
        # Cleans out the spaces
        for part in parts:
            if part != "":
                parts_clean.append(part)
        print(parts_clean)
        ap_name = parts_clean[2]
        ap_site=ap_name[0:7]
        client_command = f"grep include \"{ap_site}\" \"show client summary\""
        # Generate our commands
        clean1_command = f"config ap primary-base clean1 {ap_name} 0.0.0.0"
        clean2_command = f"config ap secondary-base clean2 {ap_name} 0.0.0.0"
        clean3_command = f"config ap secondary-base clean3 {ap_name} 0.0.0.0"
        primary_command = f"config ap primary-base {primary_controller_name} {ap_name} {primary_controller_ip}"
        secondary_command = f"config ap secondary-base {secondary_controller_name} {ap_name} {secondary_controller_ip}"
        reset_command = f"config ap reset {ap_name} "
        confirm_command = f"y"
        
        #primary_command = f"ap name {ap_name} controller primary {primary_controller_name} {primary_controller_ip}"                                  
        #secondary_command = f"ap name {ap_name} controller secondary {secondary_controller_name} {secondary_controller_ip}"
        commands.append(clean1_command)
        commands.append(clean2_command)
        commands.append(clean3_command)
        commands.append(primary_command)
        commands.append(secondary_command)
        commands.append(reset_command)
        commands.append(confirm_command)

    print('\n')
    print(client_command)
    print('\n')
    for command in commands:
        print(command)
    print('\n')
    with open("output.txt", "w+") as file:
        for command in commands:
            file.write(command + '\n')

if __name__ == "__main__":
    main()