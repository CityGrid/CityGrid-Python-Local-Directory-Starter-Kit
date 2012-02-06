<%@ include file="config.py"%>
<%@ include file="../system/class-citygrid-places-api.py"%>
<%@ include file="../system/class-citygrid-ad-api.py"%>
<%
import string
import socket
import random

import json
from pprint import pprint

import urllib
import urllib2

from cgi import escape
from urllib import unquote

hostname = escape(unquote(str(req.__getattribute__('hostname'))))
uri = escape(unquote(str(req.__getattribute__('uri'))))

where = Site_Where
%>

<!DOCTYPE html>
<html lang="en">
  <head>
  
    <meta charset="utf-8">
    
    <title><%= Site_Name %></title>
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le HTML5 shim, for IE6-8 support of HTML elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

	<script type="text/javascript" src="http://static.citygridmedia.com/ads/scripts/v2/loader.js"></script>

    <link href="bootstrap.css" rel="stylesheet">
    
    <style type="text/css">
      body {
        padding-top: 60px;
      }
    </style>

    <!-- This is for the Flickr Images -->
	<style>
	.img
		{
		display: inline-block;
		position: relative;
		text-decoration: none;
		}
	.img img
		{
		border: 1px solid #cccccc;
		padding: 10px;
		}
	img:hover { border-color: #aaaaaa; }
	.img div
		{
		background: #666666;
		color: #ffffff;
		opacity: .70;
		padding: 3px 0px;
		position: absolute;
		left: 0px;
		bottom: 25px;
		text-align: center;
		width: 100%;
		}
	.img:hover div { opacity: .90; }
	</style>
    
  </head>

  <body>

    <div class="topbar">
      <div class="topbar-inner">
        <div class="container-fluid">
          <a class="brand" href="http://hyp3rl0cal.com/"><%= Site_Name %></a>
          <ul class="nav">
            <li><a href="http://hyp3rl0cal.com/">Home</a></li>
            <li><a href="http://hyp3rl0cal.com/blog/">Blog</a></li>
			<li><a href="http://phplibraries.hyp3rl0cal.com/">PHP</a></li>
			<li class="active"><a href="http://pythonlibraries.hyp3rl0cal.com/">Python</a></li>
			<li><a href="http://rubylibraries.hyp3rl0cal.com/">Ruby</a></li>
			<li><a href="http://hyp3rl0cal.com/contact.php">Contact</a></li>
          </ul>
        </div>
      </div>
    </div>

    <div class="container-fluid">
    
      <div class="sidebar">
        <div class="well">
        
			<ul>
			
<%          
json_data=open('/var/www/html/system/business-categories-datastore.txt')
data = json.load(json_data)
business = { };
for d in data:
	releases = dict(json.loads(json.dumps(d)))
	business[releases[u'Name']] = releases[u'ID']
%>
<li><a href="/search.py?what=<%= releases[u'Name'] %>"><%= releases[u'Name'] %></a></li>
<%
#

#choose a random business to show on home page
what = random.choice(business.keys())
%>

          </ul>     
          
        </div>
      </div>     
      
      <div class="content">
			
			<div class="row">  
			
			