import random

DINO_NAMES = (
    "Alenossauro Rex",
    "Lucirodonte",
    "Alex Raptor",
    "Caiquerátops",
    "Raphazilla",
    "Gustarodáctilo"
)


def generate_dino_deck() -> list[dict]:
    # Caso base 1
    # dino_cards = []

    # for dino_name in DINO_NAMES:
    #     dino_dict = {
    #         "name": dino_name,
    #         "strength": random.randint(1, 10),
    #         "agility": round(random.uniform(0, 10), 1),
    #         "heigth": round(random.uniform(0, 10), 2)
    #     }

    #     dino_cards.append(dino_dict)

    dino_cards = [
        {
            "name": dino_name,
            "strength": random.randint(1, 10),
            "agility": round(random.uniform(0, 10), 1),
            "heigth": round(random.uniform(0, 10), 2)
        }
        for dino_name in DINO_NAMES
    ]

    return dino_cards


def split_deck(deck: list[dict]) -> tuple[list[dict], list[dict]]:
    half_deck = len(deck) // 2

    random.shuffle(deck)

    # deck[:3]
    p1_deck = deck[:half_deck]
    # deck[3:]
    p2_deck = deck[half_deck:]

    # print('p1 deck:')
    # for card in p1_deck:
    #     print(card)

    # print()

    # print('p2 deck:')
    # for card in p2_deck:
    #     print(card)

    return p1_deck, p2_deck


def get_random_attr(card: dict) -> str:
    card_keys = card.keys()
    # print(list(card_keys))
    card_keys = [key for key in card.keys() if key != 'name']
    # print(card_keys)

    # 1.
    # 0 1 e 2
    # rand_int = random.randint(0, len(card_keys) - 1)
    # print(card_keys[rand_int])

    # 2.
    # print(random.choice(card_keys))

    return random.choice(card_keys)
