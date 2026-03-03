from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        effect_messages = {
            'damage': f'Deal {self.cost} damage to target',
            'heal': f'Heal {self.cost} health to target',
            'buff': f'Buff target by {self.cost}',
            'debuff': f'Debuff target by {self.cost}',
        }
        effect_msg = effect_messages.get(self.effect_type, self.effect_type)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': effect_msg
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            'spell_name': self.name,
            'effect_type': self.effect_type,
            'targets': targets
        }
