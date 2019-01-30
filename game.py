import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
from random import randint

co1s = [[1,20,21,40,41,60,61,80,81,100],
         [2,19,22,39,42,59,62,79,82,99],
         [3,18,23,38,43,58,63,78,83,98],
         [4,17,24,37,44,57,64,77,84,97],
         [5,16,25,36,45,56,65,76,85,96],
         [6,15,26,35,46,55,66,75,86,95],
         [7,14,27,34,47,54,67,74,87,94],
         [8,13,28,33,48,53,68,73,88,93],
         [9,12,29,32,49,52,69,72,89,92],
         [10,11,30,31,50,51,70,71,90,91]]

rows = [[1,2,3,4,5,6,7,8,9,10],
        [20,19,18,17,16,15,14,13,12,11],
        [21,22,23,24,25,26,27,28,29,30],
        [40,39,38,37,36,35,34,33,32,31],
        [41,42,43,44,45,46,47,48,49,50],
        [60,59,58,57,56,55,54,53,52,51],
        [61,62,63,64,65,66,67,68,69,70],
        [80,79,78,77,76,75,74,73,72,71],
        [81,82,83,84,85,86,87,88,89,90],
        [100,99,98,97,96,95,94,93,92,91]]

def row_no(pos):
    for i in range(0,10):
	if pos in rows[i]:
		row = i+1
    return row

def col_no(pos):
    for i in range(0,10):
        if pos in cols[i]:
            col = i+1
    return col


def move(initial,final):

    def real_move(robot):

        global x

        current_pos = initial

        
        for i in range(0,final-initial):

            if current_pos == 100:
                #Declare winner
                print("Winner")
                break
            
            elif current_pos in [10,30,50,70,90]:
                #left turn
                robot.turn_in_place(degrees(90)).wait_for_completed()
                #move forward 10mm
                robot.drive_straight(distance_mm(100), speed_mmps(20)).wait_for_completed()
                #left turn
                robot.turn_in_place(degrees(90)).wait_for_completed()
                current_pos = current_pos + 1

            elif current_pos in [20,40,60,80]:
                #right turn
                robot.turn_in_place(degrees(-90)).wait_for_completed()
                #move forward 10mm
                robot.drive_straight(distance_mm(100), speed_mmps(20)).wait_for_completed()
                #right turn
                robot.turn_in_place(degrees(-90)).wait_for_completed()
                current_pos = current_pos + 1

            else:
                #move forward 10mm
                robot.drive_straight(distance_mm(100), speed_mmps(20)).wait_for_completed()
                current_pos = current_pos + 1
        x = current_pos
 
    return real_move


def ladder(start_pos):

    def real_ladder(robot):
        
        #initial = x
        #final = ladders[x]

        row_initial = row_no(start_pos)
	col_initial = col_no(start_pos)
	row_final = row_no(ladders[start_pos])
	col_final = col_no(ladders[start_pos])

	if (row_initial % 2 == 0):
            #right turn
            robot.turn_in_place(degrees(-90)).wait_for_completed()
                
        else:
            #left turn
            robot.turn_in_place(degrees(90)).wait_for_completed()
            
        robot.drive_straight(distance_mm((row_final-row_initial)*100), speed_mmps(20)).wait_for_completed()
                    
	if (row_final % 2 == 0):
            #left turn
            robot.turn_in_place(degrees(90)).wait_for_completed()
            robot.drive_straight(distance_mm((col_initial-col_final)*100), speed_mmps(20)).wait_for_completed()
                      
        else:
            #right turn
            robot.turn_in_place(degrees(-90)).wait_for_completed()
            robot.drive_straight(distance_mm((col_final-col_initial)*100), speed_mmps(20)).wait_for_completed()
            

    return real_ladder


def snake(start_pos):

    def real_snake(robot):
        
        #initial = x
        #final = snakes[x]

        row_initial = row_no(start_pos)
	col_initial = col_no(start_pos)
	row_final = row_no(snakes[start_pos])
	col_final = col_no(snakes[start_pos])

	if (row_initial % 2 == 0):
            #left turn
            robot.turn_in_place(degrees(90)).wait_for_completed()
                
        else:
            #right turn
            robot.turn_in_place(degrees(-90)).wait_for_completed()

        robot.drive_straight(distance_mm((row_initial-row_final)*100), speed_mmps(20)).wait_for_completed()
                    
	if (row_final % 2 == 0):
            #right turn
            robot.turn_in_place(degrees(-90)).wait_for_completed()
            robot.drive_straight(distance_mm((col_initial-col_final)*100), speed_mmps(20)).wait_for_completed()
                      
        else:
            #left turn
            robot.turn_in_place(degrees(90)).wait_for_completed()
            robot.drive_straight(distance_mm((col_final-col_initial)*100), speed_mmps(20)).wait_for_completed()

    return real_snake


    
    

initial_pos = 0
final_pos = randint(1,6)
print(final_pos)
condition = True

while condition:
    
    cozmo.run_program(move(initial_pos,final_pos))

    ladders = {2:11,7:14,8:31,15:26,21:42,28:56,63:85,87:94}

    snakes = {16:6,46:25,49:11,64:60,74:53,89:68,99:60}

    if ( x in ladders):

        cozmo.run_program(ladder(x))
        x = ladders[x]
        #cozmo.run_program(move(x,ladders[x]))
	                        
		
    elif ( x in snakes):

        cozmo.run_program(snake(x))
        x = snakes[x]
    	#cozmo.run_program(move(x,snakes[x]))
                
          
	
    initial_pos = x
    dice = randint(1,6)
    print(dice)
    final_pos =  x + dice
    condition = (x != 100)

