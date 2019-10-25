# -*- coding: utf-8 -*-
import unittest
from JeuVoiture.Voiture import Voiture


class TestDeplacementVoiture(unittest.TestCase):
    def setUp(self):
        self.voiture = Voiture()
        
    def testDeplacementSimple(self):
        self.voiture.avancer(lambda x:True)
        self.assertTrue((self.voiture.position == [1,0]).all())

    def testDeplacementSurObstacle(self):
        self.voiture.avancer(lambda x:False)
        self.assertTrue((self.voiture.position == [0,0]).all())

    def testDeplacementCheckObstacleWrongType(self):
        with self.assertRaises(TypeError):
            self.voiture.avancer(False)
