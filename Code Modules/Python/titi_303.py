# Folder: code_modules\python\driver
# Filename: tti_303.py
# --- returns the visa reference
def initialize(resource:str): pass
# --- set output voltage for given channel
def set_voltage(ref, chn:str, voltage:float): pass
# --- set output current limit for given channel
def set_current_limit(ref, chn:str, i_limit:float): pass
# --- set output state (on/off) for the given channel
def set_output_state(ref, chn:str, state:bool): pass
# -- resets the power supply to default values, set output always off
def reset(ref): pass
# -- returns the errors captured by the power supply
def get_errors(ref): pass
# -- returns the *IDN? query
def get_id(ref): pass
# -- close the visa reference
def close(ref): pass

if __name__ == "__main__":
# place here some function calls to test your code. For instance
    resource = 'PSU02'
    ref = initialize(resource)
    print(reset(ref))
    close(ref)
