from typing import List
from qcodes.instrument import Instrument
from qcodes.parameters import Parameter


class BaseVoltageSource(Instrument):
    """
    Abstract Instrument representing voltage source with some range
    """

    def __init__(self, name: str):
        super().__init__(name)

        self.voltage = self.add_parameter("voltage", abstract=True)
        self.phase = self.add_parameter("phase", abstract=True)


class DensityParameter:
    def __init__(
        self,
        displacement: Parameter,
        capacitances: List[float],
        voltages: List[BaseVoltageSource],
    ):
        self.D = displacement
        self.Caps = capacitances
        self.Vsrcs = voltages

    def get_dennsity(self) -> float:
        sum = 0
        for i in range(len(self.Caps)):
            sum += self.Caps[i] * self.Vsrcs[i].voltage()
        return sum

    def set_density(self, setpoint: float):
        raise NotImplementedError
