from rich import print
from rich.text import Text
import requests
from random import randint

from ranked_letter import RankedLetter
from wordle import Wordle

class AdinWordle:
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
    words: list[str]
    
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
                'https://www.mit.edu/~ecprice/wordlist.10000'
            ).text.split('\n')
            if len(word) == self.WORD_LENGTH
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
                0 if c1 not in self.target
                or word[:i + 1].count(c1) > self.target.count(c1)
                else # no occurance or filled occurances
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
        
        # set target word
        self.target = self.words[randint(0, len(self.words) - 1)]
        
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
        
        return word.lower() in self.words

class AdinWordleAdapter(Wordle):
    inner: AdinWordle
    last_guess: str
    
    def __init__(self, WORD_LENGTH: int, GUESS_COUNT: int):
        self.inner = AdinWordle(WORD_LENGTH, GUESS_COUNT)
        
    def guess(self, word: str) -> bool:
        if not self.inner.is_valid(word):
            return False
        
        self.inner.guess(word)
        self.last_guess = word
        
        return True
    
    def get_state(self) -> tuple[list[list[RankedLetter]], bool]:
        return self.inner.grid, self.inner.target == self.last_guess

if __name__ == '__main__':
    game = AdinWordle(3, 4)
    game.run()