height = int(input("Въведете своята височина в см: "))
gender = input("Въведете своя пол(мъж/жена): ").lower()

if gender == "мъж":
    weight = 50 + 0.9 * (height - 152)
elif gender == "жена":
    weight = 45.5 + 0.9 * (height - 152)
else:
    print("Грешно въведен пол.")
    exit()

print(f"Твоето идеално тегло е приблизително: {round(weight, 1)} kg.")
