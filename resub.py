import re
    
def solve(expression):
    sym = expression.group(0)
    
    if sym == "&&":
        return "and"
    elif sym == "||":
        return "or"
def main():
    n = int(input().strip())
    for _ in range(n):
        print(re.sub(r'(?<= )(&&|\|\|)(?= )', solve, input()))
        
if __name__=='__main__':
    main()
