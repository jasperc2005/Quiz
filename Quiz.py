import sys
from time import sleep

words = "Welcome to ChemistryQuiz(Nothing to do with chemistry but we made it in Chemistry..."
for char in words:
  sleep(0.1)
  sys.stdout.write(char)
  sys.stdout.flush()

question = ("what is a cpu")



def check_guess(guess, answer):
  global score
  if guess == answer:
    print('Correct!')
    score = score + 1
  if guess != answer:
    print('Incorrect!')
    score = score - 1

score = 0
guess1 = input('What is cpu? ')
check_guess(guess1, 'central processing unit')

