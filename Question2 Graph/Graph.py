from person import Person

class Graph:
    def __init__(self):
        # Dictionary that maps a username to the list of users they follow
        self.graph = {}
        # Dictionary that stores Person objects (user profiles)
        self.vertex_data = {}

    def add_vertex(self, person):
        """Add a new user vertex (with a Person object)."""
        if len(self.graph) >= 10:  
            print("❌ Cannot add more than 10 users.")
            return        
        if person.name in self.graph:
            print("⚠️ User already exists.")
            return
        
        self.graph[person.name] = []
        self.vertex_data[person.name] = person
        print(f"✅ Added user: {person.name}")

    def add_edge(self, follower, followed):
        """Add a 'follows' relationship (directed edge)."""
        if follower == followed:
            print("⚠️ A user cannot follow themselves.")
            return
        if follower not in self.graph or followed not in self.graph:
            print("❌ One or both users not found.")
            return
        if followed in self.graph[follower]:
            print("⚠️ Already following this user.")
            return
        
        self.graph[follower].append(followed)
        print(f"🔗 {follower} now follows {followed}")

    def remove_edge(self, follower, followed):
        """Remove an existing follow relationship."""
        if follower in self.graph and followed in self.graph[follower]:
            self.graph[follower].remove(followed)
            print(f"❌ {follower} unfollowed {followed}")
        else:
            print("⚠️ Follow relationship not found.")

    def list_users(self):
        """List all registered users."""
        print("\n=== List of Users ===")
        for i, user in enumerate(self.graph.keys(), start=1): 
            print(f"{i}. {user}")

    def view_profile(self, person_name):
        """Display a user's profile (with privacy consideration)."""
        if person_name not in self.vertex_data:
            print("❌ User not found.")
            return
        
        user = self.vertex_data[person_name]
        if user.privacy.lower() == "private":
            print(f"Name: {user.name} (Private Profile)")
        else:
            print(f"Name: {user.name}")
            print(f"Gender: {user.gender}")
            print(f"Biography: {user.biography}")
            print(f"Privacy: {user.privacy}")

    def list_following(self, person_name):
        """Show who this user is following (outgoing edges)."""
        if person_name not in self.graph:
            print("❌ User not found.")
            return
        print(f"\n👉 {person_name} follows:")
        following = self.graph[person_name]

        if not following:
            print("No one.")
        else:
            for u in following:
                print(f" - {u}")

    def list_followers(self, person_name):
        """Show who follows this user (incoming edges)."""
        if person_name not in self.graph:
            print("❌ User not found.")
            return
        print(f"\n👥 Followers of {person_name}:")
        followers = [u for u, v in self.graph.items() if person_name in v]  
        if not followers:
            print("No followers.")
        else:
            for user in followers:
                print(f" - {user}")

    def sample_data(self):
        """Populate the graph with example users and follow relationships."""
        people = [
            Person("Lim", "Male", "I love basketball", "public"),
            Person("Jenny", "Male", "I love football", "public"),
            Person("Lisa", "Male", "I love volleyball", "private"),
            Person("John", "Female", "I love pingpong", "public"),
            Person("Cena", "Female", "I love baseball", "private"),
        ]

        for p in people:  
            self.add_vertex(p)

        # Add sample follow relationships
        self.add_edge("Lim", "Jenny")
        self.add_edge("Jenny", "John")
        self.add_edge("John", "Cena")
        self.add_edge("Lisa", "Lim")
        self.add_edge("Cena", "Lim")

    def view_profile_ignore_privacy(self, person_name):
        """Display full profile details regardless of privacy setting."""
        if person_name not in self.vertex_data:
            print("❌ User not found.")
            return

        user = self.vertex_data[person_name]
        print("\n=== Profile Information (Ignore Privacy) ===")
        print(f"Name: {user.name}")
        print(f"Gender: {user.gender}")
        print(f"Biography: {user.biography}")
        print(f"Privacy: {user.privacy}")

