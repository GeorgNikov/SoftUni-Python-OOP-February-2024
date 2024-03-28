from project import Band
from project import Drummer
from project import Guitarist
from project import Singer
from project import Concert


class ConcertTrackerApp:

    MUSICIANS_TYPE = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer,
    }

    CONCERTS = {
        "Rock": {
            "Drummer": "play the drums with drumsticks",
            "Singer": "sing high pitch notes",
            "Guitarist": "play rock",
        },
        "Metal": {
            "Drummer": "play the drums with drumsticks",
            "Singer": "sing low pitch notes",
            "Guitarist": "play metal",
        },
        "Jazz": {
            "Drummer": "play the drums with drum brushes",
            "Singer": ["sing high pitch notes", "sing low pitch notes"],
            "Guitarist": "play jazz",
        },
    }

    CONCERTS_GENRE_SKILLS = {
        "Rock": ["play the drums with drumsticks", "sing high pitch notes", "play rock"],
        "Metal": ["play the drums with drumsticks", "sing low pitch notes", "play metal"],
        "Jazz": ["play the drums with drum brushes", "sing high pitch notes", "sing low pitch notes", "play jazz"],
    }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.MUSICIANS_TYPE:
            raise ValueError("Invalid musician type!")

        musician = self._get_musician_by_name(name)

        if musician in self.musicians:
            raise Exception(f"{name} is already a musician!")

        new_musician = self.MUSICIANS_TYPE[musician_type](name, age)
        self.musicians.append(new_musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = self._get_band_by_name(name)

        if band in self.bands:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self._get_concert_by_place(place)

        if concert in self.concerts:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._get_musician_by_name(musician_name)
        band = self._get_band_by_name(band_name)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        musician = self._get_musician_by_name(musician_name)
        band = self._get_band_by_name(band_name)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        if musician not in band.members:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self._get_band_by_name(band_name)
        concert = self._get_concert_by_place(concert_place)

        for musician_type in self.MUSICIANS_TYPE:
            if not all(filter(lambda x: x.__class__.__name__ == musician_type, band.members)):
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        existing_skills = ([s for s in [', '.join(bm.skills) for bm in band.members]
                            if s in self.CONCERTS_GENRE_SKILLS[concert.genre]])
        print(existing_skills)
        # MY SOLUTION
        added = []
        count_skills = 0

        for member in band.members:
            if member.__class__.__name__ == "Singer" and concert.genre == "Jazz":
                try:
                    if (member.skills[0] in self.CONCERTS_GENRE_SKILLS[concert.genre] and
                            member.skills[1] in self.CONCERTS_GENRE_SKILLS[concert.genre]):
                        added.append(member)
                        count_skills += 2
                except IndexError:
                    break
            else:
                if member.skills[0] in self.CONCERTS_GENRE_SKILLS[concert.genre]:
                    added.append(member)
                    count_skills += 1

        if concert.genre == "Jazz":
            if len(added) < 3 and count_skills < 4 and len(existing_skills) < 3:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
        else:
            if len(added) < 3 and count_skills < 3 and len(existing_skills) < 3:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        # AUTHOR SOLUTION
        # if concert.genre == 'Rock':
        #     for band_member in band.members:
        #         if band_member.__class__.__name__ == 'Drummer' and \
        #                  "play the drums with drumsticks" not in band_member.skills:
        #             raise Exception(f"The {band_name} band is not ready to play at the concert!")
        #         if band_member.__class__.__name__ == 'Singer' and "sing high pitch notes" not in band_member.skills:
        #             raise Exception(f"The {band_name} band is not ready to play at the concert!")
        #         if band_member.__class__.__name__ == 'Guitarist' and "play rock" not in band_member.skills:
        #             raise Exception(f"The {band_name} band is not ready to play at the concert!")
        #
        # elif concert.genre == 'Metal':
        #     for band_member in band.members:
        #         if band_member.__class__.__name__ == 'Drummer' and "play the drums with drumsticks"
        #         not in band_member.skills:
        #             raise Exception(f"The {band_name} band is not ready to play at the concert!")
        #         if band_member.__class__.__name__ == 'Singer' and "sing low pitch notes" not in band_member.skills:
        #             raise Exception(f"The {band_name} band is not ready to play at the concert!")
        #         if band_member.__class__.__name__ == 'Guitarist' and "play metal" not in band_member.skills:
        #             raise Exception(f"The {band_name} band is not ready to play at the concert!")
        #
        # elif concert.genre == 'Jazz':
        #     for band_member in band.members:
        #         if band_member.__class__.__name__ == 'Drummer' \
        #                 and "play the drums with drum brushes" not in band_member.skills:
        #             raise Exception(f"The {band_name} band is not ready to play at the concert!")
        #         if band_member.__class__.__name__ == 'Singer' \
        #                 and ("sing low pitch notes" not in band_member.skills
        #                      or "sing high pitch notes" not in band_member.skills):
        #             raise Exception(f"The {band_name} band is not ready to play at the concert!")
        #         if band_member.__class__.__name__ == 'Guitarist' and "play jazz" not in band_member.skills:
        #             raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    # Helper methods
    def _get_musician_by_name(self, name):
        musician = [m for m in self.musicians if m.name == name]
        return musician[0] if musician else None

    def _get_band_by_name(self, name):
        band = [b for b in self.bands if b.name == name]
        return band[0] if band else None

    def _get_concert_by_place(self, place):
        concert = [c for c in self.concerts if c.place == place]
        return concert[0] if concert else None
