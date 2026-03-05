text = input("Enter text: ").replace(" ", "")
key = int(input("Enter number of columns: "))
choice = input("Enter E for Encryption or D: ").lower()

result = ""

if choice == 'e':
    for i in range(key):
        for j in range(i, len(text), key):
            result += text[j]

elif choice == 'd':
    rows = len(text) // key
    index = 0
    matrix = [""] * rows

    for i in range(key):
        for j in range(rows):
            matrix[j] += text[index]
            index += 1

    result = "".join(matrix)

print("Result:", result)
