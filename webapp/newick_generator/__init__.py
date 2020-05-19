#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys
sys.path.append("..")

from .. import models
from pyramid.response import Response
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import to_tree
import math
import csv
from itolapi import Itol


class NewickProcessor():
    def createDF(self, lst):
        return pd.DataFrame(lst)


    def deletion(self, a,b):
        if (a < 0 and b < 0 and a == b):
            return False
        elif a < 0 or b < 0:
            return True
        return False
        
    
    def both_non_na(self, a,b):
        if a != np.nan and b != np.nan:
            return True
        return False
        
    
    def shriver_distance(self,list_A, list_B):
        listA = list_A
        listB = list_B
        nc = len(listA)
        dist = None
        count = 0
        Jxy = 0
        for i in range(len(listA)):
            if self.both_non_na(listA[i], listB[i]):
                if self.deletion(listA[i], listB[i]):
                    Jxy += 2
                else:
                    Jxy += math.fabs(listA[i] - listB[i])
                count += 1
        if count == 0:
            #TODO: DEF na_real
            return na_real
        dist = float(Jxy / count)
        if count != nc :
            dist = float(dist/float((count/nc)))
        return dist
            
    def distance_matric (self,df, dc=0):
        df_array = np.asarray(df, order='c')
        nr, nc = df_array.shape  
        result = np.empty((nr * (nr - 1)) // 2, dtype=np.double)
        pos = 0
        for index_i in range(nr):
            j_counter = index_i
            start = j_counter + dc + 1
            for index_j in range(start, nr):
                result[pos] = self.shriver_distance(df_array[j_counter], df_array[start])      
                pos += 1
                start += 1
        return result
    
    def linkage_to_newick(self,Z, labels):
        """
        Input :  Z = linkage matrix, labels = leaf labels
        Output:  Newick formatted tree string
        """
        tree = to_tree(Z, False)
        def buildNewick(node, newick, parentdist, leaf_names):
            if node.is_leaf():
                return "%s:%f%s" % (leaf_names[node.id], parentdist - node.dist, newick)
            else:
                if len(newick) > 0:
                    newick = "):%f%s" % (parentdist - node.dist, newick)
                else:
                    newick = ");"
                newick = buildNewick(node.get_left(), newick, node.dist, leaf_names)
                newick = buildNewick(node.get_right(), ",%s" % (newick), node.dist, leaf_names)
                newick = "(%s" % (newick)
                return newick
        return buildNewick(tree, "", tree.dist, labels)

    def generate_newick(self, lst, index):
        df = self.createDF(lst)
        dmatrix = self.distance_matric(df)
        dm_linkage = linkage(dmatrix, 'average')
        newick = self.linkage_to_newick(dm_linkage, index)
        return newick
    
    @staticmethod
    def write_newick(process_ID, newick):
        with open("/home/ubuntu/coxbase/tools/grapeTree/tre/{}.nwk".format(process_ID), "wb") as open_file:
            open_file.write(newick.encode('utf-8'))
            open_file.close
    @staticmethod
    def write_metadata(process_ID, metadata_list):
        with open("/home/ubuntu/coxbase/tools/grapeTree/tre/{}.txt".format(process_ID),
                  "w", newline="", encoding='utf-8') as open_file:
            writer = csv.writer(open_file)
            writer.writerows(metadata_list)
    @staticmethod
    def create_itol_link(process_ID, newick):
        with open("/home/ubuntu/coxbase/tools/grapeTree/tre/{}.tree".format(process_ID),
                  "w", encoding='utf-8') as open_file:
            open_file.write(newick)
        itol_uploader = Itol()
        itol_uploader.add_file("/home/ubuntu/coxbase/tools/grapeTree/tre/{}.tree".format(process_ID))
        itol_uploader.params['treeName'] = process_ID
        itol_uploader.upload()
        return itol_uploader.get_webpage()

