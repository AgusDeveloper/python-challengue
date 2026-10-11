print("-------Class Name")
class Name:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third
 
first = "Educative"
name = Name(first, 'F', "Smith")
first = "is"
name.third = "Interactive"
print(name.first, name.second, name.third)

print("-----for range 5")
for k in range(5):
  print(k)

print("-----Capitalize")
print("edu CATIVE".capitalize())

print("-----Class check")
class Check:
  def __init__(self, count = 0):
    self.__count = count

c1 = Check(2)
c2 = Check(2)
print(id(c1) == id(c2), end = " ")

s1 = "Educative"
s2 = "Educative"
print(id(s1) == id(s2))

print("-----Array")
a = [0, 1, 2, 3, 4]
for a[-1] in a:
  print(a[-1])

print("-----Array")
a = ["a", "B", "C", "D", "E"]
for a[-1] in a:
  print(a[-1])

print("-----Class teste")
class tester:
    def __init__(self, id):
        self.id = str(id)
        id="333"

temp = tester(33)
print(temp.id)

print("-----variable educative")
x = 'educative'
for i in range(len(x)):
    a = x[i].upper()
    print(a, end = "")
print (x)

print("-----educative")
x = "educative"
while i in x:
    print(i, end=" ")