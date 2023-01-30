# from top_dino import deck
# import try_except

# from top_dino.game import play
import top_dino


def printing_try_except():
    # res = try_except.example_1()
    # print(res)
    user = {'username': 'chrystian', 'password': '1234'}
    try:
        try_except.example_2(user)
    except KeyError as error:
        # print('key error tratado')
        print(error)


def main():
    # dino_deck = deck.generate_dino_deck()
    # for card in dino_deck:
    #     print(card)
    # p1_d, p2_d = deck.split_deck(dino_deck)
    top_dino.play()
    # play()


if __name__ == '__main__':
    main()
