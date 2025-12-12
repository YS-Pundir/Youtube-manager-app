import json
videos=[]
def load_data():
    try :
        with open("youtube.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos,file)       
    
def list_all_videos(videos):
    for index,value in enumerate(videos,start=1):
        print(f"{index}.  {value["name"]}, Duration:{value['time']} ")

def add_video(videos):
    name=input("enter the name of the video")
    time=input("enter the length of the video")
    videos.append({"name":name,"time":time})
    save_data_helper(videos)

def update_videos(videos):
    pass
def delete_video(videos):
    pass
def exit_app(videos):
    pass
                  





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
        print(videos)
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
    
    
        
        
