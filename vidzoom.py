# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
try:
    from moviepy.editor import *
except:
    print("pip install ffpyplayer")

import cv2
video_location  = "/home/linuxdev/Videos/"
video = "sample-mp4-file.mp4"


def grab_audio():
    movie_clip = VideoFileClip(video_location + video)
    return movie_clip.audio


def process_movie():
    movie = cv2.VideoCapture(video_location + video)
    fps = movie.get(cv2.cv2.CAP_PROP_FPS)
    width = int(movie.get(3))
    height = int(movie.get(4))
    movie_is_open = movie.isOpened
    audio = grab_audio()
    frame_list = []

    if not movie_is_open:
        print("Video Stream Error")

    while movie_is_open:
        ret, frame = movie.read()

        if ret:
            frame = cv2.resize(frame, (width * 2, height * 2),  interpolation=cv2.INTER_NEAREST)
            frame = frame[0:height, 0:width]

            frame_list.append(ImageClip(frame).set_duration(1/fps))

        else:
            break

    new_video = concatenate_videoclips(frame_list, method="compose")
    final_video = new_video.set_audio(audio)
    final_video.write_videofile("test.mp4", fps=24)
    movie.release()
    cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process_movie()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
