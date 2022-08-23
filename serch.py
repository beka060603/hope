def mm(lst,num=11):
    sert=list([abs(i-num),i]for i in lst)
    sert.sort()
    sert_2 = []
    for j in sert:
        sert_2.append(j[-1])
    return num,sert_2
print(mm([1,2,3,4,5,6,8,7,9],2))