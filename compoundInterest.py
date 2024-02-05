def calculateCompoundInterest():
  #create for loop to repeat 3 times. once per client
    for i in range(3):   
        # This first 3 lines are provided for yougetACompoundInterest()
        # This first 3 lines are provided for you
        client_one_principal = float(input("Principle (amount): "))
        client_one_time =      float(input("Time:               "))
        client_one_rate =      float(input("Rate:               "))
        #print("Compound Interest: "+str(intrest))
        amnt = client_one_principal * ( 1 + client_one_rate / 100)**client_one_time
        intrest = amnt - client_one_principal
        
        #have to add round arguement to match excpeted answer of 133.01 instead of 133.0992000000001
        #just noticed that although this fixes the first expected answer it messes up the second one.

        intrest = round(intrest, 2)
        print("Compound Interest:", intrest)
        #got stuck here for a bit, added this "if i > 2" line to not have the line break print after the last output. pytest didnt like that as it didnt want it there.
        if i < 2:
            print('---')
            # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
