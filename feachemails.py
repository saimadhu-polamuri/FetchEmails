__author__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '14-June-2015'

import re
import sys
import pandas as pd

class Emails():

	def __init__(self,filename):

		""" Initial function in Emails class to feach emails from raw data """

		self.filename = filename

	def get_mail(self,line):

		tempemailslist = []

		for word in re.split(',|-| \n|/|:| ',line):

			#relist = re.findall(r'[^@]+@[^@]+\.[a-z]+',word)
			relist = re.findall(r'[A-Za-z0-9.]+@[^@]+\.[a-z]+',word)
			#relist = re.findall(r'[\w\.-]+@[\w\.-]+',word)
			if len(relist):
				tempemailslist.extend(relist)

		
		return tempemailslist


	def read_file(self):

		""" Reads the input file and gets the Emails  """

		emailList = []
		with open(self.filename, 'r') as f:
			for line in f:
				if line.split():
					emails = self.get_mail(line)
					if len(emails)>0:
						emailList.extend(emails)

		return emailList

	def list_to_csvfile(self,emailslist):

		df = pd.DataFrame(emailslist, columns=['Emailids'])
		df.to_csv('emails.csv')


def main():

	filename = sys.argv[1]
	emailsInstance = Emails(filename)
	emailids = emailsInstance.read_file()
	#print emailids
	#print len(list(set(emailids)))
	emailsInstance.list_to_csvfile(list(set(emailids)))
	print "{emailscount} Emails  has be save to emails.csv file\n".format(emailscount=len(list(set(emailids))))

if __name__ == "__main__":
	main()






