# Last updated: 01/05/2025 16:27:30
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        numbers = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        for value in numbers.keys():
            while num >= value:
                num -= value
                res += numbers[value]
        return res