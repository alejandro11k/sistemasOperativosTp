from software.paging_memory.frame import Frame
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
        self.frames = {}
        self.initializeFrame()
        
    def initializeFrame(self):
        frameQuantity = self.memory.size() + 1 // self.pageSize
        for n in range(frameQuantity):
            self.frames[n]= Frame(n,self.pageSize)
        
    def pagesOK(self):
        return self.pageSize % self.memory.size() == 0
    
    def numberOfFrames(self):
        return self.memory.size() / self.pageSize
    
    def takeAFreeFrame(self):
        for n in range(len(self.frames)):
            if self.frames[n].isFree:
                return self.frames[n]
    
    def freeFrame(self):
        freeFrame = self.takeAFreeFrame()
        if not (freeFrame == False):
            return freeFrame
        else:
            print("SIN MEMORIA!!! ...sin marcos... ")
            
    def freePage(self):
        usedPages = len(self.pages)
        return usedPages
            
    def makePage(self):
        n = self.freePage()
        self.pages[n] = Page(n,self.pageSize)
        return n
    
    def dumpPage(self,realPage,pcb,page,frame):
        #firstIntructionNumber = self.pageSize*page
        self.pages[realPage].dump(pcb,page,self.memory,frame)
        
        
    def get(self,pcb):
        
        page = pcb.programCounter // self.pageSize
        positionInFrame = pcb.programCounter % self.pageSize
        
        print("page:",page,"pos:",positionInFrame)
        
    ## where is_
        ## nowhere, to Load
        
        if not (self.isDumped(pcb.idProcess,page)):
            ## are free frames -> create page, dump, load    
            n = self.makePage()
            
            ## si hay frames libres
            frame = self.freeFrame()
            
            self.dumpPage(n,pcb,page,frame)
            ## need to swap a frame -> later, dump, load
        ## in any page
        else:
            n = self.dumpedPageFromMemory(pcb.idProcess,page)
            # in local Memory -> load
            # in virtual memory -> swap a frame, dump, load
            
        if not (self.pages[n].isInFrame):
            #swap
            pass
        else:
            frame = self.frame(n)
        
        return self.getInstruction(n,frame,page,positionInFrame)
    
    def frame(self,pageId):
        for n in range(len(self.frames)):
            if self.frames[n].page == pageId:
                return self.frames[n]
        
    
    def isDumped(self,idProcess,page):
        value = False
        for n in self.pages:
            value = value or self.pages[n].isPid(idProcess,page)
            
        return value
    
    def dumpedPageFromMemory(self,idProcess,page):
        for n in self.pages:
            if self.pages[n].isPid(idProcess,page):
                return n
        
    def getInstruction(self,n,frame,page,positionInFrame):
        return self.pages[n].get(page,frame,positionInFrame,self.memory)
    
    