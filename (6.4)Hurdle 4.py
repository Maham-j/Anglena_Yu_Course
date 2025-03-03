def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    while not at_goal():
        if  wall_on_right():
            turn_left()
        else:
            move()
        while wall_on_right() and not at_goal()and not wall_in_front():
            move()
        if not wall_on_right():
            turn_right()
            move()
            turn_right()
            while not wall_in_front():
                move()
            
        
        
while front_is_clear():
    move()
else:
    jump()            


   
    



#while at_goal != True:
 #   jump()
    
   
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
