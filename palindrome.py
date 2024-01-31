def removeElement(nums, val):
    for i in nums:
        if i == val:
            nums.remove(val)
    return nums


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

# print(removeElement(nums, val))

s = "A man, a plan, a canal: Panama"

# print(len(s.split()[-1]))
ad = " "


def get_palindrome(s):
    ads = ''.join(filter(str.isalnum, s.lower()))
    i = 0
    j = len(ads) - 1
    while i < j:
        if ads[i] != ads[j]:
            return False
        i += 1
        j += 1
    return True


def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() == s[j].lower():
            i += 1
            j -= 1
        else:
            return False
    return True


print(get_palindrome(ad))
