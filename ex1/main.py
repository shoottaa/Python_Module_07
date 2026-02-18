from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    dragon = CreatureCard("Fire Dragon", 4, "Legendary", 7, 5)
    lightning = SpellCard("Lightning Bolt", 4, "Rare", "damage")
    crystal = ArtifactCard("Mana Crystal", 4, "Common", 5, "+1 mana per turn")

    deck = Deck([])

    deck.add_card(dragon)
    deck.add_card(lightning)
    deck.add_card(crystal)

    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:")

    card1 = deck.draw_card()
    print(f"\nDrew: {card1.name} (Spell)")
    if isinstance(card1, CreatureCard):
        print("Play result:", card1.play({'player_mana': 10, 'board': []}))
    else:
        print("Play result:", card1.play({}))

    card2 = deck.draw_card()
    print(f"\nDrew: {card2.name} (Artifact)")
    if isinstance(card2, CreatureCard):
        print("Play result:", card2.play({'player_mana': 10, 'board': []}))
    else:
        print("Play result:", card2.play({}))

    card3 = deck.draw_card()
    print(f"\nDrew: {card3.name} (Creature)")
    if isinstance(card3, CreatureCard):
        print("Play result:", card3.play({'player_mana': 10, 'board': []}))
    else:
        print("Play result:", card3.play({}))

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
    )


if __name__ == "__main__":
    main()
