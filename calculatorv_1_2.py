print("""
┌───────────────────────────────────────────────┐
│             PYTHON CALCULATOR v1.2            │
├───────────────────────────────────────────────┤
│  Welcome, Operator.                           │
│  Your terminal is now your canvas.            │
│  Crunch numbers. Break limits.                │
│  Precision meets performance.                 │
├───────────────────────────────────────────────┤
│  Type 'help' to see available operations.     │
│  Press Ctrl+C or type 'exit' to quit.         │
└───────────────────────────────────────────────┘
""")
def greet(to="Stranger"):
    print(f"Hello, {to}!")
def user_name():
    name=input(" What's Your Name ? : ").strip().title()
    first = name.split(" ")[0]
    print(f"Hello {name} , may I call you {first} ?")
    print(f"{first}, welcome to the calculator!")
    return first
def cal():
    p=input(f"""Available Operations:
+  → Addition
-  → Subtraction
*  → Multiplication
/  → Division
p  → Power
c  → Check Odd/Even 
            Please select an operation: """).strip().lower()
    return p
def add():
    print(f"lets do addition first.!")
    a=float(input(" Enter the first number: "))
    b=float(input(" Enter the second number: "))
    while True:
        if a.is_integer() and b.is_integer():
            a = int(a)
            b = int(b)
            break
        else:
            print("Please enter valid numbers.")
            a = float(input(" Enter the first number: "))
            b = float(input(" Enter the second number: "))
    c=a+b
    print(f"Sum of {a} and {b} is : {round(c,2)}")
def minus():
    print(f" lets do Substraction!")
    d=float(input(" Enter the first number: "))
    e=float(input(" Enter the second number: "))
    while True:
        if d.is_integer() and e.is_integer():
            d = int(d)
            e = int(e)
            break
        else:
            print("Please enter valid numbers.")
            d = float(input(" Enter the first number: "))
            e = float(input(" Enter the second number: "))
    f=d-e
    print(f"Difference  of {d} and {e} is : {round(f,2)}")
def multi():
    print(f"lets do Multiplication!")
    g=float(input(" Enter the first number: "))
    h=float(input(" Enter the second number: "))
    while True:
        if g.is_integer() and h.is_integer():
            g = int(g)
            h = int(h)
            break
        else:
            print("Please enter valid numbers.")
            g = float(input(" Enter the first number: "))
            h = float(input(" Enter the second number: "))
    i=g*h
    print(f"Muliplication of {g} and {h} is : {round(i,2)}")
def div():
    print(f" lets do Division!")
    j=float(input(" Enter the first number: "))
    k=float(input(" Enter the second number: "))
    while True:
        if j.is_integer() and k.is_integer() and k != 0:
            j = int(j)
            k = int(k)
            break
        elif k == 0:
            print("Division by zero is not allowed. Please enter a valid second number.")
            k = float(input(" Enter the second number: "))
        else:
            print("Please enter valid numbers.")
            j = float(input(" Enter the first number: "))
            k = float(input(" Enter the second number: "))
    l=j/k
    print(f"Division of {j} and {k} is : {round(l,2)}")
def power():
    print(f"lets do Power!")
    m=float(input(" Enter the Number of which you want power of: "))
    n=float(input(" Enter the Power Factor: "))
    while True:
        if m.is_integer() and n.is_integer():
            m = int(m)
            n = int(n)
            break
        else:
            print("Please enter valid numbers.")
            m = float(input(" Enter the Number of which you want power of: "))
            n = float(input(" Enter the Power Factor: "))
    o=pow(m,n)
    print(f"Power of {m} by factor of {n}is : {round(o,2)}")
def check():
    print(f"lets check number is odd or even !")
    p=float(input(" Enter the Number of which you want to check: "))
    while True:
        if p>= 0:
            break
        else:
            print("Please enter a valid number.")
            p = float(input(" Enter the Number of which you want to check: "))
    print(f" The number {p} even !") if p % 2 == 0 else print(f" The number {p} is odd !")
def main():
    greet()
    user_name()
    op = cal()
    if op == "+":
        add()
    elif op == "-":
        minus()
    elif op == "*":
        multi()
    elif op == "/":
        div()
    elif op == "p":
        power()
    elif op == "c":
        check()
    else:
        print("Invalid operation selected.")
main()

