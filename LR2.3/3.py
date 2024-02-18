class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, pages: int):
        self.pages = pages

    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом.")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга {self._name}. Автор {self._author}"


class AudioBook(Book):
    def __init__(self, duration: float):
        self.duration = duration

    def duration(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise ValueError("Продолжительность должна быть числом.")
        self._duration = value

    def __str__(self):
        return f"Аудио книга {self._name}. Автор {self._author}"


