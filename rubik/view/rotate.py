from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    
    try:
        encodedCube = parms.get('cube')
    except:
        result['status'] = 'error: invalid cube'
        return result
        
    theCube = Cube(encodedCube)
    
    try:
        directions = parms.get('dir')
    except:
        result['status'] = 'error: invalid cube'
        return result
    
    if Cube._validation(encodedCube) == False:
        result['status'] = 'error: invalid cube'
        return result
    
    theCube.rotate(directions)
    
    result['cube'] = theCube.get()
    result['status'] = 'ok'                     
    return result