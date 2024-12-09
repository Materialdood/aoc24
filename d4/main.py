#full shit send in day 4

#read input

lines =[]
with open("input.txt", "r") as f:
    for line in f:
        txt = line.strip()
        lines.append("OOOO"+txt+"OOOO")
        
padding = "O"*len(lines[0])
lines = [padding]*4 + lines + [padding]*4
# print(lines[4], lines[len(lines)-5])

c=0
for i in range(1,len(lines)-1):
    for j in range(1, len(lines[i])-1):
        if lines[i][j] == "X":
            if lines[i][j:j+4] == "XMAS":
                c += 1
            if lines[i][j-3:j+1] == "SAMX":
                c+=1
            if "".join([x[j] for x in lines[i:i+4]])== "XMAS":
                c+=1
            if "".join([x[j] for x in lines[i-3:i+1]])== "SAMX":
                c+=1

            if lines[i][j]+lines[i+1][j+1]+lines[i+2][j+2]+lines[i+3][j+3]== "XMAS":
                c+=1

            if lines[i][j]+lines[i-1][j+1]+lines[i-2][j+2]+lines[i-3][j+3]== "XMAS":
                c+=1

            if lines[i][j]+lines[i+1][j-1]+lines[i+2][j-2]+lines[i+3][j-3]== "XMAS":
                c+=1

            if lines[i][j]+lines[i-1][j-1]+lines[i-2][j-2]+lines[i-3][j-3]== "XMAS":
                c+=1
            
            
print(c)
#end part 1
# print("".join(sorted("MSAMS")))

ans=0
for i in range(2,len(lines)-2):
    for j in range(2, len(lines[i])-2):
        if lines[i][j] == "A":
            temp = "A"
            if lines[i-1][j-1] in ["M", "S"]:
                temp+=lines[i-1][j-1]
            if lines[i-1][j+1] in ["M", "S"]:
                temp+=lines[i-1][j+1]
            if lines[i+1][j-1] in ["M", "S"]:
                temp+=lines[i+1][j-1]
            if lines[i+1][j+1] in ["M", "S"]:
                temp+=lines[i+1][j+1]
            # print("".join(sorted(temp)), "".join(sorted(temp)) =="AMMSS")
            if "".join(sorted(temp)) =="AMMSS" and not lines[i-1][j-1]==lines[i+1][j+1]:
                ans+=1

print(ans)
