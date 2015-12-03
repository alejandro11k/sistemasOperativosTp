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
            
            count = 0
            
            for n in range(self.pageSize):
                print("pageID:",self.pageId)
                
                nextI = n+(self.pageSize*pageNumber)
                if nextI<pcb.program.programLength():
                    instruction = pcb.program.getInstruction(nextI)
                    print("OLD stupidNumber:",self.pageId*self.pageSize+n)
                    baseD = frame.firstMemoryDirection
                    address = baseD+n
                    memory.put(address,instruction)
                    count+=1
                    
            self.isInFrame = True
            frame.setPage(self.pageId,count)
            self.pcb = pcb
            self.pageNumber = pageNumber
    
    def get(self,page,frame,positionInFrame,memory):
        
        memoryFrame = frame.firstMemoryDirection
        return memory.get(memoryFrame+positionInFrame)
    
        