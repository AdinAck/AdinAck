from dataclasses import dataclass
from rich.text import Text

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