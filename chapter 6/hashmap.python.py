   def _hash(self, key):
        return hash(key) % self.size

    def _rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, key, value):
        hash_value = self._hash(key)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                next_slot = self._rehash(hash_value)
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self._rehash(next_slot)

                self.slots[next_slot] = key
                self.data[next_slot] = value

    def get(self, key, default=None):
        start_slot = self._hash(key)

        data = None
        found = False
        stop = False
        position = start_slot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self._rehash(position)
                if position == start_slot:
                    stop = True

        return data if found else default

    def remove(self, key):
        start_slot = self._hash(key)

        found = False
        stop = False
        position = start_slot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                self.slots[position] = None
                self.data[position] = None
            else:
                position = self._rehash(position)
                if position == start_slot:
                    stop = True

        if not found:
            raise KeyError(f"Key '{key}' not found")

    def keys(self):
        return [key for key in self.slots if key is not None]

    def values(self):
        return [self.data[i] for i in range(self.size) if self.slots[i] is not None]

    def items(self):
        return [(self.slots[i], self.data[i]) for i in range(self.size) if self.slots[i] is not None]

my_hashmap = HashMap()
my_hashmap.put("name", "John")
my_hashmap.put("age", 25)
my_hashmap.put("city", "Example City")
print("Keys:", my_hashmap.keys())  # Ожидаемый вывод: ['name', 'age', 'city']
print("Values:", my_hashmap.values())  # Ожидаемый вывод: ['John', 25, 'Example City']
print("Items:", my_hashmap.items())  # Ожидаемый вывод: [('name', 'John'), ('age', 25), ('city', 'Example City')]

# Доступ к значениям по ключу
print("Name:", my_hashmap.get("name"))  # Ожидаемый вывод: John
print("Gender:", my_hashmap.get("gender", "Not specified"))  # Ожидаемый вывод: Not specified

# Удаление пары ключ-значение
my_hashmap.remove("age")
print("Keys after removing 'age':", my_hashmap.keys())  # Ожидаемый вывод: ['name', 'city']