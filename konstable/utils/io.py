import os
import time

# generates a random string
random_number_string = lambda length: str(random.random()).split('.')[-1][:length]

# generate a timestamp string

timestamp_string = lambda: time.strftime('%Y-%m-%d--%H-%M-%S')

# one liner to create a folder
create_folder = lambda f: [os.makedirs(os.path.join('./', f))
                           if not os.path.exists(os.path.join('./', f)) else False]