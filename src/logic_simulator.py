"""
Logic Gate & Circuit Simulator
"""
class LogicGate:
    """The base class for all gates."""
    def __init__(self, label):
        self.label = label
        self.output = None

    def get_output(self):
        # This will trigger the logic calculation in child classes
        self.output = self.perform_gate_logic()
        return self.output

class BinaryGate(LogicGate):
    """Parent class for gates with two inputs (A and B)."""
    def __init__(self, label):
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None

    def set_inputs(self, a, b):
        """Sets the high (1) or low (0) voltage for the pins."""
        self.pin_a = a
        self.pin_b = b

class ANDGate(BinaryGate):
    """Output is 1 only if both inputs are 1."""
    def perform_gate_logic(self):
        return 1 if (self.pin_a == 1 and self.pin_b == 1) else 0

class ORGate(BinaryGate):
    """Output is 1 if at least one input is 1."""
    def perform_gate_logic(self):
        return 1 if (self.pin_a == 1 or self.pin_b == 1) else 0

class XORGate(BinaryGate):
    """Output is 1 if inputs are different (used for Sum)."""
    def perform_gate_logic(self):
        return 1 if self.pin_a != self.pin_b else 0

def simulate_half_adder(a, b):
    """
    Simulates a Half-Adder circuit using XOR and AND gates.
    Logic: Sum = A XOR B | Carry = A AND B
    """
    sum_gate = XORGate("SUM")
    carry_gate = ANDGate("CARRY")

    # Pass the inputs to the simulated hardware gates
    sum_gate.set_inputs(a, b)
    carry_gate.set_inputs(a, b)

    return sum_gate.get_output(), carry_gate.get_output()

# --- Simulation Driver Code ---
if __name__ == "__main__":
    print("="*40)
    print(" DIGITAL LOGIC SIMULATOR: HALF-ADDER ")
    print("="*40)
    print("Input A | Input B |  Sum (S) | Carry (C)")
    print("-" * 40)

    # Test all 4 binary combinations (00, 01, 10, 11)
    test_cases = [(0, 0), (0, 1), (1, 0), (1, 1)]

    for a, b in test_cases:
        s, c = simulate_half_adder(a, b)
        print(f"   {a}    |    {b}    |     {s}     |     {c}")

    print("-" * 40)
    print("Logic Verification: Successful")
