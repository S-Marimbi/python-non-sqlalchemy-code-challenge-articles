import pytest

class TestArticle:

    def test_title_is_immutable_str(self):
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        assert article_1.title == "How to wear a tutu with style"
        assert isinstance(article_1.title, str)

        # Testing immutability of the title attribute
        with pytest.raises(AttributeError):  # Assuming setting title raises AttributeError
            article_1.title = 500

        # Testing invalid title assignment on initialization
        with pytest.raises(ValueError):  # Replace ValueError with the specific exception your class raises
            Article(author, magazine, 500)

    def test_title_is_valid(self):
        """title is between 5 and 50 characters inclusive"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        assert 5 <= len(article_1.title) <= 50

        # Testing invalid titles on initialization
        with pytest.raises(ValueError):  # Replace ValueError with the specific exception your class raises
            Article(author, magazine, "Test")  # Title too short

        with pytest.raises(ValueError):
            Article(author, magazine, "How to wear a tutu with style and walk confidently down the street")  # Title too long

    def test_has_an_author(self):
        """article has an author"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        assert article_1.author == author

# Assuming the class definitions for Author, Magazine, and Article are available
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot modify name")

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(category, str) or not category:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot modify name")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        raise AttributeError("Cannot modify category")

class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters inclusive")
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Cannot modify title")

    @property
    def author(self):
        return self._author

# Sample code for running the tests
if __name__ == "__main__":
    pytest.main()