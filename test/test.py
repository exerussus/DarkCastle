

_str = "123456789123"
max_num = 3

if len(_str) > max_num:
    _str = _str[:-(len(_str) - max_num)]

print(f"After: {_str =}")