from unittest import TestCase
from rubik.view.rotate import rotate
from rubik.model.constants import *
from rubik.view.solve import solve, _getIntegrity
 

class SolveTest(TestCase):
    # Happy Path
    def test_010_solve_Integrity(self):
        parms = {}
        parms['cube'] = 'ccpattYcpYaaYaatcYotaoootcocYtppYpptopYoYtaaoapcYcoctp'

        actualResult = solve(parms)

        theCube = parms.get('cube')
        solution = actualResult.get('solution')

        expectedToken = '16551a2ef32869f249f2994d5456a7cad0b946f0578de0cd65806d27b6f689d0'

        actualToken = _getIntegrity(theCube, solution)
        self.assertIn(actualToken, expectedToken)
        
    def test_020_solve_Integrity(self):
        parms = {}
        parms['cube'] = 'poap344343343aOOaoaaaoo3poo4OOaOOOpO3oo44O34p3poap4ppa'

        actualResult = solve(parms)

        theCube = parms.get('cube')
        solution = actualResult.get('solution')

        expectedToken = '3756408d941c9ec075be1127fa9b06e16cfe1242de2c785043d3a7d9470c173d'

        actualToken = _getIntegrity(theCube, solution)
        self.assertIn(actualToken, expectedToken)
        
    def test_030_unsolvedCubesFromIteration1AreFullySolved(self):
        cubes = ['Q5KQQKQfftQKtfyyyQ5f5KKfytfK55Ktf5tyfytQyttKyt5K55QQyf',
                 '33vvvyDrrtDyDrtyrrDvvv3vv3tDDtDDy33ytrvty3rrr3t3ytyDty',
                 'cXEdrXrrXr1cr1E1EX1cdXd1ddXEd1dEXr1EcrdEcrr1cXEdcXc1cE',
                 'dVVdTTTVWeTVddTedVlVelVVeeVTeWeelWedlddWlWTlllWTTWWdlW',
                 'GGAA9LL9ALkaAAAkLL9aAkLLa99G9akaGkGA9GGkGaLLGkA99kaaak',
                 'zooz3I33myzImzm3z33yz3o3zmoyIIzmoIoIo3zoIyoymmIymyImyy',
                 'yQhhnh8nh00yyy8008QyhQ8nQynyQ8h000hQnnn0Q8hy8yQn8hnQ80',
                 'xx3IFFII444PPPxFFPF3I333FFPFI3Ixx33xx4IP4P44P3FxPIxI44',
                 '70h0qGhGqGGGzz77hzqz7hh00qhGzqz770q0hqzhG70hz7qG70Gz0q',
                 'OoNbbNNbPbiOiNNbObiiioOOPiObNiPPPPPoNbNOiOPboONoooooPi',
                 'UU66UUKYi0KiiY0KKYKK6iKYU6YKYii00iU60iYU6Y00UY606i0UK6',
                 'IMMIMiMiMIMIufiImfmImfimumifIufIuuufiMimmuifumImfuifMM',
                 'ggt88I8c8gIIcIcII8ttqgcqqtgI8c8ggqggccctq8qqctqtttq8II'
                ]
        for cube in cubes:
            parms = {}
            parms['op'] = 'solve'
            parms['cube'] = cube

            expectResult = {}
            expectResult['status'] = 'ok'

            actualResult = solve(parms)

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
            
    def test_040_unsolvedCubesFromIteration2AreFullySolved(self):
        cubes = ['bwbWbbwUUVffwVbWWWwVwVUfUUVfVWbfbWfVbWUwwwfUwUVVUWfbWf',
                 'BFeBBzFBzzzxeeKKzxKeFFzKKxBBBxxKxeezKBBKxFeexeFFxFKFzz',
                 'Co3ooo773B7UCUBUUB73CC7o77ooC7UB3UCUBB3733BBoCBoUC3CU3',
                 'N4ra422r4hrhhaN2arrhh4rN2h44NrahrNaaN42rN2a2N4hh422aNa',
                 'uHphhppNhHWuWuupuhWhhWWhNNhuuWppHuWWHuHHHHNpWNhHNNNNpp',
                 'MvdbuubuubRvRvbRudMRuRbdbvMRvuMdMbdvvvuMMdduRRddbRMvbM',
                 '42RRR624b4b6hhb26R2R6222h4bRbh4b6644bhhR46Rhbhh4R622b6',
                 'zSzZZZNNJZJJSzNNXNSZZzNSJXXzSNzJXZXXXzZNXZSJSzJXzSJJNS',
                 '44NN47MNN7M4MxNxMMN2227747774Mx2xx47MM22Nx2x2x74NM4N2x',
                 'v3DccJDDv3366JJ3DDDc6c6633Jvvcv3v6Jc3DJ3D6JDcJJcvv6vc6',
                 'RN1NNUXUUR1ssUXXsR1XUN1Us1NXUNXRRURRNRUNXRssXN11ss1sX1',
                 'AA11YYQA3QHAA13Y1A3YHQQ3HH11YY1AYYA1Y3QH3QHQ3HHA3HQ31Q',
                 '5XzXKyXyz55yKzgXKgggKzgzXKK55yKyzy5Kzy5yXzKggzXgg5XX5y',
                 'FFGGMFVTTMTTZVGZVFZFMMFMZTVVZGVZZGGFTVMMTMVTZTZFFGGMVG',
                 'LgCCdCZgdmmmLmZZCCLCZdLZLLCggCmgggLLdmZdZdmZdgLmZCddmg',
                 'HHgoVVoVHAHuuooouAgHVuHAVguoVgHgAggAugVouuAoVHAuAAgHVo',
                 'etYeDNYNAettAtYDDYDDteeAtYeNNteAtAAAetNeYNYYADDNDNYNAD',
                 'Www3WwWWw33u3MWMMw3uMuBB3MMBwMu3BB33wMBBwWuWWuMWuuwuBB',
                 '3YotuuYoovv3ttY3YuY3YoovYov3uutY3tYvuuovvotuto3tv33utv',
                 'WLWLV00oLVW0VLLWWoVLLVMW0MWVoVVoWoMM00oVWMoMLL0Mo0oM0M'
                ]
        for cube in cubes:
            parms = {}
            parms['op'] = 'solve'
            parms['cube'] = cube

            expectResult = {}
            expectResult['status'] = 'ok'

            actualResult = solve(parms)

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
            
    def test_050_unsolvedCubesFromIteration3AreFullySolved(self):
        cubes = ['WSWSiiWWWDDDcWQDiSQDciDQcciQcQWcDccSiQcDSWiiSiSQSQWSQD',
                 'BOJJB6DB6zOBJD6BzzJDOzzB6B6zDOO6zOBz6JDzO6DDDODJ6JOBJJ',
                 'W09RIVWIRRVVIVR000909W0IWIIVRIRR0W9R09I99WVWI0W9VWVR9V',
                 'YCoCiHinCCnYinnHHYHYYoCoHYoniniHoiiHCCiYYYiHnoConoonHC',
                 'FaFa3qIF3IFqffFFIqff3Iqqfa3af3IIqaFaI3Faa3f3qqfIqF3fIa',
                 'TsXTVCTXX777sCTVVTX7sVsT7CCTXV77sssVCXVVTV7XsCCC7XCXTs',
                 'E7gvv5vv5775E5EEo5Eg7gg77EogovvoEg5o5ovvEgo5o75gg77Eov',
                 'rdcCrCd4r44CddVVCCrc4ccrcCVc44d4cdrrVddVCcCVCVr4VVrc4d',
                 'kkXNNkNVkIVmXVXVIXVImNkXmmNNVmmXIXNVXXNIImVmkIkIVmkINk',
                 'B9AgBHgB9990g90HHB9gH90BHBg0AA9g0HH0gAA0HAgHBAg0BA0BA9',
                 'AAplmmlmmiiillilllApmAppoopomliioiioilmoooppomAAmAAApp',
                 'bGiicSSnSniGcSbbnScSiciScibGGibGSGGbnnnnnGGbSicccbicbn',
                 'BHBaSBaS00SBaaBS0aaSwwBwS0waw0S0wSHSBaH0w0HawHHHBHH0Bw',
                 'hNm4m544P5mNPPPNm5mhhN44PmN5N4Nhhm45m5PhN5NmPhP455Phh4',
                 'SuwurrrwuuSrwRRSRrwSutuwRttSwRuwtRuSRRtSSrrRtwtwStrurt',
                 'BBPBBuuPhohBohh4oPhhoBPPoohBB44o4PPhuuuuu4oouPhBu444P4',
                 'XnXRR665Rpn6pXp6XnXpR5pp5X5XRpn56nn5nXR5n56Xnp65R6RR6p',
                 'KUffF55Ff25KUfKUf2UfU25FKUf5K2UKF2FUf2F522FfFK2FKU55K5',
                 '3zRlSSS3lSSS3zSvlz3RzRlvvlS3zlRRRvSRl3zvvvRlv3zRz3vz3l',
                 'gngOngkgOncOkNncgnngOkcnNOgcONNkNccnknNkONcOkONNkgckcg'
                ]
        for cube in cubes:
            parms = {}
            parms['op'] = 'solve'
            parms['cube'] = cube

            expectResult = {}
            expectResult['status'] = 'ok'

            actualResult = solve(parms)

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
            
    def test060_unsolvedCubesFromIteration4AreFullySolved(self):
        cubes = ['DDo555TDDDoHHzHzzTzo5zDDo55ooHooTTzoHT55THzHH5TTDHTzzD',
                 'TTogUogUoUffU1gU1TgTo1g1fU1gTUfTofooTg1fogfo11fT1fUUTg',
                 '5ys7aa8aaaasyssyaa7y7875555yy7sy8s7a878585y85s88s5s77y',
                 'A0ABB0BBtBbttAAAtCCAbBCtACt0bCC00Bb0Ct0At0bCbbbBCbB0At',
                 'BGzG6zB6zB66bGBbbnbBnnznbGn66Gbnb6nzBzGBBG6zGnnGzb6bBz',
                 'HLRRwswQQHQHQssHRRRLQwLRLwsssQHHsLwswRLLRLLHwRHwHQwQQs',
                 '90KC08K909KCKKKO9C8889C8OC80COOOKO80KCKO800OC9O8090C99',
                 'NNRRT2RTN2RJNJJTJNE2NE2TERJENRJNJE2J2ETEET2TJTERRR22NT',
                 'zzb9Yz99JzbYbzzY29z9bJbb2YYJY229bJY29J292Jb2Jb2zzJY9JY',
                 'cmmc1c1jj1hh1mjcmhm00h01j11m1jhjjjmmcc0mh01cch000chhj0',
                 'JuD7D0YD7Y0u7uuu00J7YY777Y7DJDY0JY000uDuJD0Du7JJYYJuDJ',
                 'XXuusKuFKauuaXaaKuXuXFFKXsKKFKsaassssssuKXFKFaXFauFaXF',
                 'zdoodoztoHHdtWWWHWWWWdoHooddttWzWHztHttztzdzzodtoHdzHH',
                 'Mi3aii22i2iiaa3aaaMaVMVVVi3MVaM3MV33aV32M3iMiV32V22M22',
                 '0geGzezhGGeeG0Gh0Ghe0zezz0zGzghhhhz0e0gggheehggz0GGgg0',
                 'tDtT55TaTaQDtTaQDTTTDTaQ5tt5tQ5t5aDDtD5aQT5tDaQaaD5QQQ',
                 'w2DcNNNcN2DDwccDDNtwcw22wDcNwttt2wNwD22twN2DctNttDc2tc',
                 'dUidUrUrUdiQ999i9irdddQUQdd9QQ9iQ9Q9UU9irUirUrirrdQQir',
                 'UWv9tUvtv9UqWqq9tqUqt9WtWUq9Ut9vvU9UqWttUvvvtWqWW9vWq9',
                 'PP775Pgg5PZSgPSS5ggPS5ZZ5S57gZSSP77SZ55Z77gZZZS75ggP7P'
                ]
        for cube in cubes:
            parms = {}
            parms['op'] = 'solve'
            parms['cube'] = cube

            expectResult = {}
            expectResult['status'] = 'ok'

            actualResult = solve(parms)

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
        
    # Sad Path
    def test_900_solve_ErrorOnShortCube(self):
        parms = {}
        parms['cube'] = 'w5i1w5i1S1iwa5iaSSSi1aa5iw15wSSia5waw1i5'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test_910_solve_ErrorOnLongCube(self):
        parms = {}
        parms['cube'] = 'PFUPFPLrL2rFUrrFPrrLL2PL22UUULrU222FPU2F2FrLPUPrFLLFUPPFUPFPLrL2rFUrrFPrrLL2PL22UUULrU222FPU2F2FrLPU'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test_920_solve_ErrorOnCubeWithIllegalCharacters(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbb*********rrrrrrrrroooooooooyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test_930_solve_ErrorOnMoreThan9OfAColor(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwb'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test_940_solve_ErrorOnNonUniqueMiddleCharacter(self):
        parms = {}
        parms['cube'] = 'rbbbbbbbbrrrrbrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test_950_solve_ErrorOnInvalidKey(self):
        parms = {}
        parms['cube'] = 'ogwwrywybgyrgbgrrwoogbgwyrworyryggwbbbyyowgobroobwoybr'
        parms['extra'] = 'key'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid key', result['status'])
        
    def test_bottomCross_960_ErrorOnEmptyString(self):
        parms = {}
        parms['op'] = 'solve'
        parms['cube'] = ''

        expectResult = {}
        expectResult['status'] = 'error: cube can not be empty'

        actualResult = solve(parms)
        self.assertEqual(expectResult.get('status'), actualResult.get('status'))
