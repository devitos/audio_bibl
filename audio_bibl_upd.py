class Track:
    name = ''
    track_dur = 0

    def __init__(self, name, track_dur):
        self.name = name
        self.track_dur = track_dur

    def __str__(self):
        xx = f'{self.name}-{self.track_dur}min \n'
        return xx

    def __repr__(self):
        xx = f'{self.name}-{self.track_dur}min\n'
        return xx

    def __ge__(self, other):
        return print(int(self.track_dur) >= int(other.track_dur))


tr1 = Track('Мороз', 6)
tr2 = Track('Звезда', 4)
tr3 = Track('Сойка', 2)
tr4 = Track('Медведь', 3)
tr5 = Track('Лукоморье', 3)
tr6 = Track('Песня-припев', 1)


class Album:
    name = ''
    group = ''

    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.track_list = list()
        self.album_dur = 0

    def add_track(self, Track):
        self.album_dur += Track.track_dur
        self.track_list.append(Track)

    def get_duration(self):
        print(self.album_dur)

    def get_tracks(self):
        print('Альбом:', self.name)
        for tracks in self.track_list:
            print(tracks)

    def __str__(self):
        yy = f'Album - {self.name} \nGroup - {self.group}\n Tracks: \n'
        for tracks in self.track_list:
            yy += str(tracks)
        return yy


a = Album('Природа', 'Группировка')
b = Album('Животные', 'Лесовики')

a.add_track(tr1)
a.add_track(tr2)
a.add_track(tr5)
b.add_track(tr3)
b.add_track(tr4)
b.add_track(tr6)

# a.get_tracks()
# b.get_tracks()
# a.get_duration()
# b.get_duration()

print(a)
print(b)

tr1 >= tr4