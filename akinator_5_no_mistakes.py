color = ["Красный", "Розовый", "Фиолетовый", "Черный", "Белый", "Серый"]
counts = [34, 21, 10, 64, 41, 20]
questions = [
    ["Ваш цвет из семейства красных?", 10],
    ["Ваш цвет красный или розовый?", 11],
    ["Ваш цвет красный?", 13],
    ["Ваш цвет из семейства монохромных?", 20],
    ["Ваш цвет черный или белый?", 21],
    ["Ваш цвет черный?", 23],  
]



def akinator():
    count = 0
    for i in range(len(questions)):
        if input(questions[i][0]) == "1":
            count += questions[i][1]
            print(count)
    return count

def your_color(count, colors):
    found = colors[0]
    for item in colors:
        if abs(item - count) < abs(found - count):
            found = item        
    for i in range(len(counts)):
        if found == counts[i]:
            return color[i]




count = akinator()
print(your_color(count, counts))
# print(your_color(count))



