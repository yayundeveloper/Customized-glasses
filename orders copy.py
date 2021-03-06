import csv
import asyncio

csv_keyword = csv.reader(open('./Order/Orders.csv', encoding='UTF-8', errors='ignore'))

keywords = []

for row in csv_keyword:
    keywords.append(row)

#print(keywords)

async def main():

    for i in range(len(keywords)):
        if '已确认' in keywords[i][1]:
            print(keywords[i])

    for j in range(len(keywords)):
        if '已付款' in keywords[j][1]:
            await asyncio.sleep(1)
            print(keywords[j])
'''
    for k in range(len(keywords)):
        if '20101612125137' in keywords[k][1]:
            await asyncio.sleep(1)
            print(keywords[k])

    for l in range(len(keywords)):
        if '20101703023368' in keywords[l][1]:
            await asyncio.sleep(2)
            print(keywords[l])

    for m in range(len(keywords)):
        if '20101411114548' in keywords[m][1]:
            await asyncio.sleep(2)
            print(keywords[m])

    for n in range(len(keywords)):
        if '20101114112029' in keywords[n][1]:
            await asyncio.sleep(3)
            print(keywords[n])

    for o in range(len(keywords)):
        if '20100803085083' in keywords[o][1]:
            await asyncio.sleep(3)
            print(keywords[o])

    for p in range(len(keywords)):
        if '20100802173650' in keywords[p][1]:
            await asyncio.sleep(4)
            print(keywords[p])


    for q in range(len(keywords)):
        if 'Xuya Wang' in keywords[q][1]:
            await asyncio.sleep(4)
            print(keywords[q])
'''

asyncio.run(main())
