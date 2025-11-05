from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Ahmad'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, le=4, default=2.5, description="CGPA must be between 0 and 4")

new_student = {'name': 'Ali', 'age': 29, 'email': 'ali@gmail.com'}

student = Student(**new_student)

print(student)

student_dict = dict(student)
print(student_dict)

student_json = student.model_dump_json()
print(student_json)