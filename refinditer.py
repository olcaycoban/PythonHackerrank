import re

def solve(expressions,pattern):
    matches = list(re.finditer(r'(?={})'.format(pattern), expressions))    
    return matches

def main():
    express = input()
    patrs=input()
    a=solve(express,patrs)
    for i in a:
        print((i.start(),i.end()+len(patrs)-1))
if __name__=='__main__':
    main()
