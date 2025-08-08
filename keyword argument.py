def book_info(title, author, year):
    print(f"Title: {title}, Author: {author}, Year: {year}")

# Calling with keyword arguments in different orders
book_info(author="George Orwell", title="1984", year=1949)
book_info(year=2005, title="Harry Potter", author="J.K. Rowling")
