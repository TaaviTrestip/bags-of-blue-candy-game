class GameStats():
    def __init__(self):
        self.game_active = False
        self.reset_stats()
        
        
    def reset_stats(self):
        self.enemy_spawn_rate = 7500
        self.enemy_speed = 2
        self.candy_spawn_rate = 3000
        
        self.score = 0
        self.checker_idk = 15
        self.highscore = self.highscore_get()
        self.level = 1
        self.counter = 0
        
    
    def highscore_get(self):
        with open ("highscore.txt", "r") as file:
            highscore = int(file.read())
        return highscore
    
    
    def highscore_update(self, score):
        if score >= self.highscore:
            self.highscore = score
            with open ("highscore.txt", "w") as file:
                file.write(str(score))