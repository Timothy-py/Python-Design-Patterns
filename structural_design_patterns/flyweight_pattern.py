import json


class Flyweight:
    """
    The Flyweight stores a common portion of the state(intrinsic) that belongs to
    multiple real business entities. The Flyweight accepts the rest of the state(extrinsic)
    via its method parameters.
    """

    def __init__(self, intrinsic=''):
        self._intrinsic = intrinsic

    def operation(self, extrinsic=''):
        intrinsic = json.dumps(self._intrinsic)
        extrinsic = json.dumps(extrinsic)
        print(f"Flyweight: Displaying shared ({intrinsic}) and unique ({extrinsic}) state.", end='')


class FlyweightFactory:
    """
    The Flyweight Factory creates and manages the Flyweight objects. It ensures that flyweights
    are shared correctly. When the client requests a flyweight, that factory either returns
    an existing instance or creates a new one, if it doesn't exist yet.
    """

    _flyweights = dict()

    def __init__(self, initial_flyweight=[]):
        for state in initial_flyweight:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state=dict()):
        """
        returns a Flyweight's string hash for a given state.
        """
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state=dict()):
        """
        returns an existing Flyweight with a given state or creates a new one.
        """

        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self):
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(factory=FlyweightFactory, plates="", owner="", brand="", model="", color=""):
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight([brand, model, color])
    # The client code either stores or calculates extrinsic state and passes it to the flyweight's methods.
    flyweight.operation([plates, owner])


if __name__ == '__main__':
    """
    The client code usually creates a bunch of pre-populated flyweights in
    the initialization stage of the population.
    """

    factory = FlyweightFactory([
        ["Chevrolet", "Camero2018", 'Pink'],
        ['Mercedes Benz', 'C300', 'black'],
        ["Mercedes Benz", "C500", 'red'],
        ['BMW', 'M5', 'red'],
        ['BMW', 'X6', 'white'],
    ])

    factory.list_flyweights()

    add_car_to_police_database(factory, "CL234IR", 'Timothy', 'BMW', 'M5', 'red')
    add_car_to_police_database(factory, "CL234IR", 'Timothy', 'BMW', 'X1', 'red')

    print('\n')
    factory.list_flyweights()
