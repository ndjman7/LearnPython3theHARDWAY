formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("하나", "둘", "셋", "넷"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "난 이게 있죠.",
    "지금 막 써 주신 것 그것.",
    "하지만 '노래' 하진 않아요.",
    "그러니까 잘 자요."
))
