from icecream import ic
def find_lizard_time(date_beginning: str, date_ending: str) -> tuple[int, int]:
    year1, month1, day1, hour1, minute1, second1 = map(int, date_beginning.split())
    year2, month2, day2, hour2, minute2, second2 = map(int, date_ending.split())
    month_dictionary = {
        1: (31, 31),
        2: (28, 59),
        3: (31, 90),
        4: (30, 120),
        5: (31, 151),
        6: (30, 181),
        7: (31, 212),
        8: (31, 243),
        9: (30, 273),
        10: (31, 304),
        11: (30, 334),
        12: (31, 365)
    }
    days1 = year1 * 365 + month_dictionary.get(month1-1, [0, 0])[1] + day1-1
    days2 = year2 * 365 + month_dictionary.get(month2-1, [0, 0])[1] + day2-1
    hours1 = (days1*24 + hour1-1)
    hours2 = (days2*24 + hour2-1)
    minutes1 = (hours1*60 + minute1-1)
    minutes2 = (hours2*60 + minute2-1)
    seconds1 = (minutes1*60 + second1-1)
    seconds2 = (minutes2*60 + second2-1)
    difference = seconds1 - seconds2
    days = int(difference/86400)
    return -days, -(difference - days*86400)





if __name__ == '__main__':
    date_beginning = "980 2 12 10 30 1"
    date_ending = "980 3 1 10 31 37"
    days, seconds = find_lizard_time(date_beginning, date_ending)
    ic(days, seconds)
