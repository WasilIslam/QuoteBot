from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo

# loggin into the channel
channel = Channel()
channel.login("client_secrets.json", "credentials.storage")

def upload_video(file_path,title,description):

    # setting up the video that is going to be uploaded
    video = LocalVideo(file_path=file_path)

    # setting snippet
    video.set_title(title)
    video.set_description(description)
    video.set_tags(["muslim", "deen","success","Allah","Hadith","Sahih Bukhari"])
    video.set_category("education")
    video.set_default_language("en-US")

    # setting status
    video.set_embeddable(True)
    video.set_license("creativeCommon")
    video.set_privacy_status("public")
    video.set_public_stats_viewable(True)

    # setting thumbnail
    # video.set_thumbnail_path('data/image/stop.jpg')

    # uploading video and printing the results
    video = channel.upload_video(video)
    print(video.id)
    print(video)

    # liking video
    video.like()