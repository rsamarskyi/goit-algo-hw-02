from collections import deque


def is_palindrome(text: str) -> bool:
    """Перевіряє, чи є рядок паліндромом (без урахування регістру та пробілів)."""
    # Додаємо символи в deque: приводимо до нижнього регістру, пропускаємо пробіли
    dq = deque(ch for ch in text.casefold() if not ch.isspace())

    # Порівнюємо символи з обох кінців, поки лишається більше одного елемента
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


if __name__ == "__main__":
    tests = [
        ("radar", True),                  # непарна кількість символів
        ("abba", True),                   # парна кількість символів
        ("A man a plan a canal Panama", True),  # регістр + пробіли
        ("Never odd or even", True),
        ("hello", False),
        ("ab", False),
        ("a", True),                      # один символ
        ("", True),                       # порожній рядок
    ]
    for s, expected in tests:
        result = is_palindrome(s)
        print(f"{s!r:35} -> {result} {'OK' if result == expected else 'FAIL'}")