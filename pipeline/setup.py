import json
from jinja2 import Environment, FileSystemLoader

# Load the JSON configuration
with open('pipeline/config.json', 'r') as f:
    config = json.load(f)

# Setup Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('pipeline/exp_config.j2')

# Render the template with configuration variables
output_from_parsed_template = template.render(config)

# Save the rendered template to a new Python file
with open("exps/yolox_s_pipeline.py", "w") as fh:
    fh.write(output_from_parsed_template)

print("Python configuration file generated successfully.")
