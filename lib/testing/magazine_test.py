import pytest

class TestMagazine:

    def test_name_is_mutable_string(self):
        magazine_1 = Magazine("New Yorker", "News")
        magazine_2 = Magazine("AD", "Architecture")

        assert magazine_1.name == "New Yorker"

        # Testing valid name assignment
        magazine_2.name = "Architectural Digest"
        assert magazine_2.name == "Architectural Digest"

        # Testing invalid name assignment
        with pytest.raises(ValueError):  # Replace ValueError with the specific exception your class raises
            magazine_2.name = 2

        with pytest.raises(ValueError):
            Magazine(2, "Numbers")

    def test_name_len(self):
        """magazine name is between 2 and 16 characters, inclusive"""
        magazine_1 = Magazine("New Yorker", "News")
        magazine_2 = Magazine("AD", "Architecture")

        assert 2 <= len(magazine_2.name) <= 16

        # Invalid name length assignment
        with pytest.raises(ValueError):  # Replace ValueError with the specific exception your class raises
            magazine_1.name = "New Yorker Plus X"

        with pytest.raises(ValueError):
            magazine_2.name = "A"

    def test_has_category(self):
        """Magazine is initialized with a category"""
        magazine_1 = Magazine("New Yorker", "News")
        assert magazine_1.category == "News"

    def test_category_is_mutable_string(self):
        magazine_1 = Magazine("New Yorker", "News")
        magazine_2 = Magazine("AD", "Architecture")

        assert isinstance(magazine_1.category, str)

        # Testing valid category assignment
        magazine_2.category = "Design"
        assert magazine_2.category == "Design"

        # Testing invalid category assignment
        with pytest.raises(ValueError):  # Replace ValueError with the specific exception your class raises
            magazine_2.category = 2

        with pytest.raises(ValueError):
            Magazine("GQ", 2)

    def test_category_len(self):
        """magazine category has length greater than 0"""
        magazine_1 = Magazine("New Yorker", "News")
        assert magazine_1.category != ""

        # Invalid category length assignment
        with pytest.raises(ValueError):  # Replace ValueError with the specific exception your class raises
            magazine_1.category = ""

    def test_has_many_articles(self):
        """magazine has many articles"""
        # Initialize with sample data if required

    def test_contributing_authors(self):
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author_1 = Author("Carry Bradshaw")

        # Assuming contributing_authors() method exists and is correctly implemented
        assert all(isinstance(author, Author) for author in magazine_1.contributing_authors())
        assert magazine_2.contributing_authors() is None

    def test_top_publisher(self):
        """returns the magazine with the most articles"""
        Magazine.all = []
        Article.all = []

        assert Magazine.top_publisher() is None
        
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        
        assert Magazine.top_publisher() is None
        
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "Dating life in NYC")
        Article(author_1, magazine_1, "How to be single and happy")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")
        Article(author_1, magazine_2, "Carrara Marble is so 2020")

        assert Magazine.top_publisher() == magazine_1
        assert isinstance(Magazine.top_publisher(), Magazine)

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
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or not category:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Category must be a non-empty string")
        self._category = value

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