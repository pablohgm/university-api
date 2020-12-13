from django.core.exceptions import ValidationError
from django.test import TestCase
from api.models import Student


class StudentTestCase(TestCase):

    def test_validate_birth_date(self):
        """Should return a date validation error"""

        with self.assertRaises(ValidationError):
            Student(
                first_name="name",
                last_name="lastName",
                middle_name="middleName",
                student_id="studentId",
                email="test@test.com",
                phone="000000",
                birth_date="2060/01/01",
                address="address"
            ).save()