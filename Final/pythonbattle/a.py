import random

class AI:
   #A RED ME
   #B BLUE HUNTERBOT


    def __init__(self):
        
        

        self.isFirstTurn = True
        
       
            #ask
        # self.health = 100
        # self.energy = 20
        # self.teleports = 5


            #keep
        # position = self.robot.position
        # rotation = self.rotation
        # health = self.robot.health
        # energy = self.robot.energy
        # self.teleports = 5
        # self.endgamevar = 0


        
        
    def turn(self):
        # if self.isFirstTurn:
            
        #     # self.robot.turnRight()
        #     position = self.robot.position
        #     rotation = self.robot.rotation
        #     health = self.robot.health
        #     energy = self.robot.energy
        #     endgamevar = self.endgamevar
        #     #DO NOT CHANGE IS FIRST TURN
        #     self.isFirstTurn = False

        # if self.endgamevar == 3:
        #     self.robot.health() #note this should end the game

        if self.robot.lookInFront() == "bot":
            # self.endgamevar + 1 #add one to the ticker to end the game
       
            
            if self.robot.health <= 10:
                
                if self.robot.energy <= 10:
                    self.robot.attack()

                if self.robot.energy <= 10 and self.robot.energy >= 20:
                    self.robot.attack()

                if self.robot.energy >= 20 and self.robot.energy <= 30:
                    self.robot.repair()
         
                if self.robot.energy >= 30 and self.robot.energy <= 40:
                    self.robot.repair()

                if self.robot.energy >= 40 and self.robot.energy <= 50:
                    self.robot.repair()

                if self.robot.energy >= 50 and self.robot.energy <= 60:
                    self.robot.repair()

                if self.robot.energy >= 60 and self.robot.energy <= 70:
                    self.robot.repair()

                if self.robot.energy >= 70 and self.robot.energy <= 80:
                    self.robot.toss()
                
                if self.robot.energy >= 80 and self.robot.energy <= 90:
                    self.robot.toss()

                if self.robot.energy >= 90 and self.robot.energy <= 100:
                    self.robot.toss()


                
            if self.robot.health >= 10 and self.robot.health <= 20:
                
                if self.robot.energy <= 10:
                    self.robot.attack()

                if self.robot.energy <= 10 and self.robot.energy >= 20:
                    self.robot.attack()

                if self.robot.energy >= 20 and self.robot.energy <= 30:
                    self.robot.attack()
         
                if self.robot.energy >= 30 and self.robot.energy <= 40:
                    self.robot.attack()

                if self.robot.energy >= 40 and self.robot.energy <= 50:
                    self.robot.attack()

                if self.robot.energy >= 50 and self.robot.energy <= 60:
                    self.robot.attack()

                if self.robot.energy >= 60 and self.robot.energy <= 70:
                    self.robot.attack()

                if self.robot.energy >= 70 and self.robot.energy <= 80:
                    self.robot.toss()

                if self.robot.energy >= 80 and self.robot.energy <= 90:
                    self.robot.toss()

                if self.robot.energy >= 90 and self.robot.energy <= 100:
                    self.robot.toss()


            if self.robot.health >= 20 and self.robot.health <= 30:
                
                if self.robot.energy <= 10:
                    self.robot.attack()

                if self.robot.energy <= 10 and self.robot.energy >= 20:
                    self.robot.attack()

                if self.robot.energy >= 20 and self.robot.energy <= 30:
                    self.robot.attack()
         
                if self.robot.energy >= 30 and self.robot.energy <= 40:
                    self.robot.attack()

                if self.robot.energy >= 40 and self.robot.energy <= 50:
                    self.robot.attack()

                if self.robot.energy >= 50 and self.robot.energy <= 60:
                    self.robot.attack()

                if self.robot.energy >= 60 and self.robot.energy <= 70:
                    self.robot.attack()

                if self.robot.energy >= 70 and self.robot.energy <= 80:
                    self.robot.toss()

                if self.robot.energy >= 80 and self.robot.energy <= 90:
                    self.robot.toss()

                if self.robot.energy >= 90 and self.robot.energy <= 100:
                    self.robot.toss()
     
            if self.robot.health >= 30 and self.robot.health <= 40:
                
                if self.robot.energy <= 10:
                    self.robot.attack()

                if self.robot.energy <= 10 and self.robot.energy >= 20:
                    self.robot.attack()

                if self.robot.energy >= 20 and self.robot.energy <= 30:
                    self.robot.repair()
         
                if self.robot.energy >= 30 and self.robot.energy <= 40:
                    self.robot.repair()

                if self.robot.energy >= 40 and self.robot.energy <= 50:
                    self.robot.repair()

                if self.robot.energy >= 50 and self.robot.energy <= 60:
                    self.robot.repair()

                if self.robot.energy >= 60 and self.robot.energy <= 70:
                    self.robot.repair()

                if self.robot.energy >= 70 and self.robot.energy <= 80:
                    self.robot.toss()

                if self.robot.energy >= 80 and self.robot.energy <= 90:
                    self.robot.toss()

                if self.robot.energy >= 90 and self.robot.energy <= 100:
                    self.robot.toss()

            if self.robot.health >= 40 and self.robot.health <= 50:
                
                if self.robot.energy <= 10:
                    self.robot.charge()  

                if self.robot.energy <= 10 and self.robot.energy >= 20:
                    self.robot.charge()  

                if self.robot.energy >= 20 and self.robot.energy <= 30:
                    self.robot.repair()
         
                if self.robot.energy >= 30 and self.robot.energy <= 40:
                    self.robot.repair()

                if self.robot.energy >= 40 and self.robot.energy <= 50:
                    self.robot.repair()

                if self.robot.energy >= 50 and self.robot.energy <= 60:
                    self.robot.repair()

                if self.robot.energy >= 60 and self.robot.energy <= 70:
                    self.robot.repair()

                if self.robot.energy >= 70 and self.robot.energy <= 80:
                    self.robot.toss()

                if self.robot.energy >= 80 and self.robot.energy <= 90:
                    self.robot.toss()

                if self.robot.energy >= 90 and self.robot.energy <= 100:
                    self.robot.toss()

            if self.robot.health >= 50 and self.robot.health <= 60:
                
                if self.robot.energy <= 10:
                    self.robot.attack()

                if self.robot.energy <= 10 and self.robot.energy >= 20:
                    self.robot.attack()

                if self.robot.energy >= 20 and self.robot.energy <= 30:
                    self.robot.attack()
         
                if self.robot.energy >= 30 and self.robot.energy <= 40:
                    self.robot.attack()

                if self.robot.energy >= 40 and self.robot.energy <= 50:
                    self.robot.attack()

                if self.robot.energy >= 50 and self.robot.energy <= 60:
                    self.robot.attack()

                if self.robot.energy >= 60 and self.robot.energy <= 70:
                    self.robot.attack()

                if self.robot.energy >= 70 and self.robot.energy <= 80:
                    self.robot.toss()

                if self.robot.energy >= 80 and self.robot.energy <= 90:
                    self.robot.toss()

                if self.robot.energy >= 90 and self.robot.energy <= 100:
                    self.robot.toss()

            if self.robot.health >= 60 and self.robot.health <= 70:
                
                if self.robot.energy <= 10:
                    self.robot.attack()

                if self.robot.energy <= 10 and self.robot.energy >= 20:
                    self.robot.attack()

                if self.robot.energy >= 20 and self.robot.energy <= 30:
                    self.robot.attack()
         
                if self.robot.energy >= 30 and self.robot.energy <= 40:
                    self.robot.attack()

                if self.robot.energy >= 40 and self.robot.energy <= 50:
                    self.robot.attack()

                if self.robot.energy >= 50 and self.robot.energy <= 60:
                    self.robot.attack()

                if self.robot.energy >= 60 and self.robot.energy <= 70:
                    self.robot.attack()

                if self.robot.energy >= 70 and self.robot.energy <= 80:
                    self.robot.toss()

                if self.robot.energy >= 80 and self.robot.energy <= 90:
                    self.robot.toss()

                if self.robot.energy >= 90 and self.robot.energy <= 100:
                    self.robot.toss()

            if self.robot.health >= 70 and self.robot.health <= 80:
                
                if self.robot.energy <= 10:
                    self.robot.attack()

                if self.robot.energy <= 10 and self.robot.energy >= 20:
                    self.robot.attack()

                if self.robot.energy >= 20 and self.robot.energy <= 30:
                    self.robot.attack()
         
                if self.robot.energy >= 30 and self.robot.energy <= 40:
                    self.robot.attack()

                if self.robot.energy >= 40 and self.robot.energy <= 50:
                    self.robot.attack()

                if self.robot.energy >= 50 and self.robot.energy <= 60:
                    self.robot.attack()

                if self.robot.energy >= 60 and self.robot.energy <= 70:
                    self.robot.attack()

                if self.robot.energy >= 70 and self.robot.energy <= 80:
                    self.robot.toss()

                if self.robot.energy >= 80 and self.robot.energy <= 90:
                    self.robot.toss()

                if self.robot.energy >= 90 and self.robot.energy <= 100:
                    self.robot.toss()

            if self.robot.health >= 80 and self.robot.health <= 90:
                
                if self.robot.energy <= 10:
                    self.robot.attack()

                if self.robot.energy <= 10 and self.robot.energy >= 20:
                    self.robot.attack()

                if self.robot.energy >= 20 and self.robot.energy <= 30:
                    self.robot.attack()
         
                if self.robot.energy >= 30 and self.robot.energy <= 40:
                    self.robot.attack()

                if self.robot.energy >= 40 and self.robot.energy <= 50:
                    self.robot.attack()

                if self.robot.energy >= 50 and self.robot.energy <= 60:
                    self.robot.attack()

                if self.robot.energy >= 60 and self.robot.energy <= 70:
                    self.robot.attack()

                if self.robot.energy >= 70 and self.robot.energy <= 80:
                    self.robot.toss()

                if self.robot.energy >= 80 and self.robot.energy <= 90:
                    self.robot.toss()

                if self.robot.energy >= 90 and self.robot.energy <= 100:
                    self.robot.toss()

            if self.robot.health >= 90 and self.robot.health <= 100:
                
                if self.robot.energy <= 10:
                    self.robot.attack()

                if self.robot.energy <= 10 and self.robot.energy >= 20:
                    self.robot.attack()

                if self.robot.energy >= 20 and self.robot.energy <= 30:
                    self.robot.attack()
         
                if self.robot.energy >= 30 and self.robot.energy <= 40:
                    self.robot.attack()

                if self.robot.energy >= 40 and self.robot.energy <= 50:
                    self.robot.attack()

                if self.robot.energy >= 50 and self.robot.energy <= 60:
                    self.robot.attack()

                if self.robot.energy >= 60 and self.robot.energy <= 70:
                    self.robot.attack()

                if self.robot.energy >= 70 and self.robot.energy <= 80:
                    self.robot.toss()

                if self.robot.energy >= 80 and self.robot.energy <= 90:
                    self.robot.toss()

                if self.robot.energy >= 90 and self.robot.energy <= 100:
                    self.robot.toss()






        #     if self.robot.health <= 10 and self.robot.energy <= 40:

        #     if self.robot.health >= 30:
        #         self.robot.locateEnemy()
                
        #         return #note this will cause 10 damage to enemy and uses a turn

        #     elif self.robot.health >= 30 and self.robot.energy <= 40:
        #         self.robot.charge()
        #         return #note this will uses a turn and +20 energy

        #     elif self.robot.health <= 20:
        #         self.robot.locateEnemy()
        #         self.robot.repair()
        #         return #+10 health, uses 20 energy
           
        #     elif self.robot.energy >= 30 and self.robot.health <= 20:
        #         self.robot.locateEnemy()
        #         self.robot.escape()
        #         return #about to lose, uses a turn, teleports, uses 30 energy


        #     elif self.robot.energy >= 30 and self.robot.health <= 40:
        #         self.robot.locateEnemy()
        #         self.robot.toss()
        #         return #tosses to random location on the map
            

        #     elif self.robot.energy >= 50 and self.robot.health >= 30:
        #         self.robot.locateEnemy()
        #         self.robot.crush()
        #         return #15-25 damage, 40 energy used, end turn            
            
        #     else:
        #         return
       

        # elif self.robot.lookInFront()== "clear":
        #     # self.endgamevar + 1 #add one to the ticker to end the game

        #     if self.robot.health <=35 and self.robot.energy >= 25:
        #         self.robot.repair()
        #         return
            
        #     elif self.robot.health >= 45 and self.robot.energy >= 45:
        #         self.robot.locateEnemy()
        #         self.robot.luckyshot()
        #         return

        #     elif self.robot.health <= 40 and self.robot.energy >=30:
        #         self.robot.charge()
        #         return

        #     elif self.robot.health <= 50 and self.robot.energy >= 50:
        #         self.robot.teleport()
        #         return

        #     else:
        #         return


        # elif self.robot.lookInFront()=="wall":
        #     # self.endgamevar + 1
            
        #     self.robot.turnRight() or self.robot.turnLeft()

        #     return
            

