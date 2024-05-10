import os
from moviepy.editor import ImageSequenceClip, AudioFileClip


def pic2vid(image_directory: str, total_duration: int, music_file: str, output_file_name: str):
    image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
    image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(image_extensions)]
    image_files.sort()
    num_images = len(image_files)
    fps = num_images / total_duration
    clip = ImageSequenceClip([os.path.join(image_directory, filename) for filename in image_files], fps)
    audio_clip = AudioFileClip(music_file)
    trimmed_audio_clip = audio_clip.subclip(0, clip.duration)
    clip = clip.set_audio(trimmed_audio_clip)
    clip.write_videofile(output_file_name, codec="libx264", fps=60)


# folder containing the images
image_directory = "/Users/armansyed/Downloads/pic to vid/images"
total_duration = 12
# find more at https://pixabay.com/music/search/theme/background%20music/
music_file = "audio_files/vibrant-pulse-201770.mp3"
output_file_name = "output_videos/couch_listing_video.mp4"
pic2vid(image_directory, total_duration, music_file, output_file_name)
