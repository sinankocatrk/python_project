#recursive rakam toplama bulma
def bul(x):
    if x<=0:
        return 0
    return x%10 + bul(x//10)


x=131
print(bul(x))
