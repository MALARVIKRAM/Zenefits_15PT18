inp_str=raw_input()

print inp_str

for i in range(len(inp_str)):
    if inp_str[i]=='}':
        if int(inp_str[i-3])!=0:
            print int(inp_str[i-2])
        
