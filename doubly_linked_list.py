# Exercise: make doubly linked list 

class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
    
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_prev_node(self):
        return self.prev_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node
    
    def __repr__(self):
        return f'<Node: {self.data}>'


class DoublyList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0
        
    def add(self, data):
        new_node = Node(data, self.root)
        if self.size == 0:
            self.root = new_node
        else:
            self.root.set_prev_node(new_node)
            self.root = new_node
        self.size += 1


    def show(self):
        this_node = self.root
        while this_node:
            print(f"Node: {this_node} Prev node: {this_node.get_prev_node()} Next node: {this_node.get_next_node()}")
            this_node = this_node.get_next_node()


    def remove(self, data):
        this_node = self.root     
        # if first node remove it and next node exists
        if this_node.get_data() == data:
            # if only one element 
            if this_node.next_node:
                self.root = this_node.next_node
                self.root.set_prev_node(None)
            else: # only one element in the list
                self.root = None
            self.size = self.size - 1

        else:
            while this_node.get_next_node():
                if this_node.get_next_node().get_data() == data: # if that number we were looking for is found
                    node = this_node.get_next_node().get_next_node()
                    if node:
                        this_node.set_next_node(node)
                        node.set_prev_node(this_node)
                    else: #last index
                        this_node.set_next_node(None)
                    self.size = self.size - 1
                    return True
                else:
                    this_node = this_node.get_next_node()
        return False 

    def find(self,data):
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                return this_node
            else:
                this_node = this_node.get_next_node()
        return None # Return None, not an error

dd = DoublyList()
dd.add(4)
dd.remove(4)
dd.show()
print(dd.size)