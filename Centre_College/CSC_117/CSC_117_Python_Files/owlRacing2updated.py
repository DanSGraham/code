#Obstacles: Different kinds of trees? Castles/houses? 


#New features: Portals? Rogue Bludgers? Wizards on brooms in the background
#Around Christmas, the trees become christmas trees.
#The game changes with seasons? Shadows for time of day?
# Story?
# Way to subtly incorporate Slytherin
#Add music


from graphics import *
import random
from custom_library import *
import math



##
##def background():
##Add some kind of ground/clouds/other stuff in background


#Create main menu with selection of difficulty
def title(win_name):
    title_text = Text(Point(0,200), "Owl Game") 
    title_text.setSize(35)
    title_text.setStyle('bold')
    title_text.draw(win_name)
    Easy = 0
    Normal = 0
    Hard = 0
    button1 = 0

    #uses self-created button module (author: Daniel Graham)
    Easy = button(win_name, Easy, 200,100,-200,0, "Bunny Slope: Few Obstacles (Easy)")
    Normal = button(win_name, Normal, 200,-100,-200,-200, "Grasslands: Normal Obstacles (Normal) ")
    Hard = button(win_name, Hard, 200,-300,-200,-400, "Forest: Many Obstacles (Hard)")
    button_returned = button_check(win_name)
    if button_returned == Easy:
        button1 = "Easy"
    elif button_returned == Normal:
        button1 = "Normal"
    elif button_returned == Hard:
        button1 = "Hard"
    button_undraw(button_list)
    title_text.undraw()
    if button1 != 0:
        return button1

#Second graphic window introduces basic instructions depending on terrain 
def tutorial(win_name, difficulty):
    if difficulty == 'Easy':
        tutorial_text = Text(Point (0,200), "Click to move owl! \n \n Deliver your packages to houses (green dot on radar)! \n \n Avoid snowmen! \n \n Don't let Moldywart catch you!")
        tutorial_text.setSize(20)
    if difficulty == 'Normal':
        tutorial_text = Text(Point (0,200), "Click to move owl! \n \n Deliver your packages to houses (green dot on radar)! \n \n Avoid trees! \n \n Don't let Moldywart catch you!")
        tutorial_text.setSize(20)
    if difficulty == 'Hard':
        tutorial_text = Text(Point (0,200), "Click to move owl! \n \n Deliver your packages to houses (green dot on radar)! \n \n Avoid trees! \n \n Don't let Moldywart catch you! \n \n \n Good Luck...")
        tutorial_text.setSize(20)
    tutorial_text.draw(win_name)
    win_name.getMouse()
    tutorial_text.undraw()

#creates random point a designated distance away
def create_objective(objective_distance):

    #creates random point on larger circle
    #finds random x value then plugs into pythagorean theorem and solves for y value
    objective_point_x = random.randint(-objective_distance,objective_distance)
    objective_point_y = math.sqrt(objective_distance**2 - (objective_point_x)**2)

    #squaroot can be positive or negative so we put it at a 50% chance either way
    choice = random.randint(1,2)
    if choice == 1:
        objective_point_y = -objective_point_y
    objective_point = Point(objective_point_x,objective_point_y)
    return objective_point

#draws radar so user knows where objective is when it is off-screen
def radar(objective_point,radar_scope):

    #uses proportions of similar triangles to scale distance between
    #owl and created objective to fit nicely on the radar 
    objective_point_distance = math.sqrt((objective_point.getX())**2 + (objective_point.getY())**2)
    radar_radius = 12

    #if the owl is further than a specified distance from the objective,
    #then the objective on the radar will remain on the edge of the circle
    #in the direction of the objective
    outer_circle = Circle(Point(500,500),radar_scope)
    if objective_point_distance < radar_scope:
        radar_target_x = (radar_radius*objective_point.getX())/float(radar_scope) - 300
        radar_target_y = (radar_radius*objective_point.getY())/float(radar_scope) - 300
        
    else:
        radar_target_x = (radar_radius*objective_point.getX())/float(objective_point_distance) -300
        radar_target_y = (radar_radius*objective_point.getY())/float(objective_point_distance) -300
    radar_target = Circle(Point(radar_target_x,radar_target_y),3)
    radar_target.setFill('green')
    return radar, radar_target

#checks to see if owl has hit any trees if applicable
def tree_boundary(tree_list):
    boundary_list = []
    proximity_list = []
    for tree in tree_list:
        if ((tree.getAnchor().getX())**2 + (tree.getAnchor().getY())**2)**0.5 < 100.0:
            proximity_list.append(tree)
    if proximity_list != []:
        for tree in proximity_list:
            low_leftx = tree.getAnchor().getX() - 57
            low_lefty = tree.getAnchor().getY() + 94
            low_rightx = tree.getAnchor().getX() + 57
            low_righty = tree.getAnchor().getY() + 94
            upper_x = tree.getAnchor().getX()
            upper_y = tree.getAnchor().getY() - 59
            boundary_list.append(low_leftx)
            boundary_list.append(low_lefty)
            boundary_list.append(low_rightx)
            boundary_list.append(low_righty)
            boundary_list.append(upper_x)
            boundary_list.append(upper_y)
            boundary_list.append(tree.getAnchor().getX())
            boundary_list.append(tree.getAnchor().getY())
        return boundary_list

#checks to see if owl has hit any snowmen, if applicable  
def snowman_boundary(obstacle_list):
    boundary_list = []
    proximity_list = []
    for snowman in obstacle_list:
        if ((snowman.getAnchor().getX())**2 + (snowman.getAnchor().getY())**2)**0.5 < 200.0:
            proximity_list.append(snowman)
    if proximity_list != []:
        for snowman in proximity_list:
            bottom_circlex = snowman.getAnchor().getX() +12
            bottom_circley = snowman.getAnchor().getY() -49
            middle_circlex = snowman.getAnchor().getX() + 8
            middle_circley = tree.getAnchor().getY() - 5
            top_circlex = snowman.getAnchor().getX()+ 6
            top_circley = snowman.getAnchor().getY() + 29
            boundary_list.append(bottom_circlex)
            boundary_list.append(bottom_circley)
            boundary_list.append(middle_circlex)
            boundary_list.append(middle_circley)
            boundary_list.append(top_circlex)
            boundary_list.append(top_circley)
        return boundary_list
    
#This function chooses the obstacle type based on the terrain, randomly places the obstacles in the window,
#moves the obstacles in the opposite direction that the user clicks (to simulate movement), deletes
#obstalces if they go too far off screen, and creates obstacles just off the screen in the 'direction' that
#the user is 'flying.'
def obstacle(window_name,location_obstacle, obstacle_type):

    #obstacle type based on terrain
    snowmen_images = ['Snowman_blue.gif', 'Snowman_purple.gif', 'Snowman_green.gif', 'Snowman_yellow.gif', 'Snowman_orange.gif']
    if obstacle_type == 'snowmen':
        obstacle_image = snowmen_images[random.randrange(6)]
    else:
        obstacle_image = 'owl_tree1.gif'

    #places obstacles randomly depending on situation
    if location_obstacle == 'starting':

        random_x = random.randrange(-1000,1000)
        random_y = random.randrange(-1000,1000)
        while random_x < 250 and random_x > -250 and random_y < 250 and random_y > -250:
            random_x = random.randrange(-1000,1000)
            random_y = random.randrange(-1000,1000)
        obstacle = Image(Point(random_x, random_y), obstacle_image)

        obstacle.draw(window_name)
        return obstacle

    if location_obstacle == 'moving up':
        random_x = random.randrange(-1000,1000)
        random_y = random.randrange(700,1000)
        obstacle = Image(Point(random_x, random_y),obstacle_image)

        obstacle.draw(window_name)
        return obstacle

    if location_obstacle == 'moving down':
        random_x = random.randrange(-1000,1000)
        random_y = random.randrange(-1000,-700)
        obstacle = Image(Point(random_x, random_y),obstacle_image)

        obstacle.draw(window_name)
        return obstacle

    if location_obstacle == 'moving right':
        random_x = random.randrange(700,1000)
        random_y = random.randrange(-1000,1000)
        obstacle = Image(Point(random_x, random_y),obstacle_image)

        obstacle.draw(window_name)
        return obstacle

    if location_obstacle == 'moving left':
        random_x = random.randrange(-1000,-700)
        random_y = random.randrange(-1000,1000)
        obstacle = Image(Point(random_x, random_y),obstacle_image)

        obstacle.draw(window_name)
        return obstacle

#Sets up background and obstacles for terrain and draws
#radar and owl.
def game_window_setup(win_name, difficulty):
    if difficulty == 'Easy':
        background_image = Image(Point(0,0), 'snow.gif')
        background_image.draw(win_name)
        obstacles = 'snowmen'
    else:
        background_image = Image(Point(0,0), 'grasstexture.gif')
        background_image.draw(win_name)
        obstacles = 'trees'
    owl = Image(Point(0,0), 'Owl.gif')
    owl.draw(win_name)
    radar = Image(Point(-300,-300), 'radar.gif')
    radar.draw(win_name)
    return obstacles
    
        
#This function is somewhat dense and executes the "playing" of the game.
def owl_move(win_name, difficulty, obstacle_type):

    #several variables require a neutral assignment before they are used
    obstacle_list = []
    mouse_point = 0
    location = 'starting'
    level_counter = 1
    
    num_obstacles = 10
    j = 0
    time_sleep_value = .005
    num_trees = 5
    next_step = True
    win_or_lose = 'win!'
    score = 0

    #"Moldywart," a bad guy trying to catch you, is simulated.
    moldywart_distance = (level_counter*1000+100000)
    warning_text = 0
    objective1 = create_objective(level_counter*1000+4000)

    #image for objective and radar
    objective_image = Image(objective1, 'objective_house.gif')
    objective_image.draw(win_name)
    radar_point = radar(objective1,3000)[1]
    radar_point.draw(win_name)


    #game keeps running as long as user doesn't hit an obstacle. Redraws new objective and radar point if the user keeps getting to the objective.
    #Increases speed of obstacle movement as the user progresses
    while win_or_lose == 'win!':
        next_step = True
        moldywart_distance = (level_counter*1000+100000) #Allows twenty seconds to win. Need to display distance and allow more time
        warning_text = 0
        mouse_point = 0
        location = 'starting'
        objective1 = create_objective(level_counter*1000+4000)
        objective_image = Image(objective1, 'objective_house.gif') 
        objective_image.draw(win_name)
        radar_circle = radar(objective1, 3000)[0]
        radar_circle.draw(win_name)
        radar_point = radar(objective1,3000)[1]
        radar_point.draw(win_name)
        difficulty = difficulty + .2
        time_sleep_value = time_sleep_value - time_sleep_value/4

        #executes one level of gameplay
        while next_step:
            
            #time monitor
            elapsed_time = time.clock()
            
            time_display = Text(Point(0,-490), "Elapsed time: %0.2f seconds" %elapsed_time)
            time_display.draw(win_name)

            #creates new_obstacles as others disappear (idea credit to Dr. Stonedahl's "spider nasty" example)
            while len(obstacle_list) < num_obstacles:

                new_obstacle = obstacle(win_name,location, obstacle_type)
                obstacle_list.append(new_obstacle)
            if obstacle_type == 'snowmen':
                if snowman_boundary(obstacle_list) != None:
                    boundary_list = tree_boundary(tree_list)
                       
                    for i in range(len(boundary_list)/6):  #The numbers following are coordinates of points that make up 3 circles that define the snowman boundary
                        if boundary_list[i*6] < 120 and boundary_list[i*6] > -120 and boundary_list[((i*6)+1)] < 35 and  boundary_list[((i*6)+1)] > -35 :
                           next_step = False
                           win_or_lose = 'Lose!'
                        elif boundary_list[i*6+2] < 120 and boundary_list[i*6+2] > -120 and boundary_list[((i*6)+3)] < 35 and  boundary_list[((i*6)+3)] > -35:
                           next_step = False
                           win_or_lose = 'Lose!'
                        elif boundary_list[i*6+4] < 120 and boundary_list[i*6+4] > -120 and boundary_list[((i*6)+5)] < 35 and  boundary_list[((i*6)+5)] > -35:
                           next_step = False
                           win_or_lose = 'Lose!'

                
            else:    
                if tree_boundary(tree_list) != None:
                    boundary_list = tree_boundary(tree_list)
                       
                    for i in range(len(boundary_list)/8):  #The numbers following are coordinates of points that make up a triangle that defines the owl boundary
                        if boundary_list[i*8] < 120 and boundary_list[i*8] > -120 and boundary_list[((i*8)+1)] < 35 and  boundary_list[((i*8)+1)] > -35 :
                           next_step = False
                           win_or_lose = 'Lose!'
                        elif boundary_list[i*8+2] < 120 and boundary_list[i*8+2] > -120 and boundary_list[((i*8)+3)] < 35 and  boundary_list[((i*8)+3)] > -35:
                           next_step = False
                           win_or_lose = 'Lose!'
                        elif boundary_list[i*8+4] < 120 and boundary_list[i*8+4] > -120 and boundary_list[((i*8)+5)] < 35 and  boundary_list[((i*8)+5)] > -35:
                           next_step = False
                           win_or_lose = 'Lose!'
                        elif boundary_list[i*8+6] < 120 and boundary_list[i*8+6] > -120 and boundary_list[((i*8)+7)] < 30 and  boundary_list[((i*8)+7)] > -30:
                            next_step = False
                            win_or_lose = 'Lose!'
                            
           #waits for user to click, then begins game     
            if mouse_point == 0:
                mouse_point = win_name.getMouse()
            else:
                mouse_point = win_name.checkMouse()
            if mouse_point != None:
                click_x = mouse_point.getX()
                click_y = mouse_point.getY()

                #moves trees in opposite derection of owl to simulate movement.
                #No matter how far away from the owl the user clicks, the owl
                #goes the same speed.
                distance = ((click_x)**2 + (click_y)**2)**0.5  
                move_amntx = -(click_x)/distance
                move_amnty = -(click_y)/distance
                objective1.move(move_amntx*difficulty, move_amnty*difficulty)
                objective_image.move(move_amntx*difficulty, move_amnty*difficulty)
                for obstacle in obstacle_list:
                    obstacle.move(move_amntx*difficulty, move_amnty*difficulty) # One way to make faster is to multiply the move amount variables by a constant
                    if obstacle.getAnchor().getY() >  1000:
                        obstacle_list.remove(obstacle)
                        obstacle.undraw()
                        location = 'moving down'
                        
                    elif obstacle.getAnchor().getX() < -1000:
                        obstacle_list.remove(obstacle)
                        obstacle.undraw()
                        location = 'moving right'
                        
                    elif obstacle.getAnchor().getY() < -1000:
                        obstacle_list.remove(obstacle)
                        obstacle.undraw()
                        location = 'moving up'
                        
                    elif obstacle.getAnchor().getX() > 1000:
                        obstacle_list.remove(obstacle)
                        obstacle.undraw()
                        location = 'moving left'
                    if obstacle.getAnchor().getX()< objective1.getX() + 150 and obstacle.getAnchor().getX() > objective1.getX()-150 and obstacle.getAnchor().getY() < objective1.getY() + 150 and obstacle.getAnchor().getY() > objective1.getY() - 150:
                        obstacle.undraw()
            else:
               objective1.move(move_amntx*difficulty, move_amnty*difficulty)
               objective_image.move(move_amntx*difficulty, move_amnty*difficulty)
               for obstacle in obstacle_list:
                    obstacle.move(move_amntx*difficulty, move_amnty*difficulty) 
                    if obstacle.getAnchor().getY() >  1000:
                        obstacle_list.remove(obstacle)
                        obstacle.undraw()
                        location = 'moving down'
                        
                    elif obstacle.getAnchor().getX() < -1000:
                        obstacle_list.remove(obstacle)
                        obstacle.undraw()
                        location = 'moving right'
                        
                    elif obstacle.getAnchor().getY() < -1000:
                        obstacle_list.remove(obstacle)
                        obstacle.undraw()
                        location = 'moving up'
                        
                    elif obstacle.getAnchor().getX() > 1000:
                        obstacle_list.remove(obstacle)
                        obstacle.undraw()
                        location = 'moving left'
                    if obstacle.getAnchor().getX()< objective1.getX() + 150 and obstacle.getAnchor().getX() > objective1.getX()-150 and obstacle.getAnchor().getY() < objective1.getY() + 150 and obstacle.getAnchor().getY() > objective1.getY() - 150:
                        obstacle.undraw()
            radar_point.undraw()       
            radar_point = radar(objective1, 3000)[1]
            radar_point.draw(win_name)

            #if user gets to objective
            if objective1.getX() < 100 and objective1.getX() > -100 and objective1.getY() < 100 and objective1.getY() > -100:
                next_step = False
                win_or_lose = "win!"
            time.sleep(0.005)
            time_display.undraw()
            moldywart_distance -= 1
            #if caught by Moldywart
            if warning_text == 0 and moldywart_distance <= 1000:
                warning_text = Text(Point(0,480), "DANGER: MOLDYWART APPROACHING")
                warning_text.draw(win_name)
            if moldywart_distance <= 0:
                win_or_lose = 'lose!'
                next_step = False
    return score
        

#ending screen returns score and message
def ending(score):
    win = GraphWin("Score", 500,500)
    win.setCoords(-5,-5,5,5)
    if score == 1:
        score_string = "You delivered 1 package."
    else:
        score_string = "You delivered " + str(score) + " packages."
    score_text = Text(Point(0,2),score_string)
    score_text.draw(win)
    if score == 0:
        message = "I've seen blind, one winged owls do better than that.\n You can do much better."
    elif 1 < score < 2:
        message = "Not too bad, but you'll need to get better \n before you can find your first delivery job."
    elif 2 < score < 5:
        message = "Pretty good! You have great potential. \n Keep up the good work!"
    elif 6 < score < 10: 
        message = "You have acheived the status of a very skilled deliverer.\n You have much reason to be proud."
    else:
        message = "Wow! You are truly a master of the delivering arts.\n We are truly impressed and humbled \n by your incredible skill. \n You must be a Slytherin!"
    text = Text(Point(0,0),message)
    text.draw(win)
    win.getMouse()
    win.close()
    
def main():
    window = GraphWin("0wl", 1000,1000)
    window.setBackground('white')
    window.setCoords(-500,-500, 500,500)
    difficulty = title(window)
    tutorial(window,difficulty)
    obstacle_type = game_window_setup(window, difficulty)
    score = owl_move(window, difficulty, 'snowmen')
    
    ending(score)
   

    
main()
    



