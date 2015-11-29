'''
Created on Nov 29, 2015

@author: alejandrok
'''
from software.paging_memory.page import Page 

class LogicalMemory(object):
    '''
    classdocs
    '''


    def __init__(self, memory,pageSize):
        '''
        Constructor
        '''
        self.memory = memory
        self.pageSize = pageSize
        self.pages = {}
        self.virtualMemory = {}
        
    def pagesOK(self):
        return self.pageSize % self.memory.size() == 0
    
    def numberOfPages(self):
        return self.pageSize / self.memory.size()
    
    def freePage(self):
        usedPages = len(self.pages)
        if usedPages<self.numberOfPages():
            return usedPages
            
    def makePage(self,idProcess,pageNumber):
        n = self.freePage()
        self.pages[n] = Page(idProcess,pageNumber)
    
    def get(self,pcb):
        page = self.pcb.programCounter / self.pageSize
        positionInFrame = self.pcb.programCounter % self.pageSize
        
    ## where is_
        ## nowhere, to Load
            ## are free frames -> dump, dump, load
            ## need to swap a frame -> later, dump, load
        ## in any page
            # in local Memory -> load
            # in virtual memory -> swap a frame, dump, load
            