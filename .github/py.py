from string import punctuation
print ("1) Сортувати в Алфавiтному прядку текст")
print ("2) Получити кiлькiсть всiх букв в текстi")

dija = input ("Дiя:")
txt = input("Введiть текст:")
if dija == '1':
    al = txt.split()
    al = set([word for word in al if len(word) > 2])
    al = list(al)
    al.sort(reverse=0)
    print('B Алфавiтному прядку текст:')
    print(', '.join(al))

if dija == '2':
    kor = {}
    for ch in txt:
        if ch not in punctuation and ch!= " ":
            kor[ch] = kor[ch]+1 if ch in kor else 1
    for a in kor.items():
        print(f"'Буква'{a[0]} 'кiлькiсть'{a[1]}")

