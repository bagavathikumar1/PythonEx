class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print("Print items one by one using Iterater")
print(next(myit))
print(next(myit))
print(next(myit))

print("Print items using Iterater with For loop")
for x in mytuple:
  print(x)

#Strings are also iterable objects, containing a sequence of characters.
mystr = "banana"

for x in mystr:
  print(x)
  
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)