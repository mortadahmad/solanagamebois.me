
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from os import kill
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.constants import E
import tweepy
import time

CONSUMER_KEY = 'j43Iyo3z8mH3o8t96rxVQTgpo'
CONSUMER_SECRET = 'fMDaVwWwuut2khr8ZNfCMtaPq3Fbd9yA9F9IIvlyn9TcattiaU'
ACCESS_KEY = '1207219613613936641-WireC8j03t9hb37i8VW8wOiUYfzTkI'
ACCESS_SECRET = 'QpbKyEbbM0wlapIFVRLgCcasi9hCqkvidxZqriV1dh8Lr'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

LIKE = True
FOLLOW = True

def work():
    hashtag = entry_2.get()
    tweet = entry_3.get()
    follow = entry_6.get()

    if follow == '':
        pass
    else:
        api.create_friendship(follow)

    if tweet == '':
        pass
    else:
        api.update_status(tweet)

    if hashtag =='':
        pass
    else:
        for tweet in tweepy.Cursor(
            api.search, q=("#" + hashtag), lang="en").items():
            # try:
            
                print("\nTweet by: @" + tweet.user.screen_name)

                tweet.retweet()

                if LIKE:
                    tweet.favorite()

                if FOLLOW and not tweet.user.following:
                    tweet.user.follow() 

                time.sleep(200)

                
                
            
            # except tweepy.TweepError as e:
            #     print(e.reason)

            # except StopIteration:
            #     break

def myClick():
#     profile = entry_1.get()
#     hashtag = entry_2.get()
#     tweet = entry_3.get()
#     topic = entry_4.get()
#     message = entry_5.get()
#     follow = entry_6.get()
#     print(profile + hashtag + tweet + topic + message + follow)
    print('ok')
    work()


window = Tk()

window.geometry("720x512")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 512,
    width = 720,
    bd = 0,
    highlightthickness = 1,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
# button_image_1 = PhotoImage(
#     file=relative_to_assets("button_1.png"))
button_1 = Button(
    # image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=myClick,
    relief="flat"
)
button_1.place(
    x=551.0,
    y=462.0,
    width=130.0,
    height=26.66668701171875
)

button_2 = Button(
    borderwidth=0,
    highlightthickness=0,
    command= window.destroy,
    relief="flat"
)
button_2.place(
    x=25.0,
    y=462.0,
    width=130.0,
    height=26.66668701171875
)

canvas.create_text(
    218.0,
    40.0,
    anchor="nw",
    text="Social Media Bots",
    fill="#000000",
    font=("Roboto Light", 36 * -1)
)

canvas.create_rectangle(
    0.0,
    0.0,
    180.0,
    512.0,
    fill="#6A79FD",
    outline="")

canvas.create_text(
    195.0,
    133.0,
    anchor="nw",
    text="Enter desired profile: ",
    fill="#000000",
    font=("Roboto Light", 18 * -1)
)

canvas.create_text(
    195.0,
    169.0,
    anchor="nw",
    text="Enter specific hashtag:",
    fill="#000000",
    font=("Roboto Light", 18 * -1)
)

canvas.create_text(
    195.0,
    335.0,
    anchor="nw",
    text="Type your message:",
    fill="#000000",
    font=("Roboto Light", 18 * -1)
)

canvas.create_text(
    195.0,
    263.0,
    anchor="nw",
    text="Mass DMs:",
    fill="#000000",
    font=("Roboto Light", 18 * -1)
)

canvas.create_text(
    195.0,
    299.0,
    anchor="nw",
    text="Enter the message's topic:",
    fill="#000000",
    font=("Roboto Light", 18 * -1)
)

canvas.create_text(
    195.0,
    205.0,
    anchor="nw",
    text="Type desired tweet:",
    fill="#000000",
    font=("Roboto Light", 18 * -1)
)

canvas.create_text(
    15.0,
    54.0,
    anchor="nw",
    text="leave unwanted fields empty",
    fill="#FFFFFF",
    font=("Roboto Light", 12 * -1)
)

canvas.create_text(
    195.0,
    407.0,
    anchor="nw",
    text="Profile to follow:",
    fill="#000000",
    font=("Roboto Light", 18 * -1)
)

canvas.create_text(
    195.0,
    97.0,
    anchor="nw",
    text="Like & RT:",
    fill="#000000",
    font=("Roboto Light", 18 * -1)
)

canvas.create_rectangle(
    218.0,
    77.0,
    500.0,
    78.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    195.0,
    117.0,
    272.0,
    118.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    195.0,
    427.0,
    322.0,
    428.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    194.0,
    283.0,
    284.0,
    284.0,
    fill="#000000",
    outline="")

# entry_image_1 = PhotoImage(
#     file=relative_to_assets("entry_1.png"))
# entry_bg_1 = canvas.create_image(
#     484.0,
#     144.0,
#     image=entry_image_1
# )
entry_1 = Entry(
    bd=0,
    bg="#F1F1F1",
    highlightthickness=0
)
entry_1.place(
    x=371.0,
    y=136.0,
    width=226.0,
    height=14.0
)

# entry_image_2 = PhotoImage(
#     file=relative_to_assets("entry_2.png"))
# entry_bg_2 = canvas.create_image(
#     493.0,
#     178.0,
#     image=entry_image_2
# )
entry_2 = Entry(
    bd=0,
    bg="#F1F1F1",
    highlightthickness=0
)
entry_2.place(
    x=389.0,
    y=170.0,
    width=208.0,
    height=14.0
)

# entry_image_3 = PhotoImage(
#     file=relative_to_assets("entry_3.png"))
# entry_bg_3 = canvas.create_image(
#     479.5,
#     218.0,
#     image=entry_image_3
# )
entry_3 = Entry(
    bd=0,
    bg="#F1F1F1",
    highlightthickness=0
)
entry_3.place(
    x=362.0,
    y=210.0,
    width=235.0,
    height=14.0
)

# entry_image_4 = PhotoImage(
#     file=relative_to_assets("entry_4.png"))
# entry_bg_4 = canvas.create_image(
#     506.5,
#     312.0,
#     image=entry_image_4
# )
entry_4 = Entry(
    bd=0,
    bg="#F1F1F1",
    highlightthickness=0
)
entry_4.place(
    x=416.0,
    y=304.0,
    width=181.0,
    height=14.0
)

# entry_image_5 = PhotoImage(
#     file=relative_to_assets("entry_5.png"))
# entry_bg_5 = canvas.create_image(
#     482.5,
#     348.0,
#     image=entry_image_5
# )
entry_5 = Entry(
    bd=0,
    bg="#F1F1F1",
    highlightthickness=0
)
entry_5.place(
    x=368.0,
    y=340.0,
    width=229.0,
    height=14.0
)

# entry_image_6 = PhotoImage(
#     file=relative_to_assets("entry_6.png"))
# entry_bg_6 = canvas.create_image(
#     467.0,
#     420.0,
#     image=entry_image_6
# )
entry_6 = Entry(
    bd=0,
    bg="#F1F1F1",
    highlightthickness=0
)
entry_6.place(
    x=337.0,
    y=412.0,
    width=260.0,
    height=14.0
)

canvas.create_text(
    75.0,
    440.0,
    anchor="nw",
    text="QUIT",
    fill="#000000",
    font=("Roboto Light", 12 * -1)
)

canvas.create_text(
    600.0,
    440.0,
    anchor="nw",
    text="START",
    fill="#000000",
    font=("Roboto Light", 12 * -1)
)

window.resizable(False, False)
window.mainloop()