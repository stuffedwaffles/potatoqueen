before_server = 463000


server_or_stacks = input("server stats or stacks collected: ")
if "server" in server_or_stacks:

    server = int(input("how many potatoes(see stats): "))
    total = before_server + server
elif "stacks" in server_or_stacks:
    stacks = int(input("How many stacks of potatoes collected: "))
    stacks = stacks*64
    extra = int(input("how many extra(not a total stack): "))
    with open(r'stuf\actual projects\potatoqueen\potatoes.txt', 'r') as f:
        current = int(f.read())
    total = current + stacks + extra
    

print (f"{str(total)} potatoes")
with open(r'stuf\actual projects\potatoqueen\potatoes.txt', 'w') as file:
        file.write(str(int(total)))   
