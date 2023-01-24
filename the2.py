studentid = str(input())
std = list(studentid)
if std[5] == 'X':
    std[5]=10
ind = studentid.find('?')
if ind == -1:
    check = int(std[0])*2+int(std[1])*3+int(std[2])*5+int(std[3])*7
    if check%11 == int(std[5]):
        print('VALID')
    else:
        print('INVALID')
elif ind == 0:
    check = int(std[1])*3 + int(std[2])*5 + int(std[3])*7
    if check // 11 * 11 - check + int(std[5]) < 0:
        check1 = (check // 11 + 1) * 11
    else:
        check1 = (check // 11) * 11
    if check1-check+int(std[5]) == 11:
        std[0] = 0
    else:
        if (check1-check+int(std[5]))%2==0:
            std[0] = int((check1-check+int(std[5]))/2)
        else:
            check1+=11
        if (check1-check+int(std[5]))%2==0:
            std[0] = int((check1-check+int(std[5]))/2)
        else:
            check1+=11
        if std[0] == 10:
            std[0]='X'
        if std[5] == 10:
                std[5]='X'
    print(str(std[0])+str(std[1])+str(std[2])+str(std[3])+str(std[4])+str(std[5]))
elif ind == 1:
    check = int(std[0])*2 + int(std[2])*5 + int(std[3])*7
    if check // 11 * 11 - check + int(std[5]) < 0:
        check1 = (check // 11 + 1) * 11
    else:
        check1 = (check // 11) * 11
    if check1-check+int(std[5]) == 11:
        std[1] = 0
    else:
        if (check1-check+int(std[5]))%3==0:
            std[1] = int((check1-check+int(std[5]))/3)
        else:
            check1+=11
        if (check1-check+int(std[5]))%3==0:
            std[1] = int((check1-check+int(std[5]))/3)
        else:
            check1+=11
        if (check1-check+int(std[5]))%3==0:
            std[1] = int((check1-check+int(std[5]))/3)
        else:
            check1+=11
        if std[1] == 10:
            std[1]='X'
        if std[5] == 10:
            std[5]='X'
    print(str(std[0])+str(std[1])+str(std[2])+str(std[3])+str(std[4])+str(std[5]))
elif ind == 2:
    check = int(std[0])*2 + int(std[1])*3 + int(std[3])*7
    if check // 11 * 11 - check + int(std[5]) < 0:
        check1 = (check // 11 + 1) * 11
    else:
        check1 = (check // 11) * 11
    if check1-check+int(std[5]) == 11:
        std[2] = 0
    else:
        if (check1-check+int(std[5]))%5==0:
            std[2] = int((check1-check+int(std[5]))/5)
        else:
            check1+=11
        if (check1-check+int(std[5]))%5==0:
            std[2] = int((check1-check+int(std[5]))/5)
        else:
            check1+=11
        if (check1-check+int(std[5]))%5==0:
            std[2] = int((check1-check+int(std[5]))/5)
        else:
            check1+=11
        if (check1-check+int(std[5]))%5==0:
            std[2] = int((check1-check+int(std[5]))/5)
        else:
            check1+=11
        if (check1-check+int(std[5]))%5==0:
            std[2] = int((check1-check+int(std[5]))/5)
        else:
            check1+=11
        if std[2] == 10:
            std[2]='X'
        if std[5] == 10:
                std[5]='X'
    print(str(std[0])+str(std[1])+str(std[2])+str(std[3])+str(std[4])+str(std[5]))
elif ind == 3:
    check = int(std[0])*2 + int(std[1])*3 + int(std[2])*5
    if check // 11 * 11 - check + int(std[5]) < 0:
        check1 = (check // 11 + 1) * 11
    else:
        check1 = (check // 11) * 11
    if check1-check+int(std[5]) == 11:
        std[3] = 0
    else:
        if (check1-check+int(std[5]))%7==0:
            std[3] = int((check1-check+int(std[5]))/7)
        else:
            check1+=11
        if (check1-check+int(std[5]))%7==0:
            std[3] = int((check1-check+int(std[5]))/7)
        else:
            check1+=11
        if (check1-check+int(std[5]))%7==0:
            std[3] = int((check1-check+int(std[5]))/7)
        else:
            check1+=11
        if (check1-check+int(std[5]))%7==0:
            std[3] = int((check1-check+int(std[5]))/7)
        else:
            check1+=11
        if (check1-check+int(std[5]))%7==0:
            std[3] = int((check1-check+int(std[5]))/7)
        else:
            check1+=11
        if (check1-check+int(std[5]))%7==0:
            std[3] = int((check1-check+int(std[5]))/7)
        else:
            check1+=11
        if (check1-check+int(std[5]))%7==0:
            std[3] = int((check1-check+int(std[5]))/7)
        else:
            check1+=11
        if std[3] == 10:
            std[3]='X'
        if std[5] == 10:
                std[5]='X'
    print(str(std[0])+str(std[1])+str(std[2])+str(std[3])+str(std[4])+str(std[5]))
elif ind==5:
    check = int(std[0])*2 + int(std[1])*3 + int(std[2])*5 + int(std[3])*7
    std[5]=int(check%11)
    if std[5] == 10:
        std[5]='X'
    print(str(std[0])+str(std[1])+str(std[2])+str(std[3])+str(std[4])+str(std[5]))
