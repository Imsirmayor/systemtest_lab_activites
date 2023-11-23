# Folder: code_modules\python\driver
# Filename: keysight_34450A.py
# -- returns the visa reference
def initialize(resource:str): pass
# -- configures the measurement mode: voltage, current, range and resolution
def configure_measurement(ref, mode:str, range:float, digits:float): pass
# -- set the input impedance for voltage measurements
def set_impedance(ref, impedance:float): pass
# -- returns a floating point number of the measurement
def measure(ref): pass
# -- resets the multimeter to default values
def reset(ref): pass
# -- returns the errors captured by the power supply
def get_errors(ref): pass
# -- returns the *IDN? query
def get_id(ref): pass
# -- close the visa reference
def close(ref): pass


if __name__ == "__main__":
    # place here some function calls to test your code. For instance
    resource = 'DMM02'
    ref = initialize(resource)
    print(measure(ref))
    close(ref)