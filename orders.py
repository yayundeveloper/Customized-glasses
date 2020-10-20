
import csv

csv_keyword = csv.reader(open('./Order/Orders.csv', encoding='gbk'))

keywords = []

for row in csv_keyword:
    keywords.append(row)

#print(keywords)

for i in range(len(keywords)):
    if 'member1' in keywords[i][1]:
        print(keywords[i])

for j in range(len(keywords)):
    if 'member2' in keywords[j][1]:
        print(keywords[j])

for k in range(len(keywords)):
    if 'member3' in keywords[k][1]:
        print(keywords[k])

for l in range(len(keywords)):
    if 'member4' in keywords[l][1]:
        print(keywords[l])

for m in range(len(keywords)):
    if 'member5' in keywords[m][1]:
        print(keywords[m])

for n in range(len(keywords)):
    if 'member6' in keywords[n][1]:
        print(keywords[n])

for o in range(len(keywords)):
    if 'member7' in keywords[o][1]:
        print(keywords[o])

for p in range(len(keywords)):
    if 'member8' in keywords[p][1]:
        print(keywords[p])

for q in range(len(keywords)):
    if 'member9' in keywords[q][1]:
        print(keywords[q])

for r in range(len(keywords)):
    if 'member10' in keywords[r][1]:
        print(keywords[r])
