import random
import datetime
parcels = []

def trackingId():
    now = datetime.datetime.now()
    date_part = now.strftime("%d%m%Y%H%M%S")
    random_part = random.randint(100, 999)
    return f"TRk{date_part}{random_part}"

while True:
    print("----- Parcel Delivery Management System -----")
    print("1.Add New Parcel")
    print("2.Update Delievry Status")
    print("3.Track a Parcel")
    print("4.View All Parcels")
    print("5.Filter Parcels")
    print("6.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sender_name = input("Enter sender name: ")
        reciever_name = input("Enter receiver name: ")
        parcel_weight = input("Enter parcel weight: ")
        delievery_address = input("Enter delievery address: ")
        delievery_type = input("Enter delivery type (Normal/Express): ")
        tracking_id = trackingId()

        parcels.append({
            "Sender" : sender_name,
            "Reciever" : reciever_name,
            "Parcel Weight" : parcel_weight,
            "Delievery Address" : delievery_address,
            "Delievery Type" : delievery_type,
            "Tracking ID" : tracking_id,
            "Status" : "Pending"
        })

        print("Parcel Added Successfully!")
        print(f"Tracking ID: {tracking_id}")

    elif choice == "2":
        through_tid = input("Enter Tracking ID to Update: ")
        found = False

        for parcel in parcels:
            if parcel["Tracking ID"] == through_tid:
                new_status = input("Enter new status (Pending, In Transit, Delivered, Cancelled): ")
                parcel["Status"] = new_status
                print("Status Updated Successfully.")
                found = True
                break

        if not found:
            print("Parcel with this Tracking ID not found.")       

    elif choice == "3":
        tid = input("Enter Tracking ID: ")
        found = False

        for parcel in parcels:
            if parcel["Tracking ID"] == tid:
                print("Parcel Found!")
                print(f"Sender: {parcel['Sender']}")
                print(f"Reciever: {parcel['Reciever']}")
                print(f"Status: {parcel['Status']}")
                found = True
                break

        if not found:
            print("Parcel with this Tracking ID not found.")

    elif choice == "4":
        print("All Parcels.")
        print(parcels)

    elif choice == "5":
        status  = input("Input Status: ")

        for parcel in parcels:
            if parcel["Status"] == status:
                print(f"Parcel send by {parcel['Sender']} to {parcel['Reciever']}, status is...... {parcel['Status']}")
    
    elif choice == "6":
        print("Thanks for using!")
        break