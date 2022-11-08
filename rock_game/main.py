import random
import os


def main():

    tools = ['Rock', 'Paper', 'Scissors']
    
    p1_count = 0
    com_count = 0
    rounds = 0
    os.system('cls')

    print('*' * 45 + '\n' + 'Welcome to rock, paper or scissors game!' + '\n' + '*' * 45)

    while True:

        rounds += 1
        print()
        print('Round: ', rounds)
        print('Player 1 points: ', p1_count)
        print('Computer points: ', com_count)
        print()

        random_tool = random.choice(tools)
        choosen_tool = int(input('Select your tool: rock(1), paper(2) or scissors(3): '))
        print()

        if choosen_tool == 1:
            choosen_tool = tools[0]
        elif choosen_tool == 2:
            choosen_tool = tools[1]
        else:
            choosen_tool = tools[2]
        
        print(choosen_tool + ' (you)' + ' vs ' + random_tool + ' (com)')
        
        print()
        
        if choosen_tool == random_tool:
            print('Tie!')
        elif choosen_tool == tools[0]:
            if random_tool == tools[1]:
                print('You Lose!')
                com_count += 1
            else:
                print('You Win!')
                p1_count += 1
        elif choosen_tool == tools[1]:
            if random_tool == tools[0]:
                print('You Win')
                p1_count += 1
            else:
                print('You Lose!')
                com_count += 1
        elif choosen_tool == tools[2]:
            if random_tool == tools[0]:
                print('You Lose')
                com_count += 1
            else:
                p1_count += 1
                print('You Win!')

        if  p1_count == 3:
            print()
            print('You Win the Game!')
            break

        if  com_count == 3:
            print()
            print('You Lose the Game!')
            break

        print()
        print(input('Press enter to continue'))
        os.system('cls')

    print('Round: ', rounds)
    print('Player 1 points: ', p1_count)
    print('Computer points: ', com_count)
    print()
    print('End of the game. Please drink water \n')  


if __name__ == "__main__":
    main()