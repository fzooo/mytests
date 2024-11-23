from random import randint


def temperature():
    return str(randint(363, 369) / 10)


def day_temperature(day=1):
    return [temperature() for i in range(4 * day)]


all = ""
day = 5
count = 21
for i in range(count):
    t = day_temperature(day)
    all += "\t".join(t)
    if i != count - 1:
        all += "\n"

with open("logs/temperature.txt", "w") as f:
    f.write(all)
