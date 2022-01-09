"""
AI Name: Hunterbot

Strategy:
Hunts down an opponent, albeit not efficiently, and attacks it head on.
"""


                            #AI1 randybot - red is me
                            #AI2 hunterbot - blue is hunterbot

class AI:
    def __init__(self):
        self.isFirstTurn = True
        self.around_wall = False
        self.lastvar = False
        self.booleanA = False
        self.robotturn = False
        self.varB = True
        self.luckyshots = 0
        self.teleporttokens = 5
        self.luckshotticker = 0
        self.healticker = 5
        self.tickerA = 0
        self.wallcounter = 0
        self.countertwo =0
        self.howmanyroundscounter = 0
        

    def turn(self):

        enemy_location = self.robot.locateEnemy()[0] #return tuple of location e.g. (3,5)
        enemy_rotation = self.robot.locateEnemy()[1] # returns a number which is the rotation; 0 = up, 1 = right, 2 = down, 3 = left
        two_spaces = self.checkTwo()
        self.howmanyroundscounter += 1

        self.ThisIsMyFunction()
       
        if self.robot.lookInFront() == "wall" and self.lastvar == False:
            self.robotturn == True
            self.around_wall = False
            if self.around_wall == False:
                self.robot.turnLeft()
                self.wallcounter += 1
                self.booleanA = True

 ##################################################################################################################

        if self.around_wall == False and self.wallcounter == 1 and self.booleanA == False and self.lastvar == False:
            
            self.robot.goForth()
            self.booleanA = True
            self.wallcounter += 1

        elif self.around_wall == False and self.wallcounter == 2 and self.booleanA == False and self.lastvar == False:
            
            if self.robot.lookInFront() == "wall": 
                self.robot.turnLeft()
                self.wallcounter == 4
            else:
                self.robot.turnRight()
                self.wallcounter += 1
        
        elif self.around_wall == False and self.wallcounter == 3 and self.booleanA == False and self.lastvar == False:
            
            
            if self.robot.lookInFront() == "wall": 
                self.robot.goBack()
                self.wallcounter == 4
            else:    
                self.robot.goForth()
                self.booleanA = True
                self.wallcounter += 1
##################################################################################################################
        
        if self.around_wall == False and self.wallcounter == 4 and self.booleanA == False and self.lastvar == False:
            self.around_wall = True
            self.wallcounter -= 4
            self.robotturn == False

        self.booleanA = False
        self.luckshotticker += 1

##################################################################################################################




        if self.robot.lookInFront() == "clear" and self.robotturn == False and self.wallcounter == 0 and self.luckshotticker == 5 and self.lastvar == False:
            if self.robot.energy >= 50 and self.robot.health >=40:
                self.robot.luckyshot()
                self.luckyshots + 1
            else:
                self.robot.charge()
        

        elif self.robot.lookInFront() == "clear" and self.robotturn == False and self.wallcounter == 0 and self.varB == True and self.lastvar == False:

            if self.robot.energy >= 50 and self.robot.health >=40 and self.luckshotticker >= 7 and self.luckyshots <= 2:
                self.robot.luckyshot()
                self.luckyshots + 1
            
            elif self.robot.health <= 40 and self.robot.energy >=20:
                self.robot.repair()
                # self.varB == False

            else:
                
                if self.robot.health <= 20 and self.robot.energy >=20 and self.robot.energy <= 40 and self.lastvar == False:
                    self.robot.repair()
                else:
##################### THIS IS THE ROOT BOTOM GO-TO FUNCTION ####################
                    self.goTowards(self.robot.locateEnemy()[0])



        elif self.robot.lookInFront() == "clear" and self.robotturn == False and self.wallcounter == 0 and self.healticker >=2 and self.lastvar == False:
            if self.tickerA == 3:
                self.healticker == 5
                self.varB == True

            elif self.robot.energy >= 20:
                self.robot.repair()
                self.healticker -= 1
                self.tickerA += 1

            elif self.robot.locateEnemy()[0] == self.robot.rotation and self.robot.energy >= 80 and self.robot.health >= 50 and self.teleporttokens >= 1 and self.howmanyroundscounter >= 13:
                self.robot.teleport()
            else:
                self.robot.charge()
   
        elif self.robot.lookInFront() == "bot" and self.robotturn == False and self.wallcounter == 0 and self.lastvar == False:
            
            if self.robot.health < 30 and self.teleporttokens >= 1 and self.robot.energy >= 30:
                self.robot.escape()
                
                self.teleporttokens -= 1
                self.healticker -= 1

            elif self.robot.health >= 30 and self.robot.energy >=40:
                    self.robot.crush()

            else:
                self.robot.attack()
     
        self.lastvar == False
       


    def ThisIsMyFunction(self):
        if self.robot.energy >= 80 and self.howmanyroundscounter >= 3 and self.robotturn == False and self.wallcounter >= 0 and self.teleporttokens >= 1:
            self.robot.teleport()
            self.lastvar == True







        

            




    def checkDelta(self,enemyLocation):
        myLocation = self.robot.position
        delta = (enemyLocation[0]-myLocation[0],enemyLocation[1]-myLocation[1])
        return delta
            
    def goTowards(self,enemyLocation):
        myLocation = self.robot.position
        delta = (enemyLocation[0]-myLocation[0],enemyLocation[1]-myLocation[1])
        if abs(delta[0]) > abs(delta[1]):
            if delta[0] < 0:
                targetOrientation = 3 #face left
            else:
                targetOrientation = 1 #face right
        else:
            if delta[1] < 0:
                targetOrientation = 0 #face up
            else:
                targetOrientation = 2 #face down
        if self.robot.rotation == targetOrientation:
            self.robot.goForth()
        else:
            leftTurnsNeeded = (self.robot.rotation - targetOrientation) % 4
            if leftTurnsNeeded <= 2:
                self.robot.turnLeft()
            else:
                self.robot.turnRight()

    def checkTwo(self):
        my_position_x = self.robot.position[0]
        my_position_y = self.robot.position[1]
        my_rotation = self.robot.rotation


        if my_rotation == 0:
            two_spaces_location = (my_position_x, my_position_y - 2)
        elif my_rotation == 1:
            two_spaces_location = (my_position_x + 2, my_position_y)
        elif my_rotation == 2:
            two_spaces_location = (my_position_x, my_position_y + 2)
        else:
            two_spaces_location = (my_position_x - 2, my_position_y)

        two_spaces = self.robot.lookAtSpace(two_spaces_location)
        return two_spaces

