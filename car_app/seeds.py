from cars_and_brands.models import Brand, Car

b1 = Brand(name="Jeep")
b1.save()

b2 = Brand(name="Ford")
b2.save()

b3 = Brand(name="BMW")
b3.save()

c1 = Car(brand=b1, name="Cherokee", year="2018")
c1.save()

c2 = Car(brand=b1, name="Wrangler", year="2012")
c2.save()

c3 = Car(brand=b2,name="Mustang", year="2020")
c3.save()

c4 = Car(brand=b2,name="Explorer", year="1994")
c4.save()

c5 = Car(brand=b3,name="M3", year="1990")
c5.save()

c4 = Car(brand=b3,name="325i", year="2006")
c4.save()