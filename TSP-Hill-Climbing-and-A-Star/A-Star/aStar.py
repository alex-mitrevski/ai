import graph
import heap
import aStarNode
import coordinates
import math
import random

class AStarLibrary(object):
    """Defines a library for finding shortest paths using A*.

    Author: Aleksandar Mitrevski

    """
    def __init__(self, node_graph):
        """Creates a new A* search library.

        Keyword arguments:
        graph -- A 'Graph' object.

        """
        self.node_graph = node_graph

    def find_shortest_path(self):
        """Finds a solution to the traveling salesman problem."""
        source = random.randint(0, self.node_graph.number_of_nodes()-1)

        open_list = heap.MinHeap()
        closed_list = []

        source_node = aStarNode.AStarNode(source, self.node_graph.nodes[source].coordinates, -1, 0, 0)
        open_list.insert(source_node)

        path_found = False
        while not open_list.empty() and not path_found:
            current_node = open_list.extract_min()
            closed_list.append(current_node)

            if self._goal_state(closed_list):
                path_found = True
                continue

            adjacent = self._get_adjacent_nodes(current_node, source, closed_list)
            for _,node in enumerate(adjacent):
                node_position = open_list.get_index(node)
                node_closed = False
                for _,closed_node in enumerate(closed_list):
                    if node.nodeLabel == closed_node.nodeLabel:
                        node_closed = True
                        break

                if not node_closed and node_position == -1:
                    open_list.insert(node)

        visited_node_labels = [node.nodeLabel for _,node in enumerate(closed_list)]
        visited_node_labels.append(source)

        if not path_found:
            return 'A path between the stations was not found', -1
        else:
            cost = self._calculate_path_cost(closed_list)
            return visited_node_labels, cost

    def _goal_state(self, closed_list):
        return len(closed_list) == self.node_graph.number_of_nodes()

    def _get_adjacent_nodes(self, current_node, goal, closed_list):
        """Returns a list of 'AStarNode' objects representing the nodes adjacent to 'currentNode'.

        Keyword arguments:
        currentNode -- An 'AStarNode' object representing a node currently processed by the search algorithm.
        goal -- A node label (an integer) representing the goal node.
        closed_list -- A list of already visited nodes.

        """
        adjacent_nodes = []
        visited_node_labels = [node.nodeLabel for _,node in enumerate(closed_list)]

        unvisited_nodes = list(set(self.node_graph.nodes.keys()) - set(visited_node_labels))
        mst_cost = self.node_graph.minimum_spanning_tree_cost(unvisited_nodes)

        #the heuristic used is the sum of:
        #- the cost of the minimum spanning tree of the unvisited nodes.
        #- the smallest distance from an unvisited node to the start node
        #- the smallest distance from the current node to an unvisited node
        for child,cost in self.node_graph.nodes[current_node.nodeLabel].children.items():
            child_coordinates = self.node_graph.nodes[child].coordinates
            cost = current_node.cost + cost
            heuristic = self._calculate_heuristic(child, goal, visited_node_labels) + mst_cost
            total_cost = cost + heuristic

            new_node = aStarNode.AStarNode(child, child_coordinates, current_node.nodeLabel, cost, total_cost)
            adjacent_nodes.append(new_node)

        return adjacent_nodes

    def _calculate_heuristic(self, node, goal, closed_list):
        """Calculates a value for the heuristic between 'node' and 'goal'.

        Keyword arguments:
        node -- A node label (an integer) representing a node in the graph.
        goal -- A node label (an integer) representing the goal node.
        closed_list -- A list of labels of already visited nodes.

        """
        unvisited_nodes = list(set(self.node_graph.nodes.keys()) - set(closed_list))
        heuristic = self._minimum_distance_to_goal(goal, unvisited_nodes)
        heuristic += self._minimum_distance_to_unvisited(node, unvisited_nodes)

        return heuristic

    def _minimum_distance_to_goal(self, goal, unvisited_nodes):
        """Returns the minimum distance from the nodes in 'unvisited_nodes' to goal.

        Keyword arguments:
        goal -- A node label (an integer) representing the goal node.
        unvisited_nodes -- A list of node labels representing unvisited nodes.

        """
        distances = []
        number_of_unvisited_nodes = len(unvisited_nodes)
        goal_coordinates = self.node_graph.nodes[goal].coordinates

        for _,key in enumerate(unvisited_nodes):
            node_coordinates = self.node_graph.nodes[key].coordinates
            distance = math.sqrt((node_coordinates.x - goal_coordinates.x)**2 + (node_coordinates.y - goal_coordinates.y)**2)
            distances.append(distance)

        return min(distances)

    def _minimum_distance_to_unvisited(self, node, unvisited_nodes):
        """Returns the minimum distance from 'node' to the nodes in 'unvisited_nodes'
        or 0. if there are no unvisited nodes.

        Keyword arguments:
        node -- A node label (an integer) representing a node.
        unvisited_nodes -- A list of node labels representing unvisited nodes.

        """
        distances = []
        number_of_unvisited_nodes = len(unvisited_nodes)
        source_coordinates = self.node_graph.nodes[node].coordinates

        for _,key in enumerate(unvisited_nodes):
            if key != node:
                node_coordinates = self.node_graph.nodes[key].coordinates
                distance = math.sqrt((node_coordinates.x - source_coordinates.x)**2 + (node_coordinates.y - source_coordinates.y)**2)
                distances.append(distance)

        if len(distances) > 0:
            return min(distances)
        else:
            return 0.

    def _calculate_path_cost(self, nodes):
        total_cost = 0.
        number_of_nodes = len(nodes)

        for i in xrange(number_of_nodes-1):
            node_1_coordinates = nodes[i].coordinates
            node_2_coordinates = nodes[i+1].coordinates
            distance = math.sqrt((node_1_coordinates.x - node_2_coordinates.x)**2 + (node_1_coordinates.y - node_2_coordinates.y)**2)
            total_cost += distance

        return total_cost
