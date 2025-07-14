def greet(to="Stranger"):
    print(f"Hello, {to}!")
def user_name():
    name=input(" What's Your Name ?").strip().title()
    first, last=name.split(" ")
    print(f"Hello {name} , may I call you {first} ?")
    print(f"{first}, welcome to the calculator!")
    return first
def cal():
    p=input(f"what do you want to do press + for sum, - substraction, / divison,* multiplication and p for power !")
    print(f"lets do {p}")
    return p
def add():
    print(f"lets do addition first.!")
    a=float(input(" Enter the first number: "))
    b=float(input(" Enter the second number: "))
    c=a+b
    print(f"Sum of {a} and {b} is : {round(c,2)}")
def minus():
    print(f" lets do Substraction!")
    d=float(input(" Enter the first number: "))
    e=float(input(" Enter the second number: "))
    f=d-e
    print(f"Difference  of {d} and {e} is : {round(f,2)}")
def multi():
    print(f"lets do Multiplication!")
    g=float(input(" Enter the first number: "))
    h=float(input(" Enter the second number: "))
    i=g*h
    print(f"Muliplication of {g} and {h} is : {round(i,2)}")
def div():
    print(f" lets do Division!")
    j=float(input(" Enter the first number: "))
    k=float(input(" Enter the second number: "))
    l=j/k
    print(f"Division of {j} and {k} is : {round(l,2)}")
def power():
    print(f"lets do Power!")
    m=float(input(" Enter the Number of which you want power of: "))
    n=float(input(" Enter the Power Factor: "))
    o=pow(m,n)
    print(f"Power of {m} by factor of {n}is : {round(o,2)}")
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
    else:
        print("Invalid operation selected.")
main()

