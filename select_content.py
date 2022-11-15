#content selection
import random


videos=["bird","nature","sand","lily","rain"]




audios=["bird.wav","rain 1.wav","rain 2.wav","sand.mp3","water.wav"]


def select_audio():
    return "./data/audio/{}".format(random.choice(audios))


def select_video():
    return "./data/video/{}.mp4".format(random.choice(videos))