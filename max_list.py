def max_list(scores):
    max_ = scores[0]   #socres에 있는 맨 앞에 있는 아이를 최대값으로 일단 대입
    for score in scores:  #scores 하나씩 꺼내어 score라고 함
        if max_ < score:  #갖고 있던 최대값보다 score가 크면 최대값으로 대입
            max_ = score
    return max_

scores = [10, 3, 20, 50]
print(max_list(scores))

def min_list(scores):
    min_ = scores[0]
    for socre in scores:
        if min_ > socre:  #갖고 있던 최소값보다 더 작으면 최소값으로 대입
            min_ = socre
    return min_

print(min_list((scores)))

