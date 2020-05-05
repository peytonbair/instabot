from Driver import Driver
import time
import key
#create an instance and get activit every 1 minute
def main():
    instabot = Driver(key.username, key.password)
    instabot.login()
    instabot.messages()
    starttime=time.time()
    while True:
        print (instabot.getactivity())
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))
        instabot.refresh()


if __name__ == '__main__':
    main()
