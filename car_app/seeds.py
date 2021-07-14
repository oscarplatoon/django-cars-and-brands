from cars_and_brands.models import Brand, Car

brand1 = Brand(brand='Volvo')
brand1.save()

brand2 = Brand(brand='Chevy')
brand2.save()

brand3 = Brand(brand='Ford')
brand3.save()

brand4 = Brand(brand='Subaru')
brand4.save()

car1 = Car(brand=brand1, model='XYZ', year=2020, color='red')
car1.save()

car2 = Car(brand=brand2, model='truck', year=2010, color='white')
car2.save()

car3 = Car(brand=brand3, model='car', year=2000, color='blue')
car3.save()

car4 = Car(brand=brand4, model='outback', year=2001, color='yellow')
car4.save()
