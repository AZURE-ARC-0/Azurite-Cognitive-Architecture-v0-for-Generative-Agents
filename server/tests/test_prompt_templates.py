import unittest
import os
import json
from unittest.mock import patch
from services.text_generation.prompt_templates import PromptTemplates

class PromptTemplatesTest(unittest.TestCase):
    def setUp(self):
        self.templates = PromptTemplates()

    def tearDown(self):
        # Clean up any template files created during the tests
        template_directory = "templates"
        for filename in os.listdir(template_directory):
            if filename.endswith(".json"):
                template_filename = os.path.join(template_directory, filename)
                os.remove(template_filename)

    def test_create_variable_template(self):
        text = "Variable template text"
        input_variables = ["var1", "var2"]
        template_name = "variable_template"
        role = "user"

        expected_output = "Template created."
        result = self.templates.create_variable_template(text, input_variables, template_name, role)
        self.assertEqual(result, expected_output)

    def test_create_template(self):
        text = "Template text"
        template_name = "template"
        role = "user"

        expected_output = "Template created."
        result = self.templates.create_template(text, template_name, role)
        self.assertEqual(result, expected_output)

    def test_chain_template(self):
        # Create a sample template
        template_name = "sample_template"
        template_filename = f"templates/{template_name}.json"
        template_content = {"role": "user", "template": "Sample template text"}
        with open(template_filename, "w") as file:
            json.dump(template_content, file)

        # Simulate user input for template selection
        user_input = ["1", "q"]
        expected_output = "Template added to chain:\nsample_template"

        # Patch the input function to return the simulated user input
        with patch("builtins.input", side_effect=user_input):
            result = self.templates.chain_template()

        # Clean up the created template file
        os.remove(template_filename)

        self.assertEqual(result, expected_output)

    def test_select_template(self):
        # Create a sample template
        template_name = "sample_template"
        template_filename = f"templates/{template_name}.json"
        template_content = {"role": "user", "template": "Sample template text"}
        with open(template_filename, "w") as file:
            json.dump(template_content, file)

        # Simulate user input for template selection
        user_input = ["1", "q"]
        expected_output = "sample_template"

        # Patch the input function to return the simulated user input
        with patch("builtins.input", side_effect=user_input):
            result = self.templates.select_template([template_name])

        # Clean up the created template file
        os.remove(template_filename)

        self.assertEqual(result, expected_output)

    def test_delete_template(self):
        # Create a sample template
        template_name = "sample_template"
        template_filename = f"templates/{template_name}.json"
        template_content = {"role": "user", "template": "Sample template text"}
        with open(template_filename, "w") as file:
            json.dump(template_content, file)

        expected_output = "Template deleted."
        result = self.templates.delete_template(template_name)
        self.assertEqual(result, expected_output)

    def test_clear_template_chain(self):
        self.templates.templates = ["template1", "template2", "template3"]

        self.templates.clear_template_chain()

        expected_output = []
        self.assertEqual(self.templates.templates, expected_output)

    def test_display_templates(self):
        self.templates.templates = ["template1", "template2", "template3"]

        expected_output = "Available Templates:\n1. template1\n2. template2\n3. template3"
        result = self.templates.display_templates()
        self.assertEqual(result, expected_output)

    def test_remove_chained_template(self):
        # Set up templates
        template1 = "template1"
        template2 = "template2"
        template3 = "template3"
        self.templates.templates = [template1, template2, template3]

        # Simulate user input for template selection
        user_input = ["2"]
        expected_output = f"You removed template: {template2}"

        # Patch the input function to return the simulated user input
        with patch("builtins.input", side_effect=user_input):
            result = self.templates.remove_chained_template()

        self.assertEqual(result, expected_output)
        self.assertEqual(self.templates.templates, [template1, template3])

    def test_get_templates(self):

        template1 = "template1"
        template2 = "template2"
        template3 = "template3"
        self.templates.templates = [template1, template2, template3]

        expected_output = ["template1", "template2", "template3"]
        result = self.templates.get_templates()
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
