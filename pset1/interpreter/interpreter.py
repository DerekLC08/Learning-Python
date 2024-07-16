n1, o, n2 = input("Expression: ").split(" ")
x = float(n1)
y = float(n2)

match o:
  case "+" :
     print(x + y)
  case "-" :
     print(x - y)
  case "*" :
     print(x * y)
  case "/" :
     print(x / y)
  case _ :
     print("Invalid operator")