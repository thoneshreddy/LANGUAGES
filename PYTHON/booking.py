from datetime import datetime
class Bus:
    def __init__(self,bno,ac,cap):
        self.bno=bno
        self.ac=ac
        self.cap=cap
    def get_bno(self):
        return self.bno
    def get_ac(self):
        return self.ac
    def get_cap(self):
        return self.cap
    def display(self):
        print(f"BUS NO : {self.bno}  AC : {self.ac} CAPACITY : {self.cap}")
class Bookings:
    def __init__(self):
        self.name=""
        self.date=None
        self.bno=None
    def make_booking(self,buses,bookings):
        self.name=input("Enter passenger name : ")
        self.bno=int(input("enter the bus no : "))
        d=input("Enter the date in dd-mm-yy")
        self.date=datetime.strptime(d,"%d-%m-%Y").date();
        if(self.isavailable(buses,bookings,self.bno,self.date)):
            bookings.append(self)
            print("Your booking is confirmed")
        else:
            print("bus is full,try another bus or date ")
    def isavailable(self,buses,bookings,bno,date):
        capacity=0;
        booked=0
        for i in buses:
            if(bno == i.bno):
                capacity=i.cap
                break;
        for j in bookings:
            if(date == j.date and bno == j.bno):
                booked=booked+1
        return booked<capacity
def main():
    buses=[Bus(100,True,2),Bus(200,False,50),Bus(300,False,48)];
    bookings=[]
    for i in buses:
        i.display()
    while(True):
        opt=int(input("Enter 1 to book,Enter 2 to exit"))
        if(opt==1):
            book=Bookings()
            book.make_booking(buses,bookings)
        else:
            break
if __name__=="__main__":
    main()