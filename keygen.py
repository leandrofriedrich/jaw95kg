# include needed stuff
import random

"------------------- Generate CD Key Start ----------------"

# generate first block and check if its "illegal"
def cd_keygen_first_block():
    first_block_illegal = [333, 444, 555, 666, 777, 888]
    first_block = str(random.randint(0, 998))
    while first_block in first_block_illegal:
        first_block = str(random.randint(0, 998))
    return str(first_block).rjust(3, '0')


# generate second block
def cd_keygen_second_block():
    # generate it in 2 blocks, since im lazy and the setup expects the last digit to NOT be 0 or equal/bigger than 8
    first_digits = str(random.randint(0, 999999))
    last_digit = random.randint(0, 9)
    # check if the last digit is equal/bigger than 8 or equal to zero and if it is, regenerate it
    while last_digit == 0 or last_digit >= 8:
        last_digit = random.randint(0, 9)
    second_block = (first_digits + str(last_digit)).rjust(7, '0')

    sum = 0
    for x in second_block:
        sum += int(x)

    return second_block, sum

def check_cd_second_block():
    second_block, sum = cd_keygen_second_block()
    while sum % 7 != 0:
        second_block, sum = cd_keygen_second_block()

    return second_block
"----------------- Generate CD Key Done -----------------------------------"

"----------------- Generate OEM Key Start ---------------------------------"

# generate first block
def oem_keygen_first_block():
    year = ["95", "96", "97", "98", "99", "00", "01", "02", "03"]
    digits_three = random.randint(0, 366)
    digits_two = random.choice(year)
    return str(digits_three) + str(digits_two)

# generate second block and check if the last digit is "illegal", if it is, regenerate it
def oem_keygen_second_block():
    digit_middle = random.randint(0, 99999)
    digit_last = random.randint(0, 9)
    while digit_last == 0 or digit_last >= 8:
        digit_last = random.randint(0, 9)

    second_block = ("0" + str(digit_middle) + str(digit_last)).rjust(7, "0")

    sum = 0
    for x in second_block:
        sum += int(x)

    return second_block, sum

# check if the second digits are "illegal" and if they are, regenerate them
def check_second_block():
    seven_digits, sum = oem_keygen_second_block()
    while sum % 7 != 0:
        second_block, sum = oem_keygen_second_block()
    return second_block

# generate third block

def oem_keygen_third_block():
    third_block = random.randint(0, 99999)
    return str(third_block).rjust(5, "0")

"----------------- Generate OEM Key Done ---------------------------------"
