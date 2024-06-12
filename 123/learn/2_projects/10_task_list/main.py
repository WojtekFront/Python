
""" Program for generating blog entries.
    Gets: text value, username. Generates: date, id, whether it is added.
    It then converts it to JSON and generate a file.
"""
import datetime
class Create_post:
    def __init__(self, text, username = "Guest", *args):
        self.text= text
        self.username = username
        self.generate_date = None
        self.post_id = 0 # autoicremention id

    def generate_new_post(self):
        
        print("id = {0}".format(self.post_id))
        print("new post: {0} ".format(self.post_id))

        print("username = {0}".format(self.username))
        self.generate_post_date()
        print(("date: {0}".format(self.generate_date)))

    def generate_post_date(self):
        self.generate_date = datetime.datetime.now().strftime("%y-%m-%d")    

    # def generate_post_id(self):
        # Here take last_post_id and add 1. The new value assign to self.post_id .
        # The new value must different then zero .

    def send_post_to_doc(self):
        print("new post")



new_post  = Create_post("Text to implement")

new_post.generate_new_post()






