import pickle

class Contact:
    def __init__(self, name, phone, email=""):
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"Contact(name={self.name}, phone={self.phone}, email={self.email})"


class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def find_contact(self, name):
        return self.contacts.get(name)

    def __repr__(self):
        return "\n".join(str(contact) for contact in self.contacts.values())


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  


def main():
    print("Завантаження адресної книги...")
    book = load_data()  
    print("Адресна книга успішно завантажена.")

    while True:
        print("\nМеню:")
        print("1. Додати контакт")
        print("2. Видалити контакт")
        print("3. Знайти контакт")
        print("4. Показати всі контакти")
        print("5. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            email = input("Email (необов'язково): ")
            contact = Contact(name, phone, email)
            book.add_contact(contact)
            print("Контакт додано.")

        elif choice == "2":
            name = input("Введіть ім'я контакту, який потрібно видалити: ")
            if book.find_contact(name):
                book.remove_contact(name)
                print("Контакт видалено.")
            else:
                print("Контакт не знайдено.")

        elif choice == "3":
            name = input("Введіть ім'я для пошуку: ")
            contact = book.find_contact(name)
            if contact:
                print(f"Знайдено: {contact}")
            else:
                print("Контакт не знайдено.")

        elif choice == "4":
            print("Всі контакти:")
            print(book if book.contacts else "Адресна книга порожня.")

        elif choice == "5":
            print("Збереження адресної книги...")
            save_data(book)  
            print("Дані успішно збережено. До побачення!")
            break

        else:
            print("Невірна опція. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
    