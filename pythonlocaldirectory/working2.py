<%
from cgi import escape
from urllib import unquote
%>
<html><head>
<style type="text/css">
td {padding:0.2em 0.5em;border:1px solid black;}
table {border-collapse:collapse;}
</style>
</head><body>
<table cellspacing="0" cellpadding="0">
<%
attribs = ''

# Loop over the attributes of the Request object
for attrib in dir(req):
   #
%>
<tr>args

<%-- The attribute name --%>
<td><%= attrib %></td>

<%-- The attribute value --%>
<td><%= escape(unquote(str(req.__getattribute__(attrib)))) %></td>

</tr>
<%
#
%>
</table></body></html>

??