scores = [10, 3, 20, 50]


def sum_list(scores):
    sum_ = 0
    for score in scores:  #scores에 있는거 하나씩 꺼내서 score에 대입
        sum_ += score
    return sum_

print(sum_list(scores))
