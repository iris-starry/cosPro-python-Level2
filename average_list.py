scores = [10, 3, 20, 50]


def avg_list(scores):    #합계 / 갯수
    sum_ = 0
    count_ = 0
    for score in scores:
        sum_ += score
        count_ += 1

    return sum_ / count_



print(avg_list(scores))