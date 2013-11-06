import aStarNode

class MinHeap(object):
    """Defines a min heap structure.

    Author: Aleksandar Mitrevski

    """
    def __init__(self):
        """Initializes a min heap. Uses nodes of type 'AStarNode'."""
        self.nodes = []

    def insert(self, node):
        """Inserts a node into the heap.

        Keyword arguments:
        node -- An 'AStarNode' object.

        """
        self.nodes.append(node)
        self.bubble_up(len(self.nodes) - 1)

    def extract_min(self):
        """Returns the minimum cost node from the heap."""
        minimumNode = self.nodes[0]
        self.nodes[0] = self.nodes[len(self.nodes) - 1]
        self.nodes.pop()
        self._bubble_down(0)
        return minimumNode

    def bubble_up(self, index):
        """Pushes the node whose heap indes is 'index' up
        as long as the min heap property is violated.

        Keyword arguments:
        index -- Index of a node in the heap.

        """
        currentChild = index
        currentParent = -1

        if currentChild & 1:
            currentParent = currentChild / 2
        else:
            currentParent = currentChild / 2 - 1

        while currentChild > 0 and self.nodes[currentParent].totalCost > self.nodes[currentChild].totalCost:
            self._swap(currentParent, currentChild)
            currentChild = currentParent

            if currentChild & 1:
                currentParent = currentChild / 2
            else:
                currentParent = currentChild / 2 - 1

    def _bubble_down(self, index):
        """Pushes the node whose heap indes is 'index' down
        as long as the min heap property is violated.

        Keyword arguments:
        index -- Index of a node in the heap.

        """
        currentParent = index
        leftChild = currentParent * 2 + 1
        rightChild = currentParent * 2 + 2
        currentChild = -1

        if leftChild < len(self.nodes) and rightChild < len(self.nodes):
            if self.nodes[leftChild].totalCost < self.nodes[rightChild].totalCost:
                currentChild = leftChild
            else:
                currentChild = rightChild
        elif leftChild < len(self.nodes):
            currentChild = leftChild
        elif rightChild < len(self.nodes):
            currentChild = rightChild

        while currentChild > -1 and self.nodes[currentParent].totalCost > self.nodes[currentChild].totalCost:
            self._swap(currentChild, currentParent)
            currentParent = currentChild

            leftChild = currentParent * 2 + 1
            rightChild = currentParent * 2 + 2

            if leftChild < len(self.nodes) and rightChild < len(self.nodes):
                if self.nodes[leftChild].totalCost < self.nodes[rightChild].totalCost:
                    currentChild = leftChild
                else:
                    currentChild = rightChild
            elif leftChild < len(self.nodes):
                currentChild = leftChild
            elif rightChild < len(self.nodes):
                currentChild = rightChild
            else:
                currentChild = -1

    def _swap(self, index1, index2):
        """Swaps the heap nodes whose indices are 'index1' and 'index2'.

        Keyword arguments:
        index1 -- Index of a node in the heap.
        index2 -- Index of another node in the heap.

        """
        temp = self.nodes[index1]
        self.nodes[index1] = self.nodes[index2]
        self.nodes[index2] = temp
        return self

    def get_index(self, node):
        """Returns the index of 'node' in the heap or -1 if 'node' does not exist in the heap.

        Keyword arguments:
        node -- An 'AStarNode' object representing the node whose index we want to find.

        """
        index = -1
        for i in xrange(len(self.nodes)):
            if self.nodes[i].nodeLabel == node.nodeLabel:
                index = i
                break

        return index

    def empty(self):
        """Returns 'True' if the heap is empty and 'False' otherwise."""
        return len(self.nodes) == 0
