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
        
    def isPid(self,idProcess,pageNumber):
        return self.pcb.idProcess==idProcess #and self.pageNumber==pageNumber
    
    def dump(self,pcb,pageNumber,memory):
        # needs
            # instructions quantity to dump, pageSize
            # the instructions! <- from pcb?... acces to hardDisc?
            # for the moment the pcb know de program pcb2 class
            
            for n in range(self.pageSize):
                # uncalculated N to get instruction!!!!!!!!!!!!!!!!!!!!!!!!! :(
                instruction = pcb.program.getInstruction(n)
                # the first pos in memory -> pageId
                memory.put(self.pageId+n,instruction)
            
            # record a number to calculate longevidad, NO! --> delegate to read!
            self.pcb = pcb
    
    def get(self,page,positionInFrame,memory):
        memoryFrame = self.pageId*self.pageSize
        return memory.get(memoryFrame+positionInFrame)
    
        