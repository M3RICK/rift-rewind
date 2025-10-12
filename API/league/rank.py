from ..base import BaseAPI


class Rank(BaseAPI):
    """Handles League Rank/League API calls"""

    def get_rank_info(self, summoner_id, platform="euw1"):
        """
        Get rank information for a summoner

        Args:
            summoner_id: Encrypted summoner ID (from get_summoner_infos)
            platform: Platform region (na1, euw1, kr, etc.)

        Returns:
            List of league entries (can have multiple queues - ranked solo, flex, etc.)
        """
        base_url = self.PLATFORM_URLS[platform]
        url = f"{base_url}/lol/league/v4/entries/by-summoner/{summoner_id}"

        return self._make_request(url)
