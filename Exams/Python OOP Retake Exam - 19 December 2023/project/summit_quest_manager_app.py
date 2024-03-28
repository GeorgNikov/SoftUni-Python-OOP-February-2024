from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBERS = {
        "ArcticClimber": ArcticClimber,
        "SummitClimber": SummitClimber,
    }

    VALID_PEAKS = {
        "ArcticPeak": ArcticPeak,
        "SummitPeak": SummitPeak,
    }

    def __init__(self):
        self.climbers = []
        self.peaks = []
        self.climbers_names = set()

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBERS:
            return f"{climber_type} doesn't exist in our register."

        if climber_name in self.climbers_names:
            return f"{climber_name} has been already registered."

        new_climber = self.VALID_CLIMBERS[climber_type](climber_name)
        self.climbers.append(new_climber)
        self.climbers_names.add(climber_name)

        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAKS:
            return f"{peak_type} is an unknown type of peak."

        new_peak = self.VALID_PEAKS[peak_type](peak_name, peak_elevation)
        self.peaks.append(new_peak)

        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: list):
        climber = self._get_climber_by_name(climber_name)
        peak = self._get_peak_by_name(peak_name)

        for item in peak.get_recommended_gear():
            if item not in gear:
                climber.is_prepared = False
                missing_gear = list(set(peak.get_recommended_gear()) - set(gear))
                return (f"{climber_name} is not prepared to climb {peak_name}. "
                        f"Missing gear: {', '.join(sorted(missing_gear))}.")
        else:
            return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self._get_climber_by_name(climber_name)
        if not climber:
            return f"Climber {climber_name} is not registered yet."

        peak = self._get_peak_by_name(peak_name)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        sorted_climbers = sorted([c for c in self.climbers if c.conquered_peaks],
                                 key=lambda c: (-len(c.conquered_peaks), c.name))

        result = [
            f"Total climbed peaks: {len(self.peaks)}",
            "**Climber's statistics:**"
        ]

        climber_statistics = "\n".join(str(c) for c in sorted_climbers)
        result.append(climber_statistics)

        return '\n'.join(result)
    def _get_climber_by_name(self, climber_name):
        climber = [c for c in self.climbers if c.name == climber_name]
        return climber[0] if climber else None

    def _get_peak_by_name(self, peak_name):
        peak = [p for p in self.peaks if p.name == peak_name]
        return peak[0] if peak else None