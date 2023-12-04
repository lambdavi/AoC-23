MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
with open("Day2/input.txt", "r") as f:
    rows = f.read().split("\n")

sum=0
for r in rows:
    possible = True
    game, text = r.split(": ")
    episodes = text.split("; ")
    for e in episodes:
        if possible:
            single = e.split(",")
            for s in single:
                elem = s.split(" ")
                if len(elem)==3:
                    elem = elem[1:]
                if elem[1]=="blue" and int(elem[0])>MAX_BLUE:
                    possible=False
                if elem[1]=="red" and int(elem[0])>MAX_RED:
                    possible=False
                if elem[1]=="green" and int(elem[0])>MAX_GREEN:
                    possible=False
        else:
            break
    
    if possible:
        print(game)
        sum+=int(game.split(" ")[1])

print(sum)

