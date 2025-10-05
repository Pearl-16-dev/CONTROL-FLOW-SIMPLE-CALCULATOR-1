operator = input("Select an operator(+ * / -): ")
num_1 = int(input("Input your first number: "))
num_2 = int(input("Input your second number: "))
if operator== "+":
    result = num_1 + num_2
    print(result)
elif operator== "-":
    result = num_1 - num_2
    print(result)
elif operator== "*":
    result = num_1 * num_2
    print(result)
elif operator== "/":
    result = num_1 / num_2
    print(result)
else:
    print(f"Invalid operator")