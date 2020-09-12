from random import randint
while True:
  print("""\nwelcome to my game friends. in this game.. victory is depends on the range that you provide for the characters (the larger you provide the scale of range, probability of winning of that character will increase) and remember that you have to enter power in integers or else you have to run the code again!!\n""")

  try:
    class Game(object):
      def __init__(self,name,password):
        self.name=name
        self.password=password
    
      def impl(self):
        return f"your name is {self.name} and your password is {len(self.password)*'*'}"

    class Actual(Game):
      def __init__(self,char_name,power):
        self.char_name=char_name
        self.power=power

      def run(self):
        return f'\ncharacter\'s name is     {self.char_name} and power is {self.power}'

    s1=input("enter name: ")
    s2=input("enter password: ")
    a1=Game(s1,s2)
    print(a1.impl())

    x1=input("\nenter character 1\'s name: ")
    e1=int(input('(for char 1) start of power(enter in numbers): '))
    e2=int(input('(for char 1) end of power(enter in numbers): '))
    x2=randint(e1,e2)
    y1=input("enter character 2\'s name: ")
    f1=int(input('(for char 2) start of power(enter in numbers): '))
    f2=int(input('(for char 2) end of power(enter in numbers): '))
    y2=randint(f1,f2)
    z1=Actual(x1,x2)
    z2=Actual(y1,y2)

    for i in [z1,z2]:
      print(i.run())

    if x2==y2:
      print(f'\ntied')
    elif x2>y2:
      print(f'\n{x1} is won')
    else:
      print(f'\n{y1} is won')
    break

  except:
    print("wrong inputs!! please run the code again and give proper inputs for powers of the character(it must be in integer)")