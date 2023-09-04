#creat class methods that allows you to take tickets  from the parkinng garage. 
#the more tickets sold the less will be avaliable and the # of parking spaces you will have decreases.
#show input for payment of tickets. if not empty show message paid or 15 mins remaining.
#paid ticket should = true
#when leaving the garge, if ticket is paid  'thank you, have a nice day'. if not prompt for payment
#once paid update spaces and ticket lists to increase by 1.

class parking_garage:
    def __init__(self, total_tickets, total_spaces):
        self.ticket = [i for i in range(1, total_tickets +1)]
        self.parking_spaces = [i for i in range(1, total_spaces +1)]
        self.current_ticket = {}

    def take_ticket(self):
        if len(self.tickets) >0 and len(self.parking_spaces) > 0:
            ticket = self.ticket.pop(0)
            space = self.parking_spaces.pop(0)

            print(f'your number is {ticket} and your parking space is {space}')
        
        else:
            print('sorry, the garage is full.')

    def pay_for_parking(self):
        ticket = int (input('enter your ticket number'))
        if ticket in self.current_ticket:
            if not self.current_ticket[ticket]['paid']:
                payment = input('Please enter payment amount')
                if payment:
                    self.current_ticket[ticket]['paid'] = True
                else: 
                    print('Your ticket has been paid. You have 15 minutes to leave, or we will have to use excessive force')
            else:
                print('The ticket has been paid')
        else:  
            print('wrong ticket number')

    def Leave_garage(self):
        ticket = int(input("We need your ticket number to exit: "))
        if ticket in self.current_ticket:
                if self.current_ticket[ticket]['paid']:
                   print("Thank you, have a wonderful day. ")
                   del self.current_ticket[ticket]
                   self.tickets.append(ticket)
                   self.parking_spaces.append(ticket)
        else:
            print("Wrong ticket number! I'll wait.....")

    


    def fake(fuction):
        not_real == fake
        return (not real)
