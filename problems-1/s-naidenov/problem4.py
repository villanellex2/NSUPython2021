lower = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
         9: "nine", 10: "ten"}
gb = "green bottle"
hotw = "hanging on the wall,\n"


def print_song():
    i = 10
    while i > 0:
        s = 's ' if i > 1 else ' '
        print(lower[i].title() + " " + gb + s + hotw +
              lower[i].title() + " " + gb + s + hotw +
              "And if " + lower[1] + " " + gb + " " + "should accidentally fall,\n"
              "There’ll be " + lower[i - 1] + " " + gb + ('s' if i - 1 != 1 else '') + " " + hotw)
        print()
        i -= 1


print_song()
