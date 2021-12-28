# สร้างเกม blackjack

import random
from random import shuffle
from art import logo

# สร้าง while ขึ้นมาเนื่องจาก ทำให้สามารถวนกลับมาเล่นเกมได้เรื่อย ๆ
again = True
while again:
    play = input("Do you want to play a game of Blackjake? Type 'yes' or 'no': ").lower()
    if play == "no":
        print("Good bye")
        again = False
    # เริ่มเล่นเกม
    elif play == "yes":
        print(logo)

        cards = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
        }

        deck_cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        # สุ่มไพ่ให้ผู้เล่น 2 ไพ่ โดยการ shuffle deck_cards 
        random_card = random.shuffle(deck_cards)
        card_player_1 = deck_cards[0]
        card_player_2 = deck_cards[1]
        # เพื่อดูว่าผู้เล่นสุ่มได้การ์ดอะไร
        player_card = [card_player_1, card_player_2]
        # เปลี่ยนการ์ดให้เป็น integer โดยการนำ ไพ่ที่สุ่มได้ไปจับคู่กับ key ใน dict เพื่อแปรค่าเป็นตัวเลข
        player_card_result = [cards[card_player_1], cards[card_player_2]]

        # ทำ deck ใหม่ เพื่อที่จะ make sure ว่าไพ่ที่ bot สุ่มได้มานั้นจะไม่ซ้ำกับผู้เล่นแน่ ๆ
        new_deck_cards = []
        for new in deck_cards:
            # โดยการ check ว่าผู้เล่นได้ไพ่อะไร แล้วทำการตัดเลขนั้นออกจาก list
            if new == player_card[0] and new != player_card[1]:
                new_deck_cards = []
            elif new != player_card[0] and new == player_card[1]:
                new_deck_cards = [] 
            else:
                new_deck_cards.append(new)

        # random ไพ่ให้ bot 2 ใบ โดยที่การ์ดไม่มีทางที่จะซ้ำกับผู้เล่นแน่นอน
        random_new_deck_cards = random.shuffle(new_deck_cards)
        card_computer_1 = new_deck_cards[0]
        card_computer_2 = new_deck_cards[1]
        # ต้องแสดงไพ่ ให้ผู้เล่นดูว่า bot มีการ์ดใบแรกเป็นอะไร
        show_computer_card = card_computer_1
        # ตรวจสอบว่า bot ได้การ์ดอะไรไปบ้าง
        computer_card = [card_computer_1, card_computer_2]
        # เปลี่ยนค่าของการ์ดจาก str() --> int()
        computer_card_result = [cards[card_computer_1], cards[card_computer_2]]

        # ทำ deck ใหม่ เพื่อในกรณีที่ผู้เล่นต้องการ์ดจั่วการ์ดเพิ่มอีก 1 ใบ จะไม่ซ้ำกับการ์ดก่อนหน้าและของ bot
        new_deck_cards_2 = []
        for new in new_deck_cards:
            if new == computer_card[0] and new != computer_card[1]:
                new_deck_cards_2 = []
            elif new != computer_card[0] and new == computer_card[1]:
                new_deck_cards_2 = [] 
            else:
                new_deck_cards_2.append(new)
        
        # random ลำดับของ deck ที่จะจั่วการ์ด
        random_new_deck_cards_2 = random.shuffle(new_deck_cards_2)
        # สุ่มการ์ดให้ผู้เล่นกรณีที่มีการจั่วเพิ่มอีก 1 ใบ โดยการนำการ์ด 2 ใบแรกมา แล้วเพิ่มอีก 1 ใบ จากการสุ่มใน deck ล่าสุด
        player_card_result = [cards[card_player_1], cards[card_player_2], cards[new_deck_cards_2[0]]]

        # function คำนวณการชนะ ในกรณีที่ผู้เล่นไม่ั่จั่วการ์ดเพิ่ม
        def result():
            result_player = player_card_result[0] + player_card_result[1]
            # เนื่องจากตามกฎแล้ว การ์ดหมายเลข 1 หรือ ace มีค่าได้ 2 ค่า คือ 1 และ 11 เพราะฉะนั้นแล้ว กรณีที่ผู้เล่นมีการ์ด 1 ที่บวกกันแล้วค่า < 22 จะถือว่าการ์ด 1 มีค่า = 11
            if result_player < 22:
                cards["1"] = 11
                result_player = player_card_result[0] + player_card_result[1]
            else:
                cards["1"] = 1
                result_player = player_card_result[0] + player_card_result[1]
            
            result_computer = computer_card_result[0] + computer_card_result[1]
            if result_computer < 22:
                cards["1"] = 11
                result_computer = computer_card_result[0] + computer_card_result[1]
            else:
                cards["1"] = 1
                result_computer = computer_card_result[0] + computer_card_result[1]
            
            if result_player == result_computer:
                print("You draw")
            elif result_player > result_computer and result_player <= 21:
                print("You win")
            elif result_player < result_computer or result_player > 21:
                print("You lose")

        # function คำนวณการชนะ ในกรณีที่ผู้เล่นจั่วการ์ดเพิ่ม
        def result_2():
            result_player = player_card_result[0] + player_card_result[1] + player_card_result[2]
            # ที่ไม่มี เงื่อนไขเหมือน 2 ใบก็เพราะว่า ไม่ว่าจะกรณีไหนที่มีการ์ด 3 ใบ ถ้าการ์ด 1 ทีค่า = 11 จะทำให้ผลรวมเกิน 21 เสมอ จึงไม่มีทางที่การ์ด 1 จะ = 11 ไม่งั้นผู้เล่นจะแพ้เสมอ
            result_computer = computer_card_result[0] + computer_card_result[1]
            if result_computer < 22:
                cards["1"] = 11
                result_computer = computer_card_result[0] + computer_card_result[1]
            else:
                cards["1"] = 1
                result_computer = computer_card_result[0] + computer_card_result[1]
                
            if result_player == result_computer:
                print("You draw")
            elif result_player > result_computer and result_player <= 21:
                print("You win")
            elif result_player < result_computer or result_player > 21:
                print("You lose")

        print(f"Your cards: {player_card}")
        print(f"Computer's first card: {show_computer_card}")
        draw_cards = input("Type 'yes' to get another card, type 'no' to pass: ").lower()
        if draw_cards == "yes":
            player_card = [card_player_1, card_player_2, new_deck_cards_2[0]]
            print(f"Your cards: {player_card}")
            print(f"Computer's card: {computer_card}")
            result_2()
        else:
            print(f"Your cards: {player_card}")
            print(f"Computer's card: {computer_card}")
            result()

    else:
        print("You should 'yes' or 'no'")


