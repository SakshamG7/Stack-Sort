rList = [23, 87, 97, 80, 49, 84, 81, 13, 66, 93]
finalList = []
subLists = [[]]

lCount = 0
for i in range(len(rList) - 1):
    subLists[lCount].append(rList[i])
    if rList[i] > rList[i+1]:
        lCount += 1
        subLists.append([])

print(subLists)


for _ in range(len(subLists)):
    smallest = 0
    for i in range(1, len(subLists)):
        if subLists[i][0] < subLists[smallest][0]:
            smallest = i
    smallestList = subLists[smallest]
    subLists.pop(smallest)

    if finalList == []:
        for i in smallestList:
            finalList.append(i)
    else:
        for i in smallestList:
            inserted = False
            for j in range(smallest, len(finalList)):
                finalList.insert(j, i)
                inserted = True
                break
            if not inserted:
                finalList.append(i)
print(finalList)
rList.sort()
print(rList)
