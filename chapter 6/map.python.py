class SimpleMap:
    def __init__(self):
        self.items = []

    def set(self, key, value):
        self.items.append([key,value])

    def get(self, key, default=None):
        for i,j in self.items:
            if i==key:
                return j
        return default

    def remove(self, key):
        for i,j in self.items:
            if i==key:
                self.items.remove([i,j])
                return self.items
        return False

    def keys(self):
        a=[]
        for i,j in self.items:
            a.append(i)
        return a

    def values(self):
        a = []
        for i,j in self.items:
            a.append(j)
        return a

    def itemss(self):
        return self.items
# Example usage:
my_map = SimpleMap()

my_map.set("name", "John")
my_map.set("age", 25)
my_map.set("city", "Example City")

print("Keys:", my_map.keys())
print("Values:", my_map.values())
print("Items:", my_map.itemss())

# Accessing values by key
print("Name:", my_map.get("name"))
print("Gender:", my_map.get("gender", "Not specified"))

# Removing a key-value pair
my_map.remove("age")

print("Keys after removing 'age':", my_map.keys())