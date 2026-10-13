# EXTREMELY ALPHA, EVERYTHING SUBJECT TO CHANGE
import time

switch_active = 1  # subject to change

# input state (switches & keypad)
states = {
    "west": 0,
    "north": 0,
    "south": 0,
    "east": 0
}

keypad_buffer = ""

# direction constants
dir_none = 0
dir_west = 1
dir_north = 2
dir_south = 3
dir_east = 4

# position class and player state
class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
player_pos = Position(0, 0)  # starting position

# switch inputs (selecting direction)
def debounce():
    time.sleep(0.005)

def read_switches():
    # pins values?
    west_value = switch_west.value()
    north_value = switch_north.value()
    south_value = switch_south.value()
    east_value = switch_east.value()
    
    # check switches, determine directional inputs
    
    # west, leftmost switch
    if states["west"] == 0 and west_value == switch_active:
        debounce()
        if switch_west.value() == switch_active:
            states["west"] = 1
            return dir_west
        
    # north, second switch
    if states["north"] == 0 and north_value == switch_active:
        debounce()
        if switch_north.value() == switch_active:
            states["north"] = 1
            return dir_north
        
    # south, third switch
    if states["south"] == 0 and south_value == switch_active:
        debounce()
        if switch_south.value() == switch_active:
            states["south"] = 1
            return dir_south
    
    # east, rightmost switch   
    if states["east"] == 0 and east_value == switch_active:
        debounce()
        if switch_east.value() == switch_active:
            states["east"] = 1
            return dir_east
        
    # update states when switch pressed
    states["west"]  = 1 if west_value  == switch_active else 0
    states["north"] = 1 if north_value == switch_active else 0
    states["south"] = 1 if south_value == switch_active else 0
    states["east"]  = 1 if east_value  == switch_active else 0
    
    return dir_none

# keypad input for distance
def keypad_debounce():
    time.sleep(0.01)
    
def read_numpad():
    global keypad_buffer
    
    # digit mapping
    digit_map = {
        "0": key_0,
        "1": key_1,
        "2": key_2,
        "3": key_3,
        "4": key_4,
        "5": key_5,
        "6": key_6,
        "7": key_7,
        "8": key_8,
        "9": key_9
    }

    # digits
    for digit, pin in digit_map.items():
        if pin.value() == 1:  # key press
            keypad_debounce()
            if pin.value() == 1:  # pressed after debounce
                keypad_buffer += digit
                return None
            
    # clear input (*)
    if key_star.value() == 1:
        keypad_debounce()
        if key_star.value() == 1:
            keypad_buffer = ""
            return None
        
    # confirm input (#)
    if key_hash.value() == 1:
        keypad_debounce()
        if key_hash.value() == 1:
            if keypad_buffer == "":
                return 0  # empty confirmation
            distance = int(keypad_buffer)
            keypad_buffer = ""
            return distance
        
    # no key pressed
    return None

# movement calculations
def direction_to_delta(direction):
    if direction == dir_west:
        return -1, 0
    if direction == dir_north:
        return 0, 1
    if direction == dir_south:
        return 0, -1
    if direction == dir_east:
        return 1, 0
    return 0, 0

def calculate_new_pos(current_pos, direction, distance):
    dx, dy = direction_to_delta(direction)
    new_x = current_pos.x + dx * distance
    new_y = current_pos.y + dy * distance
    return Position(new_x, new_y)

# movement validation (placeholder)
def validate_movement(new_pos):
    return True

# movement engine
def move_player():
    global player_pos
    
    # 1. direction
    direction = read_switches()
    if direction == dir_none:
        return  # no chosen direction
    
    # 2. distance
    distance = read_numpad()
    if distance is None:
        return  # still typing digits
    
    if distance <= 0:
        return  # invalid or empty input
    
    # 3. position computation
    new_pos = calculate_new_pos(player_pos, direction, distance)
    
    # 4. validation
    if not validate_movement(new_pos):
        out_of_bounds()
        return
    
    # 5. commit movement
    player_pos = new_pos
    

# handle out of bounds
def out_of_bounds():
    display.show("ERR")  # placeholder for display
    
    time.sleep(0.5)
    
    global keypad_buffer
    keypad_buffer = ""
    
    return

