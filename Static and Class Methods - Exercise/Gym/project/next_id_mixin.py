class NextIdMixin:
    id = 0      # NOT USED
    @classmethod
    def get_next_id(cls):
        return cls.id

    @classmethod
    def increment_id(cls):
        cls.id += 1