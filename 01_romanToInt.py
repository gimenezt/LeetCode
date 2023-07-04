class Solution:
    def romanToInt(self, s: str) -> int:
        obj = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev_value = 0

        # Estamos olhando a string do final para o começo
        for char in reversed(s):
            curr_value = obj[char]
            
            if curr_value < prev_value: # Se a letra tiver valor menor do que anterior, subtraimos
                result -= curr_value
            else:
                result += curr_value
                prev_value = curr_value

        return result
