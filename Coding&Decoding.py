print("Welcome to Code and Decode Center")
st = input("Enter your message: ")
coding = input("Type 1 For Coding and 2 For Decoding: ")
coding = True if coding == "1" else False
print(coding)
words = st.split(" ")
if coding:
    nword = []
    for word in words:
        if len(word) >= 3:
            r1 = "dir"
            r2 = "rid"
            stnew = r1 + word[1:] + word[0] + r2
            nword.append(stnew)
        else:
            nword.append(word[::-1])
    print(" ".join(nword))
else:
    nword = []
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nword.append(stnew)
        else:
            nword.append(word[::-1])

    print(" ".join(nword))
