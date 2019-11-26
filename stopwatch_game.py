# template for "Stopwatch: The Game"
import simplegui
# define global variables
current_time = 0
perfect_stops = 0
stop_count = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t/60000
    B = t%60000/10000
    C = t%10000/1000
    D = t%1000/100
    formatted_string = str(A)+":"+str(B)+str(C)+"."+str(D)
    return formatted_string
   
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global current_time
    timer.start()
    

def stop_handler():
    global current_time, perfect_stops, stop_count
    if timer.is_running() == True:
        stop_count+=1
        pass
    if timer.is_running() == True and current_time%1000 == 0:
        perfect_stops+=1
    timer.stop()
    
    
def reset_handler():
    global current_time, perfect_stops, stop_count
    timer.stop()
    current_time = 0
    perfect_stops = 0
    stop_count = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global current_time
    current_time += 100
        
# define draw handler
def draw_handler(canvas):
    """Draw the circle."""
    time_now = format(current_time)
    canvas.draw_text(time_now, [100, 150], 35,  "Pink", "sans-serif")
    canvas.draw_text(str(perfect_stops)+"/"+str(stop_count),[200, 30], 30,  "Green", "monospace")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300,300)


# register event handlers
timer = simplegui.create_timer(100, tick)
frame.add_button("Start", start_handler, 100)
frame.add_button("Stop", stop_handler, 100)
frame.add_button("Reset", reset_handler, 100)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
timer.start()
timer.stop()

# Please remember to review the grading rubric