#Idk if you were looking for a graphical solution but i am already sick of graphs
#So you get bitwise operations

num_villagers = int(input())
num_evenings = int(input())

songs_known = [0] * num_villagers
songCount = 0
for _ in range(num_evenings):
    evening_data = list(map(int, input().split()))
    present_villagers = evening_data[1:]
    if 1 in present_villagers:
        for villager in present_villagers:
            songs_known[villager - 1] |= 1 << songCount
        songCount+=1
    else:
        shared_songs = songs_known[present_villagers[0] - 1]
        for villager in present_villagers[1:]:
            shared_songs |= songs_known[villager - 1]
        for villager in present_villagers:
            songs_known[villager - 1] |= shared_songs

for i in range(num_villagers):
    if songs_known[i] == songs_known[0]:
        print(i+1)
