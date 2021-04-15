from django.test import TestCase
from todo.models import ToDo, Priority

# Create your tests here.


class TestPage(TestCase):
    def setUp(self):
        self.my_priority = Priority.objects.create(
            name='Low'
        )
        self.my_todo = ToDo.objects.create(
            name='WOWO',
            priority=Priority.objects.get(id=1)
        )

    def test_add(self):
        todo_add = self.client.post('/add_todo')
        self.assertEqual(todo_add.status_code, 200)

    def test_edit(self):
        todo_edit = self.client.post(f'/edit_todo/{self.my_todo.id}')
        self.assertEqual(todo_edit.status_code, 200)

    def test_del(self):
        todo_del = self.client.post(f'/delete_todo/{self.my_todo.id}')
        self.assertEqual(todo_del.status_code, 302)
