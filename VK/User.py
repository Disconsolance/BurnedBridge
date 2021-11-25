class User:
    Name=None
    Surname=None
    Identity=None
    Username=None
    ProfilePicture=None

    def __init__(self, Name, Surname, ID, Username, ProfilePictureURL):
        self.Name=Name
        self.Surname=Surname
        self.Identity=ID
        self.Username=Username
        self.ProfilePicture=ProfilePictureURL