from sys import argv
import phonenumbers as ph
from phonenumbers import parse, geocoder, carrier, timezone


def pni_help():
	print('pni usage : python pni.py [+COUNTRY_CODE NUMBER] --> +ZZXXXXXXXXXX')

def phone_number_info(num):

	print(f'- pni (phone number info) information')

	#Country code and National number
	num_info = parse(num, None)
	print(f"\t{num_info}")

	#Country name
	num_country = parse(num, 'CH')
	print(f"\tCountry   : {geocoder.description_for_number(num_country, 'en')}")

	#Name of Service
	num_service = parse(num, 'RO')
	print(f"\tService   : {carrier.name_for_number(num_service, 'en')}")

	#Phone number time-zone
	num_tzone = parse(num, "GB")
	print(f"\tTime-zone : {timezone.time_zones_for_number(num_tzone)[0]}")

	#Is it emergency number?
	print(f"\tEmergency : {ph.is_emergency_number(num, '+98')}")

def main():
	if len(argv) > 1:
		num=argv[1]
		phone_number_info(num)
	else:
		pni_help()

if __name__ == "__main__":
	main()
