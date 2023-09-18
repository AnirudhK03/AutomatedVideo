#Author: Anirudh Kondapaneni
#AutoVid generator, utilizes multiple api class to generate youtube short/tik tok videos that have a simple format of text-to-speech and subtitle overlay

import praw
from gtts import gTTS
import config
from mp3Edit import cutMP3
import config.txt

reddit = praw.Reddit(
    client_id = config.client_id,
    client_secret = config.client_secret,
    user_agent = 'autoVid by u/CurryGod03'
)

proceed = input("Hot = h, New = n, Top = t:    ")

while (proceed == 'h' or proceed == 'n' or proceed == 't'):

    subreddit_name = input("Enter name of subreddit:   ")

    subreddit = reddit.subreddit(subreddit_name)

    if (proceed == 'h'):
        new_posts = subreddit.hot(limit=1)

    if (proceed == 'n'):
        new_posts = subreddit.new(limit=1)

    if (proceed == 't'):
        new_posts = subreddit.top(limit=1)


    for post in new_posts:

        print("Title - ", post.title)

        author_name = (post.author).name
        config.sound_file_name_part = author_name

        print("Author - ", author_name)

        story = post.selftext
        print(story)

        print("\n")

    proceed = input("Story Good? (num=yes)  ")

    if (proceed.isdigit()):

        #obviously this is an area of improvment where more human-like speech can be implemented for exmaple GoogleTTS API, Amazon Polly, Speechify API, etc.

        lang = 'en'

        reader = gTTS(text=story, lang=lang, slow=False)

        sound_file_name = author_name + ".mp3"

        reader.save((sound_file_name))

        cutMP3(sound_file_name, author_name)

    else:

        proceed = input("Hot = h, New = n, Top = t:    ")

