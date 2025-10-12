from API.riot.account import RiotAccountAPI
from API.league.summoner import Summoner
from API.league.rank import Rank
from API.league.match import Match
from API.league.mastery import ChampionMastery


class Player:
    def __init__(self, game_name, tag_line, region="europe", platform="euw1"):
        self.game_name = game_name
        self.tag_line = tag_line
        self.region = region
        self.platform = platform

        self._account_api = RiotAccountAPI()
        self._summoner_api = Summoner()
        self._rank_api = Rank()
        self._match_api = Match()
        self._mastery_api = ChampionMastery()

        self.puuid = None
        self.summoner_info = None
        self.rank_info = None
        self.match_history = []
        self.matches = []
        self.champion_mastery = None

    def load_profile(self):
        """Load basic player profile (puuid, summoner, rank, mastery)"""
        print(f"PROFILE : {self.game_name}#{self.tag_line}")

        # Get PUUID
        self.puuid = self._account_api.get_puuid(
            self.game_name, self.tag_line, self.region
        )

        if not self.puuid:
            print("Failed to get PUUID!")
            return False

        print(f"✓ PUUID: {self.puuid}")

        # summoner info
        self.summoner_info = self._summoner_api.get_summoner_infos(
            self.puuid, self.platform
        )

        print(f"Level: {self.summoner_info['summonerLevel']}")

        # rank info
        self.rank_info = self._rank_api.get_rank_info(
            self.puuid,
            self.platform,
            by_puuid=True
        )

        if self.rank_info:
            for queue in self.rank_info:
                if queue["queueType"] == "RANKED_SOLO_5x5":
                    print(f"Rank: {queue['tier']} {queue['rank']}")

        self.champion_mastery = self._mastery_api.get_top_masteries(
            self.puuid, self.platform, count=5
        )
        print(f"[DEBUG] Champion Mastery: Loaded top 5")

        return True

    def load_match_history(self, count=100):
        self.match_history = self._match_api.get_match_history(
            self.puuid, self.region, count=count
        )

        print(f"MATCHES: {len(self.match_history)} matches")
        return self.match_history

    def load_match_details(self, match_ids=None):
        if match_ids is None:
            match_ids = self.match_history

        print(f"Loading details for {len(match_ids)} matches...")

        self.matches = []
        for i, match_id in enumerate(match_ids):
            match_data = self._match_api.get_match_details(match_id, self.region)
            if match_data:
                self.matches.append(match_data)

            if (i + 1) % 10 == 0:
                print(f"  Loaded {i + 1}/{len(match_ids)} mathces")

        print(f"MATCH DETAILS {len(self.matches)}")
        return self.matches

    def __str__(self):
        rank_str = "Unranked"
        if self.rank_info:
            for queue in self.rank_info:
                if queue["queueType"] == "RANKED_SOLO_5x5":
                    rank_str = f"{queue['tier']} {queue['rank']}"

        return f"Player({self.game_name}#{self.tag_line}, {rank_str})"
