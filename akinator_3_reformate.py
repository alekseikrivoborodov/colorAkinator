answers = ["Да Да Да Нет Нет Нет ", "Да Да Нет Нет Нет Нет ", "Да Нет Нет Нет Нет Нет ",
           "Нет Нет Нет Да Да Да ", "Нет Нет Нет Да Да Нет ", "Нет Нет Нет Да Нет Нет "]

color = ["Красный", "Розовый", "Фиолетовый", "Черный", "Белый", "Серый"]


# Решение с циклом for

def questions():
    question = input("Ваш цвет из семейства красных? ответ 'Да' или 'Нет'") + " "
    question = question + input("Ваш цвет красный или розовый? ответ 'Да' или 'Нет'") + " "
    question = question + input("Ваш цвет красный? ответ 'Да' или 'Нет'") + " "
    question = question + input("Ваш цвет из семейства монохромных? ответ 'Да' или 'Нет'") + " "
    question = question + input("Ваш цвет черный или белый? ответ 'Да' или 'Нет'") + " "
    question = question + input("Ваш цвет черный? ответ 'Да' или 'Нет'") + " "
    print(question)
    return question


def akinator(answer):
    for i in range(len(answers)):
        if answer == answers[i]:
            return color[i]
    return "Я не знаю твой цвет"
        

print(akinator(questions()))        
