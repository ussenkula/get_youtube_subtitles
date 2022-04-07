from youtube_transcript_api import YouTubeTranscriptApi
import os


def get_path(url):
    index = url.find('watch?v=') + 8
    output = url[index:]
    return output


def get_youtube_subtitles(url):
    srt = YouTubeTranscriptApi.get_transcript(url)
    text = ''
    with open('file.txt', 'w') as file:
        for i in srt:
            text += i['text'] + '\n'
        file.write(text)
    os.startfile('file.txt')


def start():
    # replace with your own url
    url = 'https://www.youtube.com/watch?v=rwgwSomR0B8&ab_channel=TheDodo'
    my_path = get_path(url)
    get_youtube_subtitles(my_path)


if __name__ == '__main__':
    start()
