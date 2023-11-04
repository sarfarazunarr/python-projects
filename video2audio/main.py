from moviepy.editor import *
# Moviepy module is used here
# Audio to Video

video = VideoFileClip('videosample.mp4')
video.audio.write_audiofile('audiogot.mp3')

# Removing Audio from vide
clip2 = VideoFileClip('video2.mp4')
clip2 = clip2.without_audio()
clip2.write_videofile('silentvideo.mp4')


# add audio on another video
video = VideoFileClip('videosample.mp4')
audio = AudioFileClip('audiogot.mp3')

final_video = video.set_audio(audio)
final_video.write_videofile('it is last video.mp4')

