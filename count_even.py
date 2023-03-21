scores = [10, 3, 20, 50]


def count_even(scores):
    count_ = 0
    for score in scores:
        if score % 2 == 0:
            count_ += 1
    return count_


print(count_even(scores))

