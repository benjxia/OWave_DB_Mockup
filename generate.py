import csv
import random
import datetime
import numpy as np

if __name__ == "__main__":
    """
    Write sample data into csv file
    """
    
    # First and last names to generate random names from
    first_names = ["Liam", "Olivia", "Noah", "Emma", "Oliver", "Charlotte", "Elijah", "Amelia", "James", "Ava", "William", "Sophia", "Benjamin", "Isabella", "Lucas" , "Mia", "Henry", "Evelyn", "Theodore", "Harper"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Cooper", "Adams", "Zamora", "Nguyen" ,"Hernandez"]
    
    # Potential hardships
    causes = ["Injury/Illness", "Legal Costs/Fees", "Child Care", "Elder Care", "Car Accident", "Victim of Crime", "Loss of Residency", "Loss of Transportation", "Misc."]
    
    # Approval Process
    status_small = ["APPROVED", "IN-PROGRESS - APPROVAL", "DELIVERED", "DENIED - FIN FITNESS MEETING", "DENIED", "APPEALED"]
    status_big = ["APPROVED", "DELIVERED", "IN-PROGRESS - COMMITTEE", "DENIED", "APPEALED"]
    # Generate dates
    timeformat = "%Y-%m-%d %H:%M:%S"
    curr_time = datetime.datetime(2022, 6, 10, 7, 14, 30)
    
    # Request amounts
    req_vals = [200, 225, 300, 350, 475, 790, 860, 540, 550, 999, 800, 100, 150, 450, 400, 600, 650, 900, 120, 110, 105, 65, 50, 1500, 2000, 1200, 1400, 2000, 2400, 2500]
    
    ticket_num = 100000
    
    with open("data.csv2", 'w', newline='') as csvfile:
        builder = csv.writer(csvfile)
        builder.writerow(["ticket", "first_name", "last_name", "apply_timestamp", "last_update", "cause", "requested", "status", "given"])
        # Write each sample row
        for i in range(1000):
            # Generate row
            ticket_num += random.randint(0,1000)
            curr_time = curr_time + datetime.timedelta(days = random.randint(0, 10), seconds = random.randint(0,60), hours = random.randint(0,24), minutes = random.randint(0, 60))
            last_update = curr_time + datetime.timedelta(days = random.randint(0, 1), seconds = random.randint(0,60), hours = random.randint(0,24), minutes = random.randint(0, 60))
            ctime_str = curr_time.strftime(timeformat)
            lutime_str = last_update.strftime(timeformat)
            fname = np.random.choice(first_names)
            lname = np.random.choice(last_names)
            ccause = np.random.choice(causes)
            req_amt = np.random.choice(req_vals)
            cstatus = np.random.choice(status_small) if req_amt < 1000 else np.random.choice(status_big)
            req_gvn = int(req_amt * random.random() * 2) if "APPROVED" in cstatus or "DELIVERED" in cstatus else 0
            
            builder.writerow([ticket_num, fname, lname, ctime_str, lutime_str, ccause, req_amt, cstatus, req_gvn])
            