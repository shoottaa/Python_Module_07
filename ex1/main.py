from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def get_card_type(card):
    if isinstance(card, CreatureCard):
        return "Creature"
    elif isinstance(card, SpellCard):
        return "Spell"
    elif isinstance(card, ArtifactCard):
        return "Artifact"
    return "Card"


def main():
    print("=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    dragon = CreatureCard("Fire Dragon", 4, "Legendary", 7, 5)
    lightning = SpellCard("Lightning Bolt", 4, "Rare", "damage")
    crystal = ArtifactCard("Mana Crystal", 4, "Common", 5, "+1 mana per turn")

    deck = Deck()

    deck.add_card(dragon)
    deck.add_card(lightning)
    deck.add_card(crystal)

    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:")

    game_state = {'player_mana': 10, 'board': []}

    card1 = deck.draw_card()
    print(f"\nDrew: {card1.name} ({get_card_type(card1)})")
    print("Play result:", card1.play(game_state))

    card2 = deck.draw_card()
    print(f"\nDrew: {card2.name} ({get_card_type(card2)})")
    print("Play result:", card2.play(game_state))

    card3 = deck.draw_card()
    print(f"\nDrew: {card3.name} ({get_card_type(card3)})")
    print("Play result:", card3.play(game_state))

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
    )


if __name__ == "__main__":
    main()
