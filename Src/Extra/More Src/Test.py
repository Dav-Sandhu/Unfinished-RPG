class Enemy():
    health = 5
    attack = 1
    player = Player()
    
    def Attack(self):
        self.player.health -= self.attack

        
    def Stats(self):
        print "Player Health: " + str(self.player.health)
        
class Player():    
    health = 5
    attack = 1
    enemy = Enemy()
    
    def Attack(self):
        self.enemy.health -= self.attack
        
    def Stats(self):
        print "Enemy Health: " + str(self.enemy.health)

player = Player()
enemy = Enemy()

player.Attack()
player.Stats()
enemy.Attack()
enemy.Stats()

