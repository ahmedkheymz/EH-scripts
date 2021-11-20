import requests
from os import path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Put a domain")
parser = parser.parse_args()

def main():
	if parser.target:
		if path.exists('subdomains.txt'): # store your wordlist with same folder or give the path...
			wordlist = open('subdomains.txt','r') # change wordlist name or name your wordlist exactly..
			wordlist = wordlist.read().split('\n')

			for subdomain in wordlist:
				urls ="https://"+subdomain+"."+parser.target
				try:
					requests.get(urls)
                
				except requests.ConnectionError:
                       
					    print("Not found ")
         
				else:
                    
					print("Found!!"+"(+) Subdomain: "+urls)

			for subdomain in wordlist:
				url = "http://"+subdomain+"."+parser.target
				try:
                    
					requests.get(url)
                    
				except requests.ConnectionError:
					pass
				else:
					print("(+) Subdomain: " + url)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()