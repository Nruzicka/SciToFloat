import re

#Returns the amount of decimals the number should contain. 
def get_precision(sci_num: str) -> int:
    sci_num = ''.join(char.lower() if char == 'E' else char for char in sci_num)
    base, exp = sci_num.split("e")
    if int(exp) < 0:
        if "." in base:
            base_dec = len(base.split(".")[1])
        else:
            base_dec = 0
        return int(abs(int(exp)) + base_dec)

#Takes a number (in string value) in scientific notation and changes it to a float. 
def exp_to_float(val: str) -> str:
    if re.match(r'[-+?[0-9]*\.?[0-9]+[Ee][-+]?[0-9]+', val):
        try:
            precision = get_precision(val)
            return f"{float(val):.{precision}f}"
        except ValueError:
            pass
    return val
