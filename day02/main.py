elf_plays = ["A","B","C"]
player_plays = ["X","Y","Z"]

sum_score0 = 0
sum_score1 = 0

f=open('input.txt','r')
lines = f.readlines()

for line in lines:
    l = line.split()
    elf_move = elf_plays.index(l[0])
    player_move =   player_plays.index(l[1])
    #part 1
    if player_move == elf_move:
        outcome_score = 3
    elif player_move == (elf_move + 1)%3:
        outcome_score = 6
    elif player_move == (elf_move - 1)%3:
        outcome_score = 0

    sum_score0 += outcome_score + player_move + 1

    #part 2
    if player_move == 0:
        outcome_score = 0
        player_move = (elf_move - 1)%3
    elif player_move == 1:
        outcome_score = 3
        player_move = elf_move
    elif player_move == 2:
        outcome_score = 6
        player_move = (elf_move + 1)%3
        
    sum_score1 += outcome_score + player_move +1


print("part1:", sum_score0)
print("part2:", sum_score1)
    
f.close()
