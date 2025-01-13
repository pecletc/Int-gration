import os
import unittest
import tempfile
import file_utils

class TestFileUtils(unittest.TestCase):
    """Tests unitaires du module file_utils."""
    def setUp(self):
        """Montage de la fixation de test - appelé avant chaque cas de test."""
        _, self.file_first_name = tempfile.mkstemp()
        _, self.file_second_name = tempfile.mkstemp()
        _, self.file_not_found = tempfile.mkstemp()

        with open(self.file_first_name, "w+") as file_first_id:
            file_first_id.write("") # create file with an empty content

        with open(self.file_second_name, "w+") as file_second_id:
            file_second_id.write("foo") # create file with "foo" in it

        os.remove(self.file_not_found)

    def tearDown(self):
        """Démontage de la fixation de test - appelé après chaque cas de test."""
        os.remove(self.file_first_name)
        os.remove(self.file_second_name)
    
    def testAreSame(self):
        """Cas de test vérifiant que les fichiers sont identiques."""
        assert not file_utils.diff(self.file_first_name, self.file_first_name), "similitude non détectée"
    
    def testAreDifferent(self):
        """Cas de test -  fichiers différents."""
        assert file_utils.diff(self.file_first_name, self.file_second_name), "différence non détectée"

    def testFirstFileNotFound(self):
        """Cas de test - premier fichier inexistant."""
        with self.assertRaises(FileNotFoundError):
            file_utils.diff(self.file_not_found, self.file_second_name)

    def testSecondFileNotFound(self):
        """Cas de test - second fichier inexistant."""
        with self.assertRaises(FileNotFoundError):
            file_utils.diff(self.file_first_name, self.file_not_found)

""" Lancement des tests """
if __name__ == "__main__":
    unittest.main(warnings="ignore")
