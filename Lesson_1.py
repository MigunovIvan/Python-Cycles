age = int(input("Введите ваш возраст: "))
gender = input("Введите ваш пол М/Ж: ").upper()
name = input("Введите ваше имя: ")

gender_text = gender

# Проверка пола
if gender in ("М", "Ж", "M", "F"):
    print("Вход разрешён")

    # Проверка возраста и пола
    if age > 18 and gender == "М":
        print(f"Приветствую, мистер {name}")
        age_group = "Совершеннолетний"

    elif age > 18 and gender == "Ж":
        print(f"Добро пожаловать, {name}")
        age_group = "Совершеннолетняя"

    else:
        age_group = "Несовершеннолетний"

    # Бесплатный проход
    if age > 55 and gender == "Ж":
        print("Проходите бесплатно")

    print("Возрастная группа:", age_group)

else:
    gender_text = "Неизвестный пол"
    print("Введите пол М или Ж")
