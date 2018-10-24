from django.test import TestCase
from sample_app.models import Dog
# Create your tests here.

class TestDogModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods")
        Dog.objects.create(NAME='Jacky', BREED='doberman', AGE=4, SEX='M')

    def test_name_label(self):
        dog = Dog.objects.get(id=1)
        name = dog._meta.get_field('NAME').verbose_name
        print('Test Name Lable: Test if the lable NAME is correctly labeled')
        self.assertEqual(name, 'NAME')

    def test_object_name_is_dog_name_comma_breed(self):
        dog = Dog.objects.get(id=1)
        expected_object_name = f'{dog.NAME}, {dog.BREED}'
        print('Test Object Name: Test if the object name == dog name, dog breed')
        self.assertEquals(expected_object_name, str(dog))

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two")
        self.assertEqual(1 + 1, 2)
