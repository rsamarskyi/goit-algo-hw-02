from queue import Queue
from itertools import count

# Черга заявок
request_queue = Queue()

# Генератор унікальних номерів: 1, 2, 3, ...
request_numbers = count(start=1)


def generate_request():
    """Створює нову заявку та додає її до черги."""
    request_id = next(request_numbers)
    request_queue.put(request_id)
    print(f"Створено та додано до черги заявку №{request_id}")


def process_request():
    """Видаляє найстарішу заявку з черги та імітує її обробку."""
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Обробляється заявка №{request_id}")
        print(f"Заявку №{request_id} оброблено")
        request_queue.task_done()
    else:
        print("Черга заявок пуста.")


def main():
    print("Система обробки заявок")
    print("Натисніть Enter для наступного циклу або введіть q для виходу.")

    while True:
        generate_request()
        process_request()

        command = input("\nEnter — продовжити, q — вийти: ").strip().lower()
        if command == "q":
            print("Роботу програми завершено.")
            break


if __name__ == "__main__":
    main()