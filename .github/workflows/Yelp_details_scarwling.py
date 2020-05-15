from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
driver = webdriver.Chrome(ChromeDriverManager().install())

Name=[] 
review=[]
address=[]
cattagory = []

#https://www.yelp.com/search?find_desc=Small%20Businesses&find_loc=Newark%2C%20CA%2094560	
#https://www.yelp.com/search?find_desc=Small%20Businesses&find_loc=Newark%2C%20CA%2094560&start=10
#https://www.yelp.com/search?find_desc=Small%20Businesses&find_loc=Newark%2C%20CA%2094560&start=20

no_of_pages_toscrowl = int(input('Enter the no of pages need to be scrowled :  '))
#no_of_pages_toscrowl=1 
for i in range(10,(no_of_pages_toscrowl+1)*10,10):
	try:
		driver.get("https://www.yelp.com/search?find_desc=Small%20Businesses&find_loc=Newark%2C%20CA%2094560&start="+ str(i))
		content = driver.page_source
		soup = BeautifulSoup(content,features="lxml")

		for a in soup.findAll('li', attrs={'class':'lemon--li__373c0__1r9wz border-color--default__373c0__3-ifU'}):
			name=a.find('a',href=True,attrs={'class':"lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE"})

			pno=a.find(attrs={'class':'lemon--span__373c0__3997G text__373c0__2Kxyz reviewCount__373c0__2r4xT text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-'})

			add=a.find(attrs={'class':'lemon--span__373c0__3997G raw__373c0__3rcx7'})

			catt=a.find(attrs={'class':'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--default__373c0__7tls6'})


			if name !=None:
				#print('hotel name is : ',name.text)
				Name.append(name.text)
			else:Name.append(np.nan)

			if name !=None:
				review.append(pno.text)
			else:review.append(np.nan)
			if add !=None:
				address.append(add.text)
			else:address.append(np.nan)
			if catt !=None:	
				cattagory.append(catt.text)
			else:cattagory.append(np.nan)
			
	except :
		print('some error occured.!')
		print('1) try to chenge the number of pages to scrowl "preffered number is 4"')
		print('2) check your internet connection')
		print('3) run the script agin')
		print('4) close all current chrome tabs')
		pass

index=[]
for i in range(1,len(Name)+1):index.append(i)


df = pd.DataFrame({'index':index, 'Hotel Name':Name ,'Catogory':cattagory, 'number of reviews' :review,'address':address}) 
df.to_csv('new_hotels.csv', index=False, encoding='utf-8')

