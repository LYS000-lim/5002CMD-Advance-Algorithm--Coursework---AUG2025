class Person:
    def __init__(self, name, gender, biography, privacy="public"):
        self.name = name
        self.gender = gender
        self.biography = biography
        self.privacy = privacy

    def __str__(self):
        """String representation of the user (ignore privacy)."""
        return f"{self.name} ({self.gender}) - {self.biography} [{self.privacy.capitalize()}]"
