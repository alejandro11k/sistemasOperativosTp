'''
Created on Nov 29, 2015

@author: alejandrok
'''

class Page(object):
    '''
    classdocs
    '''


    def __init__(self,pageId,pageSize):
        '''
        Constructor
        '''
        self.pageId = pageId
        self.pcb = None
        self.pageNumber = None
        self.pageSize = pageSize
        self.isInFrame = False
        
    def isPid(self,idProcess,pageNumber):
        return self.pcb.idProcess==idProcess and self.pageNumber==pageNumber
    
    def dump(self,pcb,pageNumber,memory,frame):
        # needs
            # instructions quantity to dump, pageSize
            # the instructions! <- from pcb?... acces to hardDisc?
            # for the moment the pcb know de program pcb2 class
            
            for n in range(self.pageSize):
                print("pageID:",self.pageId)
                # uncalculated N to get instruction!!!!!!!!!!!!!!!!!!!!!!!!! :(
                nextI = n+(self.pageSize*pageNumber)
                if nextI<pcb.program.programLength():
                    instruction = pcb.program.getInstruction(nextI)
                # the first pos in memory -> pageId
                # IDpage as the same as frame yet! resolve!!!!!!!!!!!!!!!!!!!!
                    print("stupidNumber:",self.pageId*self.pageSize+n)
                    baseD = frame.firstMemoryDirection
                    memory.put(baseD*self.pageSize+n,instruction)
                    self.isInFrame = True
                    frame.isFree = False
                    frame.page = self.pageId
            
            # record a number to calculate longevidad, NO! --> delegate to read!
            self.pcb = pcb
            self.pageNumber = pageNumber
    
    def get(self,page,frame,positionInFrame,memory):
        
        memoryFrame = frame.firstMemoryDirection*self.pageSize
        return memory.get(memoryFrame+positionInFrame)
    
        