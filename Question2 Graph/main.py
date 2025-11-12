from graph import Graph
from person import Person

def run_cli():
    app = Graph()
    app.sample_data() 

    while True:
        print("\n=== SOCIAL MEDIA MENU ===")
        print("1. List all users")
        print("2. View profile")
        print("3. View following")
        print("4. View followers")
        print("5. Add new user")
        print("6. Follow a user")
        print("7. Unfollow a user")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":  
            app.list_users()
        
        elif choice == "2":
            name = input("Enter username: ").strip().capitalize()
            app.view_profile_ignore_privacy(name)

        elif choice == "3":
            name = input("Enter username: ").strip().capitalize()
            app.list_following(name)

        elif choice == "4":
            name = input("Enter username: ").strip().capitalize()
            app.list_followers(name)

        elif choice == "5":
            name = input("Enter name: ").strip().capitalize()
            gender = input("Enter gender: ").strip().capitalize()
            bio = input("Enter biography: ").strip()
            privacy = input("Privacy (public/private): ").strip().lower()
            app.add_vertex(Person(name, gender, bio, privacy))

        elif choice == "6":
            follower = input("Enter username that user who want to follow: ").strip().capitalize()
            followed = input("Enter username that user want to follow: ").strip().capitalize()
            app.add_edge(follower, followed)

        elif choice == "7":
            unfollower = input("Enter username that user who want to unfollow: ").strip().capitalize()
            unfollowed = input("Enter username that user want to unfollow: ").strip().capitalize()
            app.remove_edge(unfollower, unfollowed)  

        elif choice == "0":
            print("👋 Exiting program.")
            break

        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    run_cli()
