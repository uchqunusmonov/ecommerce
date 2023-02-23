# online shopping app using django
# 
#
#   Run the following commands to run the app:

# $ git clone https://github.com/uchqunusmonov/ecommerce.git

# $ python3 -m venv venv

# $ source venv/bin/activate

# $ pip install -r requirements.txt

# $ python manage.py migrate

# $ docker pull rabbitmq

# $ docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

# Then do this in a new terminal window:

# $ celery -A config worker -l info

# Then run the following command again in a new terminal (You must be registered with Stripe and Stripe CLI for this!)

# $ stripe listen --forward-to localhost:8000/payment/webhook/

# Then run the following command in a new terminal

# $ docker run -it --rm --name redis -p 6379:6379 redis

# Then run the following command in a new terminal window

# python manage.py runserver

