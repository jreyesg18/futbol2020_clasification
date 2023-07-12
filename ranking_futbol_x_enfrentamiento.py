class ChileRanking:
    def __init__(self):
        self.teams = {}

    def add_team(self, name, rating):
        self.teams[name] = rating

    def update_rankings(self, team1, team2, result):
        rating1 = self.teams[team1]
        rating2 = self.teams[team2]

        expected1 = self.get_expectation(rating1, rating2)
        expected2 = self.get_expectation(rating2, rating1)

        k_factor = 32  # Puedes ajustar el factor K según tus necesidades

        new_rating1 = self.modify_rating(rating1, expected1, result, k_factor)
        new_rating2 = self.modify_rating(rating2, expected2, 1 - result, k_factor)

        self.teams[team1] = new_rating1
        self.teams[team2] = new_rating2

    def get_rankings(self):
        return dict(sorted(self.teams.items(), key=lambda item: item[1], reverse=True))

    def get_expectation(self, rating1, rating2):
        calc = 1.0 / (1.0 + pow(10, (rating2 - rating1) / 400.0))
        return calc

    def modify_rating(self, rating, expected, actual, k_factor):
        calc = rating + k_factor * (actual - expected)
        return calc

    def print_ranking(self):
        for index, (team, rating) in enumerate(final_rankings.items(), start=1):
            print(f"{index}. {team}: {round(rating)}")


ranking = ChileRanking()

# Agregar los equipos con sus clasificaciones iniciales
ranking.add_team("Equipo A", 1200)
ranking.add_team("Equipo B", 1100)
ranking.add_team("Equipo C", 1000)  # Agregar Equipo C
ranking.add_team("Equipo D", 1050)  # Agregar Equipo D
# Agrega el resto de los equipos de la misma manera

# Actualizar los rankings después de cada partido
ranking.update_rankings("Equipo A", "Equipo B", 1)  # El primer equipo ganó
ranking.update_rankings("Equipo C", "Equipo D", 0.5)  # Empate entre los equipos

# Obtener el ranking final
final_rankings = ranking.get_rankings()

# Imprimir el ranking
ranking.print_ranking()

