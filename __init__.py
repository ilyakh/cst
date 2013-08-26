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

    try:
        spellbook[ get_argument(1) ]
    except TypeError as e:
        print "Spell not found"

    current_path = Context( '.' )

    print current_path.elements()
    
    print "Casting in {0}".format( os.getcwd() )
    
    # parse arguments
    
    
