class Publication:
    def __init__(self,name):
        self.name = name

    def print_information(self):
        print(f"Publication {self.name}")

class Book(Publication):
    def __init__(self,name,author,page):
        super().__init__(name)
        self.author = author
        self.page = page

    def print_information(self):
        super().print_information()
        print(f"Book {self.name}'s author is {self.author} and has {self.page} pages\n")

class Magazine(Publication):
    def __init__(self,name,chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f"Magazine {self.name}'s chief editor is {self.chief_editor}\n")
        

book1 = Book("Compartment No. 6","Rosa Liksom", 192)
book1.print_information()

magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
magazine1.print_information()