from googleapiclient.discovery import build
import json
import os

api_key: str = os.getenv('API-KEY-YouTube')
youtube = build('youtube', 'v3', developerKey=api_key)

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        id = self.channel_id
        channel = youtube.channels().list(id=id, part='snippet,statistics').execute()

        return print(json.dumps(channel, indent=2, ensure_ascii=False))
