class Roman:
    
    def __init__(self):
        self.dict_roman = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
                           10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
                           100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC',
                           900: 'CM', 1000: 'M', 2000: 'MM', 3000: 'MMM',
                           'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    def to_roman(self, n):
        ronam_number = list(str(n))
        for i, j in enumerate(range(len(ronam_number), 0, -1)):
            ronam_number[i] = int(ronam_number[i]) * 10 ** (j - 1)
            ronam_number[i] = self.dict_roman[ronam_number[i]]
        return str().join(ronam_number)
    
    def from_roman(self, n):
        roman_number = list(n)
        for i in range(len(roman_number)):
            roman_number[i] = self.dict_roman[roman_number[i]]
        if roman_number[0] < roman_number[-1]:
            return roman_number[-1] + sum([-i for i in roman_number[:-1]])
        return sum(roman_number)


RomanNumerals = Roman()

print(RomanNumerals.to_roman(1000) == 'M', '1000 should == "M"')
print(RomanNumerals.to_roman(1990) == 'MCMXC', '1990 should == "MCMXC"')

print(RomanNumerals.from_roman('XXI') == 21, 'XXI should == 21')
print(RomanNumerals.from_roman('MMVIII') == 2008, 'MMVIII should == 2008')
print(RomanNumerals.from_roman('XXC'))
print(RomanNumerals.from_roman('IV'))
