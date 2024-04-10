class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = deque()
        result.append(deck.pop())
        while deck:
            result.appendleft(result.pop())
            result.appendleft(deck.pop())
        return list(result)
        