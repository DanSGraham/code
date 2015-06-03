def create_objective(objective_distance):

    #creates random point on larger circle of radius "radius"
    objective_point_x = randint(-objective_distance,objective_distance)
    objective_point_y = math.sqrt(objectve_distance**2 - (objective_point_x)**2)
    choice = randint(1,2)
    if choice = 1
        objective_point_y = -objective_point_y
    objective_point = Point(objective_point_x,objective_point_y)
    return objective_point

def radar(objective_point,radar_scope):

    #draw background of radar
    radar_radius = 125
    radar_location = Point(-300,-300)
    radar = Circle(radar_location,radar_radius)
    radar.setFill('gray')
    

    #get target from parameter "objective_point" and put in into the radar
    objective_point_distance = math.sqrt((objective_point.getX())**2 + (objective_point.getY())**2)

    outer_circle = Circle(Point(500,500),radar_scope)
    if objective_point_distance < radar_scope:
        radar_target_x = (radar_radius*objective_point.getX())/float(radar_scope)
        radar_target_y = (radar_radius*objective_point.gety())/float(radar_scope)
        radar_target = Circle(Point(radar_target_x,radar_target_y),3)
        radar_target.setFill('green')
    else:
        radar_target_x = (radar_radius*objective_point.getX())/float(objective_point_distance)
        radar_target_y = (radar_radius*objective_point.getY())/float(objective_point_distance)
    return radar, radar_target
 
