import numpy as np
number = np.random.randint(1,101)
def game_core_v2(number):
    count = 1
    range_h = 101
    range_l = 1
    predict = (range_h-range_l)/2
    while number != predict:
        count+=1
        if number > predict: 
            range_l = predict
            predict = int(range_l+(range_h-range_l)/2)
        elif number < predict: 
            range_h = predict
            predict = int(range_l+(range_h-range_l)/2)
    return(count) # ����� �� �����, ���� �������
def score_game(game_core_v2):
    '''��������� ���� 1000 ���, ����� ������, ��� ������ ���� ��������� �����'''
    count_ls = []
    np.random.seed(1)  # ��������� RANDOM SEED, ����� ��� ����������� ��� �������������!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v2(number))
    score = int(np.mean(count_ls))
    print(f"��� �������� ��������� ����� � ������� �� {score} �������")
    return(score)
score_game(game_core_v2)