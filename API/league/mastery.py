from ..base import BaseAPI


class ChampionMastery(BaseAPI):
    """Handles Champion Mastery API calls"""

    def get_all_masteries(self, puuid, platform="euw1"):
        """
        Get all champion masteries for a player

        Args:
            puuid: Player's PUUID
            platform: Platform region (na1, euw1, kr, etc.)

        Returns:
            List of all champion masteries, sorted by mastery points
        """
        base_url = self.PLATFORM_URLS[platform]
        url = f"{base_url}/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"

        return self._make_request(url)

    def get_top_masteries(self, puuid, platform="euw1", count=10):
        """
        Get top N champion masteries for a player

        Args:
            puuid: Player's PUUID
            platform: Platform region
            count: Number of top champions to return

        Returns:
            List of top champion masteries
        """
        base_url = self.PLATFORM_URLS[platform]
        url = f"{base_url}/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top"

        params = {"count": count}
        return self._make_request(url, params=params)
