<%@ include file="header.py"%>
		
<div class="span14">

  	<div class="row">

	<table cellpadding="5" cellspacing="5" with="500" align="center" class="zebra-striped">
		<tbody>

<%	
type='' 
where = Site_Where
page = '1'
rpp = '20'
sort = 'dist'
rformat='json'
placement=''
hasoffers=''
histograms=''
i=''
			
searchwhere = citygridplaces()
response = searchwhere.srchplaceswhere(what,type,where,page,rpp,sort,rformat,placement,hasoffers,histograms,i,publishercode)

pResponse = json.loads(response)

data = dict(json.loads(json.dumps(pResponse)))
results = dict(json.loads(json.dumps(data[u'results'])))

for locations in results[u'locations']:
	location = dict(json.loads(json.dumps(locations)))
	
	rating = location[u'rating']
	
	featured = location[u'featured']
	public_id = location[u'public_id']
	name = location[u'name']
	
	addressblock = location[u'address']
	address = dict(json.loads(json.dumps(addressblock)))
	city = address[u'city']
	state = address[u'state']
	street = address[u'street']
	postal_code = address[u'postal_code']
	
	neighborhood = location[u'neighborhood']
	latitude = location[u'latitude']
	longitude = location[u'longitude']
	distance = location[u'distance']
	image = location[u'image']
	phone_number = location[u'phone_number']
	fax_number = location[u'fax_number']
	rating = location[u'rating']
	tagline = location[u'tagline']
	profile = location[u'profile']
	website = location[u'website']
	has_video = location[u'has_video']
	has_offers = location[u'has_offers']
	offers = location[u'offers']
	
	sample_categories = location[u'sample_categories']
	impression_id = location[u'impression_id']
	expansion  = location[u'expansion']	
	
%>
<tr>
	<td align="left">
        <address>
            <strong><%= name %></strong><br />
            <%= street %><br />
            <%= city %>, <%= state %><br />
         </address>							
	</td>
	<td align="left" valign="middle" width="7%" style="padding-top: 40px;">
		<a href="detail.py?id=whatisthis&what=<%= what %>&where=<%= where %>" class="btn small primary">Detail</a>
	</td>
</tr>	
<%
#
%>
<tbody>
</table>
	</div>      
		

</div>
    
<%@ include file="footer.py"%>