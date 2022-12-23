#read file
lst = []
f=open('input.txt', 'r')
lines = f.readlines()
for line in lines:
    lst.append(int(line.replace('\n','')))
f.close()


def mix(lst, num):
    length = len(lst)
    tmp = [i for i in range(length)] # index list
    for z in range(num):
        for i, val in enumerate(lst):
            if val == 0:
                continue
            j = tmp.index(i)
            k=(j+val) % (length - 1)
            v = tmp.pop(j)           
            tmp.insert(k, v)

    return [lst[i] for i in tmp]

final_lst=mix(lst,1)
ind1 = (final_lst.index(0)+1000) % len(final_lst)
ind2 = (final_lst.index(0)+2000) % len(final_lst)
ind3 = (final_lst.index(0)+3000) % len(final_lst)
print("part1:",final_lst[ind1]+final_lst[ind2]+final_lst[ind3])

decryption_key = 811589153
new_list = [decryption_key*z for z in lst]
final_lst=mix(new_list,10)
ind1 = (final_lst.index(0)+1000) % len(final_lst)
ind2 = (final_lst.index(0)+2000) % len(final_lst)
ind3 = (final_lst.index(0)+3000) %  len(final_lst)
print("part2:",(final_lst[ind1]+final_lst[ind2]+final_lst[ind3]))

