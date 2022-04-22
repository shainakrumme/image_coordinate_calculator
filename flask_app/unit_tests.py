"""
Author: Shaina Krumme
Description: Unit Testing
"""

import unittest # Unit testing framework

class Testdatatype(unittest.TestCase):
    """
    Description: Base class used to create new test cases.
    """
    
    def test_shape(self, corner_points):
       """
       Description: 
           Confirm that the corner points form a rectangle. In other words,
           confirm that there are exactly 2 unique x values and exactly
           2 unique y values amongst the 4 (x, y) coordinate pairs.
       Parameters:
           corner_points:  list of 4 tuples or 4 (x, y) coordinate pairs.
       """
       x_cor = list(set([i[0] for i in corner_points])) # x coordinates
       y_cor = list(set([i[1] for i in corner_points])) # y coordinates
       
       self.assertEqual(len(x_cor), 2, 'The 4 corners need to include 2 unique x values.')
       self.assertEqual(len(y_cor), 2, 'The 4 corners need to include 2 unique y values.')
       
    def test_unique_corner_points(self, corner_points):   
        """
        Description: Confirm that each corner point is unique.
        
        Parameters:
           corner_points:  list of 4 tuples or 4 (x, y) coordinate pairs.
        """
        for i in range(len(corner_points)):
            for j in range(len(corner_points)):
                if(i != j):
                    if(corner_points[i][0] == corner_points[j][0]):
                        x_cor = True
                    else:
                        x_cor = False
                    
                    if(corner_points[i][1] == corner_points[j][1]):
                         y_cor = True
                    else:
                        y_cor = False
               
                    self.assertEqual(False, x_cor&y_cor,'(x,y) tuples must be unique')