#!/usr/bin/env python
# coding: utf-8

# In[8]:


from selenium import webdriver


# In[4]:


browser = webdriver.Chrome()
browser.get("https://www.seloger.com")


# In[5]:


button = browser.find_element_by_css_selector(".c-quest-actions-search")
button.click()


# In[10]:


from selenium.webdriver.common.keys import Keys

inp = browser.find_element_by_css_selector("#agatha_autocomplete_autocompleteUI__input")
inp.send_keys("Toulouse")
inp.send_keys(Keys.ENTER)

button = browser.find_element_by_css_selector(".c-quest-actions-search")
button.click()


# In[13]:


prices = browser.find_elements_by_css_selector(".Price__Label-sc-1g9fitq-1.jGOFou")


# In[19]:


liste = [ elem.text for elem in prices]
liste


# In[20]:


from time import sleep

sleep(2)


# In[ ]:


ma_liste = ['9 900 000 €',
 '6 300 000 €',
 '1 600 000 €',
 '1 790 000 €',
 '1 988 000 €',
 '2 470 000 €',
 '1 080 000 €',
 '619 000 €',
 '630 000 €',
 '620 000 €',
 '825 000 €',
 '415 000 €',
 '1 670 000 €',
 '1 750 000 €',
 '2 290 000 €',
 '1 799 000 €',
 '3 120 000 €',
 'bouquet\n294 660 €',
 '1 750 000 €',
 'de 3M à 10M €',
 '1 995 000 €',
 '425 000 €',
 '542 000 €',
 '1 600 000 €',
 '850 000 €']

