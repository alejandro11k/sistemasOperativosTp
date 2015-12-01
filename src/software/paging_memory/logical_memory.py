'''
Created on Nov 29, 2015

@author: alejandrok
'''
from software.paging_memory.page import Page 
from idlelib.ColorDelegator import idprog

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
        return self.memory.size() / self.pageSize
    
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
        page = pcb.programCounter // self.pageSize
#        page = int(round(page))
        positionInFrame = pcb.programCounter % self.pageSize
        
        print("page:",page,"pos:",positionInFrame)
        
        
    ## where is_
        ## nowhere, to Load
        
        if not (self.isDumped(pcb.idProcess,page)):
            ## are free frames -> create page, dump, load    
            n = self.makePage()
            self.dumpPage(n,pcb,page)
            ## need to swap a frame -> later, dump, load
        ## in any page
        else:
            n = self.dumpedPageFromMemory(pcb.idProcess,page)
            # in local Memory -> load
            # in virtual memory -> swap a frame, dump, load
            
        return self.getInstruction(n,page,positionInFrame)
    
    
    def isDumped(self,idProcess,page):
        value = False
        for n in self.pages:
            value = value or self.pages[n].isPid(idProcess,page)
            
        return value
    
    def dumpedPageFromMemory(self,idProcess,page):
        for n in self.pages:
            if self.pages[n].isPid(idProcess,page):
                return n
        
    def getInstruction(self,n,page,positionInFrame):
        return self.pages[n].get(page,positionInFrame,self.memory)
    
    