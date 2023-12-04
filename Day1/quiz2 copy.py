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

spelled = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
with open("input_test.txt") as f:
    inputs = f.readlines()

result=0

for s in inputs:
    min_ind = len(s)
    max_ind = -1
    max_num = 1
    min_num = 9
    for i, spell in spelled:
        try:
            ind = s.index(spell)
            if ind>max_ind:
                max_ind=ind
                max_num=spelled[]
            if ind<min_ind:
                min_ind=ind            
        except:
            pass
    i = 0
    f=s[0]
    while not f.isnumeric() and i<min_ind:
        i+=1
        f = s[i]
    i=-1
    
    l=s[-1]
    while not l.isnumeric() and i>max_ind:
        i-=1
        l = s[i]
    result = result + int(f+l)

print(result)    