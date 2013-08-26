# -*- coding: utf-8 -*-

import sh
import sys
import os
import readline

from spellbook import *



def get_argument( index ):
    value = ""
    try:
        value = sys.argv[index]
    except IndexError:
        pass
    
    return value



if __name__ == "__main__":

    spellbook = Spellbook()
    spellbook[ get_argument(1) ]
    
    
    print "Casting in {0}".format( os.getcwd() )
    
    # parse arguments
    
    
