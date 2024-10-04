first = input().split()
size = int(first[0])
walls = int(first[1])
partitions = []
string = ""
spacings = []
for _ in range(size + 1):
    spacings.append(0)
values = input().split()
spacings[size] = 1
for _ in range(walls):
    partitions.append(int(values[_]))
    
for parition in partitions:
    spacings[size - parition] = 1
    spacings[parition] = 1
    for inner in partitions:
        if(parition > inner):
            spacings[parition - inner] = 1
        else: break
spacings[0] = 0

for spacing in range(size + 1):
    if spacings[spacing]:
        string += str(spacing) + " "
        
print(string)