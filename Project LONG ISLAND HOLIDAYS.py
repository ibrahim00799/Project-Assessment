# Author: Ibrahim Abdule
# Student Id: R00221794
# Project -LONG ISLAND HOLIDAYS
import random

def save_bookings(acc, price, booked):
    f = open("bookings.txt", "w")

    for i in range(len(acc)):
        f.write(acc[i] + "," + price[i] + "," + booked[i] + "\n")

    f.close()

def bookings():
    f = open('bookings.txt', 'r')
    acc = []
    price = []
    booked = []

    for i in f.readlines():
        i=i.replace("\n","")
        l = i.split(",")
        acc.append(l[0])
        price.append(l[1])
        booked.append(l[2])

    f.close()
    return acc,price,booked

def extras():
    f = open('extras.txt', 'r')
    
    kids = f.readline().replace("\n", "").split(",")
    pool_pass = f.readline().replace("\n", "").split(",")
        
    f.close()
        
    return kids,pool_pass

def save_extras(kids, pool_pass):
    f = open("extras.txt", "w")

    f.write(",".join(kids) + "\n" + ",".join(pool_pass))

    f.close()


def make_bookings():
    
    kidList, poolList = extras()
    acc,price,booked = bookings()
    
    print("\nLONG ISLAND HOLIDAYS - Making a Booking\n=======================================")
    name = input("Enter your family name => ")
    num = int(input("Enter your phone number => "))
    print("Choose your accommodation type: ")
    
    for i in range(len(acc)):
        print(str(i+1) + ". " + acc[i] + " (€" + price[i] + ") " + booked[i] + " booked")
    print(str(len(acc)+1) + ". No Booking")
    book = int(input("=> "))
    people = int(input("How many people in your group? "))
    pool_pass = input("Do you require a family pool pass (Y/N)? ")
    kids = int(input("How many kids will join the kids club? "))
    
    booking_id = random.randint(1, 30)
    
    cost = int(price[book-1])
    
    if(pool_pass.upper() == "Y"):
        poolList[1] = str(int(poolList[1]) + people)
        
    if(kids > 0):
        cost = cost + 100*kids
        kidList[1] = str(int(kidList[1]) + kids)
    
    details = "Booking Details\n---------------\n" + "Booking id: " + str(booking_id) + "\nAccommodation Type: " + acc[book-1] + "\nNo of People: " + str(people) + "\nPool Pass: " + pool_pass + "\nNo. for kids club: " + str(kids) + "\nCost €" + str(cost)
    
    print("\n" + details)
    
    booked[book-1] = str(int(booked[book-1]) + 1)
    
    save_bookings(acc, price, booked)
    save_extras(kidList, poolList)
    
    f = open(name + str(booking_id) + ".txt", "w")
    f.write(details)
    f.close()
    

def calc_cost():
    cost=0
    booking_cost=0
    
    kidList, poolList = extras()
    acc,price,booked = bookings()
    
    for i in range(len(acc)):
        if(int(booked[i])>0):
            booking_cost = booking_cost + int(price[i])*int(booked[i])
            
    cost = cost + 100*int(kidList[1]) + 150*int(poolList[1])
    cost = cost + booking_cost
    
    return cost, booking_cost

def bookings_review():
    kidList, poolList = extras()
    acc,price,booked = bookings()
    
    print("\nLONG ISLAND HOLIDAYS – Review Bookings\n======================================")
    print("The number of bookings made in each category :")
    for i in range(len(acc)):
        print(acc[i] + " => " + booked[i])
    
    print("The number of kids who plan to attend kids club :", kidList[1])
    print("The number of pool passes sold :", poolList[1])
    
    cost, booking_cost = calc_cost()
    booked = [int(i) for i in booked]
    
    print("The projected income based on current bookings (including extras) :",cost)
    print("Average income per bookings :", round(booking_cost/sum(booked),2))
    print("The number of remaining sites :", 30-sum(booked))
    

if __name__ == '__main__':
    print("My Name")
    print("-----------")
    print()
    print("LONG ISLAND HOLIDAYS")
    print("===================")
    while(True):
        print("\n1. Make a Booking\n2. Review Bookings\n3. Exit")
        ch = input("Enter your choice ")
        if(ch=="1"):
            make_bookings()
        elif(ch=="2"):
            bookings_review()
        else:
            print("Thank You")
            break
        
    
    
