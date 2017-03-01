from random import randint
class SnakesAndLadders:
  # dictionary for ladders up and snake down
  # static variable : memory sharing across mulitple objects because it's 
  # same mapping of SnakesAndLadders board for all objects
  ladder_hash = {1: 0, 2: 36, 3: 0, 4: 0, 5: 0, 6: 0, 7: 7, 8: 23, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 11, 16: -10, 17: 0, 18: 0, 19: 0, 20: 0, 21: 21, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 56, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 8, 37: 0, 38: 0, 39: 0, 40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0, 46: -21, 47: 0, 48: 0, 49: -38, 50: 0, 51: 16, 52: 0, 53: 0, 54: 0, 55: 0, 56: 0, 57: 0, 58: 0, 59: 0, 60: 0, 61: 0, 62: -43, 63: 0, 64: -4, 65: 0, 66: 0, 67: 0, 68: 0, 69: 0, 70: 0, 71: 20, 72: 0, 73: 0, 74: -21, 75: 0, 76: 0, 77: 0, 78: 20, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 10, 88: 0, 89: 0, 90: 0, 91: 0, 92: -4, 93: 0, 94: 0, 95: -20, 96: 0, 97: 0, 98: 0, 99: -19, 100: 0}

  def __init__(self, p1_start_from, p2_start_from):
    self.P1 = p1_start_from
    self.P2 = p2_start_from
    self.turn = 0         #which player's turn

  def roll_dice(self):
    die1 = randint(1,6)
    die2 = randint(1,6)
    if die1 != die2:        # If role different dice then only switch the turn else player's turn continue
      self.turn = (self.turn + 1)%2
    return die1 + die2

  def start_game(self):
    while True:
      if self.P1 == 100 or self.P2 == 100:
        print 'Game Over'
        break;
      else:
        score = self.roll_dice()
        if self.turn == 0:
          self.P1 += score
          if self.P1 == 100:
            print 'Player 1 is winner'
          elif self.P1 < 100:
            if SnakesAndLadders.ladder_hash[self.P1] != 0:
              self.P1 += SnakesAndLadders.ladder_hash[self.P1]
          if self.P1 > 100:
            self.P1 = 200 - self.P1 #if score grater then 100 then bounce
        else:
          self.P2 += score
          if self.P2 == 100:
            print 'Player 2 is winner'
          elif self.P2 < 100:
            if SnakesAndLadders.ladder_hash[self.P2] != 0:
              self.P2 += SnakesAndLadders.ladder_hash[self.P2]
          if self.P2 > 100:
            self.P2 = 200 - self.P2 #if score grater then 100 then bounce

game = SnakesAndLadders(0, 0)
game.start_game()

