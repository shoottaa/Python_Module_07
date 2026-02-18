from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    game_state = {
        "player_mana": 6,
        "board": []
    }

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin = CreatureCard("Goblin Warrior", 2, "Common", 2, 2)

    print("CreatureCard Info:")
    info = dragon.get_card_info()
    info.update({
        "type": "Creature",
        "attack": dragon.attack,
        "health": dragon.health
    })
    print(info)

    print("\nPlaying Fire Dragon with 6 mana available:")
    print("Playable:", dragon.is_playable(game_state["player_mana"]))

    result = dragon.play(game_state)
    print("Play result:", result)

    print("\nFire Dragon attacks Goblin Warrior:")
    attack = dragon.attack_target(goblin)
    print("Attack result:", attack)

    print("\nTesting insufficient mana (3 available):")
    print("Playable:", dragon.is_playable(3))

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
