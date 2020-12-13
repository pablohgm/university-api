from graphene import relay, ObjectType, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Course
from .models import Student


class CourseNode(DjangoObjectType):
    class Meta:
        model = Course
        filter_fields = ['name', 'code', 'credit', 'type']
        interfaces = (relay.Node,)


class StudentNode(DjangoObjectType):
    class Meta:
        model = Student
        filter_fields = [
            'first_name',
            'last_name',
            'student_id',
            'middle_name',
            'email',
            'phone',
            'address',
            'birth_date']
        interfaces = (relay.Node,)


class Query(ObjectType):
    courses = DjangoFilterConnectionField(CourseNode)
    course = relay.Node.Field(CourseNode)
    students = DjangoFilterConnectionField(StudentNode)
    student = relay.Node.Field(StudentNode)
