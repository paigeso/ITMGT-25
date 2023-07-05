'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    fm_following = social_graph.get(from_member,{}).get("following",[])
    tm_following = social_graph.get(to_member,{}).get("following",[])
    
    if to_member in fm_following and from_member in tm_following:
        return "friends"
        
    elif from_member in tm_following:
        return "followed by"
        
    elif to_member in fm_following:
        return "follower"
        
    elif to_member not in fm_following and from_member not in tm_following:
        return "no relationship"
        
    else:
        return "error"


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    for row in board:
        if all(cell == row[0] and cell for cell in row):
            return row[0]

    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[row][col] for row in range(len(board))):
            return board[0][col]

    if all(board[i][i] == board[0][0] and board[i][i] for i in range(len(board))):
        return board[0][0]

    if all(board[i][len(board)-1-i] == board[0][len(board)-1] and board[i][len(board)-1-i] for i in range(len(board))):
        return board[0][len(board)-1]

    return "No Winner"
        

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if first_stop in route_map or second_stop in route_map:
        return "Invalid stops"

    # This code serves as a checker there is a designated path connecting those exact two stops already
    if (first_stop, second_stop) in route_map:
        return route_map[(first_stop, second_stop)]['travel_time_mins']

    # This code serves as a checker for which values to add if there is no direct path from stop 1 to stop 2
    for stop in route_map:
        if stop[0] == first_stop and stop[1] != second_stop:
            intermediate_stop = stop[1]
            if (intermediate_stop, second_stop) in route_map:
                travel_time = route_map[(first_stop, intermediate_stop)]['travel_time_mins'] + \
                              route_map[(intermediate_stop, second_stop)]['travel_time_mins']
                return travel_time

    return "No valid route found."
