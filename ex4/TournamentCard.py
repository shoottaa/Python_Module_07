from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, defense: int, rating: int = 1200):
        super().__init__(name, cost, rarity)

        self.attack_power = attack
        self.defense = defense

        self.wins = 0
        self.losses = 0
        self.rating = rating

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters the arena"
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(0, incoming_damage - self.defense)
        return {
            "damage_taken": damage_taken,
            "still_alive": True
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "defense": self.defense
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "record": f"{self.wins}-{self.losses}",
            "rating": self.rating
        }
