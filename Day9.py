'''QUE:- Mr Richard Tupper is purchasing gifts for his family.So far he has purchased the following
*3 sweaters, each valued at $68
*1 computer game valued at $75
*2 bracelets, each valued at $43
Later he returned one of the bracelets for a full refund and received a $10 rebate on the computer game.What is the total cost of the gifts
after the refund and rebate?
Calclation part of the program should be under three lines'''
#ANSWER

sweaterPr=68
sweatcnt=3
compGamePr=75
compcnt=1
braceletPr=43
braceletcnt=2

returnbracelet=1
rebateGame=10

totalcost=(sweaterPr*sweatcnt)+(compGamePr*compcnt)+(braceletPr*braceletcnt)-((braceletPr*returnbracelet)+rebateGame)

print("Total Gift Cost is",totalcost)
