# Cars and Manufacturers

We are going to create a nested CRUD app that focuses on creating cars and manufacturers. Make it look nice and make sure your code is clean! Best of luck!

Here are our recommended steps for creating CRUD apps:
1. Schema
2. Migrations
3. Models
4. Associations
5. Validations
6. Create some text data in the database
7. Manually test your associations in the `django shell`
8. Create your routes
9. Visit each page and create the views/forms for each

Read more here: [gist](https://gist.github.com/KaraAJC/a76572b6784a8317e662)

In the end, you should be able to visit the following routes:

```
/manufacturers # a list of all the manufacturers
/manufacturers/new # form for a new manufacturer
/manufacturers/<:id> # see a specific manufacturer
/manufacturers/<:id>/edit # edit page for a specific manufacturers

/manufacturers/<:manufacturer_id>/cars # a list of cars for a specific manufacturer
/manufacturers/<:manufacturer_id>/cars/new # form for a new car under a specific manufacturer
/manufacturers/<:manufacturer_id>/cars/<:car_id> # see a specific car for a specific manufacturer
/manufacturers/<:manufacturer_id>/cars/<:car_id>/edit # edit page for a specific car under a specific manufacturer
```

Remember to start by creating a new virtual environment.

`python -m venv venv source venv/bin/activate`
`source venv/bin/activate`

Once you have your virtual environment up and running you can tell pip to download all the requirements for this app by running `pip install -r requirements.txt`. Make sure you are in the main directory of the repo (the one with the readme in it).

Next set up the database `carApp` by running `createdb carApp`.

Remember to have tests to ensure all of your code is working!
