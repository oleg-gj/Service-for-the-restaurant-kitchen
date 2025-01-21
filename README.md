# Restaurant Kitchen Service

## Description
This site can help you improve communication and rules between cooks in the kitchen.

## Site Capabilities
* You can create a cook(user) with description to which dishes will be attached.
* You can create a dish that will have a name, description, price, type of dish, 
ingredients, chef preparation of the dish in its description.
* You can create a dish type with a name and a description.
* You can create ingredients that include a name and calorie count.

## Check it out
[Restaurant Kitchen Service](https://service-for-the-restaurant-kitchen.onrender.com/)

You can use the following login details

Username: addmin

Password: addmin

## Installation

Pyhton3 should be already installed
```shell
git clone https://github.com/oleg-gj/Service-for-the-restaurant-kitchen
cd kitchen_service
python3 -m venv venv
source venv/Script/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

```
## Loading Initial Data (Optional)

To load initial sample data into your database, you can use the following command:

```shell
python manage.py loaddata dump.json
```

## Licensing

This project is licensed under an Unlicense license. This license does not require
you to take the license with you to your project.
