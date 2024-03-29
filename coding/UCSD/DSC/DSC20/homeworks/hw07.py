"""
DSC 20 Homework 07
Name: Jack Kai Lim
PID:  A16919063
"""

def doctests_go_here():
    """
    >>> track1 = Song('More Life', 3.11, 'Just Until...', 'Cordae', 1220980)
    >>> print(track1)
    'More Life' by Cordae on 'Just Until...' is 3.11 minutes long with 1220980\
 streams
    >>> track1.get_artist()
    'Cordae'

    >>> Song.platform
    'Spotify'
    >>> track1.platform
    'Spotify'

    >>> play1 = Playlist('Rap Caviar', 'James')
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 0 songs
    >>> play1.add_song(track1)
    True
    >>> play1.get_total_streams()
    1220980
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 1 songs
    >>> play1.add_song(track1)
    False
    >>> play1.remove_song(track1)
    True
    
    >>> track2 = Song('Good Days', 4.65, 'Good Days', 'SZA', 276568815)
    >>> track3 = Song('Heat Waves', 3.999, 'Dreamland', 'Glass Animals', 5000)
    >>> play1.add_song(track2)
    True
    >>> play1.add_song(track1)
    True
    >>> play1.add_song(track3)
    True
    >>> track2.add_to_playlist(play1)
    False

    >>> play1.sort_songs('length')
    >>> [x.get_name() for x in play1.get_songs()]
    ['More Life', 'Heat Waves', 'Good Days']
    >>> play1.sort_songs('name')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Good Days', 'Heat Waves', 'More Life']
    >>> play1.sort_songs('streams')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Heat Waves', 'More Life', 'Good Days']

    >>> play1.get_most_played_song()
    'Good Days'
    >>> play1.get_total_streams()
    277794795
    >>> play1.get_total_length()
    11.759

    >>> print(play1.play())
    Listening to 'Heat Waves' by Glass Animals
    Listening to 'More Life' by Cordae
    Listening to 'Good Days' by SZA

    >>> print(track1.listen())
    Listening to 'More Life' by Cordae
    >>> play1.get_total_streams()
    277794799

    >>> play2 = Playlist('Anti Pop', 'Spotify')
    >>> play1.combine_playlists(play2)
    True
    >>> play2.combine_playlists(play1)
    True
    >>> print(play2)
    Playlist 'Anti Pop' by Spotify has 3 songs
    >>> play2.combine_playlists(play1)
    3
    >>> play2.remove_song(track2)
    True
    >>> play2.get_most_played_song()
    'More Life'

    >>> track2.add_to_playlist(play2)
    True
    >>> play2.get_most_played_song()
    'Good Days'


    # Add your doctests below here #

    >>> play3 = Playlist('Stonks', 'Jack')
    >>> itte = Song('Itte', 3.21, 'Flowers', 'Yorushika', 1000000)
    >>> play3.add_song(itte)
    True
    >>> print(play3)
    Playlist 'Stonks' by Jack has 1 songs
    >>> print(play3.play())
    Listening to 'Itte' by Yorushika
    >>> play3.get_total_streams()
    1000001

    """



class Song:
    """
    Implementation of a song
    """
    # TODO: Initialize class attribute
    platform = 'Spotify'

    def __init__(self, name, length, album, artist, streams):
        """
        Constructor of Song

        Parameters:
        name (str): name of the song
        length (float): song duration in minutes
        album (str): name of album the song is in
        artist (str): name of artist
        streams (int): number of times the song has been streamed
        """
        # YOUR CODE STARTS HERE #
        assert isinstance(name, str)
        assert len(name) > 0
        self.name = name
        assert isinstance(length, float)
        assert length > 0
        self.length = length
        assert isinstance(album, str)
        assert len(album) > 0
        self.album = album
        assert isinstance(artist, str)
        assert len(artist) > 0
        self.artist = artist
        assert isinstance(streams, int)
        assert streams >= 0
        self.streams = streams

    def get_name(self):
        """ Getter for name attribute """
        # YOUR CODE STARTS HERE #
        return self.name

    def get_length(self):
        """ Getter for length attribute """
        # YOUR CODE STARTS HERE #
        return self.length

    def get_album(self):
        """ Getter for album attribute """
        # YOUR CODE STARTS HERE #
        return self.album

    def get_artist(self):
        """ Getter for artist attribute """
        # YOUR CODE STARTS HERE #
        return self.artist

    def get_streams(self):
        """ Getter for streams attribute """
        # YOUR CODE STARTS HERE #
        return self.streams

    def __str__(self):
        """
        String representation of Song
        """
        # YOUR CODE STARTS HERE #
        return "'" + self.name + "'" + ' by ' + self.artist + ' on ' + "'" +\
        self.album + "'" + ' is '+ str(self.length) + ' minutes long with ' +\
        str(self.streams) +' streams'

    def listen(self):
        """
        Listens to the song, increasing the stream counter.
        Returns a string with the song name and artist
        """
        # YOUR CODE STARTS HERE #
        self.streams += 1
        return 'Listening to ' + "'" + self.name + "'" + ' by ' + self.artist

    def add_to_playlist(self, playlist):
        """
        Takes a Playlist object and adds the current Song instance into it.
        return True if successful
        return False if song is already included in playlist
        """
        # YOUR CODE STARTS HERE #
        assert isinstance(playlist, Playlist)
        if self in playlist.songs:
            return False
        else:
            playlist.songs.append(self)
            return True



