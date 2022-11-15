from quotes_reader import *
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip,vfx
from select_content import *
from youtube_upload import *
import threading
import os
import re
import random

video = VideoFileClip(select_video()).set_duration(13)
audioclip = AudioFileClip(select_audio()).set_duration(13)




def text_clip(text, start_time, duration, font="Oswald-SemiBold",font_size=60):
    return (TextClip(text, stroke_color="black",stroke_width=2,method="caption",size=video.size, color="white",fontsize=font_size,font=font)
            .set_position(("center"))
            .set_duration(duration)
            .set_start(start_time))


def init():
    quote_data= read_quote()


    # Make the text. Many more options are available.
    author_text = text_clip(text=quote_data["author"]+" said...",start_time=0, duration=3, font_size=60, font="Oswald-SemiBold")
    quote_text = text_clip(text=quote_data["quote"], start_time=3, duration=13-3, font="Roboto-Slab-ExtraBold", font_size=70)




    #saving details
    file_name=re.sub(r'[^a-zA-Z ]', '',quote_data["quote"])
    saving_path="results/{}.mp4".format(file_name)


    # Overlay text on video
    result = CompositeVideoClip(
        [video,author_text,quote_text])
    result.audio=audioclip


    result.write_videofile(saving_path)

    upload_video(file_path=saving_path,title=file_name,description="#shorts #quotes #motivation #life #nature #new #rain #relax")
    os.remove(saving_path)

    #finally
    write_next()


init()