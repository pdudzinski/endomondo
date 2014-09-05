<%inherit file="base.mako" />

<section class="top-info bg-color3">
You trained <span class="color5 text-higher">${workouts.count()}</span> times,
ran <span class="color5 text-higher">${workouts.overall_distance()}</span> km, 
which took you 
<span class="color5 text-higher">
    %if workouts.splitted_duration()['days'] > 0:
        ${workouts.splitted_duration()['days']} days
    %endif
    %if workouts.splitted_duration()['hours'] > 0:
        ${workouts.splitted_duration()['hours']} h
    %endif
    ${workouts.splitted_duration()['minutes']} min
</span>.
Your average speed is <span class="color5 text-higher">${workouts.average_speed()}</span> km/h
</section>

<section class="table-info bg-color2">
    Kilometers run per month since the beginning (${len(km_by_yearmonth)} months of trainings)
</section>

<table class="chart-table">
<tr>
%for w in km_by_yearmonth:
    <td>
        <div class="bg-color1 pole" style="height:${int(int(w[1][0])*workouts._km_by_yearmonth_chart_factor)}px;">
            ${int(round(w[1][0]))}km
        </div>
    </td>
%endfor
</tr>
<tr>
%for w in km_by_yearmonth:
    <td style="border-bottom:2px solid #485953; line-height:16px; padding:5px 0px;">
        <strong style="font-size:1.3em;">
            ${str(w[0])[4:6]} / ${str(w[0])[:4]}<br />
            <span style="font-size:0.8em;">${w[1][1]} runs</span>
        </strong>
    </td>
%endfor
<tr>
</table>

<section class="table-info bg-color2">
    Average pace per month (min/km)
</section>


<table class="chart-table">
<tr>
%for w in km_by_yearmonth:
    <td>
        <div class="bg-color1 pole" style="height:${int(int(w[1][3])*10*workouts._pace_by_yearmonth_chart_factor)}px; line-height:20px; position:relative;">
            <div style="padding-top:10px;">
            ${workouts.fractal_handle(w[1][3])} <span style="font-size:0.8em;">/km</span><br />
            <span style="font-size:0.7em;">${'%.1f'%(w[1][2])} <span style="font-size:0.8em;">km/h</span></span><br />
            </div>
            <div class="chart-dot bg-color5" style="bottom:${float(w[1][2])*5*workouts._avg_by_yearmonth_chart_factor}px;"></div>
        </div>
    </td>
%endfor
</tr>
<tr>
%for w in km_by_yearmonth:
    <td style="border-bottom:2px solid #485953; line-height:16px; padding:5px 0px;">
        <strong style="font-size:1.3em;">
            ${str(w[0])[4:6]} / ${str(w[0])[:4]}
        </strong>
    </td>
%endfor
<tr>
</table>

<section class="table-info bg-color2">
    Average speed per month (km/h)
</section>


<table class="chart-table">
<tr>
%for w in km_by_yearmonth:
    <td>
        <div class="bg-color1 pole" style="height:${int(int(w[1][2])*10*workouts._avg_by_yearmonth_chart_factor)}px; line-height:20px; position:relative;">
            <div style="padding-top:10px;">
            ${'%.1f'%(w[1][2])} <span style="font-size:0.8em;">km/h</span><br />
            <span style="font-size:0.7em;">${workouts.fractal_handle(w[1][3])} <span style="font-size:0.8em;">/km</span></span><br />
            </div>
            <div class="chart-dot bg-color5" style="bottom:${float(w[1][3])*5*workouts._pace_by_yearmonth_chart_factor}px;"></div>
        </div>
    </td>
%endfor
</tr>
<tr>
%for w in km_by_yearmonth:
    <td style="border-bottom:2px solid #485953; line-height:16px; padding:5px 0px;">
        <strong style="font-size:1.3em;">
            ${str(w[0])[4:6]} / ${str(w[0])[:4]}
        </strong>
    </td>
%endfor
<tr>
</table>
<br />

<section class="top-info bg-color3">
Run Log:
<span class="color5 text-higher">${workouts.how_many_Xk(5)}</span> 5km runs,
<span class="color5 text-higher">${workouts.how_many_Xk(7)}</span> 7km runs,
<span class="color5 text-higher">${workouts.how_many_Xk(10)}</span> 10km runs,
<span class="color5 text-higher">${workouts.how_many_Xk(14)}</span> 14km runs,
<span class="color5 text-higher">${workouts.how_many_Xk(21)}</span> half-marathons
</section>


<%def name="fastest(n, collection)" filter="trim">
    <section class="table-info bg-color2">
        Fastes ${n} km per month
    </section>

    <table class="chart-table">
    <tr>
    %for w in collection:
        <td>
            <div class="bg-color1 pole"
                 style="height:${int(int(w[1][0])*getattr(workouts, '_max_speed_factor%s' % (n)))}px;line-height:20px; position:relative;">
                <div style="padding-top:10px;">
                    ${w[1][1]}
                </div>
            </div>
        </td>
    %endfor
    </tr>
    <tr>
    %for w in collection:
        <td style="border-bottom:2px solid #485953; line-height:16px; padding:5px 0px;">
            <strong style="font-size:1.3em;">
                ${str(w[0])[4:6]} / ${str(w[0])[:4]}
            </strong>
        </td>
    %endfor
    <tr>
    </table>
</%def>

${fastest(5, best5)}
${fastest(7, best7)}
${fastest(10, best10)}
${fastest(14, best14)}

<br />
<section class="top-info bg-color3">
Best distances based on average in whole run:<br />
5km <span class="color5 text-higher">${workouts._min_speed5}</span>
<span class="smaller">on ${workouts._min_speed_stats_run5.start_time.strftime('%d-%m-%Y')}</span>
<span class="smaller">with pace <span class="color5 text-higher">${workouts.fractal_handle(workouts._min_speed_stats_run5.pace)} min/km</span></span><br />

7km <span class="color5 text-higher">${workouts._min_speed7}</span>
<span class="smaller">on ${workouts._min_speed_stats_run7.start_time.strftime('%d-%m-%Y')}</span>
<span class="smaller">with pace <span class="color5 text-higher">${workouts.fractal_handle(workouts._min_speed_stats_run7.pace)} min/km</span></span><br />

10km <span class="color5 text-higher">${workouts._min_speed10}</span>
<span class="smaller">on ${workouts._min_speed_stats_run10.start_time.strftime('%d-%m-%Y')}</span>
<span class="smaller">with pace <span class="color5 text-higher">${workouts.fractal_handle(workouts._min_speed_stats_run10.pace)} min/km</span></span><br />

14km <span class="color5 text-higher">${workouts._min_speed14}</span>
<span class="smaller">on ${workouts._min_speed_stats_run14.start_time.strftime('%d-%m-%Y')}</span>
<span class="smaller">with pace <span class="color5 text-higher">${workouts.fractal_handle(workouts._min_speed_stats_run14.pace)} min/km</span></span><br />
</section>

<br /><br />
