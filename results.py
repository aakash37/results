#written and designed by devicoven & er4Zer
#All rights reserved

import requests,json,csv

d = 1
e = 1
a1 = input(str('enter college code: ')) #college code
a2 = input(str('branch code: '))   #branch code
a3 = '191'  #year
a4 = '1'    #result for semester
a5 = 230   #last roll no
dataFile = a1+a2+a3+'.csv'

try:
    tempFile = open ( dataFile,'r' )
    l1 = tempFile.readlines()
    tempFile.close()
    try:
        l2 = l1[-1]
    except IndexError:
        l2 = l1[0]

    l3 = l2.split(',')
    l4 = l3[1]
    l5 = l4[9:]
    c = int(l5) + 1 

    print('Data.csv found')
    print('continuing to scrap results from',c,'...')
    fileWriter = csv.writer(open(dataFile, "a+"))
    #fileWriter.writerow('\n')

except FileNotFoundError:
    c = 1

    fileWriter = csv.writer(open(dataFile, "a+"))
    #fileWriter.writerow("{},{},{},{},{}".format('NAME','ENROLL','RESULT','CGPA','SGPA'))
    print('Data.csv created')
    print('initalising results scraping...')

while c <= a5:

    a = 'https://rgpv-result.herokuapp.com/api2?rollNo='+a1+a2+a3
    b = '&semester='+a4
    url = a + str(c).zfill(3) + b
    
    res = requests.get(url)
    pback = res.json()
    
    try:
        x = [pback["body"]["data"]["name"],pback["body"]["data"]["rollNo"],pback["body"]["data"]["result"],pback["body"]["data"]["sgpa"],pback["body"]["data"]["cgpa"]]
        fileWriter.writerow(x)
        
        print('result of roll number',c,'appended')
        c += 1
        d += 1
    
    except KeyError:
        
        if e < 4:
            print('error while getting the result for roll number',c,'retrying['+str(e)+']...')
            e += 1
            continue
            
        else:
            x1 = a1+a2+a3+ str(c).zfill(3)
            print('failed to get the result for roll number',c,'>_<')
            #fileWriter.writerow("{},{},{},{},{}".format('NULL',x1,'NULL','NULL','NULL'))
            e = 1
            c += 1
print('data of',d,'students scraped successfully ;)')
