class Madre:
    def __init__(self):
        print(f"Soy Madre")


class Padre:
    def __init__(self):
        print(f"Soy Padre")


class Hijo(Madre, Padre):
    def __init__(self):
        Madre.__init__(self)
        Padre.__init__(self)
        print(f"Soy Hijo")


hijo = Hijo()
