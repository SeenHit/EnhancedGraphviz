from graphviz import Digraph
import os

# 实例化一个Digraph对象(有向图)，name:生成的图片的图片名，format:生成的图片格式
dot = Digraph(name="MyPicture", comment="the test", format="png")

dictNode = {}
dictNodeMap = {}
beforeNode = ""
f = open("init.cfg")
while True:
    line = f.readline()
    if not line:
        break
    line = line.rstrip('\n')
    strlist = line.split(' ')
    # 指定连线
    try:
        firstNode = strlist[0]
        secondNode = strlist[1]
    
        if firstNode not in dictNode:
            dictNode[firstNode] = 1
            dot.node(name = firstNode, label = firstNode)
        if secondNode not in dictNode:
            dictNode[secondNode] = 1
            dot.node(name = secondNode, label = secondNode)
        #dot.edge(firstNode, secondNode, label = firstNode + " to " + secondNode)
        # 解决相邻节点间有多根连线的问题
        cmpStr = firstNode + secondNode
        if cmpStr not in dictNodeMap:
            dot.edge(firstNode, secondNode)
            dictNodeMap[cmpStr] = 1            
    # 上下文连线
    except:
        if (beforeNode == ""):
            beforeNode = line
            continue
        currNode = line
        if currNode not in dictNode:
            dictNode[currNode] = 1
            dot.node(name = currNode, label = currNode)
        #dot.edge(beforeNode, currNode, label = beforeNode + " to " + currNode)
        
        dot.edge(beforeNode, currNode)
        dictNode[cmpStr] = 1            
        beforeNode = line

# 打印生成的源代码
print(dot.source)

# 跟view一样的用法(render跟view选择一个即可)，一般用render生成图片，不使用view=True,view=True用在调试的时候
dot.render(filename='MyPicture', directory="MyTest",view=False)
