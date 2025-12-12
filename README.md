🎬 YouTube Video Manager (Python CLI)

A Robust Python Application for Video Management | Portfolio-Ready 🚀

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white) ![Status](https://img.shields.io/badge/Status-Complete-success) ![License](https://img.shields.io/badge/License-MIT-green) ![Built With Passion](https://img.shields.io/badge/Built_With-Passion-red)


A professional-grade command-line application designed to manage a collection of YouTube videos.
The YouTube Video Manager allows seamless CRUD operations, persistent JSON storage, and a clean interactive interface for efficient video organization.

📌 Table of Contents

  1.Features

  2.Quick Start

  3.Architecture

  4.Core Functions

  5.Key Learnings

  6.Future Enhancements

  7.About Me

License

✨ Features
Feature	Status	Description
📄 List Videos	      ✅ Complete	Display all stored videos with title and duration
➕ Add Video  	      ✅ Complete	Append new video records to the collection
✏️ Update Video	      ✅ Complete	Edit existing video details efficiently
❌ Delete Video     	✅ Complete	Remove unwanted video entries
💾 Persistent Storage	✅ Complete	JSON-based storage with automatic saving and loading
🚀 Quick Start
Installation
# Clone the repository
git clone https://github.com/your-username/youtube-video-manager.git

# Navigate to project folder
cd youtube-video-manager

# Run the application
python main.py

Sample Interface
--------------------------------------------------
            YouTube Video Manager
--------------------------------------------------

Choose an option:
1. List all YouTube videos
2. Add a YouTube video
3. Update a YouTube video
4. Delete a YouTube video
5. Exit the app

🏗️ Architecture

Core Functions Overview

load_data()             # Load videos from JSON storage
save_data_helper()      # Save updates to JSON file
list_all_videos()       # Display all video entries
add_video()             # Add new video
update_videos()         # Edit existing video
delete_video()          # Remove a video
main()                  # Interactive CLI loop


Designed with modularity and scalability in mind

Clean separation of data handling and CLI logic

Easily extendable to support categories, search, or GUI

🛠️ Core Functions

 --load_data() – Load video records or initialize storage

 --save_data_helper(videos) – Persist video list to JSON

 --list_all_videos(videos) – Display formatted video list

 --add_video(videos) – Append a new video

 --update_videos(videos) – Update existing video details

 --delete_video(videos) – Remove a video

 --main() – Interactive CLI menu

🧠 Key Learnings

 --Professional Python file I/O and JSON handling

 --Writing modular, maintainable, and reusable functions

 --Building CLI-driven applications

 --Implementing real-world CRUD workflows

 --Structuring a small project for scalability and clarity

🔮 Future Enhancements

 --Implement search functionality for videos

 --Categorize videos with tags or playlists

 --Export to CSV/Excel or integrate with a database

 --Build a GUI version with Tkinter, PyQt, or web interface

 --Add input validation and robust error handling

👨‍💻 About Me

I’m Yuvraj Singh Pundir, a Python developer building practical and professional projects.
This project demonstrates creating a robust CLI-based application with persistent storage and modular design — perfect for showcasing technical skills on GitHub.

GitHub: @your-username

📄 License

This project is licensed under the MIT License.

"Built with professionalism and maintainable design" ⏰🚀
