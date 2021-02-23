class Madre:
    def __init__(self):
        print("Soy Madre")


class Padre:
    def __init__(self):
        print("Soy Padre")


class Hijo(Madre, Padre):
    def __init__(self):
        Madre.__init__(self)
        Padre.__init__(self)
        print("Soy Hijo")


hijo = Hijo()
