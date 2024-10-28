class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class UnorderedMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        # A simple hash function using the length of the key
        return len(key) % self.size

    def set(self, key, value):
        i1=0
        a=KeyValuePair(key,value)
        for i in self.buckets:
            if i==[]:
                self.buckets[i1]=([a.key,a.value])
                return
            if i[0]==a.key:
                self.buckets[i1] = ([a.key, a.value])
                return
            i1+=1
        print("buckets заполнен")
        return

    def get(self, key, default=None):
        for i in self.buckets:
            if i==[]:
                return default
            if i[0]==key:
                return [i[0],i[1]]

    def remove(self, key):
        for i in self.buckets:
            if i==[]:
                return False
            if i[0]==key:
                self.buckets.remove([i[0],i[1]])


    def keys(self):
        a = []
        for i in self.buckets:
            if i == []:
                break
            a.append(i[0])
        return a

    def values(self):
        a = []
        for i in self.buckets:
            if i == []:
                break
            a.append(i[1])
        return a

    def items(self):
        a = []
        for i in self.buckets:
            if i == []:
                break
            a.append([i[0],i[1]])
        return a


my_map = UnorderedMap()

my_map.set("name", "John")
my_map.set("age", 25)
my_map.set("city", "Example City")

print("Keys:", my_map.keys())
print("Values:", my_map.values())
print("Items:", my_map.items())

# Accessing values by key
print("Name:", my_map.get("name"))
print("Gender:", my_map.get("gender", "Not specified"))

# Removing a key-value pair
my_map.remove("age")

print("Keys after removing 'age':", my_map.keys())