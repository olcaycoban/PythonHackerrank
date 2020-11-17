import re
#1
expression=input()
pattern="[^aeiouAEIOU]?([aeiouAEIOU]{2,})[^aeiouAEIOU]"
values=re.findall(pattern,expression)
if (len(values)>0):
    for i in values:
        print(i)  
else:
    print(-1)
    
#2             
"""
def solve(S):
    vowel = '[aeiou]'
    consonant = '[qwrtypsdfghjklzxcvbnm]'
    return re.findall(r'{consonant}({vowel}{{2,}})(?={consonant})'.format(vowel=vowel, consonant=consonant), S, re.IGNORECASE)


def main():
    S = input()
    solution = solve(S)
    if solution:
        print(*solution,sep='\n')
    else:
        print(-1)
        
if __name__ == '__main__':
    main()
"""


#3
"""
expression=input()
pattern="[^aeiouAEIOU]?([aeiouAEIOU]{2,})[^aeiouAEIOU]"
values=re.findall(pattern,expression)
if len(values)>0:
    for i in values:
        print(i)    

m = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeıioAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.IGNORECASE)

if m:
    for s in m:
        print(s)
"""

