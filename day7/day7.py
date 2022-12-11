from anytree import AnyNode, RenderTree, PreOrderIter

input = open('inputDay7.txt', 'r')
lines = input.readlines()

cd = ""
rootNode = AnyNode(id="/", val=0, dir=True)
currNode = rootNode

totalSum = 0
nodeToDelete = rootNode

#create tree
for line in lines:
    newLine = line.replace("\n", "")
    if newLine[0] == '$':
        newLine = newLine.replace("$ ", "")
        command = newLine.split(" ")
        if command[0] == "cd":
            if command[1] == "/":
                currNode = rootNode
            elif command[1] == "..":
                currNode = currNode.parent
            else:
                for child in currNode.children:
                    if child.val == 0 and child.id == command[1]:
                        currNode = child
    else:
        splitText = newLine.split(" ", 1)
        if splitText[0] == "dir":
            dirNode = AnyNode(id=splitText[1], val=0, dir=True)
            dirNode.parent = currNode
        else:
            fileNode = AnyNode(id=splitText[1], val=int(splitText[0]), dir=False)
            fileNode.parent = currNode

def traverse(node):
    for child in node.children:
        traverse(child)
    # Calculates the size of each directory based on all children
    if node != rootNode:
        node.parent.val += node.val

traverse(rootNode)

for node in PreOrderIter(rootNode):
    if node.val <= 100000 and node.dir:
        totalSum += node.val

print("Part One Answer: " + str(totalSum)) #1501149

totalSpace = 70000000
spaceNeeded = 30000000
rootSpace = rootNode.val # 49199225
unusedSpace = totalSpace - rootSpace
minimumSizeToDelete = spaceNeeded - unusedSpace #9199225

for node in PreOrderIter(rootNode):
    if node.val >= minimumSizeToDelete and node.dir:
        if nodeToDelete.val > node.val:
            nodeToDelete = node

print("Part Two Answer: " + str(nodeToDelete.val)) #10096985

#Source: [AdventOfCode](https://adventofcode.com/2022/day/7)