class Playlist:
    """
    Implementation of a playlist
    """

    def __init__(self, title, user):
        """
        Constructor of Playlist

        Parameters:
        title (str): title of the playlist
        user (str): username of user who created playlist

        Attributes:
        songs (list): list used to store songs in playlist
        """
        # YOUR CODE STARTS HERE #
        assert isinstance(title, str)
        assert len(title) > 0
        self.title = title
        assert isinstance(user, str)
        assert len(user) > 0
        self.user = user
        self.songs = []

    def get_title(self):
        """ Getter for title attribute """
        # YOUR CODE STARTS HERE #
        return self.title

    def get_user(self):
        """ Getter for user attribute """
        # YOUR CODE STARTS HERE #
        return self.user

    def get_songs(self):
        """ Getter for songs attribute """
        # YOUR CODE STARTS HERE #
        return self.songs

    def __str__(self):
        """
        String representation of Playlist
        """
        # YOUR CODE STARTS HERE #
        return 'Playlist ' + "'" + self.title + "'" + ' by ' + self.user + \
        ' has ' + str(len(self.songs)) + ' songs'

    def add_song(self, song):
        """
        Adds song to list
        return True if successful
        return False if song is already included in playlist
        """
        # YOUR CODE STARTS HERE #
        assert isinstance(song, Song)
        if song in self.songs:
            return False
        else:
            self.songs.append(song)
            return True

    def remove_song(self, song):
        """
        Removes a song from the list
        return True if successful
        return False if song is not in the playlist
        """
        # YOUR CODE STARTS HERE #
        assert isinstance(song, Song)
        if song in self.songs:
            self.songs.remove(song)
            return True
        else:
            return False

    def sort_songs(self, sort_by):
        """
        Sorts the songs by the sort_by attribute in ascending order
        """
        # YOUR CODE STARTS HERE #
        assert isinstance(sort_by, str)
        assert True if sort_by in ['name', 'length', 'album', 'artist',
                                   'streams'] else False
        if sort_by == 'name':
            self.songs.sort(key=lambda x:x.name)
        elif sort_by == 'length':
            self.songs.sort(key=lambda x: x.length)
        elif sort_by == 'streams':
            self.songs.sort(key=lambda x: x.streams)
        elif sort_by == 'artist':
            self.songs.sort(key=lambda x: x.artist)
        elif sort_by == 'album':
            self.songs.sort(key=lambda x: x.album)

    def get_total_streams(self):
        """
        Returns the total amount of streams of the songs in the playlist
        """
        # YOUR CODE STARTS HERE #
        return sum([getattr(song, 'streams') for song in self.songs])

    def get_total_length(self):
        """
        Returns the total length of the playlist
        """
        # YOUR CODE STARTS HERE #
        return sum([getattr(song, 'length') for song in self.songs])

    def play(self):
        """
        Plays every song in the playlist.
        Returns a string that contains information on all the songs played.
        Format is specified in the writeup
        If the playlist is empty, return "Empty"
        """
        # YOUR CODE STARTS HERE #
        string = ''
        if len(self.songs) == 0:
            return 'Empty'
        else:
            for song in self.songs:
                string = string + song.listen()
                if song != self.songs[-1]:
                    string = string + '\n'
            return string

    def combine_playlists(self, other_playlist):
        """
        Add all songs from other_playlist to current playlist.
        If all songs were added successfully, return True. 
        If not, return the number of songs that weren't added.
        """
        # YOUR CODE STARTS HERE #
        assert isinstance(other_playlist, Playlist)
        check = [self.add_song(song) for song in other_playlist.songs]
        if all(check):
            return True
        else:
            return len(check) - sum(check)



    def get_most_played_song(self):
        """
        Return the name of the most played song
        """
        # YOUR CODE STARTS HERE #
        stream_sorted = sorted(self.songs, key=lambda x:x.streams)
        return stream_sorted[-1].name


################ RECURSION PART ##################

