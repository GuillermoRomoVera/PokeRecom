import unittest
from app import get_pokemon_types, get_random_pokemon_by_type

#Valida que las funciones esten funcionando
class TestPokeRecom(unittest.TestCase):

    def test_get_pokemon_types(self):
        types = get_pokemon_types()
        self.assertIsInstance(types, list)
        self.assertIn('fire', types)

    def test_get_random_pokemon_by_type(self):
        pokemon = get_random_pokemon_by_type('water')
        self.assertIsInstance(pokemon, dict)
        self.assertIn('name', pokemon)
        self.assertIn('id', pokemon)
        self.assertIn('sprite', pokemon)
        self.assertIn('moves', pokemon)
        self.assertTrue(len(pokemon['moves']) > 0)

if __name__ == '__main__':
    unittest.main()
