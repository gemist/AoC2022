#initialize variables
mat=[]

#read file
f=open('input.txt','r')
lines = f.readlines()
for line in lines:
    lst= [int(i) for i in line.replace("\n","")]
    mat.append(lst)
f.close()

visible = 0
maxscore = 0
nrow = len(mat)
ncol = len(mat[0])


def factor(lst,value):
    ff =  [m for m, n in enumerate(lst) if n >= value ]
    if len(ff) == 0:
        f = len(lst)
    else:
        f = min(ff)+1
    return f
    

for i in range(1,nrow-1):
    for j in range(1,ncol-1):
        
        if j == 1:
            left = [mat[i][0]]
        else:
            left = mat[i][:j]

        
        if j == ncol-2:
            right = [mat[i][ncol-1]]
        else:
            right = mat[i][j+1:]
        
        if i == 1:
            up = [mat[0][j]]
        else:
            up = []
            for k in range(0,i):
                up.append(mat[k][j])
        if i == nrow-2:
            down = [mat[nrow-1][j]]
        else:
            down = []
            for k in range(i+1,nrow):
                down.append(mat[k][j])
                
        if max(left) < mat[i][j] or max(right) < mat[i][j] or max(up) < mat[i][j] or max(down) < mat[i][j]:
            #part 1
            visible += 1

            #part2
            left.reverse()
            up.reverse()
            l=factor(left,mat[i][j])
            r=factor(right,mat[i][j])
            u=factor(up,mat[i][j])
            d=factor(down,mat[i][j])
            
            score=l*r*u*d
            if score > maxscore:
                maxscore=score
                        
#add edges 
visible += 2*ncol+2*nrow -4

print("part1:",visible)
print("part2:",maxscore)
