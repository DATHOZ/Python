def main():
    #populate data.txt with "sh ap summary | inc <ap_name>"
    with open("data.txt", 'r') as file:
        data = file.read()
        data = data.splitlines()
        
    commands = []

    for line in data:
        # Cuts line on spaces
        parts = line.split(' ')
        parts_clean = []
        # Cleans out the spaces
        for part in parts:
            if part != "":
                parts_clean.append(part)
        print(parts_clean)
        ap_name = parts_clean[0]
        # Generate our commands
        primary_command = f"ap name {ap_name} reset"
        #old_command = f"config ap reset {ap_name} "
        confirm_command = f"y"
        commands.append(primary_command)
        #commands.append(old_command)
        commands.append(confirm_command)
    for command in commands:
        print(command)

    with open("output.txt", "w+") as file:
        for command in commands:
            file.write(command + '\n')

if __name__ == "__main__":
    main()