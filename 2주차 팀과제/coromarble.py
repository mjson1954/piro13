import random
from cities import *

board=[['출발=>','1','2','3'], ['인천',' ',' ',' '], ['강원',' ',' ',' '], ['광주',' ',' ',' '],['자가격리',' ',' ',' '], ['세종',' ',' ',' '], ['부산',' ',' ',' '],
    ['황금열쇠',' ',' ',' '], ['제주도',' ',' ',' '], ['충청',' ',' ',' '], ['울산',' ',' ',' '], ['대구',' ',' ',' '], ['독도',' ',' ',' '], ['경기',' ',' ',' '], ['대전',' ',' ',' '], ['서울',' ',' ',' ']]
for item in board:
    item[0] = item[0].center(6)
    

player_location=[-1, 0, 0, 0] # player 현재 위치

wallet=[10000, 150, 150, 150] # wallet 초기값

self_isolation=[-1, 0, 0, 0] # 자가격리되어있는 사람
isolation_count=[-1, 2, 2, 2]

def rule_print():
    print("""<<<코로마블 규칙 (Coromarble rule)>>>

1. 코로마블은 코로나로 인해 해외여행을 못가는 상황에서 대한민국을 여행하는 게임입니다.
2. 게임은 3명의 플레이어로 진행되며 각 플레이어는 턴마다 주사위 2개(4x4)를 돌립니다.
3. 게임 순서는 게임 시작 시 랜덤으로 정해집니다.
4. 각 플레이어는 150 MSK의 초기 자금을 지급 받습니다.
5. 주사위를 돌려 나온 횟수만큼 이동하며 속한 땅의 주인이 없다면 구입이 가능합니다.
6. 건물은 턴에 상관없이 해당 땅에 도착하면 지을 수 있습니다.
7. 지을 수 있는 건물은 2 종류이며, 아파트와 주택의 가격은 각각 땅 가격의 10%, 5%입니다.
8. 한 바퀴를 돌때마다 월급 20 Msk가 지급됩니다.
9. 대한민국에서 섬은 구입할 수 없으며 각 섬에 도착시 해당 섬의 발전기금을 내야 합니다.
10. 자가격리 칸에 도착하게 되면 해당 칸을 빠져나올 때까지 움직일 수 없습니다.
11. 자가격리 칸에 속할 경우 나머지 플레이어의 턴이 끝날 때마다 자가격리 지원 비용으로 약 5 Msk를 지급 받습니다.
12. 황금열쇠 칸에 도착하면 랜덤으로 황금열쇠 아이템이 호출되며, 각 아이템의 속성은 황금열쇠 아이템이 호출되는 즉시 구현됩니다.
13. 만약 타인의 땅에 입장하게 되면 땅과 건물의 총 가격의 20%를 지불해야 합니다.
14. 게임은 어느 한 플레이어가 파산할 때 끝나게 되고,  남은 플레이어의 총자산 비교로 순위가 결정됩니다.
15. 언제든 h를 입력하면 이 도움말을 다시 볼 수 있습니다.
""")

def board_print(board): # 보드판 네모로 출력해주는 함수
    for i in range(5):
        print(board[i], end='')
    print("\n")
    print(board[15],"                                ♥     coromarble     ♥                            ", end='')
    print(board[5],"\n")
    print(board[14],"                            화폐단위: MSK, 초기자본: 150 MSK                      ", end='')
    print(board[6],"\n")
    print(board[13],"          아파트:땅 가격의 10%, 주택:땅 가격의 20%, 통행료:총 가격의 20%        ", end='')
    print(board[7],"\n")
    board_reverse=board.copy()
    board_reverse.reverse()
    for i in range(3, 8):
        print(board_reverse[i], end='')
    print("\n")
    

def dice(): # 주사위 굴리기
    dice_1=random.randrange(1,4) # 1~3
    dice_2=random.randrange(1,4)
    return dice_1, dice_2

def board_rerange(player, old_location, new_location): # 보드판에서 말 위치 이동
    board[old_location][player]=' '  # 예전 위치에서 빼서
    board[new_location][player]=str(player) # 새로운 위치로 말 이동

