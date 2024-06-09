def main():
    marks = int(input(("Enter your total marks achieved out of 100? ")))
    
    if marks < 100:
        print("Your GPA is " + str(marks/25))
    else:
        print("Please provide a value within a range of 100")

if __name__ == "__main__":
    main()