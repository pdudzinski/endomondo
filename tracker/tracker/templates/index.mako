<%inherit file="base.mako" />

<section class="fetching">
    <span class="logo">Tracker</span><br />
    is fetching your workouts...<br /><br />
    <img src='/static/images/loader.gif' alt="Tracker is fetching your workouts..." />
</section>

<%def name="js()">
    <script>
        $(document).ready(function() {
            $.get('${request.route_path('get_workouts')}', function(data) {
                var URL = '${request.route_path('statistics')}';
                window.location = URL;
            });
        });
    </script>
</%def>
