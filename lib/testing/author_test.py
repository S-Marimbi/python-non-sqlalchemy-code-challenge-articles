class Author():
    def __init__(self,name):
      if not isinstance(name,str):
         raise TypeError("name must be a string")
      if len(name)==0:
         raise ValueError("name must not be empty")
      self._name=name
      self._articles=[]
      self._magazines=[]

    @property
    def name(self):
        return self._name
    
    @property
    def articles(self):
        return self._articles
    
    @property
    def magazines(self):
        return self._magazines
    
    
    def add_article(self,article):
       
       self._articles.append(article)
    
    def add_magazine(self,magazine):
       
       self._magazines.append(magazine)

