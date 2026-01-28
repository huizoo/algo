import sys
input = sys.stdin.readline
M = 1000 - int(input())
print(M//500 + (M%500)//100 + (M%100)//50 + (M%50)//10 + (M%10)//5 + (M%5)//1)