import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class Deck:
    def __init__(self, cards: list[Card]) -> None:
        self.cards = cards

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card: Card) -> None:
        self.cards.remove(card)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop(0)
        else:
            raise IndexError("Deck is empty")

    def get_deck_stats(self) -> dict:
        return {
            'total_cards': len(self.cards),
            'creatures': sum(1 for card in self.cards
                             if isinstance(card, CreatureCard)),
            'spells': sum(1 for card in self.cards
                          if isinstance(card, SpellCard)),
            'artifacts': sum(1 for card in self.cards
                             if isinstance(card, ArtifactCard)),
            'avg_cost': (round(sum(card.cost for card in self.cards)
                         / len(self.cards), 1) if self.cards else 0.0)
        }
