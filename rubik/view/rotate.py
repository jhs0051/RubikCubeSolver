from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    
    validKeys = 'cube', 'dir', 'op', 'solve'
    keys = parms.keys()
    
    for key in keys:
        if key in validKeys:
            result['status'] = 'error: extraneous key detected'
            return result
        
    try:
        encodedCube = parms.get('cube')
    except:
        result['status'] = 'error: invalid cube'
        return result
        
    if encodedCube == None or encodedCube == '':
        result['status'] = 'error: invalid cube'
        return result
    else:
        theCube = Cube(encodedCube)
    
    try:
        directions = parms.get('dir')
    except:
        result['status'] = 'error: invalid cube'
        return result
    
    if Cube._validation(encodedCube, directions) == False:
        result['status'] = 'error: invalid cube'
        return result
    
    theCube.rotate(directions)
     
    
    result['cube'] = theCube.get()
    result['status'] = 'ok'                     
    return result