from ex3 import CardFactory
from ex3 import GameStrategy


class GameEngine:
    def __init__(self):
        self.card_factory = None
        self.game_strategy = None
        self.turns_simulated = 0
        self.total_damage = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.card_factory = factory
        self.game_strategy = strategy

    def simulate_turn(self) -> dict:
        hand = [
            self.card_factory.create_creature(),
            self.card_factory.create_spell(),
            self.card_factory.create_artifact()
        ]

        battlefield = []

        result = self.game_strategy.execute_turn(hand, battlefield)

        self.turns_simulated += 1
        self.total_damage += result['damage_dealt']

        return {
            'strategy': self.game_strategy.get_strategy_name(),
            'actions': result
        }

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.game_strategy.get_strategy_name()
            if self.game_strategy else None,
            'total_damage': self.total_damage,
            'cards_created': self.turns_simulated * 3
        }
