# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH/2, HEIGHT /2]
ball_vel = [120.0/60.0, -120.0/60.0]
paddle1_pos1 = [0+HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]
paddle1_pos2 = [0+HALF_PAD_WIDTH, HEIGHT/2 + HALF_PAD_HEIGHT]
paddle2_pos1 = [WIDTH-PAD_WIDTH+HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]
paddle2_pos2 = [WIDTH-PAD_WIDTH+HALF_PAD_WIDTH, HEIGHT/2 + HALF_PAD_HEIGHT]
paddle1_vel = [0,0]
paddle2_vel = [0,0]
score1 = 0
score2 = 0
direction = "RIGHT"

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT /2]
    if direction == "RIGHT":
        ball_vel = [random.randrange(120.0/60, 240/60), -(random.randrange(60.0/60, 180.0/60))]       
    else:
        ball_vel = [-(random.randrange(120.0/60, 240/60)), -(random.randrange(60.0/60, 180.0/60))]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0

def draw(c):
    global score1, score2, paddle1_pos1, paddle2_pos1, paddle1_pos2, paddle2_pos2, ball_pos, ball_vel
    global direction
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
       
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # fall into gutter or collide and reflect off of paddle  
    direction_rand = random.randrange(0,2)
    if direction_rand == 0:
        direction = "RIGHT"
    else:
        direction = "LEFT"
    
    if ball_pos[1]> paddle1_pos1[1] - BALL_RADIUS and ball_pos[1]<paddle1_pos2[1]+ BALL_RADIUS:
        hitleft = True
    else:
        hitleft = False
   
    if ball_pos[1]> paddle2_pos1[1] - BALL_RADIUS and ball_pos[1]<paddle2_pos2[1] + BALL_RADIUS:
        hitright = True
    else:
        hitright = False
        
    add_speed = 30.0/60
    
    if ball_pos[0] <= BALL_RADIUS+ PAD_WIDTH and hitleft == False:
        direction = "RIGHT"
        spawn_ball(direction)
        score2 +=1
    if ball_pos[0] <= BALL_RADIUS+ PAD_WIDTH and hitleft == True:
        if ball_vel[0] < 0:
            ball_vel[0]-=add_speed
        else:
            ball_vel[0] += add_speed
        if ball_vel[1] < 0:
            ball_vel[1]-=add_speed
        else:
            ball_vel[1] += add_speed
        ball_vel[0] = - ball_vel[0]        
    if ball_pos[0] >= WIDTH-1-BALL_RADIUS-PAD_WIDTH and hitright == False:
        direction = "LEFT"
        spawn_ball(direction)
        score1+= 1
    if ball_pos[0] >= WIDTH-1-BALL_RADIUS-PAD_WIDTH and hitright == True:
        if ball_vel[0] < 0:
            ball_vel[0]-=add_speed
        else:
            ball_vel[0] += add_speed
        if ball_vel[1] < 0:
            ball_vel[1]-=add_speed
        else:
            ball_vel[1] += add_speed
        ball_vel[0] = - ball_vel[0]        
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        pass
    if ball_pos[1] >= HEIGHT-1-BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
            
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "Black", "Pink")    
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos1[1] = paddle1_pos1[1] + paddle1_vel[1]   
    paddle1_pos2[1] = paddle1_pos2[1] + paddle1_vel[1]
    paddle2_pos1[1] = paddle2_pos1[1] + paddle2_vel[1]
    paddle2_pos2[1] = paddle2_pos2[1] + paddle2_vel[1]
    
    if paddle1_pos1[1] < 0:
        paddle1_pos1[1] = 0
        paddle1_pos2[1] = PAD_HEIGHT
        
    if  paddle1_pos1[1] > HEIGHT - PAD_HEIGHT - 1:
        paddle1_pos1[1] = HEIGHT -1 - PAD_HEIGHT
        paddle1_pos2[1] = HEIGHT - 1
    
    if paddle2_pos1[1] < 0:
        paddle2_pos1[1] = 0
        paddle2_pos2[1] = PAD_HEIGHT
        
    if  paddle2_pos1[1] > HEIGHT - PAD_HEIGHT - 1:
        paddle2_pos1[1] = HEIGHT -1 - PAD_HEIGHT
        paddle2_pos2[1] = HEIGHT - 1    
       
    # draw paddles
    c.draw_line(paddle1_pos1,paddle1_pos2,PAD_WIDTH,"Yellow")
    c.draw_line(paddle2_pos1,paddle2_pos2,PAD_WIDTH,"Green")
    
    # draw scores
    c.draw_text(str(score1), (WIDTH/4, HEIGHT/4), 50, 'Yellow')
    c.draw_text(str(score2), (WIDTH-WIDTH/4-1, HEIGHT/4), 50, 'Green')
        
def keydown(key):
    acc = 10
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = -acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = -acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0
    
def restart_handler():
    global direction
    spawn_ball(direction)
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart_handler, 100)

# start frame
new_game()
frame.start()
