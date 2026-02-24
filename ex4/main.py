from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...\n")

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 8, 3, 1200)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 6, 4, 1150)

    id1 = "dragon_001"
    id2 = "wizard_001"

    platform.cards[id1] = dragon
    platform.cards[id2] = wizard

    print(f"Fire Dragon (ID: {id1}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}\n")

    print(f"Ice Wizard (ID: {id2}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}\n")

    print("Creating tournament match...")
    result = platform.create_match(id1, id2)
    print("Match result:", result, "\n")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    rank = 1
    for cid, card in leaderboard:
        print(f"{rank}. {card.name} - Rating: {card.rating} ({card.wins}-{card.losses})")
        rank += 1

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
