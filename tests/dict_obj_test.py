import sys
from unittest import TestCase
from pyduinocoin import DictObj


class DictObjTests(TestCase):
    def setUp(self):
        self.entries = {
            'ti tl%%.-.¨¨ %e': 'images',
            'results': [
                {
                    'path': 'img/',
                    'title': 'img1'
                },
                {
                    'path': 'img/',
                    'title': 'img2'
                }
            ],
            'formats': ['.jpg', '.png'],
            'langs': {
                'ES' : 'es-ES', 
                'FR': 'fr-FR'
            }
        }

    def assert_attr(self, dict_obj):
        self.assertIsNotNone(dict_obj)

        self.assertTrue(hasattr(dict_obj, 'title'))
        self.assertTrue(isinstance(dict_obj.title, str))
        self.assertEqual(dict_obj.title, 'images')

        self.assertTrue(hasattr(dict_obj, 'results'))
        self.assertTrue(isinstance(dict_obj.results, list))
        for result in dict_obj.results:
            self.assertTrue(isinstance(result, DictObj))
            self.assertTrue(hasattr(result, 'path'))
            self.assertTrue(hasattr(result, 'title'))
            self.assertTrue(isinstance(result.path, str))
            self.assertTrue(isinstance(result.title, str))

        self.assertTrue(hasattr(dict_obj, 'formats'))
        self.assertTrue(isinstance(dict_obj.formats, list))
        self.assertIn('.jpg', dict_obj.formats)
        self.assertIn('.png', dict_obj.formats)

        self.assertTrue(hasattr(dict_obj, 'langs'))
        self.assertTrue(isinstance(dict_obj.langs, DictObj))
        self.assertTrue(hasattr(dict_obj.langs, 'ES'))
        self.assertTrue(hasattr(dict_obj.langs, 'FR'))
        self.assertTrue(isinstance(dict_obj.langs.ES, str))
        self.assertTrue(isinstance(dict_obj.langs.FR, str))
        self.assertEqual(dict_obj.langs.ES, 'es-ES')
        self.assertEqual(dict_obj.langs.FR, 'fr-FR')

    def assert_dict(self, dict_obj):
        self.assertIsNotNone(dict_obj)

        self.assertIn('title', dict_obj)
        self.assertTrue(isinstance(dict_obj['title'], str))
        self.assertEqual(dict_obj['title'], 'images')

        self.assertIn('results', dict_obj)
        self.assertTrue(isinstance(dict_obj['results'], list))
        for result in dict_obj['results']:
            self.assertTrue(isinstance(result, DictObj))
            self.assertIn('path', result)
            self.assertIn('title', result)
            self.assertTrue(isinstance(result['path'], str))
            self.assertTrue(isinstance(result['title'], str))

        self.assertIn('formats', dict_obj)
        self.assertTrue(isinstance(dict_obj['formats'], list))
        self.assertIn('.jpg', dict_obj['formats'])
        self.assertIn('.png', dict_obj['formats'])

        self.assertIn('langs', dict_obj)
        self.assertTrue(isinstance(dict_obj['langs'], DictObj))
        self.assertIn('ES', dict_obj['langs'])
        self.assertIn('FR', dict_obj['langs'])
        self.assertTrue(isinstance(dict_obj['langs']['ES'], str))
        self.assertTrue(isinstance(dict_obj['langs']['FR'], str))
        self.assertEqual(dict_obj['langs']['ES'], 'es-ES')
        self.assertEqual(dict_obj['langs']['FR'], 'fr-FR')

    def test_dict_obj__init__(self):
        dict_obj = DictObj(self.entries)
        self.assert_attr(dict_obj)
        self.assert_dict(dict_obj)
        self.assert_dict(dict_obj.__dict__)

    def test_dict_obj__len__(self):
        self.assertEqual(len(DictObj(self.entries)), 4)
        self.assertEqual(len(DictObj()), 0)

    def test_dict_obj__getitem__(self):
        dict_obj = DictObj(self.entries)
        self.assertEqual(dict_obj['title'], 'images')
        self.assertEqual(dict_obj['results'][0]['path'], 'img/')
        self.assertEqual(dict_obj['formats'][0], '.jpg')
        self.assertEqual(dict_obj['langs']['ES'], 'es-ES')

    def test_dict_obj__setitem__(self):
        dict_obj = DictObj()
        dict_obj['title'] = 'images'
        dict_obj['results'] = [{'path': 'img/'}]
        dict_obj['formats'] = ['.jpg']
        dict_obj['langs'] = {'ES': 'es-ES'}
        self.assertEqual(dict_obj['title'], 'images')
        self.assertEqual(dict_obj['results'][0]['path'], 'img/')
        self.assertEqual(dict_obj['formats'][0], '.jpg')
        self.assertEqual(dict_obj['langs']['ES'], 'es-ES')

    def test_dict_obj__delitem__(self):
        dict_obj = DictObj(self.entries)
        self.assertIn('title', dict_obj)
        del dict_obj['title']
        self.assertNotIn('title', dict_obj)

    def test_dict_obj__iter__(self):
        try:
            iter(DictObj(self.entries))
        except TypeError as e:
            self.fail('Not iterable')

    def test_dict_obj__reversed__(self):
        if sys.version_info >= (3, 8):
            try:
                reversed(DictObj(self.entries))
            except TypeError as e:
                self.fail('Not reverse iterable')

    def test_dict_obj_clear(self):
        dict_obj = DictObj(self.entries)
        dict_obj.clear()
        self.assertEqual(len(dict_obj), 0)

    def test_dict_obj_copy(self):
        dict_obj = DictObj(self.entries)
        dict_obj_copy = dict_obj.copy()
        self.assertTrue(hasattr(dict_obj_copy, 'title'))
        self.assertEqual(dict_obj.__dict__, dict_obj_copy.__dict__)

    def test_dict_obj_fromkeys(self):
        dict_obj = DictObj().fromkeys({'a','b'})
        self.assertEqual(len(dict_obj), 2)
        self.assertTrue(hasattr(dict_obj, 'a'))
        self.assertTrue(hasattr(dict_obj, 'b'))
        for value in dict_obj.values():
            self.assertIsNone(value)
            
        dict_obj = DictObj().fromkeys({'a','b'}, 1)
        self.assertEqual(len(dict_obj), 2)
        self.assertTrue(hasattr(dict_obj, 'a'))
        self.assertTrue(hasattr(dict_obj, 'b'))
        for value in dict_obj.values():
            self.assertEqual(value, 1)

    def test_dict_obj_get(self):
        get = DictObj(self.entries).get('title')
        self.assertEqual(get, 'images')

    def test_dict_obj_items(self):
        items = DictObj(self.entries).items()
        self.assertEqual(len(items), 4)
        self.assertIn(('title', 'images'), items)

    def test_dict_obj_keys(self):
        keys = DictObj(self.entries).keys()
        self.assertEqual(len(keys), 4)
        self.assertIn('title', keys)

    def test_dict_obj_pop(self):
        dict_obj = DictObj(self.entries)
        pop = dict_obj.pop('title')
        self.assertNotIn('title', dict_obj)
        self.assertEqual(pop, 'images')
        pop = dict_obj.pop('random', 'noexist')
        self.assertEqual(pop, 'noexist')

    def test_dict_obj_popitem(self):
        popitem = DictObj(self.entries).popitem()
        self.assertIsNotNone(popitem)

    def test_dict_obj_setdefault(self):
        dict_obj = DictObj(self.entries)
        self.assertEqual(dict_obj.setdefault('title'), 'images')
        self.assertEqual(dict_obj.setdefault('random', 'modnar'), 'modnar')

    def test_dict_obj_update(self):
        dict_obj = DictObj()
        dict_obj.update(self.entries)
        self.assertTrue(hasattr(dict_obj, 'title'))

    def test_dict_obj_values(self):
        values = DictObj(self.entries).values()
        self.assertEqual(len(values), 4)
        self.assertIn('images', values)

        
        
         
