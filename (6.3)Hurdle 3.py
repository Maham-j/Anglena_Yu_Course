def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():        
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    sound(True)
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
      


#while at_goal != True:
 #   jump()
    
   
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
