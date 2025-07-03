from dataclasses import dataclass
from typing import List

@dataclass
class BookDetails:
    """ A dataclass to represent book data """
    title: str = None
    publish_date: str = None
    publishers: List[str] = None
    pages: str = None
    subjects: List[str] = None
    description: str = None
    rating: float = None
    author: str = None