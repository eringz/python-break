# '''
#     Chess Dictionary Validator
#         In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', 
#         '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board. 
#         Write a function named isValidChessBoard() that takes a dictionary argument and 
#         returns True or False depending on if the board is valid.
#         A valid board will have exactly one black king and exactly one white 
#         king. Each player can only have at most 16 pieces, at most 8 pawns, and 
#         all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t 
#         be on space '9z'. The piece names begin with either a 'w' or 'b' to represent 
#         white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 
#         'king'. This function should detect when a bug has resulted in an improper 
#         chess board.
# '''


# chessBoard = {
#     '1a': '  ', '2a': '  ', '3a': '  ', '4a': '  ', '5a': '  ', '6a': '  ', '7a': '  ', '8a': '  ',
#     '1b': '  ', '2b': '  ', '3b': '  ', '4b': '  ', '5b': '  ', '6b': '  ', '7b': '  ', '8b': '  ',
#     '1c': '  ', '2c': '  ', '3c': '  ', '4c': '  ', '5c': '  ', '6c': '  ', '7c': '  ', '8c': '  ',
#     '1d': '  ', '2d': '  ', '3d': '  ', '4d': '  ', '5d': '  ', '6d': '  ', '7d': '  ', '8d': '  ',
#     '1e': '  ', '2e': '  ', '3e': '  ', '4e': '  ', '5e': '  ', '6e': '  ', '7e': '  ', '8e': '  ',
#     '1e': '  ', '2e': '  ', '3e': '  ', '4e': '  ', '5e': '  ', '6e': '  ', '7e': '  ', '8e': '  ',
#     '1f': '  ', '2f': '  ', '3f': '  ', '4f': '  ', '5f': '  ', '6f': '  ', '7f': '  ', '8f': '  ',
#     '1g': '  ', '2g': '  ', '3g': '  ', '4g': '  ', '5g': '  ', '6g': '  ', '7g': '  ', '8g': '  ',
#     '1h': '  ', '2h': '  ', '3h': '  ', '4h': '  ', '5h': '  ', '6h': '  ', '7h': '  ', '8h': '  ',
# }



# def printChessBoard(board):
#     print('+--+--+--+--+--+--+--+--+')
#     print('|%s|%s|%s|%s|%s|%s|%s|%s|8' % (board['8a'], board['8b'], board['8c'], board['8d'], board['8e'], board['8f'], board['8g'], board['8h'] ))
#     print('+--+--+--+--+--+--+--+--+')
#     print('|%s|%s|%s|%s|%s|%s|%s|%s|7' % (board['7a'], board['7b'], board['7c'], board['7d'], board['7e'], board['7f'], board['7g'], board['7h'] ))
#     print('+--+--+--+--+--+--+--+--+')
#     print('|%s|%s|%s|%s|%s|%s|%s|%s|6' % (board['6a'], board['6b'], board['6c'], board['6d'], board['6e'], board['6f'], board['6g'], board['6h'] ))
#     print('+--+--+--+--+--+--+--+--+')
#     print('|%s|%s|%s|%s|%s|%s|%s|%s|5' % (board['5a'], board['5b'], board['5c'], board['5d'], board['5e'], board['5f'], board['5g'], board['5h'] ))
#     print('+--+--+--+--+--+--+--+--+')
#     print('|%s|%s|%s|%s|%s|%s|%s|%s|4' % (board['4a'], board['4b'], board['4c'], board['4d'], board['4e'], board['4f'], board['4g'], board['4h'] ))
#     print('+--+--+--+--+--+--+--+--+')
#     print('|%s|%s|%s|%s|%s|%s|%s|%s|3' % (board['3a'], board['3b'], board['3c'], board['3d'], board['3e'], board['3f'], board['3g'], board['3h'] ))
#     print('+--+--+--+--+--+--+--+--+')
#     print('|%s|%s|%s|%s|%s|%s|%s|%s|2' % (board['2a'], board['2b'], board['2c'], board['2d'], board['2e'], board['2f'], board['2g'], board['2h'] ))
#     print('+--+--+--+--+--+--+--+--+')
#     print('|%s|%s|%s|%s|%s|%s|%s|%s|1' % (board['1a'], board['1b'], board['1c'], board['1d'], board['1e'], board['1f'], board['1g'], board['1h'] ))
#     print('+--+--+--+--+--+--+--+--+')
#     print('| a| b| c| d| e| f| g| h|')

# # chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
# chessBoard['1h'] = 'bk'
# chessBoard['6c'] = 'wq'
# chessBoard['2g'] = 'bb'
# chessBoard['5h'] = 'bq'
# chessBoard['3e'] = 'wk'

# printChessBoard(chessBoard)

def isValidChessBoard(board):
    # Initialize counters
    piece_count = {'w': 0, 'b': 0}
    king_count = {'w': 0, 'b': 0}
    pawn_count = {'w': 0, 'b': 0}

    # Valid pieces and spaces
    valid_pieces = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}
    valid_spaces = {f'{r}{c}' for r in '12345678' for c in 'abcdefgh'}

    print(valid_spaces)
    print(valid_pieces)
    print(king_count)

    for position, piece in board.items():
        print(piece[0])
        # Check if position is valid
        if position not in valid_spaces:
            return False

        # Check if piece name is valid
        if len(piece) < 5 or piece[1:] not in valid_pieces:
            return False

        color = piece[0]
        if color not in 'wb':
            return False

        # Count kings
        if piece.endswith('king'):
            king_count[color] += 1

        # Count pieces and pawns
        piece_count[color] += 1
        if piece.endswith('pawn'):
            pawn_count[color] += 1

    # Validate counts
    if king_count['w'] != 1 or king_count['b'] != 1:
        return False
    if piece_count['w'] > 16 or piece_count['b'] > 16:
        return False
    if pawn_count['w'] > 8 or pawn_count['b'] > 8:
        return False

    return True

# Example usage:
chess_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '4e': 'bking'}
print(isValidChessBoard(chess_board))  # Output: True or False depending on board validity
