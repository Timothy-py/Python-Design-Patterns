# DEMONSTRATING THE DIFFERENCE BETWEEN FACTORY AND BUILDER DESIGN PATTERN

# This code demonstrate a client buying a new computer whereby the computer is a specific and a preconfigured
# computer model, that is, all the hardware specifications are already predefined by the manufacturer.
# This is achieved through the Factory Design Pattern.
MINI14 = '1.4GHz Mac mini'


class ComputerFactory:
    def __init__(self):
        self.memory = 4
        self.hdd = 500
        self.gpu = 'Intel HD Graphics 5000'

    def __str__(self):
        info = (
            f"Model: {MINI14}",
            f"Memory: {self.memory}GB",
            f"Hard Disk: {self.hdd}GB",
            f"Graphics Card: {self.gpu}"
        )
        return '\n'.join(info)

    def build_computer(self, model):
        if model == "MINI14":
            return self.__str__()
        else:
            msg = f"I don't know how to build {model}"
            print(msg)


if __name__ == '__main__':
    fac = ComputerFactory()
    mac_mini = fac.build_computer("MINI14")
    print(mac_mini)


# This code demonstrate a client buying a new computer whereby a client gives order to the manufacturer concerning
# the ideal computer specifications he/she wants.
# This is achieved through the Builder Design Pattern

class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = (
            f"Memory: {self.memory}GB",
            f"Hard Disk: {self.hdd}GB",
            f"Graphics Card: {self.gpu}",
        )
        return '\n'.join(info)


# Builder
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('AG23385193')

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, amount):
        self.computer.gpu = amount


# Director
class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        steps = (
            self.builder.configure_memory(memory),
            self.builder.configure_hdd(hdd),
            self.builder.configure_gpu(gpu)
        )
        [step for step in steps]

    @property
    def computer(self):
        return self.builder.computer


def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(memory=8, hdd=500, gpu='GeForce GIX 650 Ti')
    computer = engineer.computer
    print(computer)


if __name__ == '__main__':
    main()
