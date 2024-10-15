def add_book(book_name):
    with open('input.txt', 'a') as file:
        file.write(book_name + 'n')
    print(f'Книга "{book_name}" добавлена.')

def list_books():
    try:
        with open('input.txt', 'r') as file:
            books = file.readlines()
            if books:
                print("Список книг:")
                for book in books:
                    print(book.strip())
            else:
                print("Список книг пуст.")
    except FileNotFoundError:
        print("Файл с книгами не найден.")

def remove_book(book_name):
    try:
        with open('input.txt', 'r') as file:
            books = file.readlines()
        
        with open('input.txt', 'w') as file:
            found = False
            for book in books:
                if book.strip() != book_name:
                    file.write(book)
                else:
                    found = True
            if found:
                print(f'Книга "{book_name}" удалена.')
            else:
                print(f'Книга "{book_name}" не найдена.')
    except FileNotFoundError:
        print("Файл с книгами не найден.")

def main():
    while True:
        print("n1. Добавить книгу")
        print("2. Показать список книг")
        print("3. Удалить книгу")
        print("4. Выход")
        
        choice = input("Выберите действие (1-4): ")
        
        if choice == '1':
            book_name = input("Введите название книги: ")
            add_book(book_name)
        elif choice == '2':
            list_books()
        elif choice == '3':
            book_name = input("Введите название книги для удаления: ")
            remove_book(book_name)
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
