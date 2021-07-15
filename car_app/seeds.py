from cars_and_brands.models import Brands, Cars

honda = Brands(title='Honda', description='Foreign')
honda.save()

ford = Brands(title='Ford', description='Domestic')
ford.save()

car_1 = Cars(brand_name=honda, make="CRV", type_model="SUV")
car_1.save()

car_2 = Cars(brand_name=honda, make="Civic", type_model="Compact")
car_2.save()

car_3 = Cars(brand_name=ford, make="Mustang", type_model="Muscle")
car_3.save()

car_4 = Cars(brand_name=honda, make="F-150", type_model="Truck")
car_4.save()

