import json

from src.mixinget import MixinGet


class PlayList(MixinGet):

    def __init__(self, playlist_id: str):
        self.__playlist_id = playlist_id
        channel = self.get_service().playlists().list(id=playlist_id, part='snippet,contentDetails', maxResults=50).execute()
        self.title = channel['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'

    @property
    def playlist_id(self):
        return self.__playlist_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале ."""
        playlist_id = self.__playlist_id
        channel = self.get_service().playlistItems().list(part='snippet,contentDetails', playlistId=playlist_id, maxResults=50).execute()
        return print(json.dumps(channel, indent=2, ensure_ascii=False))


pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
pl.print_info()
