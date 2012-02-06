<%@ include file="header.py"%>

<% 

args = escape(unquote(str(req.__getattribute__('args'))))
qString = args.replace("amp;", "");  #why does this need to happen?
querystring = dict(item.split("=") for item in qString.split("&"))

id = querystring['id']
what = querystring['what']
where = querystring['where']

%>
<div class="span14">

	<div class="page-header">
		<h2>Details</h2>
	</div>

<ul class="breadcrumb">\
	<li><a href="/index.py"><%= where%></a> / </li>
	<%
if len(what) > 0:
	  %>
	  <li><a href="/search.py?what=<%= what%>"><%= what%></a></li>
</ul>

<%
phone=''
customer_only=''
placement = ''
all_results=''
review_count=''
i=''
format='json'
callback=''
id_type='cs'

places = citygridplaces()
placesdetail = places.placesdetail(id,id_type,phone,customer_only,all_results,review_count,placement,format,callback,i,publishercode)

detail = json.loads(placesdetail)
response = dict(json.loads(json.dumps(detail)))
locations = response[u'locations'][0]

public_id = locations[u'public_id']
infousa_id = locations[u'infousa_id']
reference_id = locations[u'reference_id']
impression_id = locations[u'impression_id']
name = locations[u'name']
display_ad = locations[u'display_ad']
teaser = locations[u'teaser']
business_operation_status = locations[u'business_operation_status']
address = locations[u'address']
years_in_business = locations[u'years_in_business']
last_update_time = locations[u'last_update_time']


addressblock = locations[u'address']
address = dict(json.loads(json.dumps(addressblock)))
city = address[u'city']
state = address[u'state']
street = address[u'street']
postal_code = address[u'postal_code']

cross_street = address[u'cross_street']
latitude = address[u'latitude']
longitude = address[u'longitude']

contact_info = locations[u'contact_info']
display_phone = contact_info[u'display_phone']
display_url = contact_info[u'display_url']
%>

<address>
	<strong><%= name %></strong><br />
	<%= street %><br />
	<%= city %>, <%= state %> <%= postal_code %><br />
	<abbr title="Phone">P:</abbr> <%= display_phone %>
</address>	


<%
# 630 x 100 Ad Slot
adid = "4"
publisher = "citysearch"

%>
<div id="detail_ad_slot_<%= adid %>" align="center"></div>
<%
returnad = citygridadvertising()
response = returnad.displaywebad630x100(adid,publisher,what,where)						
%>
<%= response %>

<%
customer_content = locations[u'customer_content']
%>
<p><strong>Atribution:</strong></p>
<strong>Attribution Source:</strong> <%= customer_content[u'customer_message'][u'attribution_source'] %><br />
<strong>Attribution Text:</strong> <%= customer_content[u'customer_message'][u'attribution_text'] %><br />
<strong>Attribution Value:</strong> <%= customer_content[u'customer_message'][u'value'] %><br />
<strong>Customer URL:</strong> <%= customer_content[u'customer_message_url'] %><br /><br />

<%
offers = locations[u'offers']
if len(offers) > 0:
	%>
<p><strong>Offers:</strong></p>
<ul>	
<%
for offer in offers:	
	%>
	<li><%= offer %></a></li>
	<%
#
%>
</ul>

<%
categories = locations[u'categories']
if len(categories) > 0:
	%>
<p><strong>Categories:</strong></p>
<ul>	
<%
for c in categories:	
	%>
	<li><%= c[u'name'] %></a></li>
	<%
#
%>
</ul>

<%
attributes = locations[u'attributes']
if len(attributes) > 0:
	%>
<p><strong>Attributes:</strong></p>
<ul>	
<%
for attribute in attributes:	
	
	attribute_id = attribute[u'attribute_id']
	name = attribute[u'name']
	value = attribute[u'value']
	
%>
<li><%= name %> - <%= value %></a></li>
<%
#
%>
</ul>

<%
tips = locations[u'tips']
if len(tips) > 0:
	%>	
<p><strong>Tips:</strong></p>
<ul>	
<%
for tip in tips:	

	tip_name = tip[u'tip_name']
	tip_text = tip[u'tip_text']
	
%>
<li><%= tip_name %> - <%= tip_text %></a></li>
<%
#
%>
</ul>

<%
images = locations[u'images']
if len(images) > 0:
	%>
<p><strong>Images:</strong></p>
<ul>	
<%
for image in images:	
	
	type = image[u'type']
	height = image[u'height']
	width = image[u'width']
	image_url = image[u'image_url']
	primary = image[u'primary']
	
	attribution_source = image[u'attribution_source']
	attribution_logo = image[u'attribution_logo']
	attribution_text = image[u'attribution_text']
	
%>
<li><%= image_url %></a></li>
<%
#
%>
</ul>

<%
editorials = locations[u'editorials']
if len(editorials) > 0:
%>
<p><strong>Editorials:</strong></p>
<ul>
<%
for editorial in editorials:	
	
	attribution_source = editorial[u'attribution_source']
	attribution_logo = editorial[u'attribution_logo']
	editorial_review = editorial[u'editorial_review']
	editorial_id = editorial[u'editorial_id']
	editorial_url = editorial[u'editorial_url']
	editorial_title = editorial[u'editorial_title']
	editorial_author = editorial[u'editorial_author']
	
%>
<li><%= editorial_title %> - <%= editorial_review %></a></li>
<%
#
%>
</ul>

<%
review_info = locations[u'review_info']
reviews = review_info[u'reviews']
if len(reviews) > 0:
%>
<p><strong>Reviews:</strong></p>
<ul>	
<%	
total_user_reviews = review_info[u'total_user_reviews']
total_user_reviews_shown = review_info[u'total_user_reviews_shown']
overall_review_rating = review_info[u'overall_review_rating']

for review in reviews:	
	
	attribution_source = review['attribution_source']
	attribution_logo = review['attribution_logo']
	attribution_text = review['attribution_text']
	review_id = review['review_id']
	review_url = review['review_url']
	review_title = review['review_title']
	review_author = review['review_author']
	review_text = review['review_text']
	
%>
<li><%= review_title %></a></li>
<%
#
%>
</ul>

<%
# 630 x 100 Ad Slot
adid = "5"
publisher = "citysearch"

%>
<div id="detail_ad_slot_<%= adid %>" align="center"></div>
<%
returnad = citygridadvertising()
response = returnad.displaywebad630x100(adid,publisher,what,where)						
%>
<%= response %>

<br />

     
	<br />
	<p align="center"><a href="/search.py?what=<%= what %>" class="btn large primary">Return to Main Page</a></p>
	
	<div>
		<!---CityGrid Attribution-->
		<p align="right">
			<span style="margin-left: 5px"><strong>Powered by</strong>&nbsp&nbsp&nbsp</span><br />
			<img src="http://kinlane-productions.s3.amazonaws.com/citygrid/citygrid_logo.jpg" width="150" />
		</p>
	</div>	
	 
</div>
   
<%@ include file="footer.py"%>  