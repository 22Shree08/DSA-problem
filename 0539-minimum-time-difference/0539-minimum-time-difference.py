class Solution:
    def findMinDifference(self, timePoints):
        minutes = []

        for t in timePoints:
            h, m = t.split(":")
            total = int(h) * 60 + int(m)
            minutes.append(total)

        minutes.sort()
        ans = 1440

        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i - 1]
            ans = min(ans, diff)

        diff = 1440 - minutes[-1] + minutes[0]
        ans = min(ans, diff)

        return ans