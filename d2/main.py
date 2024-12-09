#full shit send in day 2


# One report per line 
# list of numbers called levels
# sep by space
# levels either ALL increasing or decreasing
# diff per level MAX 3 MIN 1

#read input
reports = []

with open("input.txt", "r") as f:
    for line in f:
        el = line.strip().split(" ")
        reports.append([int(x) for x in el])

# print(reports)
# print(set([len(x) for x in reports]))


save_c = 0
for report in reports:
    if len(set(report)) == len(report):
        if report == sorted(report) or report == sorted(report, reverse=True):
            temp = []
            rev = sorted(report, reverse=True)
            for i in range(len(rev)-1):
                temp.append(rev[i]-rev[i+1])
            if len([x for x in temp if x > 3 or x<1]) == 0:
                save_c +=1
                # print(save_c, report)

#end part one
            
save_c = 0
for report in reports:
    found = False
    if report == sorted(report) or report == sorted(report, reverse=True):
        temp = []
        rev = sorted(report, reverse=True)
        for i in range(len(rev)-1):
            temp.append(rev[i]-rev[i+1])
        if len([x for x in temp if x > 3 or x<1]) == 0:
            save_c +=1
            found = True
            print(save_c, report)
    
    if not found:
        for i in range(len(report)):
            if not found:
                temp_report = report[:]
                temp_report.pop(i)
                print(report, temp_report)
                if (temp_report == sorted(temp_report) or temp_report == sorted(temp_report, reverse=True)) and not found:
                    temp = []
                    rev = sorted(temp_report, reverse=True)
                    for i in range(len(rev)-1):
                        temp.append(rev[i]-rev[i+1])
                    if len([x for x in temp if x > 3 or x<1]) == 0 and not found:
                        save_c +=1
                        print(save_c, report)
                        found = True
            

