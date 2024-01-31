input_string = "ahbgdc"
substring = "abc"


is_substring = False
list_sub = list(substring)
list_inp_str = list(input_string)


for i in list_sub:
    if i in list_inp_str:
        list_inp_str.remove(i)
        list_sub.remove(i)
        if len(list_sub)==0:
            print(True)

