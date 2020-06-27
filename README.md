# InstaBot

InstaBot can be used as a python library in order to fetch followers, following and hash tagged list from Instagram.

## Installation

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to work with InstaBot.

```bash
pip3 install selenium
sudo apt-get install chromium-browser
pip3 install webdriver-manager
```

## Usage

```python
python3 insta_bot.py

Username:  # Enter Instagram username
Password:  # Enter Instagram password

Select The Choice
1  --> Hashtag         # Fetch people who have tagged in a particular Hashtag
2  --> Follow List     # Fetch followers and following list of an Instagram account
0 --> Exit             # Exit

Enter your choice:     # Please enter your choice

# If you have chosen Hashtag

Hashtag:               # Enter the hashtag in order to fetch(without including #).
1 --> Top Post         # Get the peoples list who belongs to the top post in that Hashtag
2 --> Most Recent      # Get the peoples list who have recently tagged that particular Hashtag

Select Choice:         # Select your choice

Tagged Person List:    # Gives you the selected choice list

# If you have chosen Follow

Followers/Following List
Account:               # Enter the insta name of the account in order to fetch

Total followers:       # Gives you the total followers of the account
Followers List:  {Gives you the followers list}

Total following:       # Gives you the total following of the account
Following List:        # Gives you the following list

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
