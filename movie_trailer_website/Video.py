class Video:
    """
    The Video parent is starting to be configured
    for future implements. This will hold the
    instance variables for the Movie chiild,
    and at a later date implamentation of
    a TV child.
    """

    def __init__(self, title, duration, cast):
        self.title = title        # The title of the movie
        self.duration = duration  # The length of the movie in minutes
        self.cast = cast          # The top billed actors of the movie
