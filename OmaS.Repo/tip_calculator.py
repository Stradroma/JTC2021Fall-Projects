def tip_calculator():
    #Space created for visual clarity
    print()
    print()
    #User commanded to only use number keypad to opperate app.
    print('Please use the number keypad to opperate and use \
        \nthis tip calculator.')
    print()    
    
    #User enters cost of meal
    cost_of_food= float(input(f'Hello, hope enjoyed your meal today.\
        \nWhat is the cost of your meal?  $'))
    print()
    #User enters amount of people splitting the bill.
    people_splitting= int(input(f'How many people are splitting this bill?  '))
    print()
    #User enters desired tip amount in percentage value. 
    tip_percent= int(input(f'Please enter desired percentage of gratuity\
        \n 10% / 15% / 18%/  20%/ _?_%:   '))
    
    #Sales Tax is determined from users input of Cost Of Food 
    # multiplied by pre-determinded States Tax of 10% divided by 100.
    sales_tax= float(cost_of_food) * 10 / 100
    print(f'Your sales tax total for today will be:{sales_tax:,.2f}')
    print()    
    #Tip Total is determinded by users input of Cost Of Food 
    # multiplied by users input of Tip Percent divided by 100. 
    tip_total= float(cost_of_food) * float(tip_percent) / 100
    print(f'Your tip amount comes to:${tip_total:,.2f}')
    print()
    #Total bill determinded but adding Sales Tax to the value of Cost Of Food.
    total_bill= float(sales_tax) + float(cost_of_food)
    print(f'Your total bill before taxes today is :${total_bill:,.2f}')
    print()
    #Final Bill determinded by adding Tip Total to Total Bill.
    final_bill= float(tip_total) + float(total_bill)
    print(f'Your final bill today is: ${final_bill:,.2f}')
    print()
    #Pay Per Person determinded by dividing Totoal Bill by amount
    #of people splitting the bill
    pay_per_person= float(total_bill) / float(people_splitting)
    tip_per_person= float(tip_total) / int(people_splitting)
    print (f'Each person in your party will pay a total of {pay_per_person:,.2f}, \
        \nthis breaks down to each person contributing {tip_per_person:,.2f} towards th tip amount.')
     


    




   
tip_calculator()


