class Mathematics:
    print("WELCOME YOU")
    def operation(self, number):
        if number > 6:
            print("out of no.")
            print("EXIT")
            print("Thank You")
        else:
            i = int(input("enter any no."))
            j = int(input("enter any another no. "))
            if number == 1:
                print("addition of two no.")
                add = i + j
                print("sum is:- ", add)
                print("if you are continue than enter 0  else  enter! two time greater than 6 ")
                go = int(input("enter: "))
                number = int(input("enter 1.for addition or 2 for subtraction or 3 for multiplication or 4 for devision or 5 for power or 6 for factorial or 7 for exit: "))
                self.operation(number)
            elif number == 2:
                print("subtraction of two no.")
                sub = i - j
                print("sum is:- ", sub)
                print("if you are continue than enter 0 else  enter! two time greater than 6  ")
                go = int(input("enter: "))
                number = int(input("enter 1.for addition or 2 for subtraction or 3 for multiplication  or 4 for devision or 5 for power or 6 for facto: "))
                self.operation(number)
            elif number == 3:
                print("multiplicationcation of two no.")
                mul = i * j
                print("sum is:- ", mul)
                print("if you are continue than enter 0  else  enter! two time greater than 6 ")
                go = int(input("enter: "))
                number = int(input("enter 1.for addition or 2 for subtraction or 3 for multiplication or 4 for devision or 5 for power or 6 for factorial or 7 for exit: "))
                self.operation(number)
            elif number == 4:
                print("devision of two no.")
                dev = i / j
                print("sum is:- ", dev)
                print("if you are continue than enter 0  else  enter! two time greater than 6 ")
                go = int(input("enter: "))
                number = int(input("enter 1.for addition or 2 for subtraction or 3 for multiplication or 4 for devision or 5 for power or 6 for factorial or 7 for exit: "))
                self.operation(number)
            elif number == 5:
                pow1 = int(input("enter power of %d "%(i)))
                pow2 = int(input("enter power of %d "%(j)))
                p1 = i ** pow1
                p2 = j ** pow2
                print("sum is:- ", p1)
                print("sum is:- ", p2)
                print("if you are continue than enter 0  else  enter! two time greater than 6 ")
                go = int(input("enter: "))
                number = int(input("enter 1.for addition or 2 for subtraction or 3 for multiplication or 4 for devision or 5 for power or 6 for factorial or 7 for exit: "))
                self.operation(number)
            else:
                import math
                print("factorial of %d: "%(i),math.factorial(i))
                print("factorial of %d: "%(j),math.factorial(j))
                print("if you are continue than enter 0  else  enter! two time greater than 6 ")
                go = int(input("enter: "))
                number = int(input("enter 1.for addition or 2 for subtraction or 3 for multiplication or 4 for devision or 5 for power or 6 for factorial or 7 for exit: "))
                self.operation(number)


number = int(input("enter 1.for addition or 2 for subtraction or 3 for multiplication or 4 for devision or 5 for power or 6 for factorial or 7 for exit: "))
obj = Mathematics()
obj.operation(number)