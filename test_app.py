from app import app
from unittest import TestCase

class ForexConverterTestCase(TestCase):

	def test_form(self):
		with app.test_client() as client:
			res = client.get('/')
			html = res.get_data(as_text=True)

			self.assertEqual(res.status_code, 200)
			self.assertIn('<h2>Foreign Exchange Converter</h2>', html)


	def test_converter_form(self):
		with app.test_client() as client:
			res = client.post('/conversion', data={'c1': 'EUR','c2': 'USD', 
								'amt': '1','symbol': '$'})
			html = res.get_data(as_text=True)

			self.assertEqual(res.status_code, 200)
			self.assertIn('<p>Conversion of 1 EUR to USD is: US$ 1.19</p>', html)

	def test_redirection(self):
		with app.test_client() as client:
			res = client.get('/home-btn')

			self.assertEqual(res.status_code, 302)
			self.assertEqual(res.location, 'http://localhost/') 


	def test_redirection_followed(self):
		with app.test_client() as client:
			res = client.get('/home-btn', follow_redirects=True)
			html = res.get_data(as_text=True)

			self.assertEqual(res.status_code, 200)
			self.assertIn('<h2>Foreign Exchange Converter</h2>', html)
	