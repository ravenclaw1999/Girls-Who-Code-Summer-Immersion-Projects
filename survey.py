import json
from pprint import pprint

with open('responses.json', 'r') as f:
    all_responses = json.load(f)

while True:
    survey = {}

    answer1 = input("What's your name?")
    answer2 = input("What's your favorite fictional character?")
    survey['name'] = answer1
    survey['character'] = answer2
    print (survey)

    question3 = input("What's your favorite book series?")
    question4 = input("Who is the author?")
    survey['book'] = question3
    survey['author'] = question4
    print (survey)

    question5 = input("What's your favorite tv show?")
    question6 = input("What's your favorite episode from that show?")
    survey['show'] = question5
    survey['episode'] = question6
    print (survey)

    question7 = input("What's your favorite movie?")
    question8 = input("What's your favorite actor/actress?")
    survey['movie'] = question7
    survey['actor'] = question8
    print (survey)

    print("Thank you for answering my survey questions!")

    all_responses.append(survey)
    pprint(all_responses)

    # dump all responses into json
    # then save it to a file (responses.json)
    data = json.dumps(all_responses)
    with open('responses.json', 'w') as fp:
        fp.write(data)
    break
