import os
import subprocess
from jinja2 import Environment, FileSystemLoader

def ensure_output_dir(output_dir="output"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def escape_latex(text):
    """
    Escapes LaTeX special characters in the given text.
    """
    if not text:
        return ""
    replacements = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
    }
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text

def render_latex_template(data, template_path="src/latex_template.tex", output_dir="output"):
    ensure_output_dir(output_dir)
    output_path = os.path.join(output_dir, "output.tex")
    env = Environment(
        loader=FileSystemLoader(searchpath="src"),
        block_start_string='{%',
        block_end_string='%}',
        variable_start_string='{{',
        variable_end_string='}}',
        comment_start_string='{#',
        comment_end_string='#}',
    )
    env.filters['escape_latex'] = escape_latex  # Register the filter
    template = env.get_template("latex_template.tex")
    rendered = template.render(data=data)
    with open(output_path, "w") as f:
        f.write(rendered)
    return output_path

def compile_latex_to_pdf(tex_path, output_dir="output"):
    ensure_output_dir(output_dir)
    try:
        subprocess.run(
            ["pdflatex", "-output-directory", output_dir, tex_path],
            check=True
        )
        print("PDF generated successfully in", output_dir)
    except subprocess.CalledProcessError as e:
        print("Error during PDF compilation:", e)
