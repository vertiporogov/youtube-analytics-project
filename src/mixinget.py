import os
from googleapiclient.discovery import build


class MixinGet:
    api_key: str = os.getenv('API-KEY-YouTube')

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)
