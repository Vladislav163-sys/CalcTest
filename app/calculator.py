class Calculator:
   def multiply(self, x, y):
       return x * y

   def division(self, x, y):
       if y == 0:
           raise ValueError("Деление на ноль невозможно!")
       return x / y

   def subtraction(self, x, y):
       return x - y

   def add(self, x, y):
       return x + y