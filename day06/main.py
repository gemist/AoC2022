signal = []
packet_start = 0
message_start = 0
counter = 0
f=open('input.txt','r')
while True:
    counter += 1
    # read by character
    char = f.read(1)
    #break when no more characters - end of file
    if not char:
        break
    signal.append(char)
    #part 1
    if len(set(signal[len(signal)-4:])) == 4 and packet_start == 0:
        packet_start = counter
    #part 2
    if len(set(signal[len(signal)-14:])) == 14 and message_start == 0:
        message_start= counter

print("part1:",packet_start)
print("part1:",message_start)
    
f.close()
