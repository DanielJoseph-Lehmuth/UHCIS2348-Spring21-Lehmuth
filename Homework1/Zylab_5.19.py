# Daniel Lehmuth
# 1936204

print("Davy's auto shop services")  # print list of services
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")

service_dict = {"Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12}  # services dictionary

print("")  # prompt customer for service selection. "-" means no service.
first_service = input("Select first service:\n")
second_service = input("Select second service:\n")

print("")  # print invoice for services
print("Davy's auto shop invoice")
print("")

if first_service in service_dict and second_service in service_dict:
    total_cost = service_dict[first_service] + service_dict[second_service]
    print("Service 1: {}, ${}".format(first_service, service_dict[first_service]))
    print("Service 2: {}, ${}".format(second_service, service_dict[second_service]))
    print("")
    print("Total: ${}".format(total_cost))

elif first_service in service_dict and second_service == "-":
    total_cost = service_dict[first_service]
    print("Service 1: {}, ${}".format(first_service, service_dict[first_service]))
    print("Service 2: No service")
    print("")
    print("Total: ${}".format(total_cost))

elif first_service == "-" and second_service in service_dict:
    total_cost = service_dict[second_service]
    print("Service 1: No service")
    print("Service 2: {}, ${}".format(second_service, service_dict[second_service]))
    print("")
    print("Total: ${}".format(total_cost))
