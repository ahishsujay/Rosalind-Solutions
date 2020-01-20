def CountingWords(s):
    count_dict = {}
    words = list(s.split(" "))

    for i in range(len(words)):
        count = 0
        for j in range(len(words)):
            if words[i] == words[j]:
                count += 1
        count_dict[words[i]] = count

    for key,value in count_dict.items():
        print(key,value)
