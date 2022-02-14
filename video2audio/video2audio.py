from sys import argv
from moviepy.editor import VideoFileClip


def _help():
    print("usage : python3 video2audio.py [path_to_video_file]")

def aspliter(path): 
        video = VideoFileClip(path)
        name = path.split("/").split(".")[-2]
        video.audio.write_audiofile(fr"{name}.mp3")

aspliter(argv[1]) if len(argv) > 1 else _help()
