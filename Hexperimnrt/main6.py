class Lights:
    light_state=False
    def tur1():
      light_state=True
    def tur0():
      light_state=False

light = Lights

print(light.light_state)

def turn_on_switch():
    """Turns off the light"""
    light.tur1
    return "turned on lights"

def turn_off_switch():
    """Turns ON the light"""
    light.tur0
    return "turn of lights"

print(light.light_state)
turn_on_switch()
print(light.light_state)
turn_off_switch()
print(light.light_state)
turn_on_switch()
print(light.light_state)
turn_off_switch()
print(light.light_state)
turn_on_switch()