def parse_int(string):
    string = string.replace('and', '').split()
    
    ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
             "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if string[0] == 'zero':
        return 0
    
    for s in range(len(string)):
        if '-' in string[s]:
            string[s] = string[s].split('-')
        if len(string[s]) == 2:
            for o in range(len(ones)):
                if string[s][1] == ones[o]:
                    string[s][1] = str(o + 1)
            for t in range(len(tens)):
                if string[s][0] == tens[t]:
                    string[s][0] = str((t + 2) * 10)
            string[s] = int(string[s][0]) + int(string[s][1])
    
    for s in range(len(string)):
        if string[s] == 'hundred':
            string[s] = int(string[s - 1]) * 100
            string[s - 1] = ''
            try:
                if 'thous' == string[s + 2]:
                    string[s] *= 1000
            except IndexError:
                pass
        if string[s] == 'thous':
            string[s] = int(string[s - 1]) * 1000
            string[s - 1] = ''
        if string[s] == 'million':
            string[s] = int(string[s - 1]) * 1000000
            string[s - 1] = ''

        for o in range(len(ones)):
            if string[s] == ones[o]:
                string[s] = int(str(o + 1))
        for t in range(len(teens)):
            if string[s] == teens[t]:
                string[s] = int(str(t + 10))
        for t in range(len(tens)):
            if string[s] == tens[t]:
                string[s] = int(str((t + 2) * 10))
    
    return sum([s for s in string if type(s) == int])


print(parse_int('zero'), 0)
print(parse_int('one'), 1)
print(parse_int('two'), 2)
print(parse_int('three'), 3)
print(parse_int('four'), 4)
print(parse_int('five'), 5)
print(parse_int('six'), 6)
print(parse_int('seven'), 7)
print(parse_int('eight'), 8)
print(parse_int('nine'), 9)
print(parse_int('ten'), 10)
print(parse_int('twenty'), 20)
print(parse_int('twenty-one'), 21)
print(parse_int('thirty-seven'), 37)
print(parse_int('forty-six'), 46)
print(parse_int('fifty-nine'), 59)
print(parse_int('sixty-eight'), 68)
print(parse_int('seventy-two'), 72)
print(parse_int('eighty-three'), 83)
print(parse_int('ninety-four'), 94)
print(parse_int('one hundred'), 100)
print(parse_int('one hundred one'), 101)
print(parse_int('one hundred and one'), 101)
print(parse_int('one hundred sixty-nine'), 169)
print(parse_int('two hundred and ninety-nine'), 299)
print(parse_int('seven hundred thirty-six'), 736)
print(parse_int('two thousand'), 2000)
print(parse_int('one thousand three hundred and thirty-seven'), 1337)
print(parse_int('ten thousand'), 10000)
print(parse_int('twenty-six thousand three hundred and fifty-nine'), 26359)
print(parse_int('thirty-five thousand'), 35000)
print(parse_int('ninety-nine thousand nine hundred and ninety-nine'), 99999)
print(parse_int('six hundred sixty-six thousand six hundred sixty-six'), 666666)
print(parse_int('seven hundred thousand'), 700000)
print(parse_int('two hundred thousand three'), 200003)
print(parse_int('two hundred thousand and three'), 200003)
print(parse_int('two hundred three thousand'), 203000)
print(parse_int('five hundred thousand three hundred'), 500300)
print(parse_int('eight hundred eighty-eight thousand eight hundred and eighty-eight'), 888888)
print(parse_int('one million'), 1000000)
