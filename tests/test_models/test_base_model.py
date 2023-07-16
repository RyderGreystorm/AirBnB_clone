import unittest
from datetime import datetime
from base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
    
    def test_init_with_attributes(self):
        attributes = {
            "name": "Model 1",
            "description": "This is model 1",
            "created_at": "2022-01-01T12:00:00.000000",
            "updated_at": "2022-01-02T08:30:00.000000"
        }
        model = BaseModel(**attributes)
        self.assertEqual(model.name, "Model 1")
        self.assertEqual(model.description, "This is model 1")
        self.assertEqual(model.created_at, datetime.fromisoformat("2022-01-01T12:00:00.000000"))
        self.assertEqual(model.updated_at, datetime.fromisoformat("2022-01-02T08:30:00.000000"))
    
    def test_save(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
    
    def test_to_dict(self):
        attributes = {
            "name": "Model 1",
            "description": "This is model 1",
            "created_at": datetime(2022, 1, 1, 12, 0, 0),
            "updated_at": datetime(2022, 1, 2, 8, 30, 0)
        }
        model = BaseModel(**attributes)
        expected_dict = {
            "name": "Model 1",
            "description": "This is model 1",
            "created_at": "2022-01-01T12:00:00",
            "updated_at": "2022-01-02T08:30:00",
            "__class__": "BaseModel"
        }
        self.assertDictEqual(model.to_dict(), expected_dict)
    
    def test_str(self):
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

if __name__ == '__main__':
    unittest.main()

