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
        else:
            return -1
            
    def makePage(self):
        n = self.freePage()
        self.pages[n] = Page(n,self.pageSize)
        return n
    
    def dumpPage(self,realPage,pcb,page):
        firstIntructionNumber = self.pageSize*page
        self.pages[realPage].dump(pcb,page,self.memory)
        
        
    def get(self,pcb):
        page = pcb.programCounter / self.pageSize
        positionInFrame = pcb.programCounter % self.pageSize
        #page = int(round(page))
        
    ## where is_
        ## nowhere, to Load
            ## are free frames -> create page, dump, load
            
        n = self.makePage()
        self.dumpPage(n,pcb,page)
        return self.getInstruction(n,page,positionInFrame)
            
            ## need to swap a frame -> later, dump, load
        ## in any page
            # in local Memory -> load
            # in virtual memory -> swap a frame, dump, load
    def getInstruction(self,realPage,page,positionInFrame):
        return self.pages[realPage].get(page,positionInFrame,self.memory)