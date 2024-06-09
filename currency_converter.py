def main():
    currency_from = input("Currency converting from? (USD, GBP, EUR): ").lower()
    currency_into = input("Currency converting into? (USD, GBP, EUR): ").lower()
    amount = int(input("Amount to be converted: "))

    if currency_from == "usd" and currency_into == "gbp":
        print(str(amount) + " dollars is equal to " + str(float(amount*0.79)) + " pounds")
    elif currency_from == "usd" and currency_into == "eur":
        print(str(amount) + " dollars is equal to " + str(float(amount*0.92)) + " euros")
    elif currency_from == "gbp" and currency_into == "usd":
        print(str(amount) + " pounds is equal to " + str(float(amount*1.27)) + " dollars")
    elif currency_from == "gbp" and currency_into == "eur":
        print(str(amount) + " pounds is equal to " + str(float(amount*1.17)) + " euros")
    elif currency_from == "eur" and currency_into == "usd":
        print(str(amount) + " euros is equal to " + str(float(amount*1.08)) + " dollars")
    elif currency_from == "eur" and currency_into == "gbp":
        print(str(amount) + " euros is equal to " + str(float(amount*0.85)) + " pounds")
    else:
        print("Please enter a valid currency and/or amount.")

if __name__ == "__main__":
    main()
