num = { 'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }

f = open('089_roman.txt').read()
initLength = len(f)
roman = f.split()

def toInt(numeral):
    integer = 0
    for i in range(len(numeral)):
        if i == len(numeral) - 1 or num[numeral[i]] >= num[numeral[i+1]]:
            integer += num[numeral[i]]
        else: 
            integer += num[numeral[i+1]] - num[numeral[i]]
            i += 1
    return integer

def toRoman(integer):
    numeral = ""
    denoms = list(num.values())
    denoms.reverse() 
    chars = list(num.keys())
    chars.reverse()
    print(chars)
    print(denoms)
    for i in range(len(denoms)):
        x = integer / denoms[i]
        integer = integer % denoms[i]
        numeral += int(x) * chars[i]
    return numeral

print(toRoman(100))
