scores = [50,70,54,23,91,86,76,100,65,77]

for grade in scores:
    if grade >= 80:
        print("The grade", grade, "is an A")
    elif 70 <= grade < 80:
        print("The grade", grade, "is a B")
    elif 60 <= grade < 70:
        print("The grade", grade, "is a C")
    elif 50 <= grade < 60:
        print("The grade", grade, "is a D")
    else:
        print("The grade", grade, "is an F")
