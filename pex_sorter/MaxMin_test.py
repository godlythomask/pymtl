import unittest

from MaxMin import *

class TestMaxMin(unittest.TestCase):

  def setUp(self):
    self.model = MaxMin()
    self.model.elaborate()
    self.sim = SimulationTool( self.model )

  def test_one(self):
    test_cases = [ [ 1, 2,],
                   [ 5, 3,],
                   [ 9, 8,],
                   [ 5, 5,],
                   [ 0, 2,],
                 ]

    self.sim.reset()
    for test in test_cases:
      self.model.in0.value = test[0]
      self.model.in1.value = test[1]
      self.sim.cycle()
      test.sort()
      self.assertEquals( self.model.min.value, test[0] )
      self.assertEquals( self.model.max.value, test[1] )

  def test_vcd(self):
    self.sim.dump_vcd( 'MaxMin_test.vcd' )
    self.test_one()

  def test_translate(self):
    self.hdl = VerilogTranslationTool( self.model )
    self.hdl.translate( 'MaxMin.v' )


if __name__ == '__main__':
  unittest.main()
