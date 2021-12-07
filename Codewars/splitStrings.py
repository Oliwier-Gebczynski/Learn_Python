def solution(text):
    string_result = ""
    list = []

    if len(text) % 2 != 0:
        text += "_"

    for index in text:
        string_result += index
        if len(string_result) == 2:
            list.append(string_result)
            string_result = ""


