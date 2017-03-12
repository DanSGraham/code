#A module for a decision tree
#By DanG

import math
import numpy as np

##---------Cost Function----------

#From here: http://machinelearningmastery.com/implement-decision-tree-algorithm-scratch-python/
def gini_index(groups, class_values):
    
    gini = 0.0
    for class_value in class_values:
        for group in groups:
            g_size = len(group)
            if g_size != 0:
                proportion = [row[-1] for row in group].count(class_value) / float(size)
                gini += (proportion * (1.0 - proportion))
    return gini


