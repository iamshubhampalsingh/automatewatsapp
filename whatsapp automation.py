#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import uiautomator2 as u2
import time
d=u2.connect('66be464c')
d.unlock()
d.press('home')
time.sleep(2)
d.app_start('com.whatsapp')
time.sleep(2)
d(className="android.widget.TextView",resourceId="com.whatsapp:id/conversations_row_contact_name",text="Flat discussion").click()
time.sleep(2)
d.app_stop('com.whatsapp')


# In[ ]:




