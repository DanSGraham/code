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

def title(win_name):
    title_text = Text(Point(0,200), "Owl Game") #Change game title later
    title_text.setSize(35)
    title_text.setStyle('bold')
    title_text.draw(win_name)
    Easy = 0
    Normal = 0
    Hard = 0
    button1 = 0
    Easy = button(win_name, Easy, 200,100,-200,0, "North Pole: Few Obstacles (Easy)")
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
    #TITle of game and select difficulty
    title_text.undraw()
    if button1 != 0:
        return button1
def tutorial(win_name):
    
    tutorial_text = Text(Point (0,200), "Click to move owl! \nAvoid trees! \n Don't let Moldywart catch you!")
    tutorial_text.setSize(20)
    tutorial_text.draw(win_name)
    win_name.getMouse()
    tutorial_text.undraw()
def create_objective(objective_distance):

    #creates random point on larger circle of radius "radius"
    objective_point_x = random.randint(-objective_distance,objective_distance)
    objective_point_y = math.sqrt(objective_distance**2 - (objective_point_x)**2)
    choice = random.randint(1,2)
    if choice == 1:
        objective_point_y = -objective_point_y
    objective_point = Point(objective_point_x,objective_point_y)
    return objective_point

def radar(objective_point,radar_scope):
    #RADAR WOULD LOOK BETTER IF IT SHOWED OWL POSITION ON RADAR AS WELL. MAYBE A RED DOT IN THE MIDDLE. ALSO MAYBE A CROSSHAIR?
    #MAYBE LABEL POINT ON RADAR AS OBJECTIVE?
    #DISTANCES TO POINT ON RADAR? doesnt have to be on radar could be displayed at top by time or not.
    #COULD ALSO SHOW MOLDYWART ON RADAR IF TIME
    #draw background of radar
    radar_radius = 125
    radar_location = Point(-300,-300)
    radar = Circle(radar_location,radar_radius)
    radar.setFill('gray')
    

    #get target from parameter "objective_point" and put in into the radar
    objective_point_distance = math.sqrt((objective_point.getX())**2 + (objective_point.getY())**2)

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
#WE GO THOUGH THE TREE LIST A LOT. MAYBE HAVE A TREE CHECKER FUNCTION THAT ONLY GOES THROUGH ONCE AND MOVES AND CHECKS IN ONE LOOP?
def tree_boundary(tree_list):
    boundary_list = []
    proximity_list = []
    for tree in tree_list:
        if ((tree.getAnchor().getX())**2 + (tree.getAnchor().getY())**2)**0.5 < 100.0:
            proximity_list.append(tree)
    if proximity_list != []:
        for tree in proximity_list:
            #I THINK WHEN WE ADJUSTED THE COORDINATES THE TREE BOUNDARYS got messed up
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

def trees(win_name,location_trees):
    if location_trees == 'starting':
#To polish, draw the trees starting at the top of the window so that the trees overlap correctly
        random_x = random.randrange(-1000,1000)
        random_y = random.randrange(-1000,1000)
        while random_x < 250 and random_x > -250 and random_y < 250 and random_y > -250: #OBJECTIVE POINT GOES HERE :
            random_x = random.randrange(-1000,1000)
            random_y = random.randrange(-1000,1000)
        tree = Image(Point(random_x,random_y), 'owl_tree1.gif')

        tree.draw(win_name)
        return tree

    if location_trees == 'moving up':
        random_x = random.randrange(-1000,1000)
        random_y = random.randrange(700,1000)
        tree = Image(Point(random_x,random_y), 'owl_tree1.gif')

        tree.draw(win_name)
        return tree

    if location_trees == 'moving down':
        random_x = random.randrange(-1000,1000)
        random_y = random.randrange(-1000,-700)
        tree = Image(Point(random_x,random_y), 'owl_tree1.gif')

        tree.draw(win_name)
        return tree

    if location_trees == 'moving right':
        random_x = random.randrange(700,1000)
        random_y = random.randrange(-1000,1000)
        tree = Image(Point(random_x,random_y), 'owl_tree1.gif')

        
        tree.draw(win_name)
        return tree

    if location_trees == 'moving left':
        random_x = random.randrange(-1000,-700)
        random_y = random.randrange(-1000,1000)
        tree = Image(Point(random_x,random_y), 'owl_tree1.gif')

        tree.draw(win_name)
        return tree
        
    
    

##def objective():
## Multiple objectives with arrows pointing to each one. Go to post office first, then deliver package
##

    
    
#def lives(win_name, num_lives):
    #Counts and draws on screen the number of lives

def owl_move(win_name, difficulty, tree_list):

    #DIFF DIFFICLUTIES GIVE CERTAIN AMOUNT OF TIME UNTIL MOLDYWART ARRIVES
    #MOLDYWART ANIMATION
    mouse_point = 0
    location = 'starting'
    j = 0
    level_counter = 1
    moldywart_distance = (level_counter*1000+100000) #Allows twenty seconds to win. Need to display distance and allow more time
    warning_text = 0
    objective1 = create_objective(level_counter*1000+4000) #point cannot draw on a tree/trees.
    num_trees = 40
    background_image = Image(Point(0,0), 'grasstexture.gif')
    background_image.draw(win_name)
    owl = Image(Point(0,0), 'Owl.gif')
    owl.draw(win_name)
    objective_image = Image(objective1, 'objective_house.gif') #NEED TO MAKE BACKGROUND TRANSPARENT
    objective_image.draw(win_name)
    radar_circle = radar(objective1, 3000)[0]
    radar_circle.draw(win_name)
    radar_point = radar(objective1,3000)[1]
    radar_point.draw(win_name)
    next_step = True
    while next_step:
        

        elapsed_time = time.clock()
        
        time_display = Text(Point(0,-490), "Elapsed time: %2.4f seconds" %elapsed_time)
        time_display.draw(win_name)
        while len(tree_list) < num_trees:
            
            new_tree = trees(win_name,location)
            tree_list.append(new_tree)
            
            
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
            
        if mouse_point == 0:
            mouse_point = win_name.getMouse()
        else:
            mouse_point = win_name.checkMouse()
        if mouse_point != None:
            click_x = mouse_point.getX()
            click_y = mouse_point.getY()
            distance = ((click_x)**2 + (click_y)**2)**0.5  #this value may be slowing us down. Maybe limit it to a certain decimal so it doesnt have a huge float decimal number
            move_amntx = -(click_x)/distance
            move_amnty = -(click_y)/distance
            objective1.move(move_amntx*difficulty, move_amnty*difficulty)
            objective_image.move(move_amntx*difficulty, move_amnty*difficulty)
            for tree in tree_list:
                tree.move(move_amntx*difficulty, move_amnty*difficulty) # One way to make faster is to multiply the move amount variables by a constant
                if tree.getAnchor().getY() >  1000:
                    tree_list.remove(tree)
                    tree.undraw()
                    location = 'moving down'
                    
                elif tree.getAnchor().getX() < -1000:
                    tree_list.remove(tree)
                    tree.undraw()
                    location = 'moving right'
                    
                elif tree.getAnchor().getY() < -1000:
                    tree_list.remove(tree)
                    tree.undraw()
                    location = 'moving up'
                    
                elif tree.getAnchor().getX() > 1000:
                    tree_list.remove(tree)
                    tree.undraw()
                    location = 'moving left'
                if tree.getAnchor().getX()<objective1.getX() + 150 and tree.getAnchor().getX() > objective1.getX()-150 and tree.getAnchor().getY() < objective1.getY() + 150 and tree.getAnchor().getY() > objective1.getY() - 150:
                    tree.undraw()
        else:
           objective1.move(move_amntx*difficulty, move_amnty*difficulty)
           objective_image.move(move_amntx*difficulty, move_amnty*difficulty)
           for tree in tree_list:
                tree.move(move_amntx*difficulty, move_amnty*difficulty) # ^^
                if tree.getAnchor().getY() >  1000:
                    tree_list.remove(tree)
                    tree.undraw()
                    location = 'moving down'
                    
                elif tree.getAnchor().getX() < -1000:
                    tree_list.remove(tree)
                    tree.undraw()
                    location = 'moving right'
                    
                elif tree.getAnchor().getY() < -1000:
                    tree_list.remove(tree)
                    tree.undraw()
                    location = 'moving up'
                    
                elif tree.getAnchor().getX() > 1000:
                    tree_list.remove(tree)
                    tree.undraw()
                    location = 'moving left'
            #for tree in tree_list:
               #NEED TO ADD PART TO REMOVE TREES FROM AROUND THE OBJECTIVE
        radar_point.undraw()       
        radar_point = radar(objective1, 3000)[1]
        radar_point.draw(win_name)
        if objective1.getX() < 100 and objective1.getX() > -100 and objective1.getY() < 100 and objective1.getY() > -100:
            next_step = False
            win_or_lose = "win!"
        time.sleep(0.005)
        time_display.undraw()
        moldywart_distance -= 1
        if warning_text == 0 and moldywart_distance <= 1000:
            warning_text = Text(Point(0,480), "DANGER: MOLDYWART APPROACHING")
            warning_text.draw(win_name)
        if moldywart_distance <= 0:
            win_or_lose = 'lose!'
            next_step = False
    return win_or_lose  
        

##def Moldywart():

def main():
    window = GraphWin("0wl", 1000,1000)
    window.setBackground('white')
    window.setCoords(-500,-500, 500,500)
    difficulty = title(window)
    if difficulty == "Easy":
        difficulty = 3
    elif difficulty == "Normal":
        difficulty = 4
    elif difficulty == "Hard":
        difficulty = 5
    tutorial(window)
    tree_list = []
    print owl_move(window, difficulty, tree_list)
   
    
    window.getMouse()
    window.close()
    
main()
    



