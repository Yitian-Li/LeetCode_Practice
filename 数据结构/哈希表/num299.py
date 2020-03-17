class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_cnt = collections.Counter(secret)
        guess_cnt = collections.Counter(guess)
        for x, y in zip(secret, guess):
            if x == y:
                bulls += 1
                secret_cnt[x] -= 1
                guess_cnt[y] -= 1
        
        for k in secret_cnt:
            if k in guess_cnt:
                cows += min(secret_cnt[k], guess_cnt[k])
        
        return str(bulls)+'A'+str(cows)+'B'