#Question 2.5
def type_with_number(message):
    """
    >>> type_with_number('Welcome to Beijing!')
    '9352663086023454641'
    >>> type_with_number('I miss my laptop.')
    '40647706905278671'
    >>> type_with_number('!!??..  ,,')
    '1111110011'
    """
    key1 = 1
    key2 = 2
    key3 = 3
    key4 = 4
    key5 = 5
    key6 = 6
    key7 = 7
    key8 = 8
    key9 = 9
    key0 = 0

    if len(message) == 1:
        if message[0] in [',', '.', '?', '!']:
            return str(key1)
        elif message[0].lower() in ['a', 'b', 'c']:
            return str(key2)
        elif message[0].lower() in ['d', 'e', 'f']:
            return str(key3)
        elif message[0].lower() in ['g', 'h', 'i']:
            return str(key4)
        elif message[0].lower() in ['j', 'k', 'l']:
            return str(key5)
        elif message[0].lower() in ['m', 'n', 'o']:
            return str(key6)
        elif message[0].lower() in ['p', 'q', 'r', 's']:
            return str(key7)
        elif message[0].lower() in ['t', 'u', 'v']:
            return str(key8)
        elif message[0].lower() in ['w', 'x', 'y', 'z']:
            return str(key9)
        elif message[0] == ' ':
            return str(key0)
    else:
        if message[0] in [',', '.', '?', '!']:
            return str(key1) + type_with_number(message[1:])
        elif message[0].lower() in ['a', 'b', 'c']:
            return str(key2) + type_with_number(message[1:])
        elif message[0].lower() in ['d', 'e', 'f']:
            return str(key3) + type_with_number(message[1:])
        elif message[0].lower() in ['g', 'h', 'i']:
            return str(key4) + type_with_number(message[1:])
        elif message[0].lower() in ['j', 'k', 'l']:
            return str(key5) + type_with_number(message[1:])
        elif message[0].lower() in ['m', 'n', 'o']:
            return str(key6) + type_with_number(message[1:])
        elif message[0].lower() in ['p', 'q', 'r', 's']:
            return str(key7) + type_with_number(message[1:])
        elif message[0].lower() in ['t', 'u', 'v']:
            return str(key8) + type_with_number(message[1:])
        elif message[0].lower() in ['w', 'x', 'y', 'z']:
            return str(key9) + type_with_number(message[1:])
        elif message[0] == ' ':
            return str(key0) + type_with_number(message[1:])



# Question 3.1

def create_palindrome_v1(start, end):
    """
    Creates a palindrome of integers starting from start, ending at end
    (in the middle) All inputs are positive integers. No input validation
    required.
    Parameters: start, end (int), positive integers
    Returns: palindrome sequence (str)
    Restrictions. You should use recursion in this question.
    >>> create_palindrome_v1(1, 1)
    '1'
    >>> create_palindrome_v1(3, 5)
    '34543'
    >>> create_palindrome_v1(5, 2)
    '5432345'
    
    # Add your doctests below here #
    >>> create_palindrome_v1(10, 1)
    '109876543212345678910'
    >>> create_palindrome_v1(0,0)
    '0'
    >>> create_palindrome_v1(3, 0)
    '3210123'

    """
    # your code is here
    if start == end:
        return str(start)
    elif start > end:
        return str(start) + create_palindrome_v1(start - 1, end) + str(start)
    elif start < end:
        return str(start) + create_palindrome_v1(start + 1, end) + str(start)




def create_palindrome_v2(start1, end1, start2, end2):
    """
    Creates a two level palindrome of integers. The first level (outer level)
    starts from start1 and ends at end1. The second level (inner level) starts
    from start2 and end2. No input validation is required.
    Parameters: start1, end1, start2, end2 (int), positive integers
    Returns: palindrome sequence (str)
    Restrictions. You should use recursion in this question.
    >>> create_palindrome_v2(1, 1, 1, 1)
    '1_1_1'
    >>> create_palindrome_v2(2, 5, 5, 4)
    '2345_545_5432'
    >>> create_palindrome_v2(3, 1, 5, 9)
    '321_567898765_123'
    
    # Add your doctests below here #
    >>> create_palindrome_v2(3, 1, 2, 3)
    '321_232_123'
    >>> create_palindrome_v2(0, 1, 0, 1)
    '01_010_10'
    >>> create_palindrome_v2(9, 1, 1, 1)
    '987654321_1_123456789'

    """
    # your code is here
    divisor = 2
    one = create_palindrome_v1(start1, end1)
    two = create_palindrome_v1(start2, end2)
    return one[0:-(-len(one)//divisor)] + '_' + two + '_' +\
           one[len(one)//divisor:]

# Question 4


def lutee_reproduction(n):
    """
    # As the  lutee's reproduction is has the same sequence as the fibonnaci
     sequence, I crafted a alteration of the sequence, which starts at 2,
     2 and continues as the fibonacci sequence from there.#

    >>> lutee_reproduction(1)
    2
    >>> lutee_reproduction(2)
    2
    >>> lutee_reproduction(3)
    4
    >>> lutee_reproduction(4)
    6
    >>> lutee_reproduction(6)
    16

    # Add your doctests below here #
    >>> lutee_reproduction(10)
    110
    >>> lutee_reproduction(0)
    0
    >>> lutee_reproduction(5)
    10
    """

    # your code is here
    assert isinstance(n, int)
    two = 2
    if n == 0:
        return 0
    elif n == 1 or n == two:
        return two
    else:
        return lutee_reproduction(n-1) + lutee_reproduction(n-two)

