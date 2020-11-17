import re

def solve(expressions,pattern):
    matches = list(re.finditer(r'(?={})'.format(pattern), expressions))    
    if matches:
        for i in matches:
            print((i.start(),i.end()+len(pattern)-1))
    else:
        print((-1,-1))  
def main():
    express = input()
    patrs=input()
    solve(express,patrs) 
if __name__=='__main__':
    main()
