def game(Z):
    from random import randint as randomnum
    from random import shuffle as shuffle
    from copy import deepcopy as copy
    def start(a):
        mine=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)]
        mine_full=['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        return mine,mine_full
    def place_mines(a,b,c):
        mine_alt=copy(mine)
        mine_alt.pop(b*10+c)
        shuffle(mine_alt)
        print('shuffled')
        mine_list=[]
        for counter in range(a):
            mine_list.append(mine_alt[counter])
        print(mine_list)
        return mine_list
    def print_board(a):
        for counter in range(0,10):
            for counter_1 in range(0,10):
                print(mine_full[counter*10+counter_1],end='')
            print('')
        return mine_full
    def print_full(a):
        for counter in range(0,10):
            for counter_1 in range(0,10):
                if mine[counter*10+counter_1] in mine_list:
                    print('M',end=' ')
                else:
                    print(' ',end=' ')
            print('')
    def print_index(a):
        for counter in range(0,10):
            for counter_1 in range(0,10):
                print(mine[counter*10+counter_1],end='')
            print('')
        return mine_full
    def check(a,b):
        for counter in range(len(mine_list)):
            if mine[counter] in mine_list:
                print('a')
        check_output=str(mine[a*10+b])+'     '+str(a)+','+str(b)
        return check_output
    def mine_check(a, b):
        if mine[a*10+b] in mine_list:
            mine_full[a*10+b] = 'M'
            while True:
                print('GAME OVER PERSS R TO RESTART')
                if input('').upper() == 'R':
                    game(Z)
        else:
            mine_full[a*10+b] = ' '
        return mine_full
    def mine_fill(a,b):
        a_1,a_2,a_3,b_1,b_2,b_3=a,a-1,a+1,b,b-1,b+1
        if a == 0 and mine_full[a*10+b] == ' ':#done
            if b == 0 and mine_full[a*10+b] == ' ':
                if mine[a*10+b] not in mine_list:
                    mine_full[a*10+b]=' '
                if mine[a*10+b_3] not in mine_list:
                    mine_full[a*10+b_3]=' '
                if mine[a_3*10+b] not in mine_list:
                    mine_full[a_3*10+b]=' '
                if mine[a_3*10+b_3] not in mine_list:
                    mine_full[a_3*10+b_3]=' '
                return mine_full
            elif b == 9 and mine_full[a*10+b] == ' ':
                if mine[a*10+b] not in mine_list:
                    mine_full[a*10+b]=' '
                if mine[a*10+b_2] not in mine_list:
                    mine_full[a*10+b_2]=' '
                if mine[a_3*10+b_1] not in mine_list:
                    mine_full[a_3*10+b_1]=' '
                if mine[a_3*10+b_2] not in mine_list:
                    mine_full[a_3*10+b_2]=' '
                return mine_full
            else:
                if mine[a*10+b] not in mine_list:
                    mine_full[a*10+b]=' '
                if mine[a_3*10+b] not in mine_list:
                    mine_full[a_3*10+b]=' '
                if mine[a*10+b] not in mine_list:
                    mine_full[a*10+b]=' '
                if mine[a_1*10+b_2] not in mine_list:
                    mine_full[a_1*10+b_2]=' '
                if mine[a_3*10+b_2] not in mine_list:
                    mine_full[a_3*10+b_2]=' '
                if mine[a_1*10+b_3] not in mine_list:
                    mine_full[a_1*10+b_3]=' '
                if mine[a_3*10+b_3] not in mine_list:
                    mine_full[a_3*10+b_3]=' '
                return mine_full
        elif a == 9 and mine_full[a*10+b] == ' ':#done
            if b == 0 and mine_full[a*10+b] == ' ':
                if mine[a*10+b_3] not in mine_list:
                    mine_full[a*10+b_3]=' '
                if mine[a_2*10+b_1] not in mine_list:
                    mine_full[a_2*10+b_1]=' '
                if mine[a_2*10+b_3] not in mine_list:
                    mine_full[a_2*10+b_3]=' '
                return mine_full
            elif b == 9 and mine_full[a*10+b] == ' ':
                if mine[a*10+b_2] not in mine_list:
                    mine_full[a*10+b_2]=' '
                if mine[a_2*10+b_1] not in mine_list:
                    mine_full[a_2*10+b_1]=' '
                if mine[a_2*10+b_2] not in mine_list:
                    mine_full[a_2*10+b_2]=' '
                return mine_full
            else:
                if mine[a_2*10+b_1] not in mine_list:
                    mine_full[a_2*10+b_1]=' '
                if mine[a_1*10+b_1] not in mine_list:
                    mine_full[a_1*10+b_1]=' '
                if mine[a_1*10+b_2] not in mine_list:
                    mine_full[a_1*10+b_2]=' '
                if mine[a_2*10+b_2] not in mine_list:
                    mine_full[a_2*10+b_2]=' '
                if mine[a_1*10+b_3] not in mine_list:
                    mine_full[a_1*10+b_3]=' '
                if mine[a_2*10+b_3] not in mine_list:
                    mine_full[a_2*10+b_3]=' '
                return mine_full
        else:
            if b == 0 and mine_full[a*10+b] == ' ':
                if mine[a_1*10+b_3] not in mine_list:
                    mine_full[a_1*10+b_3]=' '
                if mine[a_1*10+b_1] not in mine_list:
                    mine_full[a_1*10+b_1]=' '
                if mine[a_2*10+b_1] not in mine_list:
                    mine_full[a_2*10+b_1]=' '
                if mine[a_2*10+b_3] not in mine_list:
                    mine_full[a_2*10+b_3]=' '
                if mine[a_3*10+b_1] not in mine_list:
                    mine_full[a_3*10+b_1]=' '
                if mine[a_3*10+b_3] not in mine_list:
                    mine_full[a_3*10+b_3]=' '
                return mine_full
            elif b == 9 and mine_full[a*10+b] == ' ':
                if mine[a_1*10+b_2] not in mine_list:
                    mine_full[a_1*10+b_2]=' '
                if mine[a_1*10+b_1] not in mine_list:
                    mine_full[a_1*10+b_1]=' '
                if mine[a_2*10+b_1] not in mine_list:
                    mine_full[a_2*10+b_1]=' '
                if mine[a_2*10+b_2] not in mine_list:
                    mine_full[a_2*10+b_2]=' '
                if mine[a_3*10+b_1] not in mine_list:
                    mine_full[a_3*10+b_1]=' '
                if mine[a_3*10+b_2] not in mine_list:
                    mine_full[a_3*10+b_2]=' '
                return mine_full
            else:
                if mine[a_1*10+b_3] not in mine_list:
                    mine_full[a_1*10+b_3]=' '
                if mine[a_1*10+b_2] not in mine_list:
                    mine_full[a_1*10+b_2]=' '
                if mine[a_3*10+b_1] not in mine_list:
                    mine_full[a_3*10+b_1]=' '
                if mine[a_3*10+b_2] not in mine_list:
                    mine_full[a_3*10+b_2]=' '
                if mine[a_3*10+b_3] not in mine_list:
                    mine_full[a_3*10+b_3]=' '
                if mine[a_2*10+b_1] not in mine_list:
                    mine_full[a_2*10+b_1]=' '
                if mine[a_2*10+b_3] not in mine_list:
                    mine_full[a_2*10+b_3]=' '
                if mine[a_2*10+b_2] not in mine_list:
                    mine_full[a_2*10+b_2]=' '
                return mine_full
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
    a=int(input('input no of mines'))
    b=int(input('input coordanates'))
    c=int(input('input coordanates'))
    mine_list=place_mines(a,b,c)
    a,b=b,c
    mine_full=mine_check(a,b)
    while True:
        mine_full=print_board(0)
        win_check(0)
        mine_full=mine_check(a,b)
        mine_full=mine_fill(a,b)
        a=int(input('input coordanates'))
        b=int(input('input coordanates'))
game(0)
