import maskpass
from instabot import Bot



bot = Bot()

user_name=input("Please, enter your instagram username: ")
passwd=maskpass.advpass("Please, enter your instagram account password: ")

bot.login(username=user_name, password=passwd)


######## Upload a picture #####
option = input("Would you like to upload a photo? [Y/N] ")

if (option == 'Y' or option == 'y' or option == 'Yes' or option == 'YES' or option == 'yes'):
    photo = input("Insert the full path of you image: ") 
    user_caption = input("Add a caption for your post: (Leave blank if no caption is needed)")
    bot.upload_photo(photo, caption=user_caption)

######## Follow someone #######
option_2 = input("Would you like to follow someone? [Y/N] ")

if (option_2 == 'Y' or option_2 == 'y' or option_2 == 'Yes' or option_2 == 'YES' or option_2 == 'yes'):
    user = input("Enter the username (without the @) of the person you wish to follow: ")
    bot.follow(user)

####### Send a Message ######
option_3 = input("Would you like to send a message to some user? [Y/N] ")


if (option_3 == 'Y' or option_3 == 'y' or option_3 == 'Yes' or option_3 == 'YES' or option_3 == 'yes'):
    user = input("Enter the username (without the @) of the person you wish to send a message: ")
    print("Please enter the content of the message (ended with EOF): ")
    lines = []
    line = input()
    while line != 'EOF':
        lines.append(line)
        line = input()
    mess = '\n'.join(lines)

    bot.send_message(mess, user)

##### Get followers info ######
option_4= input("Would you like to know how many followers an account has? [Y/N] ")

if (option_4 == 'Y' or option_4 == 'y' or option_4 == 'Yes' or option_4 == 'YES' or option_4 == 'yes'):
    account_followers = input("Enter the username (without the @) of the person you wish to follow: ")
    followers = bot.get_user_followers(account_followers)
    for follower in followers:
        print(bot.get_user_info(follower))
#    followers_num = int(len(followers))
#    for follower in followers:
#        with open('followers.txt', 'w') as f:
#            f.write(follower)
#option_5 = input("Would you like to know who follows ", account_followers, "? [Y/N]")
#if option_5 == 'Y':
#    with open('followers.txt', 'r') as f:
#        lines = f.readlines()
#        for i in lines:
#            print(i)
#

