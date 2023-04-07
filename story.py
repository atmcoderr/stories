from configparser import ConfigParser
from instagrapi import Client

configuration = ConfigParser()
configuration.read("credentials.ini")

username = configuration['Credentials']['username']
passcode = configuration['Credentials']['password']

print("[!] Logging in using username " + str(username) + " & password " + str(passcode))

try:
    cl = Client()
    cl.login(username, passcode)
    print("[!] Logged in")

    full_path = input("[!] Enter full path to the usernames list > ")

    if full_path == "":
        print("[!] You didn't enter a path .")
        exit(0)

    usernames_lists = []
    with_stories = []

    with open(f"{full_path}", "r") as File:
        for i in File:
            res = i.replace("\n", "")
            usernames_lists.append(res)

    for x in usernames_lists:
        id_of_user = cl.user_id_from_username(x)
        story_information = cl.user_stories(user_id=id_of_user, amount=1)

        if len(story_information) == 0:
            print(f"[!] User {x} hasn't uploaded a story")
        else:
            print(f"[!] User {x} with the id {id_of_user} has uploaded a story")
            with_stories.append(x)
            with open(f"results.txt", "w") as F2:
                for i in with_stories:
                    F2.write(f"{i}\n")

except Exception as e:
    print(f"[!] Error  {e}")

