class Painting:
    museum = "Louvre"

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year


mona_lisa = Painting(input(), input(), input())
print('"{}" by {} ({}) hangs in the {}.'.format(mona_lisa.title,
                                                mona_lisa.painter,
                                                mona_lisa.year,
                                                mona_lisa.museum))
