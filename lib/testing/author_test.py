import pytest

class TestAuthor:

    def test_name_is_immutable_string(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert isinstance(author_2.name, str)

        # Testing immutability of the name attribute
        with pytest.raises(AttributeError):  # Assuming setting name raises AttributeError
            author_1.name = "ActuallyTopher"

        assert author_1.name == "Carry Bradshaw"

        with pytest.raises(AttributeError):  # Assuming setting name raises AttributeError
            author_2.name = 2

        assert author_2.name == "Nathaniel Hawthorne"

        # Testing invalid name assignment on initialization
        with pytest.raises(ValueError):  # Replace ValueError with the specific exception your class raises
            Author(2)

    def test_name_len(self):
        """author name is longer than 0 characters"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert len(author_1.name) > 0
        assert len(author_2.name) > 0

        # Testing invalid name length on initialization
        with pytest.raises(ValueError):  # Replace ValueError with the specific exception your class raises
            Author("")

    def test_has_many_articles(self):
        """author has many articles"""
        # Initialize with sample data if required
        pass

# Assuming the class definitions for Author and other dependencies are available
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

# Sample code for running the tests
if __name__ == "__main__":
    pytest.main()