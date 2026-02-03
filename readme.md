[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=22502791&assignment_repo_type=AssignmentRepo)
# Make a discord bot!

## Step 1: Setup

1. Make a new file in this folder called `secret.py`. **NAME IT EXACTLY THAT!!!** You will NOT commit this file. It is for secrets.
2. Create a [Discord](https://discord.com/) account (or use one you already have)
3. Inside `secret.py` (**NOT anywhere else!!!!!**) define a variable `my_username` to be your actual Discord username, e.g.
    ```python:secret.py
    my_username = "juliet_capulet"
    ```
4. Join the class Discord server (see Schoology for the invitation link)
5. I need to give you student permissions. You might need to remind me how to update your role. I need to:

    a. Go to server settings
    
    ![server settings](img/server_settings.png)

    b. And roles

    ![roles](img/roles.png)

    c. And manage members for the "student" role

    ![manage members](img/manage_members.png)

6. Once I've given you the "student" role, make a text channel in the class Discord server just for your bot. 

7. Inside `secret.py` (**NOT anywhere else!!!!!**) define a variable `my_bot_channel` to be the name of the channel you created, e.g.
    ```python:secret.py
    my_username = "juliet_capulet"
    my_bot_channel = "juliet_bot"
    ```
8. Create a Discord Bot in the Developer Portal ([Instructions here](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal), but **NOTE: You do NOT need to make a new guild. Skip that step. Stop after you make your bot.**)

9. Toggle the "Privileged Gateway Intents":

    ![](img/privileged_intents.png)

9. Get your secret token (Click the "Reset Token" button) and copy it into your clipboard.

    ![](img/secret_token.png)

10. Inside the file `secret.py` (**NOT anywhere else!!!!!**) define a variable `my_discord_token` to be your actual discord token, e.g.
    ```python:secret.py
    my_username = "juliet_capulet"
    my_bot_channel = "juliet_bot"
    my_discord_token = "lkajshdf8werbkXicuhq3lkjrsasasdfqaDFVV"
    ```

11. Add your bot to the class Discord server.

    a. Go to the OAuth2 section in the [Discord Developer Portal](https://discord.com/developers/applications).
    
    b. Under OAuth2 URL Generator heading choose the "bot" scope.

    ![](img/scopes.png)

    c. Set the bot permissions you will need (at a minimum, you should check "View Channels" and "Send Messages")

    ![](img/permissions.png)

    d. Copy the URL and go to that URL in your internet browser. Invite your bot to the server.

    ![](img/oauth2_url.png)

12. Install the Python `discord` library.
    * On Mac or Linux, in the terminal of VSCode, run the following code:
        ```
        conda activate cs2526
        pip install discord
        ```
    * On Windows, open AnacondaPrompt and run the following code:
        ```
        conda activate cs2526
        pip install discord
        ```
13. Test that everything is set up correctly.

    a. In VSCode, open `main.py` and press the run button. In the terminal, you should see some messages like this:

    ![](img/im_in.png)

    b. Leave your code running in VSCode. Open up Discord, go to your bot channel, and type a message with the word "robot" in it. Your bot should reply.

    ![](img/bot.png)


## Step 2: Programming

Modify the two functions in `my_bot.py`.

The `should_i_respond` function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users

The `respond` function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
