import os
from slackclient import SlackClient


SLACK_TOKEN_KEY = os.environ.get('SLACK_TOKEN_KEY')
slack_client = SlackClient(SLACK_TOKEN_KEY)

from model import Game, Channel, User, Move

board = [1, 2, 3]


def play_game(input, channel, user):
    """Utilizes input from slack channel to process game play"""

    if input[0] == 'play':
        if Channel.query_channel_game is True:
            #Querying channel to see if game in plan
            message = """Sorry game in play!
                        type: " '/ttt board' to show the board! """
            return send_message(channel, message)
        elif input[1] is None:
            message = """You need to tag someone to play! \n
                        type:  '/ttt play @an_awesome_person' """
            return send_message(channel, message)
        else:
            Channel.link_game_channel(channel, user, input[1])
            message = """Time to play! \n
                         From left to right, top to bottom
                         the spaces are numbers 1-9
                         type: '/ttt move (then your number)''
                         to make a move!"""
            return send_message(channel, message)

    elif input[0] == 'board':
        return send_message(channel, display_board(channel))

    elif input[0] == 

    return


def display_board(channel):

    moves = Move.query_board_moves(channel)

    print moves

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #cb = current_board
    cb = []

    if not moves:
        for num in numbers:
            cb.append("     ")
    else:
        for num in numbers:
            for move in moves:
                if num == move[0]:
                    cb.append(move[1])
                else:
                    cb.append("     ")

    print cb

    board = '''
       | ''' + cb[0] + ''' | ''' + cb[1] + ''' | ''' + cb[2] + ''' |
    |---+---+---| 
    | ''' + cb[3] + ''' | ''' + cb[4] + ''' | ''' + cb[5] + ''' | 
    |---+---+---| 
    | ''' + cb[6] + ''' | ''' + cb[7] + ''' | ''' + cb[8] + ''' | 
    '''

    return board


def send_message(channel_id, message):
            slack_client.api_call(
                "chat.postMessage",
                channel=channel_id,
                text=message,
                username='me'
                )
            return


# board = ''' \n
# | X | O | O |
# |---+---+---|
# | O | X | X |
# |---+---+---|
# | X | O | X |
# '''
