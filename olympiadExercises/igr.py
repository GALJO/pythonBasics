def medals_set(_scores):
    gold = 0
    silver = 0
    brown = 0
    for score in _scores:
        if int(score) > gold:
            brown = silver
            silver = gold
            gold = int(score)
        elif int(score) > silver:
            brown = silver
            silver = int(score)
        elif int(score) > brown:
            brown = int(score)

    print(gold)
    print(silver)
    print(brown)


number_of_players = int(input())
scores = input()
scores = scores.split()
medals_set(scores)
