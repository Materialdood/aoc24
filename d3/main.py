#full shit send in day 3
import re

#read input
reports = []

with open("input.txt", "r") as f:
    txt = f.read().lower()

# print(type(txt))
def match_mul(txt):
    m=          r"mul\([0-9]+,[0-9]+\)"
    matches = re.findall(m, txt)
    pairs = [x.replace("mul(", "").replace(")", "").split(",") for x in matches]
    # print(pairs)
    return pairs

pairs = match_mul(txt)
ans = 0
for val in pairs:
    ans+= int(val[0])*int(val[1])

print(ans)
#end of part one
enabled =True
ans_str=""
for i, char in enumerate(txt):
    if enabled and not txt[i:i+7] == "don't()":
        ans_str += char
    elif txt[i:i+4] == "do()":
        enabled = True
    elif txt[i:i+7] =="don't()":
        enabled = False


pairs = match_mul(ans_str)
ans = 0
for val in pairs:
    ans+= int(val[0])*int(val[1])
print(ans)


#