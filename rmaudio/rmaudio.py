#!/usr/bin/env python3

import sys
from argparse import ArgumentParser
from moviepy.editor import VideoFileClip


def main(file_path):
    try:
        print("- Loading file", end="\t\t")
        videoclip = VideoFileClip(file_path)
        print("[Finished]")

        print("- Removing audio", end="\t")
        new_clip = videoclip.without_audio()
        print("[Finished]")

        print("- Saving the audio_removed version")
        save_name = file_path.replace(".mp4", "(audio_removed).mp4")
        new_clip.write_videofile(save_name)

    except Exception as err:
        print(err)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", '--path', help="path of video")
    args = parser.parse_args()

    if len(sys.argv) > 1:
        if file_path:=args.path:
            main(file_path)

    else:
        parser.print_help()
        sys.exit()
