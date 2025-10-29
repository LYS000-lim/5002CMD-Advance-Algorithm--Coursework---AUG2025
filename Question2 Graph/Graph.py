class Person:
    def __init__(self, name, gender, biography, privacy="public"):
        self.name = name
        self.gender = gender
        self.biography = biography
        self.privacy = privacy

    def __str__(self):
        if self.privacy == "private":
            return f"{self.name} (Private Profile)"
        return f"{self.name} ({self.gender}) - {self.biography}"
        
class Graph:
    def __init__(self):
        self.graph = {}
        self.vertex_data = {}

    def add_vertex(self, person):
        if len(self.graph) > 10:
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
        if follower in self.graph and followed in self.graph[follower]:
            self.graph[follower].remove(followed)
            print(f"❌ {follower} unfollowed {followed}")
        else:
            print("⚠️ Follow relationship not found.")

    def list_users(self):
        print("\n=== List of Users ===")
        for i, user in enumerate(self.graph.key, i = 1):
            print(f"{i} : {user}")

    def view_profile(self, person_name):
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

    def list_follewers(self, person_name):
        if person_name not in self.graph:
            print("❌ User not found.")
            return
        print(f"\n👥 Followers of {person_name}:")
        followers = [u for u, v in enumerate(self.graph.item()) if person_name in v]
        if not followers:
            print("No followers.")
        else:
            for user in followers:
                print(f" - {user}")