class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=input()
        a= {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum=0
        flag=0
        for i in range(len(s)):
            if(flag==1):
                flag=0
                continue
            if i!=len(s)-1:
                if(s[i]=="I" and s[i+1]=="V"):
                    sum+=4
                    break
                elif(s[i]=="I" and s[i+1]=="X"):
                    sum+=9
                    break
                elif(s[i]=="X" and s[i+1]=="L"):
                    sum+=40
                    flag=1
                elif(s[i]=="X" and s[i+1]=="C"):
                    sum+=90
                    flag=1
                elif(s[i]=="C" and s[i+1]=="D"):
                    sum+=400
                    flag=1
                elif(s[i]=="C" and s[i+1]=="M"):
                    sum+=900
                    flag=1
                else:
                    sum+=a[s[i]]
            else:
                sum+=a[s[i]]
        return sum