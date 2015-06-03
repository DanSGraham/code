#A Daily Journaling Program
#By Daniel Graham

import datetime
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#Add Ben Franklin Self Improvement Question.
def express_urself():
    header = '%02d/%02d/%02d\n' % (datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year)
    overview = raw_input("Briefly summarize what you did today: ")
    general = raw_input("Generally, how did you feel about today? ")
    general_confidence = raw_input("Generally, how confident did you feel today?(1-10) ")
    hours_sleep = raw_input("How many hours of sleep did you get last night? ")
    stress_level = raw_input("What is your stress level (1-10)? ")
    
    cool_thoughts_yn = raw_input("Did you have any cool thoughts today? ")
    if cool_thoughts_yn != "No" and cool_thoughts_yn != 'no':
        cool_thoughts = raw_input("What cool thoughts did you have? ")
    else:
        cool_thoughts = "None"
        
    diet_subjective_yn = raw_input("Do you feel like you ate healthy today? ")
    if diet_subjective_yn != "yes" and diet_subjective_yn != "Yes":
        diet_explaination = raw_input("Why not? ")
    else:
        diet_explaination = "None"

    diet_objective_breakfast = raw_input("What did you eat for breakfast? ")
    diet_objective_lunch = raw_input("What did you eat for lunch? ")
    diet_objective_dinner = raw_input("What did you eat for dinner? ")
    
        
    exercise_yn = raw_input("Did you exercise today? ")
    exercise_dict = {}
    if exercise_yn != "No" and exercise_yn != "no":
        while True:
            exercise_type = raw_input("What kind of exercise did you do?(x to stop) ")
            if exercise_type == 'x':
                break
            exercise_feel = raw_input("How did you feel about your performance? ")
            exercise_performance = raw_input("Enter your times/weights(if none type 'None'): ")
            exercise_dict[exercise_type] = (exercise_feel, exercise_performance)
    else:
        exercise_type = "None"
        exercise_feel = "None"
        exercise_performance = "None"
        
    humor_yn = raw_input("Did you say/do a joke today? ")
    if humor_yn != "No" and humor_yn != "no":
        humor_delivery = raw_input("Did it go over well?(1-10) ")
        humor_subjective = raw_input("How funny did you think it was?(1-10) ")

    else:
        humor_delivery = "None"
        humor_subjective = "None"

    classes_dict = {}
    while True:
        class_subject = raw_input("Please enter a class or enter x to stop:(ex CHE250)" )
        if class_subject == 'x':
            break
        academics_subjective = raw_input("How did you feel about that class today? ")
        academics_objective_yn = raw_input("Did you have any grades returned? ")
        if academics_objective_yn != "no" and academics_objective_yn != "No":
            academics_objective = raw_input("What was the assignment and grade? (ex. TEST1:A, ...) ")
        else:
            academics_objective = "None"
        classes_dict[class_subject] = (academics_subjective, academics_objective)

    other_people = raw_input("How did you feel about other people today? ")
    social_interaction_yn = raw_input("Did you spend time with someone else today? ")
    if social_interaction_yn != "no" and social_interaction_yn != "No":
        social_interaction = raw_input("Who did you spend time with? ")
    else:
        social_interaction = "None"
        

    ambition_yn = raw_input("Did you work on a project today? ")
    if ambition_yn != "no" and ambition_yn != "No":
        ambition_work = raw_input("What project did you work on? ")
    else:
        ambition_work = "None"

    waste_time_yn = raw_input("Do you feel like you wasted time today? ")
    if waste_time_yn != "no" and waste_time_yn != "No":
        waste_time = raw_input("How much time did you waste?(In hours) ")
        waste_time_activity = raw_input("What did you waste time with? ")
        waste_time_capacity = raw_input("How much time did you have to waste?(In hours) ")
    else:
        waste_time = "0"
        waste_time_activity = "None"
        waste_time_capacity = "0"

    claire_from_me = raw_input("How did you feel about Claire today? ")
    claire_to_me = raw_input("How do you think Claire felt about you? ")

    sex_yn = raw_input("Did you have sex today? ")
    if sex_yn != "no" and sex_yn != "No":
        sex = raw_input("How did you feel about sex today? ")
    else:
        sex = "None"
        
    masterbation_yn = raw_input("Did you masterbate today? ")
    if masterbation_yn != "no" and masterbation_yn != "No":
        porn_yn = raw_input("Did you watch porn today? ")
        masterbation = raw_input("How did you feel about masterbation today? ")
    else:
        porn_yn = "None"
        masterbation = "None"
        
    read_yn = raw_input("Did you read today? ")
    if read_yn != "No" and read_yn != "no":
        read_book = raw_input("What did you read? ")
        read_time = raw_input("How long did you read? ")
    else:
        read_book = "None"
        read_time = "None"

    weird_yn = raw_input("Did anything weird happen today? ")
    if weird_yn != "no" and weird_yn != "No":
        weird = raw_input("What happened? ")
    else:
        weird = "None"

    dream_yn = raw_input("Do you remember your dream last night? ")
    if dream_yn != "no" and dream_yn != "No":
        dream = raw_input("Please describe your dream: ")
    else:
        dream = "I could not remember"

    happy = raw_input("Did you feel happy today?(1-10) ")
    accomplishment = raw_input("Did you feel accomplished today?(1-10) ")
    focus = raw_input("How focused did you feel today?(1-10) ")
    misc_thoughts = raw_input("Any other thoughts about today? ")

    #creative_options = [poem, joke, short_story]
    exercise_string = ""
    for key in exercise_dict:
        exercise_string += key + ":\n" + exercise_dict[key][0] + "\nTimes/Weights:" + exercise_dict[key][1] + "\n"
        
    classes_string = ""
    for key in classes_dict:
        classes_string += key + ":\n" + classes_dict[key][0] + "\nGrades:" + classes_dict[key][1] + "\n"


    string_to_write = header + "Overview:\n" + overview + "\n" + general + "\n" + "General Confidence: " + general_confidence + "\n" + "Hours of sleep: " + hours_sleep + "\n" + \
                      "Stress level: " + stress_level + "\n" + "Intersting thoughts:\n" + cool_thoughts + "\n" + "Diet:\n   Breakfast: " + \
                      diet_objective_breakfast + "\n   Lunch: " + diet_objective_lunch + "\n   Dinner: " + diet_objective_dinner + "\n   Unhealthy excuse:\n" + \
                      diet_explaination + "\nExercise:\n" + exercise_string + \
                      "\nHumor\n   How was it recieved? \n" + humor_delivery + "\n   How did I feel about it?\n" + humor_subjective + "\nAcademics:\n" + \
                      classes_string + "\nSocial:\n   Claire:\n   I felt this way about Claire:\n" + \
                      claire_from_me + "\n   I think Claire felt this way about me:\n" + claire_to_me + "\n   In general I felt this about others:\n" + other_people + \
                      "\n   I hung out with:" + social_interaction + "\nAmbition:\n   Today I worked on:\n" + ambition_work + "\nWaste:\n   I wasted " + waste_time + \
                      " hours doing: " + waste_time_activity + "\nI had " + waste_time_capacity + " hours to waste. I wasted " + (str(float(waste_time) - float(waste_time_capacity))) + \
                      " too many hours.\nSex:\n   I felt this way about sex:\n" + sex + "\n   I felt this way about masterbation:\n" + \
                      masterbation + "\n   Porn:" + porn_yn + "\nOther:   \nReading:\n   I read " + read_book + " for " + read_time + "\n" + weird + "\nHappiness: " + happy + "\nAccomplishment: " + \
                      accomplishment + "\nFocus:" + focus + "\nDream:\n" + dream +  "\nMisc.\n" + misc_thoughts + "\n\n"
    
    month = month_list[int(datetime.datetime.now().month) - 1]
    year = str(datetime.datetime.now().year)
    fout = open(month + year + ".txt", "a")
    fout.write(string_to_write)
    fout.close()


    if month == 'Jan' and int(datetime.datetime.now().day) == 1:

        #Yearly Review
        print "This is a yearly review. Take your time with these responses and try to think holistically for all of last year."
        print
        print

        year_well = raw_input("What went well this year?" )
        year_unwell = raw_input("What did not go so well this year? ")
        future = raw_input("What am I working towards? ")

        fout2 = open(year + "InReview.txt", "w")
        fout2.write("What went well:\n\n" + year_well + "\n\n What didn't go well:\n\n" + year_unwell + "\n\nFuture Plans:\n\n" + future)
        fout2.close()
        
    
express_urself()   
    
    
