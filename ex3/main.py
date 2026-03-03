from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")

    print("Available types:", factory.get_supported_types())

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("\nSimulating aggressive turn...")
    turn_result = engine.simulate_turn()

    hand = turn_result['hand']
    hand_str = (
        f"Hand: [{hand[0].name} ({hand[0].cost}), "
        f"{hand[1].name} ({hand[1].cost}), "
        f"{hand[2].name} ({hand[2].cost})]"
    )
    print(hand_str)

    print("\nTurn execution:")
    print("Strategy:", turn_result['strategy'])
    print("Actions:", turn_result['actions'])

    print("\nGame Report:")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: "
        "Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
