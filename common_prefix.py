strings = ["flower", "flow", "flight"]


def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for word in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
            i += 1
            prefix = prefix[:i]
            if not prefix:
                break
    return prefix


word_list = ["apple", "apricot", "apartment", "apocalypse"]
result = longest_common_prefix(strings)
print("Longest Common Prefix:", result)
