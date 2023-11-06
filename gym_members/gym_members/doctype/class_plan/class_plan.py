# Copyright (c) 2023, Patrick Eissler (ALYF GmbH) and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime, timedelta


class ClassPlan(Document):
	pass

def create_classes(doc, event):
	if doc.is_initialised == 0:
		start_date = doc.start_date
		start_date = date_object = datetime.strptime(start_date, '%Y-%m-%d').date()
		weekday_start = start_date.weekday() + 1

		first_7_days = {}
		for i in range(7):
			if weekday_start == 7:
				weekday_start = 0
			first_7_days[weekday_start] = start_date
			weekday_start += 1
			start_date += timedelta(days=1)

		class_dates = []
		day_to_int = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}

		for row in doc.timetable:
			day = row.day
			class_dates.append(first_7_days[day_to_int[day]])
		
		end_of_planning_period = start_date + timedelta(days=90)
		start_of_month = datetime(end_of_planning_period.year, end_of_planning_period.month, 1).date()		
		if doc.end_date:
			end_date = date_object = datetime.strptime(doc.end_date, '%Y-%m-%d').date()
			if end_date > end_of_planning_period:
				end_of_planning_period = start_of_month - timedelta(days=1)
			else:
				end_of_planning_period = end_date

		classes = []

		for i in range(len(class_dates)):
			start_time = doc.timetable[i].start
			end_time = doc.timetable[i].end
			class_info = {
				"date": class_dates[i],
				"start_time": start_time,
				"end_time": end_time
			}
			classes.append(class_info)

		additional_dates = []
		for d in classes:
			initial_date = d["date"]
			new_date = initial_date + timedelta(days=7)
			while new_date <= end_of_planning_period:
				additional_dates.append({"date": new_date, "start_time": d["start_time"], "end_time": d["end_time"]})
				new_date = new_date + timedelta(days=7)

		for d in additional_dates:
			classes.append(d)

		for d in classes:
			gym_class = frappe.new_doc("Gym Class")
			gym_class.class_name = doc.name
			gym_class.trainer = doc.default_trainer
			gym_class.capacity = doc.capacity
			gym_class.start_time = d["start_time"]
			gym_class.end_time = d["end_time"]
			gym_class.date = d["date"]
			gym_class.location = doc.location
			gym_class.save()
			frappe.db.commit()
		doc.is_initialised = 1

