def isIsomorphic(s, t):
    s_dict = {}
    for i in range(len(s)):
        if s[i] in s_dict.keys() and s_dict[s[i]] != t[i]:
            return False
        s_dict[s[i]] = t[i]
    return True
s=raw_input("enter the 1st string ")
t=raw_input("enter the 2nd String :")
print isIsomorphic(s,t)
