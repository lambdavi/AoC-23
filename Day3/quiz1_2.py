import numpy as np
matrix = []
with open("Day3/input.txt") as f:
    text = f.read().split("\n")
    for t in text:
        matrix.append([*t])
nm = np.array(matrix)
found=[]
curr_num=""
adjacent=False
gears = {}

for i in range(nm.shape[0]):
    curr_num=""
    adjacent=False
    possible_gear = None
    criteria=0
    for j in range(nm.shape[1]+1):
        if j==nm.shape[1]:
            if curr_num!="" and adjacent:
                if possible_gear:
                    if gears.get(possible_gear):
                        if len(gears.get(possible_gear))==1:
                            found.remove(str(gears.get(possible_gear)[0]))
                        gears[possible_gear].append(int(curr_num))
                    else:
                        gears[possible_gear]=[int(curr_num)]
                        found.append(curr_num)              
                else:
                    found.append(curr_num)              
            break
        if not nm[i][j].isnumeric():
            if curr_num!="" and adjacent:
                if possible_gear:
                    if gears.get(possible_gear):
                        if len(gears.get(possible_gear))==1:
                            found.remove(str(gears.get(possible_gear)[0]))
                        gears[possible_gear].append(int(curr_num))
                    else:
                        gears[possible_gear]=[int(curr_num)]
                        found.append(curr_num)              
                else:
                    found.append(curr_num)              
            curr_num=""
            adjacent=False
            possible_gear=()
        else:
            curr_num+=nm[i][j]
            if adjacent==False:
                if i-1>=0 and (not nm[i-1][j].isnumeric() and nm[i-1][j]!="."):
                    if nm[i-1][j]=="*":
                        possible_gear=(i-1,j)
                    adjacent = True
                    continue
                if i+1<nm.shape[0] and (not nm[i+1][j].isnumeric() and nm[i+1][j]!="."):
                    if nm[i+1][j]=="*":
                        possible_gear=(i+1,j)
                    adjacent = True
                    continue
                if j-1>=0 and (not nm[i][j-1].isnumeric() and nm[i][j-1]!="."):
                    if nm[i][j-1]=="*":
                        possible_gear=(i, j-1)
                    adjacent = True
                    continue
                if j+1<nm.shape[1] and (not nm[i][j+1].isnumeric() and nm[i][j+1]!="."):
                    if nm[i][j+1]=="*":
                        possible_gear=(i, j+1)
                    adjacent = True
                    continue
                if i-1>=0 and j-1>=0 and (not nm[i-1][j-1].isnumeric() and nm[i-1][j-1]!="."):
                    if nm[i-1][j-1]=="*":
                        possible_gear=(i-1, j-1)
                    adjacent = True
                    continue
                if i-1>=0 and j+1<nm.shape[1] and (not nm[i-1][j+1].isnumeric() and nm[i-1][j+1]!="."):
                    if nm[i-1][j+1]=="*":
                        possible_gear=(i-1, j+1)
                    adjacent = True
                    continue
                if i+1<nm.shape[0] and j+1<nm.shape[1] and (not nm[i+1][j+1].isnumeric() and nm[i+1][j+1]!="."):
                    if nm[i+1][j+1]=="*":
                        possible_gear=(i+1, j+1)
                    adjacent = True
                    continue
                if i+1<nm.shape[0] and j-1>=0 and (not nm[i+1][j-1].isnumeric() and nm[i+1][j-1]!="."):
                    if nm[i+1][j-1]=="*":
                        possible_gear=(i+1, j-1)
                    adjacent = True
                    continue

partial_sum = sum([int(f) for f in found])
print(found, partial_sum, sep=": ")

s=0
for v in gears.values():
    if len(v)>=2:
        s+=np.prod(v)
print(gears, s)

        
            

            