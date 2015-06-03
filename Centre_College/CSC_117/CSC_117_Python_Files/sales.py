from graphics import *

win = GraphWin("Owlet Scouts", 500,200)
welcome_text = Text(Point(250, 20), "Enter how many of each item you would like to purchase! \n Click when finished")
botts_l_text = Text(Point(200, 80), "Number of large bags of Bott's Beans: ")
botts_s_text = Text(Point(200, 100),"Number of small bags of Bott's Beans: ")
frogs_text = Text(Point(240, 120), "Number of chocolate frogs: ")
botts_l_entry = Entry(Point(400,80), 10)
botts_s_entry = Entry(Point(400,100),10)
frogs_entry = Entry(Point(400,120),10)
welcome_text.draw(win)
botts_l_text.draw(win)
botts_s_text.draw(win)
frogs_text.draw(win)
botts_l_entry.draw(win)
botts_s_entry.draw(win)
frogs_entry.draw(win)
win.getMouse()
botts_l = float(botts_l_entry.getText())
botts_s = float(botts_s_entry.getText())
frogs = float(frogs_entry.getText())
cost_botts_l = botts_l * 10
cost_botts_s = botts_s * 6.0
cost_frogs = frogs *5.5
total_cost = cost_botts_l + cost_botts_s + cost_frogs
total_cost_message = "The cost of your order is:     $" + str(total_cost)

total_cost_text = Text(Point(275,150), total_cost_message)
total_cost_text.draw(win)




win.getMouse()
win.close()


