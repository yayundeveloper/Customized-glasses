import csv
import asyncio

csv_keyword = csv.reader(open('./User/Users.csv', encoding='gbk', errors='ignore'))

keywords = []

for row in csv_keyword:
    keywords.append(row)

#print(keywords)

for i in range(len(keywords)):
    if 'Yutao Zhou' in keywords[i][1]:
        print(keywords[i])

async def main():

    for j in range(len(keywords)):
        if 'Yuexiao Pan' in keywords[j][1]:
            await asyncio.sleep(1)
            print(keywords[j])

    for k in range(len(keywords)):
        if 'James Yang' in keywords[k][1]:
            await asyncio.sleep(1)
            print(keywords[k])

    for l in range(len(keywords)):
        if 'Ziyang Li' in keywords[l][1]:
            await asyncio.sleep(2)
            print(keywords[l])
'''
    for m in range(len(keywords)):
        if 'SHIYUN DENG' in keywords[m][1]:
            await asyncio.sleep(2)
            print(keywords[m])

    for n in range(len(keywords)):
        if 'Yin Cai' in keywords[n][1]:
            await asyncio.sleep(3)
            print(keywords[n])

    for o in range(len(keywords)):
        if 'Cathy Lee' in keywords[o][1]:
            await asyncio.sleep(3)
            print(keywords[o])

    for p in range(len(keywords)):
        if 'Zi' in keywords[p][1]:
            await asyncio.sleep(4)
            print(keywords[p])

    for q in range(len(keywords)):
        if 'Chunyao Liu' in keywords[q][1]:
            await asyncio.sleep(4)
            print(keywords[q])
'''
        
asyncio.run(main())
