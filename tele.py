import praw
import requests
def telegram_bot_sendtext(bot_token,bot_chatID,bot_message):

    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
count = 0
reddit = praw.Reddit(client_id='477ySXxt3C4kNQ',
                     client_secret='MisKIal4KHnj2mf8Sp4fKu4H7Ko', password='Alzeimers@14',
                     user_agent='PrawTut', username='thenikkkhil')
# subreddit = reddit.subreddit('CricketShitpost')
# for submission in subreddit.stream.submissions():
# # for submission in subreddit.stream.submissions(skip_existing=True):
#     print(submission.url)
#     msg  = submission.title + " " + submission.url
#     test = telegram_bot_sendtext('821905021:AAE2boEaulWc5A-O9O-3315mO-2orp2h1E4','609735179',msg)


import _thread

def run_app1():
    subreddit = reddit.subreddit('CricketShitpost')
    for submission in subreddit.stream.submissions():
    # for submission in subreddit.stream.submissions(skip_existing=True):
        print(submission.url)
        msg  = submission.title + " " + submission.url
        test = telegram_bot_sendtext('821905021:AAE2boEaulWc5A-O9O-3315mO-2orp2h1E4','609735179',msg)


def run_app2():
    subreddit = reddit.subreddit('natureismetal')
    for submission in subreddit.stream.submissions():
    # for submission in subreddit.stream.submissions(skip_existing=True):
        print(submission.url)
        msg  = submission.title + " " + submission.url
        test = telegram_bot_sendtext('805498128:AAH_NY7zQKCDWld14OjBcDrdrlHFvS-YSyw','609735179',msg)


if __name__=='__main__':
    _thread.start_new_thread(run_app1())
    _thread.start_new_thread(run_app2())
