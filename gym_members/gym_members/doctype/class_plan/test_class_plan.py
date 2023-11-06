# Copyright (c) 2023, Patrick Eissler (ALYF GmbH) and Contributors
# See license.txt

# import frappe
from frappe.tests.utils import FrappeTestCase

import frappe
import unittest

class TestClassPlan(unittest.TestCase):
    def setUp(self):
        # Create a new test document for Class Plan
        self.class_plan = frappe.new_doc("Class Plan")
        self.class_plan.class_name = "Test Class"
        self.class_plan.location = "Gym Area"
        self.class_plan.default_trainer = "Gym Trainer"
        self.class_plan.capacity = 10
        self.class_plan.start_date = "2023-08-01"
        self.class_plan.end_date = "2023-08-31"
        self.class_plan.single_price = 100.00
        self.class_plan.insert()

    def tearDown(self):
        # Clean up the test document after the test case is executed
        frappe.delete_doc("Class Plan", self.class_plan.name)

    def test_class_plan_creation(self):
        # Check if the Class Plan document was created successfully
        self.assertIsNotNone(self.class_plan.name, "Class Plan document was not created.")

    def test_class_name_required(self):
        # Try creating a Class Plan without the required class_name
        invalid_class_plan = frappe.new_doc("Class Plan")
        invalid_class_plan.location = "Gym Area"
        invalid_class_plan.capacity = 5
        invalid_class_plan.start_date = "2023-08-01"
        invalid_class_plan.end_date = "2023-08-31"
        invalid_class_plan.single_price = 50.00

        with self.assertRaises(frappe.exceptions.ValidationError):
            invalid_class_plan.insert()

    def test_capacity_positive_integer(self):
        # Try setting a negative capacity value for Class Plan
        self.class_plan.capacity = -5

        with self.assertRaises(frappe.exceptions.ValidationError):
            self.class_plan.save()

    def test_start_date_before_end_date(self):
        # Try setting a start date after the end date for Class Plan
        self.class_plan.start_date = "2023-09-01"

        with self.assertRaises(frappe.exceptions.ValidationError):
            self.class_plan.save()

    def test_default_trainer_link_validity(self):
        # Try setting an invalid default_trainer link for Class Plan
        self.class_plan.default_trainer = "Invalid Trainer"

        with self.assertRaises(frappe.exceptions.ValidationError):
            self.class_plan.save()

    def test_single_price_required(self):
        # Try creating a Class Plan without the required single_price
        invalid_class_plan = frappe.new_doc("Class Plan")
        invalid_class_plan.class_name = "Test Class 2"
        invalid_class_plan.location = "Gym Area"
        invalid_class_plan.capacity = 5
        invalid_class_plan.start_date = "2023-08-01"
        invalid_class_plan.end_date = "2023-08-31"

        with self.assertRaises(frappe.exceptions.ValidationError):
            invalid_class_plan.insert()

    def test_valid_location_options(self):
        # Try setting an invalid location option for Class Plan
        self.class_plan.location = "Invalid Location"

        with self.assertRaises(frappe.exceptions.ValidationError):
            self.class_plan.save()

if __name__ == '__main__':
    unittest.main()

