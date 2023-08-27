import logging

import util
from game import Actions, Agent, Directions
from pacman import GameState
from util import manhattanDistance


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class Q2A_Agent(Agent):


    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

    def getAction(self, gameState: GameState):
        """
            Returns the minimax action from the current gameState using self.depth
            and self.evaluationFunction.

            Here are some method calls that might be useful when implementing minimax.

            gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

            gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

            gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        logger = logging.getLogger('root')
        logger.info('MinimaxAgent')

        v = float("-inf")
        bestAction = []
        agent = 0
        actions = gameState.getLegalActions(agent)
        successors = [(action, gameState.generateSuccessor(agent, action)) for action in actions]
        for successor in successors:
            temp = minimax(1, range(gameState.getNumAgents()), successor[1], self.depth, self.evaluationFunction)
            if temp > v:
              v = temp
              bestAction = successor[0]
        return bestAction
        
def minimax(agent, agentList, state, depth, evalFunc):
      
      # at Leaf
      if depth <= 0 or state.isWin() == True or state.isLose() == True:
        return evalFunc(state)
        
      if agent == 0:
        v = float("-inf")
      else:
        v = float("inf")
              
      actions = state.getLegalActions(agent)
      successors = [state.generateSuccessor(agent, action) for action in actions]
      for j in range(len(successors)):
        successor = successors[j]
        if agent == 0: 
            v = max(v, minimax(agentList[agent+1], agentList, successor, depth, evalFunc))
        elif agent == agentList[-1]:
          v = min(v, minimax(agentList[0], agentList, successor, depth - 1, evalFunc))
        else:
          v = min(v, minimax(agentList[agent+1], agentList, successor, depth, evalFunc))
      
      return v

    


    #     legalActions = gameState.getLegalActions(self.index)
    #     bestAction = None
    #     bestScore = float('-inf')

    #     for action in legalActions:
    #         successorState = gameState.generateSuccessor(self.index, action)
    #         score = self.minValue(successorState, 1, self.depth) + self.heuristic(successorState)
            
    #         if score > bestScore:
    #             bestScore = score
    #             bestAction = action
        
    #     return bestAction

    # def heuristic(self, state):
    #     pacmanPosition = state.getPacmanPosition()
    #     foodGrid = state.getFood()
    #     remainingFood = foodGrid.asList()

    #     if not remainingFood:
    #         return 0

    #     # Calculate Manhattan distance to the closest food dot
    #     minFoodDist = float('inf')
    #     for food in remainingFood:
    #         minFoodDist = min(minFoodDist, manhattanDistance(pacmanPosition, food))

    #     # Avoid ghosts if they are too close
    #     for ghost in state.getGhostPositions():
    #         if manhattanDistance(pacmanPosition, ghost) < 2:
    #             return -float('inf')
        
    #     # Return reciprocal of distance as a heuristic value
    #     return 1.0 / minFoodDist

    
    # def base(self, state,agentIndex, depth):
    #     return depth == 0 or state.isWin() or state.isLose() or agentIndex >= state.getNumAgents()

    # def maxValue(self,state , depth):
    #     legalActions = state.getLegalActions(self.index)
    #     maxValue = float('-inf')

    #     if self.base(state,self.index,depth):
    #         return self.evaluationFunction(state)

    #     for action in legalActions:
    #         successorState = state.generateSuccessor(self.index, action)
    #         maxValue = max(maxValue, self.minValue(successorState, 1, depth))

    #     return maxValue

    # def minValue(self, state, agentIndex, depth):
    #     legalActions = state.getLegalActions(agentIndex)
    #     minValue = float('inf')

    #     if self.base(state,agentIndex,depth):
    #         return self.evaluationFunction(state)

    #     for action in legalActions:
    #         successorState = state.generateSuccessor(agentIndex, action)
    #         if agentIndex == state.getNumAgents() -1:
    #             minValue = min(minValue, self.maxValue(successorState, depth - 1))
    #         else:
    #             minValue = min(minValue, self.minValue(successorState, agentIndex + 1, depth))

    #     return minValue





    
