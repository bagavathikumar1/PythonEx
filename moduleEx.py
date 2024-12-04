import platform
import mymodule
from mymodule import person1
import mymodule as mx

mymodule.greeting("Jonathan")
print (person1["age"])

a = mx.person1["age"]
print(a)

x = platform.system()
print(x)

x = dir(platform)
print(x)