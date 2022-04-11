color = ["красный", "розовый", "фиолетовый", "черный", "белый", "серый",
         "зеленый", "синий", "коричневый", "желтый", "голубой", "оранжевый",
         "лаймовый", "бирюзовый", "темно-зеленый", "пурпурный", "светло-серый"]

questions = [
    ["Яблоко может быть вашего цвета?", 35],
    ["Небо может быть вашего цвета?", 20],
    ["Лес может быть вашего цвета?", 60],
    ["Ваш цвет это цвет снега?", 30],
    ["В вашем цвете 7 букв?", 50],
    ["Ваш цвет светлый?", 30], 
    ["Ваш цвет монохромный?", 80],  
    ["Панда может быть вашего цвета?", 60],
    ["Ваш цвет популярен у фруктов?", 40],  
    ["Ваш цвет похож на воду?", 40], 
    ["Ваш цвет женский?", 50],
    ["Ваш цвет как у бетона?", 80],
]
full_answers = []

good_answers = ["Да", "Д", "Y", "Yes", 1, "1"]



def auto_balls():
    for i in range(len(questions)):
        solo_answers = []
        answer = ""
        while answer != "с":
            answer = input(questions[i][0])
            solo_answers.append(answer)    
        full_answers.append(solo_answers)
    
    return full_answers

# print(auto_balls())

full_answers = [
    ['красный', 'желтый', 'зеленый', 'коричневый', 'с'],
    ['голубой', 'синий', 'фиолетовый', 'розовый', 'бирюзовый', 'черный', 'пурпурный', 'с'], 
    ['зеленый', 'темно-зеленый', 'коричневый', 'лаймовый', 'с'], 
    ['белый', 'светло-серый', 'серый', 'черный', 'желтый', 'с'], 
    ['красный', 'розовый', 'зеленый', 'голубой', 'с'], 
    ['красный', 'розовый', 'белый', 'желтый', 'голубой', 'оранжевый', 'лаймовый', 'бирюзовый', 'пурпурный', 'светло-серый', 'с'], 
    ['черный', 'белый', 'серый', 'светло-серый', 'с'], 
    ['черный', 'белый', 'с'], 
    ['красный', 'зеленый', 'желтый', 'оранжевый', 'лаймовый', 'с'], 
    ['синий', 'голубой', 'с'], 
    ['голубой', 'розовый', 'светло-серый', 'с'], 
    ['серый', 'светло-серый', 'с']
    ]

def questions_rebrend(full_answers):
    for i in range(len(full_answers)):
        for j in range(len(full_answers[i])):
            full_answers[i][-1] = questions[i][1]
    return full_answers
        
        
def akinator():
    count = [0] * len(color)
    
    for i in range(len(questions)):
        if max(count) <= 200: 
            answer = input(questions[i][0])
            for j in range(len(full_answers[i])):
                for k in range(len(color)):
                    if answer in good_answers:
                        if full_answers[i][j] == color[k]:
                            count[k] += full_answers[i][-1]
                        
    return count

full_answers = questions_rebrend(full_answers)
count = akinator()


print(count)
print(color)
print(color[count.index(max(count))])
