import random

maxq = int(input("Input how many questions you want to do: "))
questions = random.sample(range(1, maxq + 1), maxq)

results = {}

for i in questions:
    print("Question #" + str(i))
    reult = -1
    while reult < 0 or reult > 1:
        inp = input(
            "Score your result from 0.0 - 1.0(1 being 100% and 0 being 0%)")
        if inp == 'q':
            exit(0)
        try:
            reult = int(inp)
        except:
            reult = -1

    results[i] = reult

print(results)