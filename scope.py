def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    #global x
    x = "hello"
    
  myfunc2()
  return x

print(myfunc1())


x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)