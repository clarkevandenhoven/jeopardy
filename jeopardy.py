import json
from random import randrange
questions = json.load(open('jeopardy.json'))

num_q = len(questions)
stop = ""
while stop.lower() != "yes" or stop.lower() != "y":
    pick = randrange(num_q)
    question = questions[pick]["question"]
    category = questions[pick]["category"]
    air_date = questions[pick]["air_date"]
    answer = questions[pick]["answer"]
    print(air_date + "\n" + category + "\n" + question)
    my_answer = input("Answer : ")
    print(answer)
    stop = input("Would you like to stop: ")

