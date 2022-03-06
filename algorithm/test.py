from collections import Counter
def findLostCard(self, p):
    # write code here
    a = sorted(Counter(p).most_common(), key=lambda x: x[1])[0]
    return a[0]