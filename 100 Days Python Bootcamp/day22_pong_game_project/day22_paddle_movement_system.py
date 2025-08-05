# Movement flags
paddle1_up = False
paddle1_down = False
paddle2_up = False
paddle2_down = False

# Paddle 1 control functions
def paddle1_up_press():
    global paddle1_up
    paddle1_up = True

def paddle1_up_release():
    global paddle1_up
    paddle1_up = False

def paddle1_down_press():
    global paddle1_down
    paddle1_down = True

def paddle1_down_release():
    global paddle1_down
    paddle1_down = False

# Paddle 2 control functions
def paddle2_up_press():
    global paddle2_up
    paddle2_up = True

def paddle2_up_release():
    global paddle2_up
    paddle2_up = False

def paddle2_down_press():
    global paddle2_down
    paddle2_down = True

def paddle2_down_release():
    global paddle2_down
    paddle2_down = False