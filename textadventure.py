# Update this text to match your story.

start = "Hi, my name is Zola."
print (start)
answer = input("What's your name?")
print (answer, "is a nice name!")
answer2 = ''
while answer2 != "go on an adventure" and answer2 != "eat ice cream":
    answer2 = input("Should I go on an adventure or eat ice cream?")
    if answer2 == "go on an adventure":
        print ("You ended up in a forest. A wizard yells 'ice cream for sale, ice cream for sale!'")
        decision = ''
        while decision != "yes" and decision != "no":
            decision = input("Do you want to buy ice cream?")
            if decision == "yes":
                flavor = ''
                while flavor != "chocolate" and flavor != "strawberry" and flavor != "vanilla":
                    flavor = input("Do you want to buy chocolate, strawberry, or vanilla ice cream?")
                    if flavor == "chocolate":
                        print ("You end up in hell because of your chronic lactose intolerance! ... You wonder if they have ice cream in hell.")
                        print ("THE END")
                    if flavor == "strawberry":
                        print ("You end up in hell because of your chronic lactose intolerance! ... You wonder if they have ice cream in hell.")
                        print ("THE END")
                    if flavor == "vanilla":
                        print ("You end up in hell because of your chronic lactose intolerance! ... You wonder if they have ice cream in hell.")
                        print ("THE END")
                if decision == "no":
                    print ("You eat ice cream anyways.")
            if answer2 == "eat ice cream":
                print ("You eat ice cream and live happily ever after...THE END.")
