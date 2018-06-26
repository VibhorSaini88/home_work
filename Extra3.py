class Mathematics:
    print("*********WELCOME YOU*************")
    def menu(self):
        print("**select any Operation for you**")
        print(" 1. for Addition")
        print(" 2. for Subtraction")
        print(" 3. for Multiplication")
        print(" 4. for Division")
        print(" 5. for Power")
        print(" 6. for Factorial")
        print(" 7. for Exit")
    def operation(self, number):
        if number > 6:
            print("Thank You")
            print("EXIT")
        else:
            if number == 1:
                print("addition of two no.")
                i = int(input("enter any no."))
                j = int(input("enter any another no. "))
                add = i + j
                print("sum of Addition:- ", add)
                print("if you are continue or Exit! enter 0, than select any operation from List")
                go = int(input("enter: "))
                obj.menu()
                selected = int(input("select any operation no.: "))
                obj.operation(selected)
            elif number == 2:
                print("subtraction of two no.")
                i = int(input("enter any no."))
                j = int(input("enter any another no. "))
                sub = i - j
                print("sum of Subtraction:- ", sub)
                print("if you are continue or Exit! enter 0, than select any operation from List")
                go = int(input("enter: "))
                obj.menu()
                selected = int(input("select any operation no.: "))
                obj.operation(selected)
            elif number == 3:
                print("multiplicationcation of two no.")
                i = int(input("enter any no."))
                j = int(input("enter any another no. "))
                mul = i * j
                print("sum of Multiplication:- ", mul)
                print("if you are continue or Exit! enter 0, than select any operation from List")
                go = int(input("enter: "))
                obj.menu()
                selected = int(input("select any operation no.: "))
                obj.operation(selected)
            elif number == 4:
                print("devision of two no.")
                i = int(input("enter any no."))
                j = int(input("enter any another no. "))
                dev = i / j
                print("sum of Devision:- ", dev)
                print("if you are continue or Exit! enter 0, than select any operation from List")
                go = int(input("enter: "))
                obj.menu()
                selected = int(input("select any operation no.: "))
                obj.operation(selected)
            elif number == 5:
                print("find out power any no.")
                i = int(input("enter any no. "))
                pow1 = int(input("enter power of %d "%(i)))
                p1 = i ** pow1
                print("sum of power:- ", p1)
                print("if you are continue or Exit! enter 0, than select any operation from List")
                go = int(input("enter: "))
                obj.menu()
                selected = int(input("select any operation no.: "))
                obj.operation(selected)
            else:
                import math
                print("find out Factorial of any no.")
                j = int(input("enter any no. "))
                print("factorial of %d is: "%(j),math.factorial(j))
                print("if you are continue or Exit! enter 0, than select any operation from List")
                go = int(input("enter: "))
                obj.menu()
                selected = int(input("select any operation no.: "))
                obj.operation(selected)

obj = Mathematics()
obj.menu()
selected = int(input("select any operation no.: "))
obj.operation(selected)
