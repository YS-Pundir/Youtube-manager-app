def list_all_videos(videos):
    


while True:
    print("-"*50)
    print("Youtube Manager")
    print("-"*50)
    print()
    print("Choose an option")
    print("1. List all Youtube Video")
    print("2. Add a Youtube video ")
    print("3. Update a youtube vedio details")
    print("4. Delete a youtube video")
    print("5. Exit the app")
    choice=int(input("Enter the choice please : ",))

    match choice:
        case 1:
            list_all_videos(video)