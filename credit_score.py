rating_score = {'AAA': 15, 'AA+': 14, 'AA': 13, 'AA-': 12, 'A+': 11, 'A': 10, 'A-': 9,
                'BBB+': 8, 'BBB': 7, 'BBB-': 6, 'BB': 5, 'B': 4,
                'CCC': 3, 'CC': 2, 'C': 1}

score_rating = {15: 'AAA'}


def getRatingToScore(key):
    if rating_score.__contains__(key):
        return rating_score[key]
    else:
        return 0
