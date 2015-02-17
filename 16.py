class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if num is None or len(num) < 3 : return None
        num.sort()
        closest, value = None, None
        for i in range(len(num)):
            a = num[i]
            start = i + 1 
            end = len(num) - 1
            while start < end :
                b, c = num[start], num[end]
                t = target - a - b - c
                if closest is None or abs(t) < closest:
                    closest = abs(t)
                    value = a + b + c
                if t > 0 :
                    start += 1
                elif t < 0:
                    end -= 1
                else:
                    return target
        return value
