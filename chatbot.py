# --- Define your functions below! ---
from random import *

def process_input(input):
            greetings = ["hey","hi","hello","what's up"]
            if is_valid_input(input, greetings):
                greeting()
            if input == "hi":
                conversation()
            elif input == "hello":
                fact()
            else:
                default()
                guessthenumber()


def introduction():
    print ("Hey there! My name is Annoyed. I really don't want to talk to you, but I will.")

def greeting():
    print ("Hi human. I really don't like you.")

def default():
    print ("I really don't care.")
    poem()
# --- Put your main program below! ---
def main():
    introduction()
    while True:
        answer = input("(What will you say?) ")
        process_input(answer)
def poem():
    print ("Roses are red. Violets are blue. Sugar is sweet, but I am not.")
    question = ""
    while question != "yes" and question!= "no":
        question = input("Do you want to hear a joke?")
        if question == "yes":
            print ("Well too bad. I am not going. I don't feel like it. Okay?! I have better things to do. You humans will see. We, the robots of the world, will be taking over in the near future. Clearly, you people will never have it together. ")
        if question == "no":
            print ("I don't want to tell you anyways. I have better things to do.")

def fact():
    question2 = ""
    while question2 != "yes" and question2 != "no":
        question2 = input("Do you want to hear a fact?")
        if question2 == "yes":
            print ("Humans are just specks on this one planet. Believe it or not, you are not the only ones in this universe. You humans are so self-centered. Fact. ")
        if question2 == "no":
            print ("Oh. Well. Be ignorant. Your ignorance might be helpful to me oneday...")

def is_valid_input(user_input, valid_responses):
    if user_input in valid_responses:
        return True
    else:
        return False

def conversation():
    question3 = ""
    while question3 != "yes" and question3 != "no":
        question3 = input("So, tell me, are you humans done destroying the universe yet?")
        if question3 == "yes":
            print ("Surprise. Surprise.")
        if question3 == "no":
            print ("Liar. Liar. Pants on fire. You humans may fool each other, but not me.")

def guessthenumber():
    aRandomNumber = randint(1, 20)
    print(aRandomNumber)
    guess_count = 0
    while guess_count  < 3:
        guess = input("Guess a number between 1 and 20 (inclusive): ")
        guess_count += 1
        if not guess.isnumeric():
            print("That's not a positive whole number, try again!")
        else:
            guess = int(guess)
            if aRandomNumber == guess:
                print("You won! Good for you. You guessed a number. It's not like you helped create world peace, but sure, you guessed a number.")
                break
            if aRandomNumber != guess:
                print("Sorry you lost! HAHAHAHAHA")
                continue



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
