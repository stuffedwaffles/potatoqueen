before_server = 463000


what_to_do = input("Add to total potatoes(server stats or stacks collected) or calculate farmed using stats(calculate): ")
if "serve" in what_to_do:
    server = int(input("how many potatoes(see stats): "))
    total = before_server + server
    print (f"total: {str(total)} potatoes")
    with open(r'stuf\actual projects\potatoqueen\potatoes.txt', 'w') as file:
        file.write(str(int(total)))   

elif "stack" in what_to_do:
    stacks = int(input("How many stacks of potatoes collected: "))
    stacks = stacks*64
    extra = int(input("how many extra(not a total stack): "))
    with open(r'stuf\actual projects\potatoqueen\potatoes.txt', 'r') as f:
        current = int(f.read())
    total = current + stacks + extra
    print (f"total: {str(total)} potatoes")
    with open(r'stuf\actual projects\potatoqueen\potatoes.txt', 'w') as file:
        file.write(str(int(total)))   

elif "calculate" in what_to_do:
    todays_stats = int(input("how many potatoes(see stats): "))
    with open(r'stuf\actual projects\potatoqueen\potatoes.txt', 'r') as f:
        current = int(f.read())
    yesterdays_stats = current - 463000
    todays_farmed = todays_stats - yesterdays_stats
    print(f"farmed {todays_farmed} potatoes today")
    add = input("add todays farmed to current total? ")
    if add == "yes":
        with open(r'stuf\actual projects\potatoqueen\potatoes.txt', 'r') as f:
            current = int(f.read())
        total = current + todays_farmed
        print (f"total: {str(total)} potatoes")
        with open(r'stuf\actual projects\potatoqueen\potatoes.txt', 'w') as file:
            file.write(str(int(total)))   



