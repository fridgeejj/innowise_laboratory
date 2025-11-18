# функция для определения этапа жизни по возрасту
def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"

# ввод данных пользователя   
user_name = input("Hi. Enter your full name: ") 
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str) # преобразование строки в число
current_age = 2025 - birth_year # вычисление возраста

# ввод хобби 
hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    # проверка на команду остановки
    if hobby.lower() == "stop": 
        break
    # добавление каждого введённого хобби в список
    hobbies.append(hobby)

life_stage = generate_profile(current_age) # получение категории жизни

# создание профиля в виде словаря
user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

# вывод итоговой информации
print("\n---\n")
print("Profile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")

# проверка наличия хобби
if len(user_profile["hobbies"]) == 0:
    print("You didn't mention any hobbies.")
else:
    for hobby in user_profile["hobbies"]:
        print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
        print(f"- {hobby}")

print("---")
