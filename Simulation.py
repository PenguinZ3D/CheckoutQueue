from customer import Customer
import random

#Simulation parameters
current_time = 0.0

simulation_duration = 60

working_time = 0

queue = []

cashier_busy = False

customers_served = 0

next_arrival_time = random.uniform(1, 4)


#Main simulation loop
while current_time < simulation_duration:
    print("Current Time: " + str(current_time)) #To test time increment

    #Add new customer to queue at next arrival time
    if current_time >= next_arrival_time:
        customer = Customer(current_time, random.uniform(2, 5))
        queue.append(customer)
        next_arrival_time = current_time + random.uniform(1, 4)
        print("Customer Arrived at: " + str(customer.arrival_time)) #To test arrival


    #Check if customers are in line and cashier is free
    if len(queue) > 0 and cashier_busy == False:
        cashier_busy = True
        service_end_time = current_time + queue[0].service_time
        print("Customer Service Started at: " + str(current_time)) #To test service start

    #Process customer service if cashier is busy
    if cashier_busy == True:
        if current_time >= service_end_time:
            cashier_busy = False
            customers_served += 1
            print("Customer Service Ended at: " + str(current_time)) #To test service end
            working_time += queue[0].service_time
            queue.pop(0)
    
    #Increment time
    current_time += 1


print("Simulation Ended")
print("Total Customers Served: " + str(customers_served))
print(f"Total Working Time:{working_time: .2f}")