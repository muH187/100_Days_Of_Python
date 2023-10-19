name = input("Enter your name\n")
print("Welcome", name, "to KBC")
ab = input("So can we start our game?\n")
if ab == "yes":
    qs = ["Q1. What country has the highest life expectancy?\n 1. India\n 2. USA\n 3. UK\n 4. Hongkong",
          "Q2. Where would you be if you were standing on the Spanish Steps?\n 1. India\n 2. USA\n 3. UK\n 4. Rome",
          "Q3. Who was the Ancient Greek God of the Sun?\n 1. Zeus\n 2. Odin\n 3. Apollo\n 4. Thor",
          "Q4. What year was the United Nations established?\n 1. 1943\n 2. 1944\n 3. 1945\n 4. 1946",
          "Q5. What car manufacturer had the highest revenue in 2020?\n 1. Volkswagen\n 2. Toyota\n 3. Honda\n 4. Tata"]

    print(qs[0])
    a1 = int(input("Enter your answer\n"))
    if a1 == 4:
        print("Your answer is correct\n You win Rs. 500")
        print(qs[1])
        a2 = int(input("Enter your answer\n"))
        if a2 == 4:
            print("Your answer is correct\n You win Rs. 1000")
            print(qs[2])
            a3 = int(input("Enter your answer\n"))
            if a3 == 3:
                print("Your answer is correct\n You win Rs. 2000")
                print(qs[3])
                a4 = int(input("Enter your answer\n"))
                if a4 == 3:
                    print("Your answer is correct\n You win Rs. 4000")
                    print(qs[4])
                    a5 = int(input("Enter your answer\n"))
                    if a5 == 1:
                        print(
                            "Your answer is correct\n You win Rs. 8000\n This is the end of the game\n Thankyou for playing with us")
                    else:
                        print("Game over\nThankyou for playing with us")
                else:
                    print("Game over\nThankyou for playing with us")
            else:
                print("Game over\nThankyou for playing with us")
        else:
            print("Game over\nThankyou for playing with us")
    else:
        print("Game over\nThankyou for playing with us")
else:
    print("Game over\nThankyou for playing with us")