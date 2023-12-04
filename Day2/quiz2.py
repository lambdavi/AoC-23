
with open("Day2/input.txt", "r") as f:
    rows = f.read().split("\n")

ps=0
for r in rows:
    possible = True
    game, text = r.split(": ")
    episodes = text.split("; ")
    minR = 0
    minB = 0
    minG = 0
    for e in episodes:
        
        single = e.split(",")
        print("Single: ", single)
        for s in single:
            elem = s.split(" ")
            if len(elem)==3:
                elem = elem[1:]
            v = int(elem[0])
            if elem[1]=="blue":
                if v>minB:
                    minB=v
            elif elem[1]=="red":
                if v>minR:
                    minR=v
            elif elem[1]=="green":
                if v>minG:
                    minG=v
            print(elem, minR, minG, minB)

    
    ps += minG*minB*minR
    print(ps)
    

