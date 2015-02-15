class Solution:
    def compareVersion(self, version1, version2):
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        l1, l2 = len(v1), len(v2)
        if l1 > l2:
            for i in range(l1-l2):
                v2.append(0)
        else:
            for i in range(l2-l1):
                v1.append(0)
        for i in range(min(len(v1), len(v2))):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0