def go(player, dice_1, dice_2): 
    if(self_isolation[player]!=0):
        return 4
    dice_sum = dice_1 + dice_2 # 가야하는 칸 수
    old_location = player_location[player] # 예전 위치
    # print("예전 위치:", old_location)
    player_location[player] += dice_sum # 새로운 위치로 변경
    # print("새로운 위치:", player_location[player])
    if(player_location[player] > 15): 
        player_location[player] -= 16 
        wallet[player]+=20 # 출발지 돌았으니까 용돈 수령
        print("한 바퀴를 돌았습니다. 월급이 20 MSK 지급되었습니다.")
    board_rerange(player, old_location, player_location[player]) #보드판을 바꿔주는 함수
    return player_location[player]

def Golden_key(player):  # <황금열쇠  목록>  (이건 랜덤으로 진행)
    print("황금 열쇠를 뽑을 수 있는 곳입니다. 황금열쇠를 뽑아주세요!(Enter 키 입력)")
    input()
    g = random.randrange(1,5)
    if g == 1: # 1. 자가격리 대상자입니다.  (-)
        old_location = player_location[player]
        player_location[player] = 4
        board[old_location][player] = ''
        board[4][player] = str(player)
        print("자가격리 대상자입니다. 자가격리 장소로 이동하세요. ㅠㅠ")

    elif g == 2: # 2. 출발지로 돌아가세요. (+ 용돈)  (+)
        old_location = player_location[player]
        player_location[player] = 0
        board[old_location][player] = ''
        board[0][player] = str(player)
        print("초심을 찾아야 합니다. 출발지로 돌아가세요.")

    elif g == 3:    # 3. 복권에 당첨되셨습니다!  (+)
        # 플레이어에게 200 Msk 지급
        wallet[player] += 200
        print("복권에 당첨됐습니다! 농협은행 본점에서 당첨금 200 Msk를 수령하세요.")

    elif g == 4:
        # 도시 클래스 이용.
        print("자유여행 이용권에 당첨됐습니다. 원하는 도시의 숫자를 입력하세요. (황금열쇠 제외) (단, 월급은 지급되지 않습니다.)")  # 4. 원하는 도시를 선택하세요! (+)
        print("0. 출발, 1. 인천, 2. 강원, 3. 광주, 4. 자가격리, 5. 세종, 6. 부산, 8.제주도, 9. 충청, 10. 울산, 11. 대구, 12. 독도, 13. 경기, 14. 대전, 15. 서울")
        city_number=int(input())
        old_location = player_location[player]
        player_location[player] = city_number
        board[old_location][player] = ''
        board[city_number][player] = str(player)
        print(f"{player}번 player님이 {cities[city_number].name}로 이동하셨습니다.")

    else:  # g == 5:      # 5. 기부 대상자에 선정되셨습니다! 나눔을 실천하세요!! (-)
        wallet[player] -= int(wallet[player] * 0.1)
        print("기부 릴레이에 참여하게 됐습니다! 나눔을 실천하세요! *보유한 금액의 10%를 기부합니다.")


def buy_land(player, city):
    if city.has_apt == True:
        city.land_price += city.apt_price
    if city.has_house == True:
        city.land_price += city.house_price
    wallet[player] -= city.land_price
    city.owner = player
    print(f"{player}번 player가 {city.name}을(를) 구입했습니다.")


def build_apt(player, city):
    if city.has_apt == False: 
        wallet[player] -= city.apt_price
        city.has_apt = True
        print("아파트를 지었습니다.")
        print(f"이제 이 도시는 {city.apt_price} MSK입니다.")
    else:
        print("이미 아파트가 있습니다!")


def build_house(player, city):
    if city.has_house == False:
        wallet[player] -= city.house_price
        city.has_house -= True
        print("주택을 지었습니다.")
        print(f"이제 이 도시는 {city.house_price} MSK입니다.")
    else:
        print("이미 주택이 있습니다!")

def pay_toll(player, city):
    if city.is_island == False:
        wallet[player] -= city.toll
        wallet[city.owner] += city.toll       
    else:
        wallet[player] -= city.land_price
 

def payments(choice, player, city):
    if choice == 0:
        buy_land(player, city)
    elif choice == 1:
        build_apt(player, city)
    elif choice == 2:
        build_house(player, city)


