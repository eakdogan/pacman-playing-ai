# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import game
import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).

  You do not need to change anything in this class, ever.
  """

  def getStartState(self):
     """
     Returns the start state for the search problem
     """
     util.raiseNotDefined()

  def isGoalState(self, state):
     """
       state: Search state

     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state

     For a given state, this should return a list of triples,
     (successor, action, stepCost), where 'successor' is a
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take

     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()


def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]

  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:

  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  fringe = util.Stack()
  fringe.push( (problem.getStartState(), [], []) )
  while not fringe.isEmpty():
      node, actions, visited = fringe.pop()
      def getKey(item): #caution: y,x seems to be reversed in medium maze
          return item[0][0] #heuristic to prefer west first (towards the dot)
          #return item[0][1] #heuristic to prefer south first (towards the dot)
          #return item[0][0]+item[0][1] #heuristic to prefer south & west (towards the dot)
      sortedcandidates = sorted(problem.getSuccessors(node), key=getKey)
      #print sortedcandidates
      for coord, direction, steps in sortedcandidates: #problem.getSuccessors(node):
          #print 'analyzing:',coord
          if not coord in visited:
              if problem.isGoalState(coord):
                  #print actions + [direction]
                  return actions + [direction]
              fringe.push((coord, actions + [direction], visited + [node] ))
  return []


def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  fringe = util.Queue()
  fringe.push( (problem.getStartState(), []))
  visited = []
  while not fringe.isEmpty():
      node, actions = fringe.pop()
      for coord, direction, steps in problem.getSuccessors(node):
          #print node,' analyzing:',coord
          if not coord in visited:
              if problem.isGoalState(coord):
                  #print actions + [direction]
                  return actions + [direction]
              fringe.push((coord, actions + [direction]))
              visited.append(coord)
  return []

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  fringe = util.PriorityQueue()
  fringe.push( (problem.getStartState(),[]), 0 )
  visited = []
  while not fringe.isEmpty():
      node, actions = fringe.pop()
      if problem.isGoalState(node):
        return actions + [direction]
      for coord, direction, steps in problem.getSuccessors(node):
          #print 'analyzing:',coord
          if not coord in visited:
              fringe.push( (coord, actions + [direction]), problem.getCostOfActions(actions + [direction]) )
              visited.append(coord)
  return []


def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def distanceHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return state[0]+state[1]

def aStarSearch(problem, heuristic=distanceHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  closedset = []
  fringe = util.PriorityQueue()
  start = problem.getStartState()
  fringe.push( (start, []), heuristic(start, problem))
  while not fringe.isEmpty():
      node, actions = fringe.pop()
      if problem.isGoalState(node):
          return actions
      closedset.append(node)
      for coord, direction, cost in problem.getSuccessors(node):
          if not coord in closedset:
              new_actions = actions + [direction]
              score = problem.getCostOfActions(new_actions) + heuristic(coord, problem)
              fringe.push( (coord, new_actions), score)

  return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
