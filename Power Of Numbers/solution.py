class Solution:
    def reverse_exponentiation(self, n):
        temp=str(n)
        temp=temp[::-1]
        temp=int(temp)
        return pow(n,temp)
        
