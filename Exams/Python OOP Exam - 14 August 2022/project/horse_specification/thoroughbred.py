from project import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    STEP_INCREASE_SPEED = 3

    def train(self):
        self.speed = min(self.speed + self.STEP_INCREASE_SPEED, self.MAX_SPEED)
