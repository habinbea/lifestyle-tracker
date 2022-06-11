from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Info
from . import db
import json
from datetime import timedelta, datetime

views = Blueprint('views', __name__)

@views.route('/input', methods=['GET', 'POST'])
@login_required
def input():
    if request.method == 'POST':
        date = request.form.get('date')
        sleep_start = request.form.get('sleep_start')
        sleep_end = request.form.get('sleep_end')
        weight = request.form.get('weight')
        exercise = request.form.get('exercise')
        breakfast = request.form.get('breakfast')
        lunch = request.form.get('lunch')
        dinner = request.form.get('dinner')

        date = datetime.strptime(date, "%Y-%m-%d").date()
        sleep_start = datetime.strptime(sleep_start, "%H:%M").time()
        sleep_end = datetime.strptime(sleep_end, "%H:%M").time()
        sleep_start_delta = timedelta(hours=sleep_start.hour, minutes=sleep_start.minute, seconds=sleep_start.second)
        sleep_end_delta = timedelta(hours=sleep_end.hour, minutes=sleep_end.minute, seconds=sleep_end.second)
        sleep_duration = sleep_end_delta - sleep_start_delta
        if sleep_duration.days < 0:
            sleep_duration += timedelta(days=1)

        if exercise == "did_exercise":
            exercise = True
        else:
            exercise = False
        if breakfast == "ate_breakfast":
            breakfast = True
        else:
            breakfast = False
        if lunch == "ate_lunch":
            lunch = True
        else:
            lunch = False
        if dinner == "ate_dinner":
            dinner = True
        else:
            dinner = False

        info = Info.query.filter_by(user_id=current_user.id, date=date).first()
        if info:
            flash('Info for the day already exists.', category='error')
        else:
            new_info = Info(date=date, sleep_start=sleep_start, sleep_end=sleep_end, sleep_duration=sleep_duration, weight=weight,
            exercise=exercise, breakfast=breakfast, lunch=lunch, dinner=dinner, user_id=current_user.id)
            db.session.add(new_info)
            db.session.commit()
            flash('New data submitted!', category='success')
            return redirect(url_for('views.output'))

    return render_template("input.html", user=current_user)

@views.route('/output', methods=['GET', 'POST'])
@login_required
def output():
    sum_sleep_duration = timedelta()
    sum_weight = 0.0
    total_exercise = 0
    total_breakfast = 0
    total_lunch = 0
    total_dinner = 0
    for info in current_user.info:
        sum_sleep_duration += info.sleep_duration
        sum_weight += info.weight
        total_exercise += info.exercise
        total_breakfast += info.breakfast
        total_lunch += info.lunch
        total_dinner += info.dinner
    if len(current_user.info) > 0:
        mean_sleep_duration = sum_sleep_duration/len(current_user.info)
        mean_weight = sum_weight/len(current_user.info)
        total_skip_exercise = len(current_user.info) - total_exercise
        total_skip_breakfast = len(current_user.info) - total_breakfast
        total_skip_lunch = len(current_user.info) - total_lunch
        total_skip_dinner = len(current_user.info) - total_dinner
    else:
        mean_sleep_duration = 0
        mean_weight = 0
        total_skip_exercise = 0
        total_skip_breakfast = 0
        total_skip_lunch = 0
        total_skip_dinner = 0

    oldest_info = Info.query.filter_by(user_id=current_user.id).order_by('date').first()

    dates = []
    sleep_starts = []
    sleep_durations = []
    weights = []
    for info in current_user.info:
        date = datetime(year=info.date.year, month=info.date.month, day=info.date.day)
        dates.append(datetime.strftime(date, "%Y-%m-%d %H:%M:%S"))
        sleep_duration_str = str(info.sleep_duration)
        if len(sleep_duration_str) == 8:
            sleep_duration_hour = int(sleep_duration_str[:2])
            sleep_duration_minute = int(sleep_duration_str[3:5])
        else:
            sleep_duration_hour = int(sleep_duration_str[:1])
            sleep_duration_minute = int(sleep_duration_str[2:4])
        sleep_duration_minute = sleep_duration_minute/60
        sleep_duration = sleep_duration_hour + sleep_duration_minute
        sleep_durations.append(sleep_duration)
        weights.append(info.weight)

    return render_template("output.html", user=current_user, mean_sleep_duration=mean_sleep_duration, mean_weight=mean_weight,
        total_exercise=total_exercise, total_breakfast=total_breakfast, total_lunch=total_lunch,
        total_dinner=total_dinner, number_days=len(current_user.info), dates=dates, sleep_durations=sleep_durations, weights=weights,
        total_skip_exercise=total_skip_exercise, total_skip_breakfast=total_skip_breakfast,
        total_skip_lunch=total_skip_lunch, total_skip_dinner=total_skip_dinner)


@views.route('/delete-info', methods=['POST'])
def delete_info():
    info = json.loads(request.data)
    infoId = info['infoId']
    info = Info.query.get(infoId)
    if info:
        if info.user_id == current_user.id:
            db.session.delete(info)
            db.session.commit()

    return jsonify({})
