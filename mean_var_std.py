import numpy as np

def calculate(list):
    if (len(list)!=9):
        raise ValueError ('List must contain nine numbers.')
        
    lst=np.array(list)
    New_lst= lst.reshape(3,3)
    
    
    
    calculations={
         

      
    'mean':[[np.mean(New_lst , axis=0).tolist()], [np.mean(New_lst ,axis=1).tolist()],[np.mean(New_lst)]],
    'variance': [[np.var(New_lst ,axis=0).tolist()],[np.var(New_lst ,axis=1).tolist()], [np.var(New_lst)]],
    'standard deviation': [[np.std(New_lst , axis=0).tolist()] ,[np.std(New_lst , axis=1).tolist()], [np.std(New_lst)]],
    'max': [[np.amax(New_lst , axis=0).tolist()] ,[np.amax(New_lst , axis=1).tolist()], [np.amax(New_lst)]],
    'min': [[np.amin(New_lst , axis=0).tolist()] ,[np.amin(New_lst , axis=1).tolist()], [np.amin(New_lst)]],
    'sum': [[np.sum(New_lst , axis=0).tolist()] ,[np.sum(New_lst , axis=1).tolist()], [np.sum(New_lst)]]
  }
  


    return calculations  
