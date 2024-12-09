#full shit send in day 1

import math

#read input into two lists
list_one = []
list_two = []
with open("input.txt", "r") as f:
    for line in f:
        el = line.strip().split("   ")
        list_one.append(int(el[0]))
        list_two.append(int(el[1]))

# print(sorted(list_one), sorted(list_two))

sorted_one = sorted(list_one)
sorted_two = sorted(list_two)

ans =0
for i in range(len(sorted_one)):
    ans += math.fabs(int(sorted_one[i]-sorted_two[i]))
    #print(int(ans))

#end part 1
counter = 0
score = 0
for val in sorted_one:
    for i in range(len(sorted_two)):
        if val == sorted_two[i]:
            counter += 1
    score += val*counter
    counter = 0
    print(score)