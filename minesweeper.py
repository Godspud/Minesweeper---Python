def game(Z):
    from random import randint as randomnum
    from random import shuffle as shuffle
    from copy import deepcopy as copy
    def start(a):
        mine=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)]
        mine_full=['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        return mine,mine_full
    def place_mines(a):
        mine_alt=copy(mine)
        shuffle(mine_alt)
        print('shuffled')
        mine_list=[]
        for counter in range(a):
            mine_list.append(mine_alt[counter])
        print(mine_list)
        return mine,mine_list
    def print_board(a):
        for counter in range(0,10):
            for counter_1 in range(0,10):
                print(mine_full[int(str(counter)+str(counter_1))],end='')
            print('')
        return mine_full
    def print_full(a):
        for counter in range(0,10):
            for counter_1 in range(0,10):
                if mine[int(str(counter)+str(counter_1))] in mine_list:
                    print('M',end=' ')
                else:
                    print(' ',end=' ')
            print('')
    def check(a,b):
        for counter in range(len(mine_list)):
            if mine[counter] in mine_list:
                print('a')
        check_output=str(mine[int(str(a)+str(b))])+'     '+str(a)+','+str(b)
        return check_output
    def mine_check(a, b):
        if mine[int(str(a)+str(b))] in mine_list:
            mine_full[int(str(a)+str(b))] = 'M'
            while True:
                print('GAME OVER PERSS R TO RESTART')
                if input('').upper() == 'R':
                    game(Z)
        else:
            mine_full[int(str(a)+str(b))] = ' '
        return mine_full
    def mine_fill(a,b):
        if a == '0' and mine_full[int(str(a)+str(b))] == ' ':
            if b == '0' and mine_full[int(str(a)+str(b))] == ' ':
                a_temp=1
                if mine[int(str(a_temp)+str(b))] in mine_list:
                    print('e')
            elif b == '9' and mine_full[int(str(a)+str(b))] == ' ':
                print('')
            else:
                print('')
        elif a == '9' and mine_full[int(str(a)+str(b))] == ' ':
            if b == '0' and mine_full[int(str(a)+str(b))] == ' ':
                print('')
            elif b == '9' and mine_full[int(str(a)+str(b))] == ' ':
                print('')
            else:
                print('')
        else:
            if b == '0' and mine_full[int(str(a)+str(b))] == ' ':
                print('')
            elif b == '9' and mine_full[int(str(a)+str(b))] == ' ':
                print('')
            else:
                print('')
    def win_check(a):
        win_counter=0
        for counter in range(100):
            if mine_full[counter] not in mine_list and mine_full[counter] == ' ':
                win_counter+=1
            if len(mine_list)+win_counter == 100 or len(mine_list) == 0:
                while True:
                    print('YOU WIN PRESS R TO START A NEW GAME')
                    if input('').upper() == 'R':
                        game(Z)
    mine,mine_full=start(0)
    mine,mine_list=place_mines(int(input('input no of mines')))
    while True:
        mine_full=print_board(0)
        win_check(0)
        a=input('input coordanites')
        b=input('input coordanates')
        mine_full=mine_check(a,b)
        mine_fill(a,b)
game(0)