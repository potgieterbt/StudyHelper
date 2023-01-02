import random
import pandas
import sys
import os
import csv
from datetime import datetime

questions = []

if len(sys.argv) != 2:
    sys.exit(
        "Usage: python app.py P1 (where 'P' is the folder of the questions and '1' is the file of the questions exclude the extention.)"
    )
try:
    f = open(
        os.path.join(".\\questions", sys.argv[1][0].lower(),
                     f"{sys.argv[1][1]}.txt"))
except:
    sys.exit("Couldn't open file please check the file path and try again")
if f:
    questions = f.readlines()
    questions = [x.strip() for x in questions]
    print(questions)

numquest = len(questions)

idx = random.sample(range(1, numquest + 1), numquest)

results = {}

for i in range(len(idx)):
    print(i)
    print(len(questions))
    print(f"Question #{i}: {questions[i]}")
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

    results[idx[i]] = reult

date = datetime.now().date()

header = ['Date'] + idx
results['Date'] = date
if os.path.exists(
        os.path.join(".\\results", sys.argv[1][0].lower(),
                     f'{sys.argv[1][1].lower()}.csv')):
    with open(os.path.join(".\\results", sys.argv[1][0].lower(),
                           f'{sys.argv[1][1].lower()}.csv'),
              'a+',
              newline='') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writerow(results)
        csvfile.close()

else:
    with open(os.path.join(".\\results", sys.argv[1][0].lower(),
                           f'{sys.argv[1][1]}.csv'),
              'w',
              newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerow(results)
        csvfile.close()