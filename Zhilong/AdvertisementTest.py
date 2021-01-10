import unittest
import AdvertisementClass

class MyTestCase(unittest.TestCase):
    def testInitadvertisement(self):
        agency_detail = AdvertisementClass.Advertisement('UCL',4402076792000,'https://www.ucl.ac.uk/','University College London,Gower Street,London','https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2739117239,1572755614&fm=26&gp=0.jpg')
        self.assertEqual(agency_detail.__repr__(),
                         'Advertisement(Agency=UCL,Tel=4402076792000,Address=University College London,Gower Street,London)')

    def testUpdateDetail(self):
        agency_detail = AdvertisementClass.Advertisement('UCL',4402076792000,'https://www.ucl.ac.uk/','University College London,Gower Street,London','https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2739117239,1572755614&fm=26&gp=0.jpg')
        self.assertEqual(agency_detail.__repr__(),
                         'Advertisement(Agency=UCL,Tel=4402076792000,Address=University College London,Gower Street,London)')
        agency_detail.UpdateAd('University College London',4402076792000,'https://www.ucl.ac.uk/','University College London,Gower Street,London','https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2739117239,1572755614&fm=26&gp=0.jpg')

        self.assertEqual(agency_detail.__repr__(),
                         'Advertisement(Agency=University College London,Tel=4402076792000,Address=University College London,Gower Street,London)')

if __name__ == '__main__':
    unittest.main()
