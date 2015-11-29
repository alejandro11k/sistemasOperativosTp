'''
Created on Nov 29, 2015

@author: alejandrok
'''

class Page(object):
    '''
    classdocs
    '''


    def __init__(self,pageId,idProcess,pageNumber):
        '''
        Constructor
        '''
        self.pageId = pageId
        self.idProcess = idProcess
        self.pageNumber = pageNumber
        
    def isPid(self,idProcess,pageNumber):
        return self.idProcess==idProcess and self.pageNumber==pageNumber
    
    def dump(self,memory):
        
        
        
    
        