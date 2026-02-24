print("hello world1")

#-----Shifr Cezarya-----

#exemple1 (создайте программу шифрования цезаря)



alfavit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = str(input("Enter your word: "))
key = int(input("Enter key: "))
result = ""

#чтобы пройти весь текст введенный пользователем нужен цикл 
for i in text:
    i = i.lower()
    #теперь этот текст введенный пользователем проходит по алфавиту
    if i in alfavit:
        #теперь нужно найти значение-позицию буквы в списке
        poz_index = alfavit.index(i)
        #переводим новый индекс со сдвигом 
        new_index = (poz_index + key) % len(alfavit)
        #добавляем новую букву в результат 
        result += alfavit[new_index]
    else:
        print("Error with shrift")
print(f"Your shifr text with key {key}: {result}")



