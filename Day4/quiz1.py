with open("Day4/input.txt") as f:
    full_text = f.read().split("\n")

# Preprocess:
total_points=0
for line in full_text:
    no_space_line = " ".join(line.split())
    winning, numbers = no_space_line.split(": ")[1].split(" | ")
    w_list = winning.split(" ")
    n_list = numbers.split(" ")
    points = 0
    for w in w_list:
        points+=(w in n_list)
    if points>0:
        total_points += 2**(points-1)
    print(total_points) 