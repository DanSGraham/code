import random

def main():
   again = 'y'
   while again == 'y':
       Slytherin = ["Daniel Graham", "David Newton", "Sarah Baliak", "Levi Sledd"]
       Elphabanana = ["Christopher Brittain", "Michael Yu", "Tristan Conroy"]
       GrandAlf = ["Colin Wurster", "Daniel Curran", "Han He", "Ye Sheng"]
       Huffandpuff =  ['Bingxu Ren', 'Forrest Kamperman', 'Nicolas Montejos', 'Philip Barsotti']
       Cravenclaw = ['Samuel Lane', 'William Thackery', 'Yifan Li']
       Gryffinsnore = ["Austin Sargraves", "John Coogan", "Matt Schendstok"]
       selected_names = []

       house_list = [Elphabanana, GrandAlf, Huffandpuff, Cravenclaw, Gryffinsnore]
       house_list1 = [Slytherin, Elphabanana, GrandAlf, Huffandpuff, Cravenclaw, Gryffinsnore]
       house_list_string = ['Slytherin', 'Elphaba', 'Gandalf', 'Hufflepuff', 'Ravenclaw', 'Gryffindor']
       random.shuffle(house_list)
       for j in range(6):
           if j%2 == 0:
               selected_house = Slytherin
           else:
               selected_house = house_list[j-1]
           x = 'n'
           num = 0
           random.shuffle(selected_house)
           while x == 'n':
         
            
               selected_hero = selected_house[num]
               for name in selected_names:
                   if name == selected_hero:
                       selected_hero = selected_house[num+1]
               selected_names.append(selected_hero)            
               print "The champion for " + str(house_list_string[house_list1.index(selected_house)]) + " is " + str(selected_hero) + "."
               x = raw_input( "Enter 'n' if he/she isn't here: ")
               print
               num +=1
               if num > len(selected_house)-1:
                   print 'Oh no! '
                   x = 'n'
       again = raw_input("Go around again?")


       #For the glory of Salazar!
main()