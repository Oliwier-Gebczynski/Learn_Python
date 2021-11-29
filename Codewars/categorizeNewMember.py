def open_or_senior(data):
    members = []

    for item in data:
        if item[0] >= 55 and item[1] > 7:
            members.append("Senior")
        else:
            members.append("Open")

    return members

open_or_senior([(41, 24), (78, 5),(87, -1), (32, 4), (75, 6), (58, 7),(16, 25)])