############################################################################



        # elif self.robot.lookInFront()== "wall":
        #     self.endgamevar + 1

        # elif self.robot.lookInFront()== "clear":
        #     self.endgamevar + 1


            
        # # if self.robot.lookInFront() == "bot":
        #     self.robot.attack()#or
        #     self.robot.charge()#or
        #     self.robot.repair()#or
        #     self.robot.escape()#or
        #     self.robot.toss()#or
        #     self.robot.crush()#or







    # self.robot.luckyshot()
    #ends bots turn / uses turn, only use if enough energy. Attacks anywhere on map.
    #between 5-30 damage, can "backfire", damaging the bot starting at 0% and
    #increases between 1-20% per shot. Increase happens BEFORE the first shot
    #if backfires, between 5-15% health. Consumes 50 energy to use. 

    # self.robot.crush()  
    #attacks in front of bot, inflicts between 15 and 25 damage(randomly).
    #uses a turn, uses 40 energy if available. 

    # self.robot.toss()  
    #attacks in front of bot. inflicts 20 damage. tosses to random location.
    #70 energy to perform. Ends bots turn ONLY SUCCESFUL if enough energy.
    #uses turn inflicts 20 damage

    # self.robot.teleport()
    # 2 turns are required to rotate 180 degrees. Cost 80 energy. 
    #Uses 1 teleport token. Uses 1 turn. Teleports directly behind opponent  
    #when teleport is used, subtract 1 teleport token. self.teleport_tokens =- 1





