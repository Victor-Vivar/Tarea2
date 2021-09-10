
def revCount(number):
    if number >= 0:
        print(number)
        if number == 0:
            print("BOOOOM!!")
            return
        revCount(number - 1)

number = 10
revCount(number)