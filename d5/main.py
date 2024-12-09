

rules=[]
updates=[]
with open("input.txt", "r") as f:
    for line in f:
        if "|" in line:
            rules.append(list(map(int,line.strip().split("|"))))
        else:
            updates.append(list(map(int,line.strip().split(","))))


# print(rules)
# print(updates)

def find_middle(l: list):
    i= len(l) // 2
    return l[i]

ans=0
ans_two=0
for update in updates:
    ok = True
    repaired = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0])> update.index(rule[1]):
                ok= False
                repaired = False
    while not repaired:
        repaired = True
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0])> update.index(rule[1]):
                    repaired = False
                    update[update.index(rule[0])], update[update.index(rule[1])] = update[update.index(rule[1])], update[update.index(rule[0])]

       
    if ok:            
        ans+=find_middle(update)
    else:
        # print(update)
        ans_two+=find_middle(update) 

print(ans)
print(ans_two)





