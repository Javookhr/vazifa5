def son(n):
    yegindi = 0
    while n > 0:
        yegindi += n % 10
        n //= 10
    return yegindi
print(son(108))  