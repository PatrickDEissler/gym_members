from . import __version__ as app_version

app_name = "gym_members"
app_title = "Gym Members"
app_publisher = "Patrick Eissler (ALYF GmbH)"
app_description = "App for the Frappe Developer\'s Certification (Final Assignment)"
app_email = "patrick@alyf.de"
app_license = "GPL"

doc_events = {
    "Gym Member": {
        "before_insert": "gym_members.gym_members.doctype.gym_member.gym_member.full_name",
        "after_insert": "gym_members.gym_members.doctype.gym_member.gym_member.create_customer",
    },
    "Locker Assignment": {
        "before_insert": "gym_members.gym_members.doctype.locker_assignment.locker_assignment.check_locker_assignment",
        "after_insert": "gym_members.gym_members.doctype.locker_assignment.locker_assignment.new_locker_assignment",
    },
    "Gym Membership": {
        "before_insert": "gym_members.gym_members.doctype.gym_membership.gym_membership.check_existing_membership",
    },
    "Trainer Plan Subscription": {
        "before_insert": "gym_members.gym_members.doctype.trainer_plan_subscription.trainer_plan_subscription.check_existing_subscription",
        "after_save": "gym_members.gym_members.doctype.trainer_plan_subscription.trainer_plan_subscription.new_rating",
    },
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gym_members/css/gym_members.css"
# app_include_js = "/assets/gym_members/js/gym_members.js"

# include js, css files in header of web template
# web_include_css = "/assets/gym_members/css/gym_members.css"
# web_include_js = "/assets/gym_members/js/gym_members.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "gym_members/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "gym_members.utils.jinja_methods",
#	"filters": "gym_members.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "gym_members.install.before_install"
# after_install = "gym_members.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "gym_members.uninstall.before_uninstall"
# after_uninstall = "gym_members.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gym_members.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"gym_members.tasks.all"
#	],
#	"daily": [
#		"gym_members.tasks.daily"
#	],
#	"hourly": [
#		"gym_members.tasks.hourly"
#	],
#	"weekly": [
#		"gym_members.tasks.weekly"
#	],
#	"monthly": [
#		"gym_members.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "gym_members.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "gym_members.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "gym_members.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["gym_members.utils.before_request"]
# after_request = ["gym_members.utils.after_request"]

# Job Events
# ----------
# before_job = ["gym_members.utils.before_job"]
# after_job = ["gym_members.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"gym_members.auth.validate"
# ]
