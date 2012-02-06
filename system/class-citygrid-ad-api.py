<%
class citygridadvertising(object):
  	 
 	def displaywebad300x250(self,adid,publisher,what,where):
 		
		returnAd = '<div id="sidebar_ad_slot_' + adid + '"></div>\r'
		returnAd += '<script type="text/javascript">\r'
		returnAd += "new CityGrid.Ads('sidebar_ad_slot_" + adid + "', {\r"
		returnAd += "    collection_id: 'web-002-300x250',\r"
		returnAd += "    publisher: '" + publisher + "',\r"
		returnAd += "    what:'" + what + "',\r"
		returnAd += "    where: '" + where + "',\r"
		returnAd += "    width: 300,\r"
		returnAd += "    height: 250\r"
		returnAd += "  })\r"
		returnAd += "</script>\r"
		
		return returnAd   
		
	def displaywebad630x100(self,adid,publisher,what,where):
		
		returnAd = '<script type="text/javascript">\r'
		returnAd += "new CityGrid.Ads('detail_ad_slot_" + adid + "', {\r"
		returnAd += "    collection_id: 'web-001-630x100',\r"
		returnAd += "    publisher: '" + publisher + "',\r"
		returnAd += "    what:'" + what + "',\r"
		returnAd += "    where: '" + where + "',\r"
		returnAd += "    width: 630,\r"
		returnAd += "    height: 100\r"
		returnAd += "  })\r"
		returnAd += "</script>\r"
		
		return returnAd  		
%>