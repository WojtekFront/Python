class Elevator:
    numbers_of_floors = [0,1,2,3,4,5,6,7,8,9,10]

    def __init__(self, elevator_model, elevator_id, elevator_move_state, elevator_door_state = True, elevator_input_state: "actually always ok" = 0, current_level=0):
        self.elevator_model = elevator_model
        self.elevator_id = elevator_id
        self.elevator_move_state = elevator_move_state
        self.elevator_door_state = elevator_door_state
        self.elevator_input_state = elevator_input_state
        self.current_level = current_level




    




