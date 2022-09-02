class Participant:
  def __init__(self, name):
    self.name = name
    self.__points__ = 0
    self.choice = ''

  def choose(self):
    self.choice = input('{name}, select rock, paper, scissor, lizard, spock: '.format(name = self.name))
    print("{name} selects {choice}".format(name = self.name, choice = self.choice))

  def numericalChoice(self):
    switcher = {
      'rock': 0,
      'paper': 1,
      'scissor': 2,
      "lizard": 3,
      "spock": 4
    }
    return switcher[self.choice]

  def incrementPoint(self):
    self.__points__ += 1

class GameRound:
  def __init__(self, p1, p2):
    p1.choose()
    p2.choose()

    self.rules = [
      [0, -1, 1, 1, -1],
      [1, 0, -1, -1, 1],
      [-1, 1, 0, 1, -1],
      [-1, 1, -1, 0, 1],
      [1, -1, 1, -1, 0]
    ]

    result = self.compareChoices(p1,p2)
    print("Round resulted in a {result}".format(result = self.getResultAsString(result) ))

    if result > 0:
      p1.incrementPoint()
    elif result < 0:
      p2.incrementPoint()

  def compareChoices(self, p1, p2):
    return self.rules[p1.numericalChoice()][p2.numericalChoice()]

  def awardPoints(self):
    print("implement")

  def getResultAsString(self, result):
    res = {
      0: "draw",
      1: "win",
      -1: "loss"
    }       
    return res[result]


class Game:
  def __init__(self):
    self.endGame = False
    self.participant = Participant('Alejo')
    self.secondParticipant = Participant('Vicky')
  
  def start(self):
    while not self.endGame:
      GameRound(self.participant, self.secondParticipant)
      self.checkEndCondition()

  def checkEndCondition(self):
    answer = input("Continue game y/n: ")

    if answer == 'y':
      GameRound(self.participant, self.secondParticipant)
      self.checkEndCondition()
    else:
      print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name, p1points= self.participant.__points__, p2name=self.secondParticipant.name, p2points=self.secondParticipant.__points__))
      self.determineWinner()
      self.endGame = True
  
  def determineWinner(self):
    resultString = "It's a draw"
    if self.participant.__points__ > self.secondParticipant.__points__:
      resultString = "Winner is {name}".format( name = self.participant.name )
    elif self.participant.__points__ < self.secondParticipant.__points__:
      resultString = "Winner is {name}".format(name=self.secondParticipant.name)
      print(resultString)

game = Game()
game.start()
