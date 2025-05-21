class Solution(object):
    def pgcd_algorithme_euclide(self,a,b):
        while(b!=0):
         reste=a%b
         a=b
         b=reste
        return a
    def countBeautifulPairs(self, nums):
        cpt=0
        taille=len(nums)
        for  i in range(taille):
         for j in range(i+1,taille):
           if self.pgcd_algorithme_euclide(int(str(nums[i])[0]),nums[j]%10)==1:
             cpt+=1
        return cpt
        