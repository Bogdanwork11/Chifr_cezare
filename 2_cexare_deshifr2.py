print("hello world2")

alfavit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Переименовали переменную в B, как просит задание
B = input("Enter your FIO (15-20 letters): ")
key = int(input("Enter key (1-26): "))
result = ""

# Проверяем длину введенной строки B
if 15 <= len(B) <= 20:
    for i in B:
        i = i.lower()
        if i in alfavit:
            poz_index = alfavit.index(i)
            new_index = (poz_index + key) % len(alfavit)
            result += alfavit[new_index]
        else:
            # Если это пробел между фамилией и именем, просто добавим его
            result += i 
    
    print(f"Your shifr text with key {key}: {result}")
else:
    print(f"Error: Your text has {len(B)} letters, but needs 15-20!")