# my teacher version
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
# import random

# def deal_card():
#   """Returns a random card from the deck."""
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#   card = random.choice(cards)
#   return card

# #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
# #and returns the score. 
# #Look up the sum() function to help you do this.
# def calculate_score(cards):
#   """Take a list of cards and return the score calculated from the cards"""

#   #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#   if sum(cards) == 21 and len(cards) == 2:
#     return 0
#   #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
#   if 11 in cards and sum(cards) > 21:
#     cards.remove(11)
#     cards.append(1)
#   return sum(cards)

# #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
# def compare(user_score, computer_score):
#   #Bug fix. If you and the computer are both over, you lose.
#   if user_score > 21 and computer_score > 21:
#     return "You went over. You lose 😤"


#   if user_score == computer_score:
#     return "Draw 🙃"
#   elif computer_score == 0:
#     return "Lose, opponent has Blackjack 😱"
#   elif user_score == 0:
#     return "Win with a Blackjack 😎"
#   elif user_score > 21:
#     return "You went over. You lose 😭"
#   elif computer_score > 21:
#     return "Opponent went over. You win 😁"
#   elif user_score > computer_score:
#     return "You win 😃"
#   else:
#     return "You lose 😤"

# def play_game():

#   #Hint 5: Deal the user and computer 2 cards each using deal_card()
#   user_cards = []
#   computer_cards = []
#   is_game_over = False

#   for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

#   #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#   while not is_game_over:
#     #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     print(f"   Your cards: {user_cards}, current score: {user_score}")
#     print(f"   Computer's first card: {computer_cards[0]}")

#     if user_score == 0 or computer_score == 0 or user_score > 21:
#       is_game_over = True
#     else:
#       #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
#       user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#       if user_should_deal == "y":
#         user_cards.append(deal_card())
#       else:
#         is_game_over = True

#   #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
#   while computer_score != 0 and computer_score < 17:
#     computer_cards.append(deal_card())
#     computer_score = calculate_score(computer_cards)

#   print(f"   Your final hand: {user_cards}, final score: {user_score}")
#   print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
#   print(compare(user_score, computer_score))

# #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#   play_game()

