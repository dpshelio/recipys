from fruits import avocado, lime, apple
from condiment import salt, olive_oil, pepper

def guacamole(people=1):
    bowl = avocado.peel().unseed() + lime.drop(2) + salt.pinch() + olive_oil.ts()
    return bowl.blend() * people

if __name__ == '__main__':
    print(guacamole(2))

