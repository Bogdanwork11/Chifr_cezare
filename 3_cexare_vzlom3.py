print("hello world3")
#exemple5 (Составьте программу дешифровку сообщения -С (полученного от другого методом полного перебора))

#ygjmyyqpahetmtuznqk

alfavit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Сообщение, которое нам нужно взломать (переменная C)
C = input("Enter the encrypted message: ")

print("\n--- 🕶  Расшифровка текста 🕶 ---")

# Запускаем цикл перебора ключей (от 1 до 25)
for key in range(1, len(alfavit)):
    result = ""
    
    for i in C:
        i = i.lower()
        if i in alfavit:
            poz_index = alfavit.index(i)
            # Мы вычитаем ключ (- key), чтобы идти в обратную сторону
            new_index = (poz_index - key) % len(alfavit)
            result += alfavit[new_index]
        else:
            result += i
            
    # Выводим каждый вариант на экран
    print(f"Key {key}: {result}")



#exemple6 (Составьте программу дешифровку сообщения -С (полученного от другого методом полного перебора)), найти значение k ключа



