from chapterCalls import Book



mockingbird = Book()
for prop, value in mockingbird.__dict__.items():
    print(f'{prop}:\n{value}\n') 