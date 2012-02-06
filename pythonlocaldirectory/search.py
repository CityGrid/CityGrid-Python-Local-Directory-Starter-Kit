<%@ include file="header.py"%>

<%
what = escape(unquote(str(req.__getattribute__('args'))))
what = what.replace("amp;", "");  #why does this need to happen?
querystring = dict(item.split("=") for item in what.split("&"))

# what
try:
	what = querystring['what']
except:
	what = "Hotel"	
	
# type
try:
	type = querystring['type']
except:
	type = ""
	
# where
try:
	where = querystring['where']
except:
	where = "Eugene, OR"
	
# page
try:
	page = querystring['page']
except:
	page = "1"
	
# rpp
try:
	rpp = querystring['rpp']
except:
	rpp = ""
	
# sort 
try:
	sort = querystring['sort'] 
except:
	sort = ""
%>

<div class="span14">
	
	<div class="page-header">
		<h2>Search</h2>
	</div>
	
	<ul class="breadcrumb">
	  <li><a href="/index.py"><%= where%></a> / </li>
	  <%
if len(what) > 0:
	  %>
	  <li><a href="/search.py?what=<%= what%>"><%= what%></a></li>
	</ul>

	<table cellpadding="5" cellspacing="5" with="500" align="center" class="zebra-striped">
		<tbody>
<%
placement=''
has_offers='false'
histograms='false'
i=''
rformat='json'

searchwhere = citygridplaces()
response = searchwhere.srchplaceswhere(what,type,where,page,rpp,sort,rformat,placement,has_offers,histograms,i,publishercode)

pResponse = json.loads(response)

data = dict(json.loads(json.dumps(pResponse)))
results = dict(json.loads(json.dumps(data[u'results'])))

for locations in results[u'locations']:
	
	location = dict(json.loads(json.dumps(locations)))

	rating = location[u'rating']
	
	featured = location[u'featured']
	public_id = location[u'public_id']
	id = location[u'id']
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
		<a href="detail.py?id=<%= id %>&what=<%= what %>&where=<%= where %>" class="btn small primary">Detail</a>
	</td>
</tr>	
<%
#
%>
<tbody>
</table>
	 
	<div>
		<!---CityGrid Attribution-->
		<p align="right">
			<span style="margin-left: 5px"><strong>Powered by</strong>&nbsp&nbsp&nbsp</span><br />
			<img src="http://kinlane-productions.s3.amazonaws.com/citygrid/citygrid_logo.jpg" width="150" />
		</p>
	</div>
	
	
</div>
  
<%@ include file="footer.py"%>  