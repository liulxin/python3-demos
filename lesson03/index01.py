def sum(a, b):
    return a + b


print(sum(2, 4))


def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2
    return damage1, damage2


print(damage(1, 2))

sk_damage1, sk_damage2 = damage(1, 2)
print(sk_damage1, sk_damage2)

# 关键参数
print(damage(skill2=2, skill1=1))

# 默认参数（默认参数必须要放在形参的最后）
def default_fn(x, y, z=0, m=2):
    print(x, y, z, m)

default_fn(1, 2)  # 1 2 0 2
default_fn(1,2,m= 5) # 1 2 0 5
