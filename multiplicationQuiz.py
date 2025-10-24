import pyinputplus as pyip
import random, time



def main():
    numberOfQuestions = input("Set Quiz Line items : ")
    correctAnswers = 0
    
    for questionNumber in range(int(numberOfQuestions)):
        multiplicand= random.randint(0, 9)
        multiplyer=random.randint(0, 9)
        prompt = f"Question#{questionNumber+1}: {multiplicand} * {multiplyer} = "
        try:
            answer = pyip.inputInt(animate(prompt), allowRegexes=[f"^{multiplicand * multiplyer}$"], timeout=3, limit=3)
            print(f"Your answer: {answer} and the correct answer is: {multiplicand * multiplyer}")
            if answer == multiplicand * multiplyer:
                print("Correct!")
                correctAnswers += 1
            else:
                print("Incorrect!")
        except pyip.TimeoutException:
            print("Ang Tagal Nangongopya ka pa kasi!")
        except pyip.RetryLimitException:
            print("Better luck next question!")

        time.sleep(1)
    print("Score: %s / %s" % (correctAnswers, numberOfQuestions))

def animate(prompt, delay=0.1):
    for char in prompt:
        print(char, end='', flush=True)
        time.sleep(delay)
    return ""
    
    


if __name__ == "__main__":
    main()