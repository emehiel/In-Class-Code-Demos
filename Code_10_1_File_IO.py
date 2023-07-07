with open('workfile.txt', 'w', encoding='utf-8') as f:
    f.write('Hello file world!\n')

    for i in range(5):
        f.write(f'This is line {i+2} of the file\n')
f.close()

with open('workfile.txt', 'r') as f:
    print(f.read())
f.close()

with open('workfile.txt', 'r') as f:
    print(f.read(20))
f.close()

with open('workfile.txt', 'r') as f:
    print(f.readline())
    print(f.readline())
f.close()

with open('workfile.txt', 'r') as f:
    data = f.readlines()
    print(data)
f.close()