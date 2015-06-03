#
#Program: Annuity
#Author: Stonedahl


inter=0.05
monthly_dpst,years=input("How much will you deposit monthly and for how many years? Please seperate answers by a comma and a space")
amnt=0
for i in range (12*years):
    amnt=amnt + (inter/12)*amnt
    amnt=amnt + monthly_dpst
    

print amnt
