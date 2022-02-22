# pip install phonenumbers
import phonenumbers
from phonenumbers import geocoder

phone = input('-Verificador de Telefone-\nDigite o telefone no formato  +551140028922: ')

try:
	phone_number = phonenumbers.parse(phone)
	print(geocoder.description_for_number(phone_number, 'pt'))
except:
	print('Digitou errado, não foi possível achar o número informado.')
