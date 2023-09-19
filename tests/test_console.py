#!/usr/bin/python3
"""Test console class"""

import os
import pep8
import unittest
import models
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


class CustomTestHBNBCommand(unittest.TestCase):
    """Custom unittests for the Airbnb console."""

    @classmethod
    def setUpClass(cls):
        """Custom setup for HBNBCommand testing."""
        try:
            os.rename("data.json", "temp_data")
        except IOError:
            pass
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Custom teardown for HBNBCommand testing."""
        try:
            os.rename("temp_data", "data.json")
        except IOError:
            pass
        del cls.HBNB
        if type(models.storage) == DBStorage:
            models.storage._DBStorage__session.close()

    def setUp(self):
        """Custom setup for FileStorage objects."""
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Custom teardown for created data.json."""
        try:
            os.remove("data.json")
        except IOError:
            pass

    def test_style_guide(self):
        """Custom test for PEP8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, "Fix PEP8 issues")

    def test_documentation(self):
        """Custom test for docstrings."""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.count.__doc__)
        self.assertIsNotNone(HBNBCommand.strip_clean.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_empty_line(self):
        """Custom test for empty line input."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_exit_command(self):
        """Custom test for exit command input."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("exit")
            self.assertEqual("", f.getvalue())

    def test_EOF_command(self):
        """Custom test for EOF command."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(self.HBNB.onecmd("EOF"))

    # Modify and customize other test cases as needed.


if __name__ == "__main__":
    unittest.main()
