def longestPalSubstr(string): 
    maxLength = 1
    start = 0
    length = len(string) 
  
    low = 0
    high = 0
  
    # One by one consider every character as center point of  
    # even and length palindromes 
    for i in range(1, length): 
        # Find the longest even length palindrome with center 
        # points as i-1 and i. 
        low = i - 1
        high = i 
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
        # Find the longest odd length palindrome with center  
        # point as i 
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
    return maxLength 


# Driver Code 
t = int(input())
for _ in range(t):
    inp = input()
    N = len(inp)
    dp = [[] for j in range(N)]
    for i in range(N-1):
        for j in range(i+1,N+1):
            dp[i].append(longestPalSubstr(inp[i:j]))
    dp[0][-1] = 0
    dp[-1].append(1)
    max = 0
    for i in range(N-1):
        if(dp[0][i] + dp[i+1][-1] > max):
            max = dp[0][i] + dp[i+1][-1]
    print(max)
