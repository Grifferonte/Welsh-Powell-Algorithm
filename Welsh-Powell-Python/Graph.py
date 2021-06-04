import pydot

from matplotlib import colors

class Graph:

    def __init__(self, v: int or str):
        if type(v) == int:
            self.v = v
            self.e = 0
            self.adj = {key: [] for key in range(self.v)}
        elif type(v) == str:
            try:
                file = open(v, 'r')
                fileLines = file.readlines()
                self.v = int(fileLines[0].rstrip("\n"))
                # self.e = int(fileLines[1].rstrip("\n"))
                self.e = 0
                self.adj = {key: [] for key in range(self.v)}
                for index in range(2, len(fileLines)):
                    lineSplit = fileLines[index].split()
                    self.addEdge(int(lineSplit[0]), int(lineSplit[1]))
                file.close()

            except FileNotFoundError:
                print('File Not Found')
                raise
        else:
            raise Exception('Enter a file or a number')

    def intV(self):
        return self.v

    def intE(self):
        return int(self.e / 2)

    def addEdge(self, v: int, w: int):
        if v <= len(self.adj):
            if w not in self.adj.get(v):
                self.adj.get(v).append(w)
                self.e += 1
        else:
            raise Exception('Enter a vertex in size of graph')
        if w <= len(self.adj):
            if v not in self.adj.get(w):
                self.adj.get(w).append(v)
                self.e += 1
        else:
            raise Exception('Enter a vertex in size of graph')

    def getWelshPowellColoration(self):
        arrayColors = {}
        for elem in colors.TABLEAU_COLORS:
            splitItem = elem.split(':')
            arrayColors[splitItem[1]] = []
        adjSortedBySize: dict = {}
        keyArray = sorted(self.adj.copy(), key=lambda k: len(self.adj.copy()[k]), reverse=True)
        for key in keyArray:
            adjSortedBySize[key] = self.adj[key]

        for key in adjSortedBySize:
            for keyColors in arrayColors:
                if len(adjSortedBySize[key]) > 0:
                    adjBoolean = True
                    for item in arrayColors.get(keyColors):
                        if key in adjSortedBySize.get(item):
                            adjBoolean = False
                    if adjBoolean:
                        arrayColors.get(keyColors).append(key)
                        break

        arrayColors = {key: item for key, item in arrayColors.items() if len(item) > 0}
        # result: str = ('Number of Color : {} \n'.format(len(arrayColors)))
        # for key in arrayColors.keys():
        #     result += ('{} : {} \n'.format(key, arrayColors.get(key)))
        # return result
        return arrayColors

    def drawWelshPowellColoration(self, name: str):
        if type(name) == str:
            arrayColors = self.getWelshPowellColoration()
            adjTuple = list()
            for key in self.adj:
                for item in self.adj.get(key):
                    if (key, item) and (item, key) not in adjTuple:
                        adjTuple.append((key, item))

            if self.e < 100:
                graph = pydot.Dot('my_graph', graph_type='graph')
                for key in arrayColors.keys():
                    for elem in arrayColors.get(key):
                        node = pydot.Node(elem, style='filled', fillcolor=key, label=elem, fontcolor='white')
                        graph.add_node(node)
                for elem in adjTuple:
                    edge = pydot.Edge(elem[0], elem[1])
                    graph.add_edge(edge)
                    graph.write_png('./GraphsPng/{}.png'.format(name))
            else:
                try:
                    file = open('./GraphsTxt/{}.txt'.format(name), 'x')
                except FileExistsError:
                    file = open('./GraphsTxt/{}.txt'.format(name), 'w')
                for key in arrayColors.keys():
                    file.write('{} : {} \n'.format(key, arrayColors.get(key)))
        else:
            raise Exception('Enter a valid name file')

    def __str__(self):
        result: str = ('V : {} \n'.format(self.intV()))
        result += ('E : {} \n'.format(self.intE()))
        for key in self.adj.keys():
            result += ('{} : {} \n'.format(key, self.adj.get(key)))
        return result
