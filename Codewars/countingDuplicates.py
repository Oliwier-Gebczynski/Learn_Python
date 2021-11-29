def duplicate_count(text):
    sign_list = []
    duplicates = []
    counter = 0

    for letter in text:
        sign_list.append(letter.lower())

    for j in range(len(sign_list)):
        for i in range(len(sign_list)):
            if sign_list[i] == sign_list[j]:
                if i != j:
                    if sign_list[i] not in duplicates:
                        duplicates.append(sign_list[i])

    counter = len(duplicates)

    return counter

duplicate_count("Indivisibilities")
