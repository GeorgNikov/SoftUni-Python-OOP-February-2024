from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    @property
    def sponsors(self):
        return {
            "Oracle": {
                1: 1500000,
                2: 800000,
            },
            "Honda": {
                8: 20000,
                10: 10000,
            }
        }

    @property
    def expenses_for_one_race(self):
        return 250000
