class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = None
        self._magazine = None
        self._title = None

        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("Author must be of type Author")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError("Magazine must be of type Magazine")

class Author:
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    def articles(self):
        pass
        return [article for article in Article.all if hasattr(article, 'author') and article.author == self]

    def magazines(self):
        pass
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        pass
        return Article(self, magazine, title)

    def topic_areas(self):
        pass
        if not self.articles():
            return None
        return list(set(article.magazine.category for article in self.articles()))

class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be a string with 2 to 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string")

    def articles(self):
        pass
        return [article for article in Article.all if hasattr(article, 'magazine') and article.magazine == self]

    def contributors(self):
        pass
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        pass
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        pass
        from collections import Counter
        author_count = Counter(article.author for article in self.articles())
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        if not hasattr(Article, 'all') or not Article.all:
            return None
        return max(cls.all_magazines, key=lambda magazine: len(magazine.articles()))