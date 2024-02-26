class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def get_time(self) -> str:
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self) -> object:
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0

            if self.minutes + 1 > Time.max_minutes:
                self.minutes = 0

                if self.hours + 1 > Time.max_hours:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1

        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
