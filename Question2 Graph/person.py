class Person:
    def __init__(self, name, gender, biography, privacy="public"):
        self.name = name
        self.gender = gender
        self.biography = biography
        self.privacy = privacy

    def __str__(self):
        """String representation of the user, hides info if private."""
        if self.privacy.lower() == "private":
            return f"{self.name} (Private Profile)"
        return f"{self.name} ({self.gender}) - {self.biography}"