if __name__ == "__main__":
    flag=1
    while(flag==1):
        for player in range(1, 4):
            print(f"\n자산현황:\n1번 player: {wallet[1]} MSK\n2번 player: {wallet[2]} MSK\n3번 player: {wallet[3]} MSK\n")
            print("***********************************************************")
            print("{0}번 player님, 주사위를 돌려주세요(Enter 키 입력)".format(player))
            print("* 게임 규칙을 확인하시려면 h 를 입력해주세요")
            a=input()
            if(a=="h"):
                rule_print()
                print("{0}번 player님, 주사위를 돌려주세요(Enter 키 입력)".format(player))
                b=input()
            if(self_isolation[player]==1):
                print(f"{player}번 player님, 자가격리가 해제되셨습니다. 다음 턴에 이동하실 수 있습니다.")
                isolation_count[player]=0
                self_isolation[player]=0
                continue
            dice_1, dice_2= dice() # 주사위 돌리기
        
            location = go(player, dice_1, dice_2) # 말 옮기기
            board_print(board) # 현재 보드 출력
            city = cities[location]
            print(f"주사위: {dice_1}, {dice_2}")
            print(f"{player}번 player님, 당신의 현재 위치는 {city.name}입니다.")
            
            if(location==7):
                Golden_key(player)
                continue
            elif(location==8 or location == 12):
                pay_toll(player, city)
                print(f"섬은 살 수 없습니다. 통행료 {city.land_price} MSK를 지불했습니다.")
                continue
            elif(location==4): # 자가격리일 때 탈출
                self_isolation[player]=1 # flag 켜짐
                if isolation_count[player]==2: # 자가격리 맨 처음 턴
                    print(f"{player}번 player가 자가격리 대상자로 선정되셨습니다. 2턴동안 이동할 수 없습니다.")   
                    isolation_count[player]-=1
                    continue
                
            elif(location==0):
                continue
            else:  
                if city.owner == player:
                    print(f"현재 위치에서 아파트({city.apt_price} MSK) 또는 주택({city.house_price} MSK)를 지을 수 있습니다.")
                    i = 0
                    while(i == 0):
                        print("건물을 짓겠습니까? (y/n)")
                        answer = input()
                        if answer != "y" and answer != "n":
                            print("잘못 입력하셨습니다. 다시 입력해주세요.")
                            continue
                        elif answer == "y":
                            
                            while(True):    
                                print("어떤 건물을 짓겠습니까? 번호를 입력해주세요. (0. 아파트 1. 주택)")
                                answer = input()
                                if answer != "0" and answer != "1":
                                    print("잘못 입력하셨습니다. 다시 입력해주세요.")
                                    continue
                                elif answer == "0":
                                    build_apt(player, city)
                                    i=1
                                    break
                                    
                                elif answer == "1":
                                    build_house(player, city)
                                    i=1
                                    break
                        else:
                            break    
                   
                if city.owner and city.owner != player:
                    print(f"이미 주인이 있는 땅입니다. 통행료 {city.toll} MSK를 지불했습니다.")

                    pay_toll(player, city)

                print(f"현재 위치 도시의 가격은 {city.land_price} MSK입니다.")
                print(f"당신의 현재 자산은 {wallet[player]} MSK입니다.\n")
                while(True):
                    print("땅을 사시겠습니까? (y/n)")
                    answer = input()
                    if answer != "y" and answer != "n":
                        print("잘못 입력하셨습니다. 다시 입력해주세요.")
                        continue
                    elif(answer == "y"):
                        buy_land(player, city)
                        break
                    else:
                        break
            
        
            for index, balance in enumerate(wallet):
                if balance <= 0:
                    print(f"Player{index}가 파산하였습니다.\n")
                    print(f"자산현황:\n1번 player: {wallet[1]} MSK\n2번 player: {wallet[2]} MSK\n3번 player: {wallet[3]} MSK\n")
                    print("최종 순위")
                    wallet_result=wallet.copy()
                    wallet_result.sort(reverse=True)
                    first_idx=wallet.index(wallet_result[1])
                    second_idx=wallet.index(wallet_result[2])
                    third_idx=wallet.index(wallet_result[3])
                    if(first_idx==second_idx):
                        print(f"1위: {first_idx}번, {second_idx}번 player")
                        print(f"3위: {third_idx}번 player")
                        print("\n게임이 종료되었습니다.")
                    else:
                        print(f"1위: {first_idx}번 player")
                        print(f"2위: {second_idx}번 player")
                        print(f"3위: {third_idx}번 player")
                        print("\n게임이 종료되었습니다.")
                    flag=0
                    break

            if(flag==0):
                break
