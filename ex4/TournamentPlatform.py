import uuid
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self):
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = str(uuid.uuid4())[:8]
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack_power > card2.attack_power:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        return sorted(
            self.cards.items(),
            key=lambda item: item[1].rating,
            reverse=True
        )

    def generate_tournament_report(self) -> dict:
        avg_rating = (
            sum(card.rating for card in self.cards.values())
            // len(self.cards)
        )

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
