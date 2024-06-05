import random 

def main():
    uppercase_letters = "ABCDDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "1234567890"
    symbols = "_-+=|:;?/>.<,{)(}[]"

    all = ""
    upper, lower, numbers, syms = True, True, True, True

    if upper:
        all += uppercase_letters
    elif lower:
        all += lowercase_letters
    elif numbers:
        all += digits
    elif syms:
        all += symbols

    length = int(input("How many characters should the password be? "))
    amount = int(input("How many passwords are to be generated? "))

    for x in range(amount): # This is a for loop
        password = "".join(random.sample(all, length))
        print(password)

if __name__ == "__main__":
    main()