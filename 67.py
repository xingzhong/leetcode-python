class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        la, lb, flag = len(a), len(b), '0'
        def add(x, y, f):
            num = [x,y,f].count('1')
            if num == 0 : return '0', '0'
            if num == 1 : return '1', '0'
            if num == 2 : return '0', '1'
            if num == 3 : return '1', '1'
            
        res = []  
        while la > 0 and lb > 0:
            r, flag = add(a[la-1], b[lb-1], flag)
            res.append(r)
            la -= 1
            lb -= 1
        while la > 0 :
            r, flag = add(a[la-1], '0', flag)
            res.append(r)
            la -= 1
        while lb > 0 :
            r, flag = add('0', b[lb-1], flag)
            res.append(r)
            lb -= 1
        if flag == '1':
            res.append(flag)
        return "".join(res[::-1])
