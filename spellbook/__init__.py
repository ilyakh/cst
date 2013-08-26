# -*- coding: utf-8 -*-

import os, shutil

class Spellbook:
    def __init__( self, preset=False, id=False ):
        default = {
            'test': test
        }

        self.preset = preset if preset else default

    def __getitem__( self, key ):
        search_result = self.preset.get( key )
        search_result()


class Context:
    def __init__( self, location ):
        self.location = location

    def elements( self ):
        result = []
        for f in os.listdir( self.location ):            
            if os.path.isfile( f ):
                result.append( f )
        return result

    def containers( self ):
        result = []
        for c in os.listdir( self.location ):
            if os.path.isdir( c ):
                result.append( c )
        return result
        


def test():

    extensions = set()
    
    for f in os.listdir( '.' ):        
        if os.path.isfile( f ):
            tokens = f.split( '.' )
            name = tokens[0]
            extension = tokens[-1]

            if name != "" and extension != "":
                extensions.add( extension.lower() )


    folders = {}
    for e in extensions:
        folders[e] = []

    for f in os.listdir( '.' ):
        if os.path.isfile( f ):
            tokens = f.split('.')
            name = tokens[0]
            extension = tokens[-1]

            if folders.get( extension.lower() ) != None:
                folders[extension.lower()].append( f )

    print folders

    for path, files in folders.items():
        if not os.path.exists(path):
            print "Creates a directory for {0}".format( path )
            os.makedirs(path)
        
        for f in files:
            print "Moving {0} to {1}".format( f, path )
            shutil.move( f, path )

                




            
                
