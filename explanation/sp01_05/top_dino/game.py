from .deck import generate_dino_deck, split_deck, get_random_attr


def play():
    # 1 - Gerar o baralho
    dino_deck = generate_dino_deck()

    # 2 - Embaralhar e dividir o baralho em 2
    p1_deck, p2_deck = split_deck(dino_deck)

    # TODO:
    # - Retirar a lógica de comparação e prints do play
    # - Ajustar lógica para calcular quantas rodadas cada player venceu e determinar
    # vencedor do jogo
    for index, p1_card in enumerate(p1_deck):
        print()
        p2_card = p2_deck[index]
        attr_to_compare = get_random_attr(p1_deck[0])

        print('p1_card -> ', p1_card)
        print('p2_card -> ', p2_card)
        print('attr_to_compare -> ', attr_to_compare)

        if p1_card[attr_to_compare] > p2_card[attr_to_compare]:
            print(f"{p1_card['name']} WINS!")
        elif p2_card[attr_to_compare] > p1_card[attr_to_compare]:
            print(f"{p2_card['name']} WINS!")
        else:
            print('DRAW!')
