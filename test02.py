# character in string has index number
    #123456789
infoA = 'Hello SAU 2023'
    #

print(infoA[6])
print(infoA[-8])

#เข้าถึงตัวอักษรหลายตัวใน string จะใช้ Slicing ด้วย index number
#SAU
print(infoA[6:9])
print(infoA[-8:-5])
#o SAU 20
print(infoA[4:12])

print( infoA.upper() )
print( infoA.lower() )
print( infoA.capitalize() )
print( infoA.count('SAU') )
print( infoA.title() )
print( infoA.isdigit() )
print( infoA.islower() )
infoB = infoA.replace('SAU', 'IOT')
print(infoB)
print(infoB.replace('Hello','Hi'))

print( len(infoA))