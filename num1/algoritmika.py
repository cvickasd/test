# with open("poem.txt", 'a') as file:
#     file.write("\nА. С. Пушкин")

# with open("poem.txt", "r") as file:
#     data = file.read()
# print(data)

with open('poem.txt', encoding='utf-8') as file:
    data = file.load()
    print(data)
    # data = file.read()
    # print(data)