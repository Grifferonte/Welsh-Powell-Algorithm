from Graph import Graph

graph = Graph(10)
graph.addEdge(5, 2)
graph.addEdge(3, 3)
graph.addEdge(4, 1)
graph.addEdge(4, 6)
graph.addEdge(8, 2)
print(graph.__str__())
graph.drawWelshPowellColoration('GraphAdd')

graphTinyG = Graph('./FilesTxt/tinyG.txt')
print(graphTinyG.__str__())
graphTinyG.drawWelshPowellColoration('tinyG')

graphMediumG = Graph('./FilesTxt/mediumG.txt')
print(graphMediumG.__str__())
graphMediumG.drawWelshPowellColoration('mediumG')
