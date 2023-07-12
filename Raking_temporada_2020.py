class Chile_Ranking:
    def __init__(self):
        self.teams = {}

    def add_team(self, name):
        self.teams[name] = {
            'wins': 0,
            'draws': 0,
            'losses': 0,
            'elo': 1000  # Puntuación inicial para todos los equipos
        }

    def update_rankings(self, team, wins, draws, losses):
        team_stats = self.teams[team]

        team_stats['wins'] = wins
        team_stats['draws'] = draws
        team_stats['losses'] = losses

        self.calculate_elo(team)

    def calculate_elo(self, team):
        team_stats = self.teams[team]

        k_factor = 32  # Puedes ajustar el factor K según tus necesidades

        expected = self.calculate_expected(team_stats['wins'], team_stats['draws'], team_stats['losses'])
        actual = self.calculate_actual(team_stats['wins'], team_stats['draws'], team_stats['losses'])

        new_elo = self.modify_elo(team_stats['elo'], expected, actual, k_factor)

        team_stats['elo'] = new_elo

    def calculate_expected(self, wins, draws, losses):
        total_games = wins + draws + losses
        if total_games == 0:
            return 0
        calc = (wins + draws / 2) / total_games
        return calc

    def calculate_actual(self, wins, draws, losses):
        total_games = wins + draws + losses
        if total_games == 0:
            return 0
        calc = wins / total_games
        return calc

    def modify_elo(self, elo, expected, actual, k_factor):
        calc = elo + k_factor * (actual - expected)
        return calc

    def get_rankings(self):
        return dict(sorted(self.teams.items(), key=lambda item: item[1]['elo'], reverse=True))


ranking = Chile_Ranking()

# Agregar los equipos
ranking.add_team("Universidad Catolica")
ranking.add_team("Union la Calera")
ranking.add_team("Universidad de Chile")
ranking.add_team("Unioa Espa;ola")
ranking.add_team("Deportes Antofagasta")
ranking.add_team("Palestino")
ranking.add_team("Cobresal")
ranking.add_team("Huachipato")
ranking.add_team("Curico Unido")
ranking.add_team("O'higgins")
ranking.add_team("Santiago Wanders")
ranking.add_team("Everton")
ranking.add_team("Audax italiano")
ranking.add_team("Deportes la Serena")
ranking.add_team("Universidad de Concepcion")
ranking.add_team("Colo Colo")
ranking.add_team("Deporte Iquique")
ranking.add_team("Coquimbo Unido")

# Agrega los demás equipos de la misma manera

# Obtener el historial total de la temporada
historial_temporada = {
    "Universidad Catolica": {
        'wins': 18,
        'draws': 11,
        'losses': 5
    },
    "Union la Calera": {
        'wins': 17,
        'draws': 6,
        'losses': 11
    },
    "Universidad de Chile": {
        'wins': 13,
        'draws': 13,
        'losses': 8
    },
    "Unioa Espa;ola": {
        'wins': 14,
        'draws': 10,
        'losses': 10
    },
    "Palestino": {
        'wins': 14,
        'draws': 9,
        'losses':11
    },
    "Deportes Antofagasta": {
        'wins': 12,
        'draws': 12,
        'losses': 10
    },
    "Cobresal": {
        'wins': 13,
        'draws': 8,
        'losses': 13
    },
    "Huachipato": {
        'wins': 34,
        'draws': 13,
        'losses': 7
    },
    "Curico Unido": {
        'wins': 13,
        'draws': 7,
        'losses': 14
    },
    "O'higgins": {
        'wins': 12,
        'draws': 9,
        'losses': 13
    },
    "Santiago Wanders": {
        'wins': 12,
        'draws': 8,
        'losses': 14
    },
    "Everton": {
        'wins': 10,
        'draws': 13,
        'losses': 11
    },
    "Audax italiano": {
        'wins': 10,
        'draws': 11,
        'losses': 13
    },
    "Universidad de Concepcion": {
        'wins': 9,
        'draws': 14,
        'losses':11
    },
    "Deportes la Serena": {
        'wins': 10,
        'draws': 9,
        'losses': 15
    },
    "Colo Colo": {
        'wins': 9,
        'draws': 12,
        'losses': 13
    },
    "Deporte Iquique": {
        'wins': 9,
        'draws': 11,
        'losses': 14
    },
    "Coquimbo Unido": {
        'wins': 9,
        'draws': 8,
        'losses': 17
    }

    # Agrega el historial de los demás equipos
}

# Actualizar los rankings utilizando el historial total de la temporada
for team, stats in historial_temporada.items():
    ranking.update_rankings(team, stats['wins'], stats['draws'], stats['losses'])

# Obtener el ranking final
final_rankings = ranking.get_rankings()

# Imprimir el ranking
for index, (team, stats) in enumerate(final_rankings.items(), start=1):
    print(
        f"{index}. {team}: Ponderacion={stats['elo']}")
