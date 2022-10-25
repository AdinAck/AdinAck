from dataclasses import dataclass
from rich import print
from rich.text import Text
import requests
from random import randint

@dataclass
class RankedLetter:
    """
    A simple type encapsulating a letter and its rank.
    
    Rank key:
    0 -> No occurance
    1 -> Some occurance
    2 -> Matched position
    
    Attributes
    ----------
    letter: str
        The letter (A-Z)
    rank: int
        The rank of the letter (0-2)
    """
    
    letter: str
    rank: int
    
    @property
    def text(self) -> Text:
        """
        The rich text representation of the letter and its rank.
        
        Returns
        -------
        Text
        """
        
        text = Text(self.letter.upper())
        text.stylize('grey' if self.rank == 0 else 'yellow' if self.rank == 1 else 'green')
        
        return text

class Wordle:
    """
    The Wordle environment. Provides the Wordle game board, helper functions, etc.
    
    Attributes
    ----------
    WORD_LENGTH: int
        The word length of the board.
    GUESS_COUNT: int
        The number of guesses of the board.
    target: str
        The target word to be guessed.
    grid: list[list[RankedLetter]]
        The wordle grid.
    """
    
    WORD_LENGTH: int
    GUESS_COUNT: int
    target: str
    grid: list[list[RankedLetter]]
    
    def __init__(self, WORD_LENGTH: int = 5, GUESS_COUNT: int = 6):
        """
        Constructor for Wordle object.
        
        Parameters
        ----------
        WORD_LENGTH: int
            The word length of the board.
        GUESS_COUNT: int
            The number of guesses of the board.
        """
        
        self.WORD_LENGTH, self.GUESS_COUNT = WORD_LENGTH, GUESS_COUNT
        
        self.target = ''
        self.grid = []
        
        # download words
        self.words = [
            word.lower()
            for word in requests.get(
                'http://www.mieliestronk.com/corncob_caps.txt'
            ).text.split('\r\n')
        ]
        
    def guess(self, word: str) -> None:
        """
        Ingest a guess and update the Wordle game.
        
        Parameters
        ----------
        word: str
            The guess to be made.
        """
        
        self.grid.append([
            RankedLetter(c1, 
                2 if c1 == c2 else # matched position
                0 if c1 not in self.target or self.freq(word[:i + 1])[c1] > self.freq(self.target)[c1] else # no occurance or filled occurances
                1 # remaining occurances
            )
            for i, (c1, c2) in enumerate(zip(word, self.target))
        ])
    
    @property
    def text(self) -> Text:
        """
        The rich text representation of the Wordle game board.
        
        Returns
        -------
        Text
        """
        
        r = Text()
        
        for row in self.grid:
            for letter in row:
                r += letter.text + ' '
            
            r += '\n'
        
        for _ in range(self.GUESS_COUNT - len(self.grid)):
            r += '- ' * self.WORD_LENGTH + '\n'
            
        return r
    
    def run(self) -> None:
        """
        The main game loop.
        """
        
        # get target word
        while len(target := self.words[randint(0, len(self.words) - 1)]) != self.WORD_LENGTH:
            pass
        
        # set target word
        self.target = target
        
        # handle each guess
        for i in range(self.GUESS_COUNT):
            print(self.text)
            
            # capture guess from user
            while not self.is_valid(guess := input('Guess: ')):
                print('Invalid guess.')
            
            # ingest guess
            self.guess(guess.lower())
            
            # check if guess is correct
            if guess.lower() == self.target:
                print(self.text)
                print(f'You won in {i + 1} guesses!')
                break
        else:
            # user ran out of guesses
            print(self.text)
            print(f'You lose!, the word was {self.target.upper()}.')

    @staticmethod
    def freq(word: str) -> dict[str, int]:
        """
        Create a frequency dictionary of the letters in the given word.
        
        Parameters
        ----------
        word: str
            The word to be analyzed.
        
        Returns
        -------
        dict[str, int]
            For each unique character in the word, the frequency of the character.
        """
        
        return {char: word.count(char) for char in word}

    def is_valid(self, word: str) -> bool:
        """
        Check if a word is a valid word for the game.
        
        Parameters
        ----------
        word: str
            The word to be checked.
        
        Returns
        -------
        bool
            `True` if the word is valid else `False`.
        """
        
        return len(word) == self.WORD_LENGTH and word.lower() in self.words
            
if __name__ == '__main__':
    game = Wordle()
    game.run()