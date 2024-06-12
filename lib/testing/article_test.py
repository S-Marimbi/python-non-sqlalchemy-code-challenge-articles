#from author import Author
#from magazine import Magazine
#

class Article():
    def __init__(self, author, magazine, title):
        self._author = author  # Author instance
        self._magazine = magazine  # Magazine instance
        self._title = None
        self.title = title  # This will invoke the title property setter
        
        author.add_article(self)
        author.add_magazine(magazine)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if self._title is not None:
            raise AttributeError("Cannot change the title after it is set")
        if not isinstance(value, str):
            raise TypeError("Title must be of type str")
        if not (5 <= len(value) <= 50):
            raise ValueError("Title must be between 5 and 50 characters, inclusive")
        self._title = value

    @property
    def author(self):
        return self._author
    
    @property
    def magazine(self):
        return self._magazine
