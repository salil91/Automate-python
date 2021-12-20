#! python3
# mult_test.py - A timed multiplication test.


import pyinputplus as pyip
import random
import time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # Pick two random numbers
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    prompt = f'Question #{questionNumber+1}: {num1} x {num2} = '
    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=7, limit=2)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1

    # time.sleep(1)  # Brief pause to let user see the result.

print(f'\nScore: {correctAnswers} / {numberOfQuestions}')
