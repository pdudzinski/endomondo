<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Sport Tracker</title>
        <!--[if IE]>
        <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
        
        
        <link href='http://fonts.googleapis.com/css?family=Amatic+SC:400,700' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="${req.static_url('tracker:static/css/style.css')}" type="text/css" media="all">
    </head>
    <body>
        ${next.body()}
    </body>
    <script type='text/javascript' src='${req.static_url('tracker:static/js/jquery-1.11.1.min.js')}'></script>
    ${self.js()}
</html>

<%def name="js()">
</%def>
