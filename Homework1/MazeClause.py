'''
MazeClause.py

Specifies a Propositional Logic Clause formatted specifically
for Grid Maze Pathfinding problems. Clauses are a disjunction of
GridPropositions (2-tuples of (symbol, location)) mapped to
their negated status in the sentence.
'''
import unittest
import collections

class MazeClause:
    
    def __init__ (self, props):
        self.props = {}
        self.valid = False
        for proposition in props:
            if proposition[0] in self.props and self.props[proposition[0]] != proposition[1]:
                self.valid = True
                self.props = {}
                break
            else:
                self.props.update({proposition[0]: proposition[1]})
            # print(self.props)

    def getProp (self, prop):
        if prop in self.props:
            return self.props.get(prop)
        else:
            return None
    
   # [x for n, x in enumerate(a) if x in a[:n]]

    def isValid (self):
        return self.valid

    def isEmpty (self): 
        return (self.props == {} and self.valid !=True)
    
    def __eq__ (self, other):
        return self.props == other.props and self.valid == other.valid
    
    def __hash__ (self):
        # Hashes an immutable set of the stored props for ease of
        # lookup in a set
        return hash(frozenset(self.props.items()))
    
    # Hint: Specify a __str__ method for ease of debugging (this
    # will allow you to "print" a MazeClause directly to inspect
    # its composite literals)
    def __str__ (self):
        return str(self.props) + ": " + str(self.valid)
    
    @staticmethod
    def resolve (c1, c2):
        # print(c1.props)
        # print(c2.props)
        resolved_clause = []
        results = set()
        for proposition, value in c1.props.items():
            if not(proposition in c2.props and c2.getProp(proposition) != value) and proposition not in c2.props:
                resolved_clause.append(((proposition[0], proposition[1]), value))

        # print(resolved_clause)        
        resolved_maze_clause = MazeClause(resolved_clause)
        print(resolved_maze_clause)
        print(c1)
        print(c2)
        # print(not resolved_maze_clause.isValid())
        if not resolved_maze_clause.isValid() and not resolved_maze_clause.isEmpty(): 
            results.add(resolved_maze_clause)
        return results
    

class MazeClauseTests(unittest.TestCase):
    def test_mazeprops1(self):
        mc = MazeClause([(("X", (1, 1)), True), (("X", (2, 1)), True), (("Y", (1, 2)), False)])
        # print((mc.getProp(("Y", (1, 2)))))
        
        self.assertTrue(mc.getProp(("X", (1, 1))))
        self.assertTrue(mc.getProp(("X", (2, 1))))
        self.assertFalse(mc.getProp(("Y", (1, 2))))
        self.assertTrue(mc.getProp(("X", (2, 2))) is None)
        self.assertFalse(mc.isEmpty())
        
    def test_mazeprops2(self):
        mc = MazeClause([(("X", (1, 1)), True), (("X", (1, 1)), True)])
        self.assertTrue(mc.getProp(("X", (1, 1))))
        self.assertFalse(mc.isEmpty())
        
    def test_mazeprops3(self):
        mc = MazeClause([(("X", (1, 1)), True), (("Y", (2, 1)), True), (("X", (1, 1)), False)])
        self.assertTrue(mc.isValid())
        self.assertTrue(mc.getProp(("X", (1, 1))) is None)
        self.assertFalse(mc.isEmpty())
        
    def test_mazeprops4(self):
        mc = MazeClause([])
        self.assertFalse(mc.isValid())
        self.assertTrue(mc.isEmpty())
        
    def test_mazeprops5(self):
        mc1 = MazeClause([(("X", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), True)])
        res = MazeClause.resolve(mc1, mc2)
        # print(res)
        self.assertEqual(len(res), 0)
        
    def test_mazeprops6(self):
        mc1 = MazeClause([(("X", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([]) in res)
        
    # def test_mazeprops7(self):
    #     mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), True)])
    #     mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (2, 2)), True)])
    #     res = MazeClause.resolve(mc1, mc2)
    #     self.assertEqual(len(res), 1)
    #     self.assertTrue(MazeClause([(("Y", (1, 1)), True), (("Y", (2, 2)), True)]) in res)
        
    # def test_mazeprops8(self):
    #     mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False)])
    #     mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True)])
    #     res = MazeClause.resolve(mc1, mc2)
    #     self.assertEqual(len(res), 0)
        
    # def test_mazeprops9(self):
    #     mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False), (("Z", (1, 1)), True)])
    #     mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True), (("W", (1, 1)), False)])
    #     res = MazeClause.resolve(mc1, mc2)
    #     self.assertEqual(len(res), 0)
        
    # def test_mazeprops10(self):
    #     mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False), (("Z", (1, 1)), True)])
    #     mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), False), (("W", (1, 1)), False)])
    #     res = MazeClause.resolve(mc1, mc2)
    #     self.assertEqual(len(res), 1)
    #     self.assertTrue(MazeClause([(("Y", (1, 1)), False), (("Z", (1, 1)), True), (("W", (1, 1)), False)]) in res)
        
if __name__ == "__main__":
    unittest.main()
    