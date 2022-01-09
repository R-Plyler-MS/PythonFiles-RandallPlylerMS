"""
AI Name: Derek Bot

Strategy:
Whatever
"""

class AI:
    def __init__(self):
        self.isFirstTurn = True
        self.luckyshots = 0

    def turn(self):

        enemy_location = self.robot.locateEnemy()[0] #return tuple of location e.g. (3,5)
        enemy_rotation = self.robot.locateEnemy()[1] # returns a number which is the rotation; 0 = up, 1 = right, 2 = down, 3 = left
        two_spaces = self.checkTwo()


        if self.robot.lookInFront() == "bot":
            if self.robot.energy >= 30:
                self.robot.escape()
            else:
                self.robot.attack()
        else:
            if self.robot.energy >= 50 and self.luckyshots < 1:
                self.robot.luckyshot()
                self.luckyshots += 1
            elif two_spaces == "bot":
                self.robot.charge()
            else:
                self.goTowards(self.robot.locateEnemy()[0])

            
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

