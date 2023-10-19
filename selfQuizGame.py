print("Welcome to Our \"Quiz Game\"")
score = 0
question1 = input("CPU stand for: ")
if question1.lower() == 'central processing unit':
    print("Correct")
    score +=1
else:
    print("Incorrect")

question1 = input("GPU stand for: ")
if question1.lower() == 'graphic processing unit':
    print("Correct")
    score +=1
else:
    print("Incorrect")

question1 = input("RAM stand for: ")
if question1.lower() == 'random access memory':
    print("Correct")
    score +=1
else:
    print("Incorrect")

question1 = input("ROM stand for: ")
if question1.lower() == 'read only memory':
    print("Correct")
    score +=1
else:
    print("Incorrect")

question1 = input("USA stand for: ")
if question1.lower() == 'united states of america':
    print("Correct")
    score +=1
else:
    print("Incorrect")

question1 = input("UK stand for: ")
if question1.lower() == 'united kingdom':
    print("Correct")
    score +=1
else:
    print("Incorrect")

print(f"Your final score is {score} out of 6")
print("Your score percentage is", score/6*100,"%")

