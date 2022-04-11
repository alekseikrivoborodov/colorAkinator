answers = ["Да Да Да Нет Нет Нет ", "Да Да Нет Нет Нет Нет ", "Да Нет Нет Нет Нет Нет ",
           "Нет Нет Нет Да Да Да", "Нет Нет Нет Да Да Нет", "Нет Нет Нет Да Нет Нет"]
answers_2 = ["111000", "110000", "100000", "000111", "000110", "000100"]
answers_3 = []

color = ["Красный", "Розовый", "Фиолетовый", "Черный", "Белый", "Серый"]

for i in range(len(answers)):
    answers[i] = answers[i].replace("Да", "1")
    answers[i] = answers[i].replace("Нет", "0")
    answers[i] = answers[i].replace(" ", "")
print(answers_3)

for i in range(len(answers_2)):
    answers_3.append(int(answers_2[i], 2))