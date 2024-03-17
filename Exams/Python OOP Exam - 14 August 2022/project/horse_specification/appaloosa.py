from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    STEP_INCREASE_SPEED = 2

    def train(self):
        self.speed = min(self.speed + self.STEP_INCREASE_SPEED, self.MAX_SPEED)
