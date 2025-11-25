s = input()
ans = ""
found_first = False
first_index = 0
for i, symbol in enumerate(s):
    if symbol.isupper() and not found_first:
        ans += symbol
        found_first = True
        first_index = i
    if found_first:
        if symbol.isdigit():
            ans += s[i + 1]
            step = i + 1 - first_index
            j = i + 1 + step
            while s[j] != ".":
                ans += s[j]
                j += step
            ans += s[j]
            break
print(ans)
