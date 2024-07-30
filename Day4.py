f = open("input.txt", "r")
lines = f.read().splitlines()
f.close


score = 0
for line in lines:
    sections = line.split(" | ")
    score_nums = [int(sd) for sd in sections[0].split() if sd.isdigit()]
    revealed_nums = [int(rd) for rd in sections[1].split() if rd.isdigit()]
    power = len(set(score_nums) & set(revealed_nums))
    if power > 0:
        score += 2 ** (power - 1)
print(score)