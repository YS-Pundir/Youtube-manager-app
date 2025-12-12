import json

def load_data():
    try :
        with open("youtube.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

    
        
            
    
def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_videos(videos):
    pass
def delete_video(videos):
    pass
def exit_app(videos):
    pass
                  




videos=[]
def main():
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
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_videos(videos)
            case 4:
                delete_video(videos)
            case 5 :
                exit_app(videos)

if __name__=="__main__":#
    main()
    
    
        
        
