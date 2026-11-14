"""BFS for HRD"""
from datetime import time
from collections import deque
import heapq
from typing import Optional, Dict, Tuple, List
from state import State
from board import Board
from sample_openings.standard import (SAMPLE_GRID, STANDARD_GRID,
                                      STANDARD_GRID_2, STANDARD_GRID_3,
                                      ALMOST_DONE, ENEMY_GRID)
from itertools import count


def bfs_pruning(state: State) -> Optional[State]:
    checks = 0
    frontier = deque([state])
    # explored = {state}
    explored_keys = {state.get_state_key()}

    while len(frontier) > 0:
        curr = frontier.popleft()
        checks += 1
        # print(checks)
        if curr.is_goal():
            # curr.board.print_board()
            # curr.goal_to_parent()
            return curr
        # print("what is the cost of the children", curr.cost_to)
        # curr.board.print_board()
        curr_sux = curr.create_successors()

        for cs in curr_sux:
            key = cs.get_state_key()
            # print("CURRENT:", curr.get_state_key())
            # print("SUCCESSOR:", key)
            # print("ALREADY VISITED:", key in explored_keys)
            # print("__________")
            if key not in explored_keys:
                explored_keys.add(key)
                frontier.append(cs)
            # if cs not in explored:
            #     explored.add(cs)
            #     frontier.append(cs)
    print("no sol found; total number of checks = ", checks)
    return None


def cost_search(state: State) -> Optional[State]:
    checks = 0
    counter = count()

    frontier = [(state.cost_to, next(counter), state)]
    explored_keys = {state.get_state_key()}

    while frontier:
        cost, _, curr = heapq.heappop(frontier)
        checks += 1

        if curr.is_goal():
            print("Total checks:", checks)
            return curr


        for cs in curr.create_successors():
            key = cs.get_state_key()

            if key not in explored_keys:
                cs.cost_to = curr.cost_to + 1

                explored_keys.add(key)
                heapq.heappush(
                    frontier,
                    (cs.cost_to, next(counter), cs)
                )
    print("No solution found. Total checks:", checks)
    return None


if __name__ == "__main__":
    import time
    print("started at", time.time())
    start = time.time()
    bored = Board(STANDARD_GRID)
    stateside = State(bored, None)
    goalie = cost_search(stateside)

    final_path = []

    # if goalie:
    #     final_path = goalie.goal_to_parent()
        # goalie.board.print_board()
        # for f in final_path:
        #     print("Cost so far:", f.cost_to)
            # f.board.print_board()
    # else:
    #     print("No solution found")

    # final_path = goalie.goal_to_parent()
    # print("cost of goal", goalie.cost_to)

    stop = time.time()
    print("Time taken:", stop - start, "seconds")
