from kanren import Relation, facts, run, var, conde


class LogicProgramming:
    def __init__(self):
        self.parent= Relation()
    def start(self):
        self.parent = Relation()
        x = var()
        facts(self.parent,
              ("DarthVader", "LukeSkywalker"),
              ("DarthVader", "LeiaOrgana"),
              ("LeiaOrgana", "KyloRen"),
              ("HanSolo", "KyloRen")
              )

        lukesParent = run(1, x, self.parent(x, "LukeSkywalker"))
        darthsChildren =run(2, x, self.parent("DarthVader", x))
        print("Luke Skywalkers parent is: ", lukesParent)
        print("Darth Vaders children are: ", darthsChildren)
        kylosGrandparent = run(1, x,self.grandparent(x, "KyloRen"))
        print("Kylo Ren's grand parent is: ", kylosGrandparent)
        self.familyTreeDataStructures()

    def grandparent(self, x, z):
        y = var()
        return conde((self.parent(x, y), self.parent(y, z)))

    def familyTreeDataStructures(self):
        print('Using just python data structures for relations and queries')
        parents = {"DarthVader": ["LukeSkywalker", "LeiaOrgana"], "LeiaOrgana":["KyloRen"], "HanSolo": ["KyloRen"]}
        lukesParent = self.findParents(parents, "LukeSkywalker")
        print("Luke Skywalkers parent is: ", lukesParent)
        vadersChildren = self.findChildren(parents, "DarthVader")
        print("Darth Vaders children are: ", vadersChildren)
        kylosGrandparents = self.findGrandparent(parents, "KyloRen")
        print("Kylo Ren's grand parent is: ", kylosGrandparents)


    def findGrandparent(self, parents, grandchild):
        grandchildsParents = []
        grandchildsGrandparents = []
        for parent in parents:
            children = parents[parent]
            for currentChild in children:
                if currentChild == grandchild:
                    grandchildsParents.append(parent)
        for parent in grandchildsParents:
            for currentparent in parents:
                children = parents[currentparent]
                for currentChild in children:
                    if currentChild == parent:
                        grandchildsGrandparents.append(currentparent)

        return grandchildsGrandparents

    def findChildren(self, parents, parent):
        for currentParent in parents:
            if currentParent == parent:
                return parents[parent]

    def findParents(self, parents, child):
        childsParents = []
        for parent in parents:
            children =  parents[parent]
            for currentChild in children:
                if currentChild == child:
                    childsParents.append(parent)
        return childsParents

logicRun = LogicProgramming()
logicRun.start()