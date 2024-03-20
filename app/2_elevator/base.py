import random
class Elevator:
    numbers_of_floors = [1,2,3,4,5,6,7,8,9,10,11]
    elevator_move_state:{
        0: "wylaczona",
        1: "techniczne zatrzymanie: serwis, awaria, konieczne prace serwisowe, czujnik dymu",
        2: "czeka",
        3: "jedzie w dół",
        4: "zatrzymała podczas jezdy w dół",
        5: "jedzie w górę",
        6: "zatrzymała w trakcie jazdy w górę"
    }

    def __init__(self, elevator_model: "write model", elevator_id: "write id: xxxxx", elevator_move_state: "check state" =2, elevator_door_state = True, elevator_input_state: "actually always ok" = 0, 
                 current_level=0,
                 current_list= None, list_up = [], list_down = []):
        self.elevator_model = elevator_model
        self.elevator_id = elevator_id
        self.elevator_move_state = elevator_move_state
        self.elevator_door_state = elevator_door_state
        self.elevator_input_state = elevator_input_state
        self.current_level = current_level
        self.current_list = current_list
        self.list_up = list_up
        self.list_down = list_down

    def test_order_generate_input(self):
        '''Testing elements
        send order_generate_input'''
        how_many_random = 20
        for i in range(how_many_random):
            self.test_generate_random_level() 

    def test_generate_random_level(self):
        '''Testing elements
        Generate a random level 10 levels with will be put in the list.
        First will put to list up
        '''
        new_random_level = random.choice(self.numbers_of_floors)
        return self.test_add_to_list(new_random_level)

    def test_add_to_list(self, new_random_level): 
        ''' If list is empty then check first imput
            if first imput is biger then current level then go up and then firs print list up.
            if first element is biger then current level then go down and then firs print list down'''
        if self.current_list is None:
            print(new_random_level)
            if self.current_level < new_random_level:
                self.current_list = self.list_up
            elif self.current_level > new_random_level:
                self.current_list = self.list_down
        
        if not new_random_level:
            self.send_error("test_add_to_list 1. Error value {0}: ".format(new_random_level))
        elif new_random_level > self.current_level:
            self.add_element_to_list_up(new_random_level)
        elif new_random_level < self.current_level:
            self.add_element_to_list_down(new_random_level)
        else:
            if new_random_level != self.current_level:
                self.send_error("test_add_to_list 2. Unpredicted value in list: {0}".format(new_random_level)) # Error to log    

    def add_element_to_list_up(self, new_random_level):
        if not self.list_up:
            print("lista pusta")
            self.list_up.append(new_random_level)
        elif new_random_level not in self.list_up:
            self.list_up.append(new_random_level)
            self.list_up.sort()        

    def add_element_to_list_down(self, new_random_level):
        if not self.list_down:
            print("lista pusta")
            self.list_down.append(new_random_level)
        elif new_random_level not in self.list_down:
            self.list_down.append(new_random_level)
            self.list_down.sort(reverse = True)            

    def send_error(self, message):
        ''' information to log'''
        return 

# test_current_level = random.choice(Elevator.numbers_of_floors)
test_current_level = 5
first_elevator = Elevator("Test_model","00001",current_level=test_current_level)

first_elevator.test_order_generate_input()
print("Aktualne piętro: {0}".format(first_elevator.current_level))
print("Lista w górę:    {0}".format(first_elevator.list_up))
print("Lista w dół:     {0}".format(first_elevator.list_down))
print("kierunek jazdy:{0}".format(first_elevator.current_list))


    




