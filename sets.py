with open("example.txt", "w") as f:
    f.write("Hello, Python!\n")

with open("example.txt", "r") as f:
    content = f.read()
    print(content)
