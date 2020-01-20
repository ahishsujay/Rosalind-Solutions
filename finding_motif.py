def PatternIndex(s,t):
    index = []
    for i in range(0,len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            print(i+1,end="\t")
