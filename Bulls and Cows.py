class Solution(object):
    def getHint(self, secret, guess):
        secret=list(secret)
        guess=list(guess)
        a=0
        b=0
        for i in range (len(guess)):
            if secret[i]==guess[i]:
                a+=1
        d=list(zip(secret,guess))
        for i in secret:
            if i in guess:
                b+=1
                guess.remove(i)
        secret="".join([str(a), "A",str(b-a), "B"])
        return(secret)