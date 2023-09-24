#!/usr/bin/env python3

from sys import argv
from moviepy.editor import VideoFileClip


def rotator(video_file, angle):
    video = VideoFileClip(video_file)
    #video = video.subclip(55, 65)
    video = video.rotate(angle)
    video_name = ''.join(video_file.split(".")[:-1])
    suffix = video_file.split(".")[-1]
    rotated_video_name = f"{video_name}({angle} rotated).{suffix}"
    print(rotated_video_name)
    video.write_videofile(rotated_video_name)


def main():
    if len(argv) > 2:
        video_file = argv[1]
        angle = int(argv[2])
        rotator(video_file, angle)

    else:
        print("Pyrotate : Usage > pyrotate [VIDEO_FILE_PATH] [ANGLE_TO_ROTATE]")

if __name__ == "__main__":
    main()
