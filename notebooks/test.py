from qcodes.instrument_drivers.QuantumDesign.DynaCoolPPMS import DynaCool

dynacool = DynaCool("dynacool", address="TCPIP0::127.0.0.1::5000::SOCKET")
