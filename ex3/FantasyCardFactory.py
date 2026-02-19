from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power=None):
        return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    def create_spell(self, name_or_power=None):
        return SpellCard("Goblin Warrior", 2, "Rare", "damage")

    def create_artifact(self, name_or_power=None):
        return ArtifactCard("Lightning Bolt", 3, "Common", 5,
                            "+1 mana per turn")

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for i in range(size):
            if i % 3 == 0:
                deck.append(self.create_creature())
            elif i % 3 == 1:
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())

        return {
            'deck': deck,
            'size': len(deck),
            'theme': 'Fantasy'
        }

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
