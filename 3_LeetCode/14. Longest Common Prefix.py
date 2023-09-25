def longestCommonPrefix(strs: List[str]) -> str:
    common = ''
    for i in range(len(strs[0])):
        for word in strs:
            if i == len(word) or word[i] != strs[0][i]:
                return common
        common += strs[0][i]
    return common