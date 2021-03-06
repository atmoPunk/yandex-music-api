from typing import TYPE_CHECKING, Optional, List

from yandex_music import YandexMusicObject

if TYPE_CHECKING:
    from yandex_music import Client, Track, AlbumEvent, ArtistEvent


class Event(YandexMusicObject):
    """Класс, представляющий .

    Attributes:
        client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

    Args:
        client (:obj:`yandex_music.Client`, optional): Объект класса :class:`yandex_music.Client`, представляющий клиент
            Yandex Music.
        **kwargs: Произвольные ключевые аргументы полученные от API.
    """

    def __init__(self,
                 id_: str,
                 type_: str,
                 type_for_from: Optional[str] = None,
                 title: Optional[str] = None,
                 tracks: List['Track'] = None,
                 artists: List['ArtistEvent'] = None,
                 albums: List['AlbumEvent'] = None,
                 message=None,
                 device=None,
                 tracks_count: Optional[int] = None,
                 client: Optional['Client'] = None,
                 **kwargs) -> None:
        self.id = id_
        self.type = type_

        self.type_for_from = type_for_from
        self.title = title
        self.tracks = tracks
        self.albums = albums
        self.artists = artists
        self.message = message
        self.device = device
        self.tracks_count = tracks_count

        self.client = client
        self._id_attrs = (self.id, self.type)

    @classmethod
    def de_json(cls, data: dict, client: 'Client') -> Optional['Event']:
        """Десериализация объекта.

        Args:
            data (:obj:`dict`): Поля и значения десериализуемого объекта.
            client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

        Returns:
            :obj:`yandex_music.Event`: Объект класса :class:`yandex_music.Event`.
        """
        if not data:
            return None

        data = super(Event, cls).de_json(data, client)
        from yandex_music import Track, AlbumEvent, ArtistEvent
        data['tracks'] = Track.de_list(data.get('tracks'), client)
        data['albums'] = AlbumEvent.de_list(data.get('albums'), client)
        data['artists'] = ArtistEvent.de_list(data.get('artists'), client)

        return cls(client=client, **data)

    @classmethod
    def de_list(cls, data: dict, client: 'Client') -> List['Event']:
        """Десериализация списка объектов.

        Args:
            data (:obj:`list`): Список словарей с полями и значениями десериализуемого объекта.
            client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

        Returns:
            :obj:`list` из :obj:`yandex_music.Event`: Список объектов класса :class:`yandex_music.Event`.
        """
        if not data:
            return []

        events = list()
        for event in data:
            events.append(cls.de_json(event, client))

        return events
