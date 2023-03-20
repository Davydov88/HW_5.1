from abc import ABC, abstractmethod

class Storage(ABC):
    """
    Абстрактный класс для хранения товаров на складе.
    """
    def __init__(self, capacity):
        """
        Инициализирует склад с заданной вместимостью.

        Args:
            capacity (int): Вместимость склада.
        """
        self.items = {}
        self.capacity = capacity

    @abstractmethod
    def add(self, name, quantity):
        """
        Увеличивает запас товара на складе.

        Args:
            name (str): Название товара.
            quantity (int): Количество товара.

        Raises:
            NotImplementedError: Этот метод должен быть реализован в дочернем классе.
        """
        pass

    @abstractmethod
    def remove(self, name, quantity):
        """
        Уменьшает запас товара на складе.

        Args:
            name (str): Название товара.
            quantity (int): Количество товара.

        Raises:
            NotImplementedError: Этот метод должен быть реализован в дочернем классе.
        """
        pass

    @abstractmethod
    def get_free_space(self):
        """
        Возвращает количество свободных мест на складе.

        Returns:
            int: Количество свободных мест.
        """
        return self.capacity - sum(self.items.values())

    @abstractmethod
    def get_items(self):
        """
        Возвращает содержимое склада в словаре {товар: количество}.

        Returns:
            dict: Содержимое склада.
        """
        return self.items

    @abstractmethod
    def get_unique_items_count(self):
        """
        Возвращает количество уникальных товаров на складе.

        Returns:
            int: Количество уникальных товаров.
        """
        return len(self.items)


class Store(Storage):
   """
   Класс для хранения товаров на складе.
   """

   def __init__(self, capacity=100):
      """
      Инициализирует склад с заданной вместимостью.

      Args:
          capacity (int): Вместимость склада. По умолчанию 100.
      """
      super().__init__(capacity)

   def add(self, name, quantity):
      """
      Увеличивает запас товара на складе с учетом лимита capacity.

      Args:
          name (str): Название товара.
          quantity (int): Количество товара.

      Raises:
          ValueError: Если добавление товара приводит к переполнению склада.
      """
      free_space = self.get_free_space()
      if quantity > free_space:
         raise ValueError("Adding this quantity of item will exceed the storage capacity.")
      if name in self.items:
         self.items[name] += quantity
      else:
         self.items[name] = quantity

   def remove(self, name, quantity):
      """
      Уменьшает запас товара на складе, но не ниже 0.

      Args:
          name (str): Название товара.
          quantity (int): Количество товара.
      """
      if name in self.items:
         self.items[name] = max(0, self.items[name] - quantity)

   def get_free_space(self):
      """
      Возвращает количество свободных мест на складе.

      Returns:
          int: Количество свободных мест.
      """
      return self.capacity - sum(self.items.values())

   def get_items(self):
      """
      Возвращает содержимое склада в словаре {товар: количество}.

      Returns:
          dict: Содержимое склада.
      """
      return self.items

   def get_unique_items_count(self):
      """
      Возвращает количество уникальных товаров на складе.

      Returns:
          int: Количество уникальных товаров.
      """
      return len(self.items)


class Shop(Storage):
   """
   Класс для хранения товаров в магазине.
   """

   def __init__(self, capacity=20):
      """
      Инициализирует магазин с заданной вместимостью.

      Args:
          capacity (int): Вместимость магазина. По умолчанию 20.
      """
      super().__init__(capacity)
      self.items = {}

   def add(self, name, quantity):
      """
      Увеличивает запас товара в магазине с учетом лимита capacity и максимального количества уникальных товаров (5).

      Args:
          name (str): Название товара.
          quantity (int): Количество товара.

      Raises:
          ValueError: Если добавление товара приводит к переполнению магазина или превышает максимальное количество уникальных товаров.
      """
      free_space = self.get_free_space()
      unique_items_count = self.get_unique_items_count()

      if unique_items_count >= 5:
         raise ValueError("The maximum number of unique items has been reached.")
      if quantity > free_space:
         raise ValueError("Adding this quantity of item will exceed the storage capacity.")

      if name in self.items:
         self.items[name] += quantity
      else:
         self.items[name] = quantity

   def remove(self, name, quantity):
      """
      Уменьшает запас товара в магазине, но не ниже 0.

      Args:
          name (str): Название товара.
          quantity (int): Количество товара.
      """
      if name in self.items:
         self.items[name] = max(0, self.items[name] - quantity)

   def get_free_space(self):
      """
      Возвращает количество свободных мест в магазине.

      Returns:
          int: Количество свободных мест.
      """
      return self.capacity - sum(self.items.values())

   def get_items(self):
      """
      Возвращает содержимое магазина в словаре {товар: количество}.

      Returns:
          dict: Содержимое магазина.
      """
      return self.items

   def get_unique_items_count(self):
      """
      Возвращает количество уникальных товаров в магазине.

      Returns:
          int: Количество уникальных товаров.
      """
      return len(self.items)


class Request:
   def __init__(self, user_str):
      data = self.get_data(user_str)
      self.from_ = data[4]
      self.to = data[6]
      self.amount = int(data[1])
      self.product = data[2]

   def get_data(self, user_str):
      return user_str.split(" ")

   def __repr__(self):
      return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'