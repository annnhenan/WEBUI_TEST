class Solution:
    def getpermutation(self, n, k):
        fact = [1] * (n + 1)
        for i in range(1, n+1):
            fact[i] = fact[i - 1] * i
        n_list = [i for i in range(1, n + 1)]
        return self.finder(n, k-1, n_list, fact)

    def finder(self, n, k, n_list, fact):
        if n == 1:
            return str(n_list[0])
        m = k // fact[n - 1]
        k %= fact[n - 1]
        res = str(n_list[m])
        n_list.remove(n_list[m])
        res += self.finder(n - 1, k, n_list, fact)
        return res

