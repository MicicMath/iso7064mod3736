# Direct implementation of ISO/EIC 7064 MOD 37,36 check digit creation algorithm.
# Source: https://www.uni-due.de/imperia/md/content/dc/yanling_2015_check_digit.pdf
# Although other implementations exist a more mathematical approach was chosen here. Why?
# "Do not use libraries which you don't understand"
# Author: Dr.sc.ETH Srdjan J. Micic
# Email: micic.math@gmail.com


# Theoretically different alphabets are allowed. Keep the below alphabet as a convention though. Note that the order matters (i.e. indices of characters in the alphabet matter)
ALPHABET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def special_mod(num, mod):  # see text below equation (18) on page 11 of the source above
    if(num % mod == 0):
        return mod
    return num % mod


def calc_check_digit(seq, alphabet=ALPHABET):  # see equation (19) on page 12 of the source above
    seq = str(seq)  # yes, yes I know... Too lazy for anything better
    mod, mod_plus_one = len(alphabet), len(alphabet) + 1
    temp = mod
    for n in seq:
        temp = (special_mod((temp + alphabet.index(n)), mod) * 2) % mod_plus_one
    indx = special_mod(1 - temp, mod)
    return alphabet[indx]  # Neet trick for the values table 0 = 0, 1 = 1, 2 = 2, ..., A = 10, B = 11, C = 12, ..., X = 34, Y = 35, Z = 36


if __name__ == "__main__":
    example_seq = '900001AXF'
    print("Example sequence:", example_seq)
    ckdg = calc_check_digit(example_seq)
    print("Check digit:", ckdg)
    print("Example sequence with check digit: ", example_seq + ckdg)
