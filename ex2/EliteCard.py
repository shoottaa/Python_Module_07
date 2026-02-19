from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, defense: int, mana_pool: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.mana_pool = mana_pool

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': "Elite card summoned with combat and magic abilities"
        }

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(0, incoming_damage - self.defense)
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': self.defense,
            'still_alive': damage_taken < self.defense
        }

    def get_combat_stats(self) -> dict:
        return {
            'name': self.name,
            'attack_power': self.attack_power,
            'defense': self.defense
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': 4
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            'channeled': amount,
            'total_mana': self.mana_pool
        }

    def get_magic_stats(self) -> dict:
        return {
            'name': self.name,
            'mana_pool': self.mana_pool
        }
