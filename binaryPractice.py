import random
import os
import time
import colorama

class BinaryGenerator:
    def __init__(self, n):
        self.bitLength = n
    def __call__(self):
        return self.generatePair()
    def generatePair(self):
        binaryGenerated = random.getrandbits(self.bitLength)
        return binaryGenerated, bin(binaryGenerated).split('b')[1]
    def setBitLength(self, n):
        self.bitLength = n

class GameHandler:
    def __init__(self, numRounds=5) -> None:
        self.numRounds = numRounds
        self.binGen = BinaryGenerator(5)
        self.score = 0

    def __call__(self):
        self.setupGame()
        return self.playGame()
    
    def playGame(self):
        self.score = 0
        for i in range(self.numRounds):
            print(f"Round {i+1}")
            self.playRound()
        print("---Game Over---")
        print(f"Your score is {self.score} out of {self.numRounds}")

    def playRound(self):

        #Clear terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        #Generate binary and get user answer
        
        answer, binary = self.binGen()
        self.printInColor("Binary: ", colorama.Fore.YELLOW, end="")
        binaryWithSpaces = " ".join(binary)
        self.printInColor(binaryWithSpaces, colorama.Fore.BLUE)
        userAnswer = self.getIntAnswer()

        # Check if answer is correct
        if userAnswer == answer:
            #print correct in green
            self.printInColor("Correct", colorama.Fore.GREEN)
            self.score += 1
            time.sleep(1)
        else:
            self.printInColor("Incorrect", colorama.Fore.RED)
            self.printInColor(f"Correct answer is {answer}", colorama.Fore.BLUE)
            self.waitOnEnter()
        

    def printInColor(self, text, color, end="\n"):
        print(f"{color}{text}{colorama.Fore.RESET}", end=end)

    def waitOnEnter(self):
        self.printInColor("Press enter to continue...", colorama.Fore.YELLOW, end="")
        input()
    
    def setupGame(self):
        print("Welcome to the binary game!")
        print("You will be given a binary number and you must convert it to decimal")
        
        self.printInColor("\nHow many rounds would you like to play?", colorama.Fore.YELLOW)
        self.numRounds = self.getIntAnswer()

        #Verify number of rounds is valid
        if self.numRounds <= 0:
            print("Number of rounds must be greater than 0")
            print("Using default of 5")
            self.numRounds = 5
    
        if self.numRounds > 15:
            print("Number of rounds must be less than or equal to 15")
            print("Capping to 15")
            self.numRounds = 15

        self.printInColor("\nHow many bits would you like to use as a maximum?", colorama.Fore.YELLOW)
        self.binGen.setBitLength(self.getIntAnswer())

        if self.binGen.bitLength <= 2:
            print("Number of bits must be greater than 2")
            print("Using default of 4")
            self.binGen.setBitLength(4)

        if self.binGen.bitLength > 12:
            print("Number of bits must be less than 12")
            print("Capping to 12")
            self.binGen.setBitLength(12)
        
        print(f"---Starting Game---")
        time.sleep(1)
        

    def getIntAnswer(self):
        while True:
            try:
                return int(input("Enter the decimal value: "))
            except:
                print("Please enter an integer")
    
if __name__ == "__main__":
    game = GameHandler()
    game()
    while not input("Play again? (y/n): ").lower() == "n":
        game()