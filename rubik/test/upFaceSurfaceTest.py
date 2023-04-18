'''
Created on April 2, 2023

@author: jonhoustonseibert
'''
import unittest
import rubik.view.solve as solve
from rubik.view.rotate import rotate
from rubik.model.constants import *
from rubik.controller import upFaceSurface


class UpFaceSurfaceTest(unittest.TestCase):

    # Happy Path Tests  
    def test_upFaceSurface_000_SolvedCubeShouldReturnOkStatus(self):
        parms = {}
        parms['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms['dir'] = 'R'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'

        actualResult = solve.solve(parms)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_upFaceSurface_010_SolvedCubeDoesNotContainRotations(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        rotations = ''
        
        expectedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedRotations = ''
        
        actualCube, actualRotations = upFaceSurface.solveUpSurface(cube, rotations)
        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_upFaceSurface_020_TestEdgePiecesMatch(self):
        cube = 'orbyrrrrrrgoggggggyrroooooogyybbobbbyygbyybbywwwwwwwww'
        rotations = ''

        expectedCube = 'orryrrrrrggoggggggbrboooooorygbbobbbyyybyyybywwwwwwwww'
        expectedSolution = 'RUrURUUrRUrURUUrRUrURUUr'

        actualCube, actualSolution = upFaceSurface._solveUpFaceEdgePieces(cube, rotations)

        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_upFaceSurface_025_TestEdgePiecesMatch(self):
        cube = 'brorrrrrrygrgggggggyyoooooobyobbbbbbroybyyyygwwwwwwwww'
        rotations = ''

        expectedCube = 'orrrrrrrrgybggggggryooooooobggbbbbbbyoyyybyyywwwwwwwww'
        expectedSolution = 'URUrURUUrRUrURUUrUURUrURUUr'

        actualCube, actualSolution = upFaceSurface._solveUpFaceEdgePieces(cube, rotations)

        self.assertEqual(expectedCube, actualCube)
        self.assertEqual(expectedSolution, actualSolution)
        
    def test_upFaceSurface_030_AreUpEdgePiecesSolved(self):
        cube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'

        actualResult = upFaceSurface._doUpFaceEdgePiecesMatch(cube)

        self.assertTrue(actualResult)
        
    def test_upFaceCross_050_SolveUpFaceSurface(self):
        cubes = ['orbyrrrrrrgoggggggyrroooooogyybbobbbyygbyybbywwwwwwwww',
                 'U2ig99iU9F9iUgFUiFggF92F92292F2FUgg2U99gUi2U2gFgiiFUii',
                 'kauEgkaEkEavvukggkkkgaauEEavuaakguvuugavEvEEgvuvgvuEkg',
                 'cxlM9MM9c99Kclx9Kc9Kc9MxlKKllxcxxllKMMxcclMKKxcxMK9Ml9',
                 'C0hhXX0XC22CC2C22h22y20000hhyXyyy2yyX00CChyhXChXXhX0Cy',
                 'm22wwmBwmwBBQ2Bw5w2mQ2Q5BQQ2mQmm2m5m5BQwBQB55wB5w5Q522']
        for cube in cubes:
            parms = {}
            parms['op'] = 'solve'
            parms['cube'] = cube

            expectResult = {}
            expectResult['status'] = 'ok'

            actualResult = solve.solve(parms)

            rotatedCube = {}
            rotatedCube['cube'] = parms.get('cube')
            rotatedCube['dir'] = actualResult.get('solution')
            actualCube = rotate(rotatedCube).get('cube')

            cubeFaces = {
                "bottom": [DTL, DTM, DTR, DML, DMM, DMR, DBL, DBM, DBR],
                "front": [FML, FMM, FMR, FBL, FBM, FBR],
                "right": [RML, RMM, RMR, RBL, RBM, RBR],
                "back": [BML, BMM, BMR, BBL, BBM, BBR],
                "left": [LML, LMM, LMR, LBL, LBM, LBR],
                "up": [UTL, UTM, UTR, UML, UMM, UMR, UBL, UBM, UBR]
            }

            for cubeFaces, cubeIndexes in cubeFaces.items():
                faceColors = [actualCube[cubeIndex] for cubeIndex in cubeIndexes]
                self.assertTrue(all(color is faceColors[FTL] for color in faceColors))
            
            self.assertEqual(expectResult.get('status'), actualResult.get('status'))
            
    def test_upFaceCross_060_SolveUpFaceSurfaceWithFailingTestCubes(self):
        cubes = ['DQZDtZQtQKKQQKBBDZBKttZKKBBKKtZQttBDDBtDDtQDBZQZZBZKQD',
                 'ZZfYYu55YY5fmmmm5ZmuuYufu5YmfYYZZZmZ5ZuufZ5fmuu5f5Yfmf',
                 '27a2T7Tsa7asDD77DT7ssa77sDDDas22TTsaTDDTa27s222DTsTaa2',
                 '1Y1zGGzaaaaazzYYnazYzGaYzGnYGYa1a1nGGznnYnG1nn11zn1G1Y'
                ]
        for cube in cubes:
            parms = {}
            parms['op'] = 'solve'
            parms['cube'] = cube

            expectResult = {}
            expectResult['status'] = 'ok'

            actualResult = solve.solve(parms)

            rotatedCube = {}
            rotatedCube['cube'] = parms.get('cube')
            rotatedCube['dir'] = actualResult.get('solution')
            actualCube = rotate(rotatedCube).get('cube')

            cubeFaces = {
                "Bottom Face": [DTL, DTM, DTR, DML, DMM, DMR, DBL, DBM, DBR],
                "Front  Face": [FML, FMM, FMR, FBL, FBM, FBR],
                "Right  Face": [RML, RMM, RMR, RBL, RBM, RBR],
                "Back   Face": [BML, BMM, BMR, BBL, BBM, BBR],
                "Left   Face": [LML, LMM, LMR, LBL, LBM, LBR],
                "Up     Face": [UTL, UTM, UTR, UML, UMM, UMR, UBL, UBM, UBR]
            }

            for cubeFaces, cubeIndexes in cubeFaces.items():
                faceColors = [actualCube[cubeIndex] for cubeIndex in cubeIndexes]
                self.assertTrue(all(color is faceColors[FTL] for color in faceColors))

            self.assertEqual(expectResult.get('status'), actualResult.get('status'))
            
    def test070_unsolvedCubesFromIteration5AreFullySolved(self):
        cubes = ['bcjj9jc9PbbjPPPjjP9JJ9cJcc9PPJbbbJJbc9bcJc9JcJb9Pj9Pjj',
                 'Odd66V3ww336w3ddOdw663OO3VOVdV3ww3wVwVd6V6wO66OOddVV3O',
                 'DgiDff33333iiHigHiDfHDg3DgDffgfigHig3DgHDHH3fHiig3DfHf',
                 'YBYbbKBxhKhKBxYbhYBKbxKbxbYBBbhhBKbKxYhhYYhxhxKBYBKxxb',
                 '1Y1zGGzaaaaazzYYnazYzGaYzGnYGYa1a1nGGznnYnG1nn11zn1G1Y',
                 'dPNfdttffffN55Pt55dtPNPPNd5ffttfNPN5tdfPtt55PPdddNNN5d',
                 'uG3Uuu3YYUG8333uU3YYG888uU8YGUGG8Guu833YYUGu8U8GYUuU3Y',
                 'O5rFor5rgooForO5gOO5rgOogOFO55Fgggro5rrg55gOFrFoOFooFF',
                 '45G44D344EDDG55G45433DEE3EDEE5DGG5E4GGGG34D3D5333D5E5E',
                 'sjssjjbbjKSKKKbSjbsKSSQQQSSKsjKbjKbQjsjQsQbSQSsbQSbQKs',
                 'aJ0LJJa0MMaMMqMLLLLa00aaqa0q000MMMLLJMaJLqqqaqqJq0JJLJ',
                 'GEPETFPFFFGnPnPnnPETPGFPFEnGFTTPPFTTTnTnEFnnGEEEGGGGTE',
                 'sjjJPPJsPPxxJjAAjsPsJPsjxAjPsJJAAxAAAxjJxPjPJsjxsJxsxA',
                 'bggeIIeII7Ib77s77sIgg7gg7bgssIsbbsbb77sbsseeegeegeebII',
                 'weTS33SeEewwwSETSEe33TTeS3SwwewwT3S3EETEeT3TSESwEE3eeT',
                 'M11BMM18Lk8kB1BBLM8k8L8BBMB1118BkLk8L1B8kkLLMkLMMLM81k',
                 'RskRRUs6UU62s22sksRR2UU6RUUU2kRss6kRkk6Rks2ksk2626U266',
                 'yoTyTTlcOOlccOycyOTlOTooycocyTOlOlTyoTloycllyoOTOclcoo',
                 'NTGGlNTlG444444AAAllGTTGlNlAl4AATGANlNNGGGTNTA4TlNT4AN',
                 'llKllkklleexxxKJkKJkKxkkxKkkxxJexeKKeKkJKJJelxJeeJeJll'
                ]
        for cube in cubes:
            parms = {}
            parms['op'] = 'solve'
            parms['cube'] = cube

            expectResult = {}
            expectResult['status'] = 'ok'

            actualResult = solve.solve(parms)

            rotatedCube = {}
            rotatedCube['cube'] = parms.get('cube')
            rotatedCube['dir'] = actualResult.get('solution')
            actualCube = rotate(rotatedCube).get('cube')

            cubeFaces = {
                "bottom": [DTL, DTM, DTR, DML, DMM, DMR, DBL, DBM, DBR],
                "front": [FTL, FTM, FTR, FML, FMM, FMR, FBL, FBM, FBR],
                "right": [RTL, RTM, RTR, RML, RMM, RMR, RBL, RBM, RBR],
                "back": [BTL, BTM, BTR, BML, BMM, BMR, BBL, BBM, BBR],
                "left": [LTL, LTM, LTR, LML, LMM, LMR, LBL, LBM, LBR],
                "up": [UTL, UTM, UTR, UML, UMM, UMR, UBL, UBM, UBR],
            }

            for cubeFaces, cubeIndexes in cubeFaces.items():
                faceColors = [actualCube[cubeIndex] for cubeIndex in cubeIndexes]
                self.assertTrue(all(color is faceColors[FTL] for color in faceColors))

            self.assertEqual(expectResult.get('status'), actualResult.get('status'))
        