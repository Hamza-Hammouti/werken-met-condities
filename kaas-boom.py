Question1 = input("is een kaas geel? ")
if Question1 == 'ja':
    Question2 = input("zitten er gaten in de kaas? ")
    if Question2 == 'ja':
        Question3 = input("is de kaas belagelijk duur? ")
        if Question3 == 'ja':
            print("De kaas heet: Emmenthaler.")
        elif Question3== 'nee':   
            print("leerdammer")
        else:
            print("Geen goed antwoord")        
    elif Question2 == 'nee':  
        Question4 = input("is de kaas hard als steen? ")
        if Question4 == 'ja':
            print("De kaas heet: Pammigiano Reggiano.")
        elif Question4 == 'nee':   
            print("De kaas heet: Goudse kaas.")
        else:
            print("Geen goed antwoord") 
    else:
        print("Geen goed antwoord")
elif Question1 == 'nee':
    Question5 =  input("heeft de kaas blauwe schiimmels? ")
    if Question5 == 'ja':
        Question6 = input("heeft de kaas een korst? ")
        if Question6 == 'ja':
            print("De kaas heet: Blue de Rochbaron.")
        elif Question6 == 'nee':   
            print("De kaas heet: Foumme d'ambert.")
        else:
            print("Geen goed antwoord") 
    elif Question5 == 'nee': 
        Question7 = input("heeft de kaas een korst? ")
        if Question7 == 'ja':
            print("De kaas heet: Camembert.")
        elif Question7 == 'nee':   
            print("De kaas heet: Mozzarella.")
        else:
            print("Geen goed antwoord")        
    else:
        print("Geen goed antwoord") 
else:
    print("Geen goed antwoord")