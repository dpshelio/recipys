from fruits import avocado, lemon
from condiment import salt, olive_oil

def guacamole(people=1):
    bowl = avocado.peel() + lemon.drop(2) + salt.pinch() + olive_oil.ts()
    return bowl.blend() * people

