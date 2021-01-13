import unittest
import AdvertisementClass
from FlaskProject import Webapplication as wb

class MyTestCase(unittest.TestCase):
    def testSetUpInit(self):
        agency_detail = AdvertisementClass.Advertisement('UCL',4402076792000,'https://www.ucl.ac.uk/','University College London,Gower Street,London','https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2739117239,1572755614&fm=26&gp=0.jpg')
        self.assertEqual(agency_detail.__repr__(),'Advertisement(Agency=UCL,Tel=4402076792000,Address=University College London,Gower Street,London)')

    def testUpdateAd(self):
        agency_detail = AdvertisementClass.Advertisement('UCL',4402076792000,'https://www.ucl.ac.uk/','University College London,Gower Street,London','https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2739117239,1572755614&fm=26&gp=0.jpg')
        self.assertEqual(agency_detail.__repr__(),
                         'Advertisement(Agency=UCL,Tel=4402076792000,Address=University College London,Gower Street,London)')
        agency_detail.UpdateAd('University College London',4402076792000,'https://www.ucl.ac.uk/','University College London,Gower Street,London','https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2739117239,1572755614&fm=26&gp=0.jpg')

        self.assertEqual(agency_detail.__repr__(),
                         'Advertisement(Agency=University College London,Tel=4402076792000,Address=University College London,Gower Street,London)')
    def testWebapplication(self):
        wb.app.run(port=5002,debug=True)

if __name__ == '__main__':
    unittest.main()
