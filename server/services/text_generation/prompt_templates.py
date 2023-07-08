import os
import json
from .messages import Messages

class PromptTemplates:
    def __init__(self):
        self.templates = []
        self.messages = Messages()

    def create_variable_template(self, text, input_variables, template_name, role="user"):

        template_content = {
            "text": text,
            "input_variables": input_variables
        }

        template = {"role": role, "template": template_content}

        template_filename = f"templates/{template_name}.json"

        if os.path.exists(template_filename):
            return "Template file name already exists."

        with open(template_filename, "w") as file:
            json.dump(template, file)

        return "Template created."

    def create_template(self, text, template_name, role):
        template = self.messages.create(text, role)

        template_filename = f"templates/{template_name}.json"

        if os.path.exists(template_filename):
            return "Template file name already exists."

        with open(template_filename, "w") as file:
            json.dump(template, file)

        return "Template created."

    def chain_template(self):
        template_directory = "templates"
        templates = []
        for filename in os.listdir(template_directory):
            if filename.endswith(".json"):
                template_name = os.path.splitext(filename)[0]
                templates.append(template_name)
        selected_template = self.select_template(templates)
        self.templates.append(selected_template)
        return f"Template added to chain:\n{selected_template}"

    def select_template(self, templates):
        if not templates:
            return "No templates available."

        print("Available Templates:")
        for index, template in enumerate(templates, start=1):
            print(f"{index}. {template}")

        selection = input("Select a template number (or 'q' to quit): ")

        if selection == "q":
            return "Exiting template selection."

        try:
            selection_index = int(selection) - 1
            return templates[selection_index]

        except (ValueError, IndexError):
            return "Invalid selection."

    def delete_template(self, template_name):
        template_filename = f"templates/{template_name}.json"

        if not os.path.exists(template_filename):
            return "Template does not exist."

        os.remove(template_filename)

        return "Template deleted."

    def clear_template_chain(self):
        self.templates = []

    def display_templates(self):
        if not self.templates:
            return "No templates available."

        templates_list = "\n".join([f"{index}. {template}" for index, template in enumerate(self.templates, start=1)])
        return f"Available Templates:\n{templates_list}"


    def remove_chained_template(self):
           selected_template = self.select_template(self.templates)
           self.templates.remove(selected_template)
           return f"You removed template: {selected_template}"

    def get_templates(self):
        return self.templates
