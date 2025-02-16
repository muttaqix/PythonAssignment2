StudentNumber = 991809457

count = 0

while True:
    num = int(input("Enter a number >=0. If you type a negative number this loop will end: "))

    if num == StudentNumber:
        print("Cutoff Point")
        break
    
    if num < 0:
        break
    count += 1

print("The loop iterated",count, "times.")