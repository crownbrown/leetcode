import unittest

def romanLookUp(s: str) -> int:
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    return roman_dict[s]

def romanSubtract(curr_ltr: str, next_ltr: str) -> int:
    curr_int = romanLookUp(curr_ltr)
    next_int = romanLookUp(next_ltr)
    return next_int - curr_int



def romanToInt(s: str) -> int:
    str_lng = len(s)
    idx = 0
    total = 0
    while str_lng > 0 and idx < str_lng - 1:
        curr_ltr = s[idx]
        next_ltr = s[idx + 1]
        if curr_ltr == "I" and (next_ltr == "V" or next_ltr == "X"):
            subtract_total = romanSubtract(curr_ltr, next_ltr)
            total += subtract_total
            idx += 2
        elif curr_ltr == "X" and (next_ltr == "L" or next_ltr == "C"):
            subtract_total = romanSubtract(curr_ltr, next_ltr)
            total += subtract_total
            idx += 2
        elif  curr_ltr == "C" and (next_ltr == "D" or next_ltr == "M"):
            subtract_total = romanSubtract(curr_ltr, next_ltr)
            total += subtract_total
            idx += 2
        else:
            curr_int = romanLookUp(curr_ltr)
            total += curr_int
            idx += 1
    curr_ltr = s[idx]
    curr_int = romanLookUp(curr_ltr)
    total += curr_int
    idx += 1
    return total





if __name__ == '__main__':
    unittest.main(verbosity=2)
