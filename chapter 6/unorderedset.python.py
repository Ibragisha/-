class UnorderedSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, value):
        return self.buckets.index(value)

    def add(self, value):
        i1=0
        for i in self.buckets:
            if i==[]:
                self.buckets[i1]=(value)
                return
            i1+=1
        print("buckets заполнен")
        return

    def remove(self, value):
        self.buckets.remove(value)

    def contains(self, value):
        if value in self.buckets:return True
        else:return False

    def elements(self):
        a=[]
        for i in self.buckets:
            if i==[]:
                continue
            a.append(i)
        return a

my_set = UnorderedSet()

my_set.add(1)
my_set.add(2)
my_set.add(3)


print("Elements:", my_set.elements())

# Check if a value is in the set
value_to_check = 2
print(f"Is {value_to_check} in the set? {my_set.contains(value_to_check)}")

# Remove a value from the set
value_to_remove = 1
my_set.remove(value_to_remove)

print("Elements after removing 1:", my_set.elements())