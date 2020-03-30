class Target:

    def request(self):
        return "Target: The default target's behavior."


class LegacyCode:

    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):

    def __init__(self, legacy_code):
        self.legacy_code = legacy_code

    def request(self):
        return f"Adapter: (TRANSLATED) {self.legacy_code.specific_request()[::-1]}"


def client_code(target):
    print(target.request(), end='')


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print('\n')

    legacy_code = LegacyCode()
    print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
    print(f"Adaptee: {legacy_code.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter(legacy_code)
    client_code(adapter)