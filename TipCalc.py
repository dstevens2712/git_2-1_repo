pretax = float(input("Enter Pre-tax total "))#Enter the pretax total and convert to float
tippercent = float(input("Enter tip percentage as a decimal "))#enter the tip in decimal for convet to float
totaltip = float(pretax * tippercent) #multiply pretax amount and tip convert to float 
numberoftippers = float(input("Enter number of Tippers "))#enter number of people tipping
tip = float(totaltip / numberoftippers)#divide total number of tip by the number of people tipping convert to float
print("Tip amount for each person $", round(tip, 2)) #print the tip amount for each person rounded to two decimal places
tipplustotal = float(pretax / numberoftippers + tip)#print the total amount each person owes rounded to two decimal places 
print("Total each person has to pay $", round(tipplustotal, 2))