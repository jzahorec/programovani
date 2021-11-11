Herald = {1: 9765, 2: 297072, 3:261104 ,4: 298819, 5: 307024}
Guardian = {1: 315524, 2: 320541, 3: 329958, 4: 336807, 5: 343249}
Crusader = {1: 357208, 2: 355176, 3: 354174, 4: 347977, 5: 339344}
Archon = {1: 343929, 2: 326957, 3: 309519, 4: 287205, 5: 266399}
Legend = {1: 262029, 2: 229849, 3: 202498, 4: 177258, 5: 154125}
Ancient = {1: 150029, 2: 122412, 3: 99869, 4: 81820, 5: 67992}
Divine = {1: 78901, 2: 60142, 3: 45535, 4: 33374, 5: 25700}
Immortal = {1: 85382}

ranks = [Herald, Guardian, Crusader, Archon, Legend, Ancient, Divine, Immortal]
ranks_named = ["Herald", "Guardian", "Crusader", "Archon", "Legend", "Ancient", "Divine", "Immortal"]
all_players = 0

for rank in ranks:
    for star in rank:
        all_players += rank[star]

print(all_players)

players_times_star = 0

star_count = 0
for rank in ranks:
    for star in rank:
        star_count += 1
        players_times_star += rank[star] * star_count

print(players_times_star)

avg_star = players_times_star / all_players

def tell_rank(stars):
    ranks_named = ["Herald", "Guardian", "Crusader", "Archon", "Legend", "Ancient", "Divine", "Immortal"]
    i = 1
    for rank in ranks_named:
        for star in range(1, 6):
            if i >= stars:
                return rank, star
            i += 1


print(avg_star)
print(tell_rank(avg_star))
print(tell_rank(33))
