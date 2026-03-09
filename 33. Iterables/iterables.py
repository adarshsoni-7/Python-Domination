# In Python, we call iterables to those data structures for which we can iterate and access, perform any operations by running any loop -- 'while' or 'for'.
# For Example, lists are iterables, sets are iterables, tuples and dictionaries are too.


racing_model = {"m311", "3d92a", "S400"}


for model in racing_model:
    print(model)


racing_car = ("m3", "m5", "formula1")


for car in racing_car:
    print(car)


racing_bike = ["10r", "panigale", "davison"]


for bike in racing_bike:
    print(bike)


racing_car_with_models = {"BMW": "M3",
                        "NISSAN": "GTR",
                        "SUPRA": "500",
                        "G-WAGON": "AMG"}


for car, model in racing_car_with_models.items():
    print(car, model)




# We can clearly see here that all these data structures are iterables.