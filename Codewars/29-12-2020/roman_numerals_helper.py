import re
class RomanNumerals:
    rom_nums = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    @classmethod
    def to_roman(cls, num):
        result = ''
        for rom_num in cls.rom_nums:
            result += rom_num[1] * (num // rom_num[0])
            num = num % rom_num[0]
        return result

    @classmethod
    def get_num_value(cls, result, is_odd=True):
        validator = 1 if is_odd else 0 
        for rom_num in [value for num, value in enumerate(cls.rom_nums) if num % 2 == validator]:
            quantity = re.findall(rom_num[1], cls.res)
            result += rom_num[0] * len(quantity)
            if quantity:
                cls.res = cls.res.replace(rom_num[1], '')
        return result
    
    @classmethod
    def from_roman(cls, rom):
        cls.res = rom
        result = cls.get_num_value(0) 
        return cls.get_num_value(result, is_odd=False)
