# -*- coding: utf-8 -*-
import time
import math

class WorkoutStatistics(object):
    
    POLE_CHART_HEIGHT = 200
    
    def __init__(self, workouts):
        self.workouts = workouts
        
    def _seconds_to_hms(self, seconds):
        return time.strftime('%H:%M:%S', time.gmtime(seconds))
    
    def _seconds_to_dhms_separate_vars(self, seconds):
        tm = time.gmtime(seconds)
        return {
            'days': int(time.strftime('%d', tm))-1,
            'hours': int(time.strftime('%H', tm)),
            'minutes': int(time.strftime('%M', tm)),
            'seconds': int(time.strftime('%S', tm)),
        }
        
        
    def count(self):
        return len(self.workouts)

    def overall_distance(self):
        return sum([x.distance for x in self.workouts])
    
    def overall_duration(self):
        return sum([x.duration for x in self.workouts])
    
    def splitted_duration(self):
        duration = self.overall_duration()
        return self._seconds_to_dhms_separate_vars(duration)
                        
    def average_speed(self):
        duration = sum([x.duration for x in self.workouts])
        distance = self.overall_distance()
        
        duration_in_hours = round(float(duration)/60/60)
        
        return "%.2f" % (float(distance)/duration_in_hours)
        
    def _get_yearmonth(self, w):
        return int("%s%s" % (w.start_time.year, "0%s"%(w.start_time.month) if int(w.start_time.month) < 10 else w.start_time.month))
        
    def duration_and_distance_by_yearmonth(self, workouts):
        struct = {}
        for w in workouts:
            yearmonth = self._get_yearmonth(w)
            if yearmonth in struct:
                struct[yearmonth] = (struct[yearmonth][0]+w.distance, struct[yearmonth][1]+1, struct[yearmonth][2]+w.duration)
            else:
                struct[yearmonth] = (w.distance, 1, w.duration)
                                
        struct = sorted(struct.iteritems())
        return struct
    
    def km_by_yearmonth(self):
        struct = self.duration_and_distance_by_yearmonth(self.workouts)
        #normalizing duration to avg pace
        aux_struct = []
        for w in struct:
            duration_in_hours = w[1][2]/60/60
            duration_in_minutes = w[1][2]/60
            aux_struct.append((w[0], (w[1][0], w[1][1], w[1][0]/duration_in_hours, duration_in_minutes/w[1][0])))
        struct = aux_struct
        
        self._max_km = int(max([x[1][0] for x in struct]))
        self._max_avg = max([x[1][2]*10 for x in struct])
        self._max_pace = max([x[1][3]*10 for x in struct])
        self._km_by_yearmonth_chart_factor = self.POLE_CHART_HEIGHT / float(self._max_km)
        self._avg_by_yearmonth_chart_factor = self.POLE_CHART_HEIGHT / float(self._max_avg)
        self._pace_by_yearmonth_chart_factor = self.POLE_CHART_HEIGHT / float(self._max_pace)
        return struct
        
    def get_run_by_distance(self, distance):
        runs = []
        for w in self.workouts:
            if w.distance > distance - 1 and w.distance < distance + 1:
                runs.append(w)
        return runs

    def how_many_Xk(self, n):
        return len(self.get_run_by_distance(n))
        
    def _convert_kmh_to_hms(self, n):
        return float(n)/3600
    
    def bests_by_yearmonth_and_distance(self, distance):
        runs = self.get_run_by_distance(distance)
        struct = {}
        max_speed = 0
        min_speed = int(round(1/self._convert_kmh_to_hms(runs[0].avg_speed)*distance))
        min_speed_stats_run = runs[0]
        for r in runs:
            yearmonth = self._get_yearmonth(r)
            avg_speed = int(round(1/self._convert_kmh_to_hms(r.avg_speed)*distance))
            if yearmonth not in struct:
                struct[yearmonth] = avg_speed
            if struct[yearmonth] > avg_speed:
                struct[yearmonth] = avg_speed
            if avg_speed > max_speed:
                max_speed = avg_speed
            if avg_speed < min_speed:
                min_speed = avg_speed
                min_speed_stats_run = r
        
        aux = sorted(struct.iteritems())
        struct = []
        for s in aux:
            struct.append((s[0], (s[1], self._seconds_to_hms(s[1]))))
        
        setattr(
            self,
            '_max_speed_factor%s' % (distance),
            self.POLE_CHART_HEIGHT / float(max_speed))
            
        setattr(
            self,
            '_min_speed%s' % (distance),
            self._seconds_to_hms(min_speed))
        
        setattr(
            self,
            '_min_speed_stats_run%s' % (distance),
            min_speed_stats_run)
                        
        return struct
    
    def fractal_handle(self, fractal):
        f, b = math.modf(fractal)
        seconds = int(f*60)
        minutes = f
        
        if seconds < 10:
            return "%s:0%s" % (int(b), int(f*60))
        else:
            return "%s:%s" % (int(b), int(f*60))
                
        
        
