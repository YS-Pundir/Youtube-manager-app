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
    for index,value in enumerate(videos,start=1):#enumerate is used to give the index to the list,tuple etc
        print(f"{index}.  {value["name"]}, Duration:{value['time']} ")

def add_video(videos):
    name=input("enter the name of the video")
    time=input("enter the length of the video")
    videos.append({"name":name,"time":time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index=int (input("Enter the no of the video to be updated : ",))
    if 1<=index<=len(videos):
        name=input("enter the new name of the video")
        time=input("enter the new duraction of the video")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
        print("The information has been updated")
    else:
        print("Enter the valid input")
        
    
def delete_video(videos):
    list_all_videos(videos)
    index=int(input("enter the number of the vidoe , which needed to be deleted : ",))
    
    if 1<=index  <=len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("the video has been deleted")
    else:
        print("please enter a valid index")
    
    
def exit_app(videos):
    pass
                  

def main():
    videos=load_data()
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
    
    
        
        
