import datetime
import json

import isodate

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

    @property
    def total_duration(self):
        channel = self.get_service().playlistItems().list(part='snippet,contentDetails',
                                                          playlistId=self.playlist_id, ).execute()
        total = isodate.parse_duration('PT')
        for i in channel['items']:
            video_id = i['snippet']['resourceId']['videoId']
            video_info = self.get_service().videos().list(part='contentDetails', id=video_id).execute()
            time_format = video_info['items'][0]['contentDetails']['duration']
            time = isodate.parse_duration(time_format)
            total += time
            # dd = total.total_seconds()
        return total

    def show_best_video(self):
        count_like = 0
        channel = self.get_service().playlistItems().list(part='snippet,contentDetails',
                                                      playlistId=self.playlist_id, ).execute()
        for i in channel['items']:
            video_id = i['snippet']['resourceId']['videoId']
            video_info = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
            video_like = int(video_info['items'][0]['statistics']['likeCount'])
            if video_like > count_like:
                best_video_id = video_id

        return f'https://youtu.be/{best_video_id}'

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале ."""
        playlist_id = self.__playlist_id
        channel = self.get_service().videos().list(part='contentDetails', id='MtWXwMCAApY').execute()
        return print(json.dumps(channel, indent=3, ensure_ascii=False))


pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
pl.print_info()
