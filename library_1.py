class Item():
    def __init__(self,*args,**kwargs) -> None:
        self.Title = "The last of us"
        self.publication = 2058
    def get_info(self):
        return self.Title,self.publication
class Book(Item()):
    def __init__(self,*args,**kwargs):
        self.author = "Hemant"
        self.ISBN = "1234"
    def get_info(self,*args,*kwargs)