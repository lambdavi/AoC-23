"""
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.


"""

spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
with open("input.txt") as f:
    inputs = f.readlines()

result=0
for s in inputs:
    min_ind = len(s)
    max_ind = -1
    max_num = 1
    min_num = 9
    for l, spell in enumerate(spelled):
        try:
            ind = s.index(spell)
            if ind<min_ind:
                min_ind=ind   
                min_num = l+1         
        except:
            pass
        try:
            ind = s[::-1].index(spell[::-1])
            if len(s)-1-ind>max_ind:
                max_ind=len(s)-1-ind
                max_num=l+1
        except:
            pass
    i = 0
    f=s[0]
    while not f.isnumeric() and i<min_ind:
        i+=1
        f = s[i]
    j=len(s)-1
    l=s[j]
    while not l.isnumeric() and j>max_ind:
        j-=1
        l = s[j]
    if j>max_ind:
        l=s[j]
    else:
        l=str(max_num)
    if i<min_ind:
        f=s[i]
    else:
        f=str(min_num)
    result += int(f+l)

print(result)    