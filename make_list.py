def make_list(n):
    list_ = []
    for _ in range(n):  #range(6) : 0, 1, 2, 3, 4, 5
        list_.append(0)   #리스트에 0의 값을 추가하기
    return list_


print(make_list(6)) #[0, 0, 0, 0, 0, 0]