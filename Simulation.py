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



while current_time < simulation_duration:
    current_time += 1
    print("Current Time: " + str(current_time)) #To test time increment

    if current_time >= next_arrival_time:
        customer = Customer(current_time, random.uniform(2, 5))
        queue.append(customer)
        next_arrival_time = current_time + random.uniform(1, 4)
        print("Customer Arrived at: " + str(customer.arrival_time)) #To test arrival

        print(len(queue)) #To test queue length
        

