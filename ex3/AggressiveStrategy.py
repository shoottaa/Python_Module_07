from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        mana_available = 5

        hand_sorted = []
        for card in hand:
            hand_sorted.append(card)

        for i in range(len(hand_sorted)):
            for j in range(i + 1, len(hand_sorted)):
                if hand_sorted[i].cost > hand_sorted[j].cost:
                    temp = hand_sorted[i]
                    hand_sorted[i] = hand_sorted[j]
                    hand_sorted[j] = temp

        for card in hand_sorted:
            if mana_used + card.cost <= mana_available:
                cards_played.append(card.name)
                mana_used += card.cost

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': ['Enemy Player'],
            'damage_dealt': 8
        }

    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets
