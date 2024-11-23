import su,sub,mul,div,fdiv,mdiv,exe

s = """" 
 Arithmetic Operation 
 ====================
    I. Addition
    2. Substraction
    3. Multiplication
    4. Division
    5. floar Division
    6. Modulo Division
    7. Exponentiation
    8. Exit
 =======================    
    Enter Ur Choice : """

while True:
    print(s)
    option = input()
    match (option):
        case "1":
            print("Enter two Number for Addition Operation : ")
            a, b = int(input()), int(input())
            print("Sum{} + {} : {}".format(a, b, su.findsum(a, b)))
        case "2":
            print("Enter two Number for Subtraction Operation : ")
            a, b = int(input()), int(input())
            print("Sub{} - {} : {}".format(a, b, sub.findsub(a, b)))
        case "3":
            print("Enter two Number for Multiplication Operation : ")
            a, b = int(input()), int(input())
            print("Mul{} x {} : {}".format(a, b, mul.findmul(a, b)))
        case "4":
            print("Enter two Number for Division Operation : ")
            a, b = int(input()), int(input())
            print("Div{} + {} / {}".format(a, b, div.finddiv(a, b)))
        case "5":
            print("Enter two Number for floor div Operation : ")
            a, b = int(input()), int(input())
            print("Floar Div{} // {} : {}".format(a, b, fdiv.findfdiv(a, b)))
        case "6":
            print("Enter two Number for Mudulo divsion Operation : ")
            a, b = int(input()), int(input())
            print("Madulo div{} % {} : {}".format(a, b, mdiv.findmdiv(a, b)))
        case "7":
            print("Enter two Number for Exponentiation Operation : ")
            a, b = int(input()), int(input())
            print("Exponentiation{}**{} : {}".format(a, b, exe.findexe(a, b)))
        case "8":
            print("Thank you for using this program")
            break
        case _:
            print("Invailid Choise ")
