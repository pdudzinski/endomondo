import time
import json

from pyramid.view import view_config

from tracker.lib.endomondo import MobileApi, Workout
from tracker.models.workout import Workout as DbWorkout
from tracker.models.workout_statistics import WorkoutStatistics

def _filter_runnings(workouts):
    aux = []
    for workout in workouts:
        if workout.sport == Workout.RUNNING:
            aux.append(workout)
    return aux
    
def _remove_workouts():
    DbWorkout.remove_all()
    
def _save_to_db(workout):
    d = {
        'duration': workout.duration,
        'distance': workout.distance,
        'avg_speed': workout.speed_avg,
        'name': workout.name,
        'start_time': workout.start_time,
        'endomondo_id': workout.id
    } 
    workout = DbWorkout(**d)
    

@view_config(route_name='home', renderer='tracker:templates/index.mako')
def home(request):
    return {}


@view_config(route_name='get_workouts', renderer='json')
def get_workouts(request):
    token = MobileApi().request_auth_token('dudzinski@csk.pl', 'imanzoel')
    endomondo = MobileApi(email='dudzinski@csk.pl', password='imanzoel')
    api_workouts = endomondo.get_workouts(maxResults = 100000)
    workouts = _filter_runnings(api_workouts)
    
    _remove_workouts()
    
    for workout in workouts:
        _save_to_db(workout)
        
    return {
        'result': 'ok'
    }

@view_config(route_name='statistics', renderer='tracker:templates/statistics.mako')
def statistics(request):
    workouts = WorkoutStatistics(DbWorkout.all())
    workouts.bests_by_yearmonth_and_distance(5)
    return {
        'workouts': workouts,
        'km_by_yearmonth': workouts.km_by_yearmonth(),
        'best5': workouts.bests_by_yearmonth_and_distance(5),
        'best7': workouts.bests_by_yearmonth_and_distance(7),
        'best10': workouts.bests_by_yearmonth_and_distance(10),
        'best14': workouts.bests_by_yearmonth_and_distance(14)
    }
