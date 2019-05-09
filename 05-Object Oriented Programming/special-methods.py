# Special methods give us the ability to use python built-ins (len, print) with our own classes
# also called magic or "dunder" methods because they use a double underscore (like __init__)

mylist = [1, 2, 3]

len(mylist)

class Sample:
    pass

sample = Sample()
# Initially we get
# TypeError: object of type 'Sample' has no len()
# So we must have to tell python what to do when len is called on Sample
len(sample)


class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

        
    def __str__(self):
        return f"{self.title} by {self.author}"


    def __len__(self):
        return self.pages

    # If I ever delete a book, I might want special things to happen
    # So I can define this dunder/special method
    def __del__(self):
        # Only side effect, can't actually return things I think
        print(f"Goodbye {self.title}") 


hp = Book("Harry Potter", "J.K. Rowling", 250)

# print() use the str() to send the str representation of the object to the console
# so if we define __str__ then when we call print(book), python knows how to represent it
print(hp)
# Same goes for __len__
len(hp)
# delete a variable from my computer's memory
del hp