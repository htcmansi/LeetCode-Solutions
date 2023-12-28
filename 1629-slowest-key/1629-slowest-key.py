class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        m = releaseTimes[0]
        key = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > m or (duration == m and keysPressed[i] > key):
                m = duration
                key = keysPressed[i]
        return key