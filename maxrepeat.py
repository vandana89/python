string=input("enter string")
common_char=' '
max_count=0
for char in string:
    if char not in common_char:
        count=string.count(char)
        if count>max_count:
            max_count=count
            common_char=char
print(common_char)
print(max_count)
