# Use this file to define custom macros for docs generation

import yaml
import pandas as pd
import os
import re

def define_env(env):

    ### Macro to print contents of a YAML file as a markdown table
    @env.macro
    def yaml_table(file_path, columns=None):
        with open(file_path, 'r') as f:
            content = yaml.safe_load(f)

        # Expect the top-level key to be 'data'
        data = content.get('data', [])

        # Validate that it's a list of dicts
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            return "⚠️ YAML file must contain a list of dictionaries under the 'data' key."

        # Flatten into a DataFrame
        df = pd.json_normalize(data)

        # Select specific columns if requested
        if columns:
            df = df[columns]

        return df.to_markdown(index=False)

    ### Macro to generate a table of contents from a specified base directory
    @env.macro
    def generate_toc(dir="docs"):
        # Sanitize and standardize input
        dir = dir.rstrip("/\\")
        base_dir = "docs"  # Assuming this script runs from project root
        if dir.startswith("docs/"):
            rel_dir = dir[5:]  # Strip 'docs/' for relative paths in links
        else:
            rel_dir = dir

        abs_path = os.path.join(base_dir, rel_dir)
        if not os.path.exists(abs_path):
            return f"**Error**: Path `{dir}` does not exist."

        rows = []

        for folder in sorted(os.listdir(abs_path)):
            folder_path = os.path.join(abs_path, folder)
            if not os.path.isdir(folder_path):
                continue

            links = []

            for fname in sorted(os.listdir(folder_path)):
                if fname.endswith(".md"):
                    filepath = os.path.join(rel_dir, folder, fname).replace("\\", "/")
                    title = camel_case_split(os.path.splitext(fname)[0])
                    links.append(f"- [{title}]({filepath})")

            folder_display = camel_case_split(folder)
            links_cell = "<br>".join(links) if links else "-"
            rows.append((folder_display, links_cell))

        top_folder_heading = camel_case_split(os.path.basename(abs_path))
        
        table_lines = [
            f"|  | {top_folder_heading} |",
            "| --- | --- |"
        ]

        for folder, files in rows:
            table_lines.append(f"| {folder} | {files} |")

        return "\n".join(table_lines)

def camel_case_split(s):
    """Split snake_case and camelCase strings into readable form.
       Capitalises first letter of each word only if it's lower case.
       Preserves internal capitalisation.
    """
    # Split on underscores first
    parts = s.split("_")

    words = []
    for part in parts:
        # Split camelCase: insert space before capital letters that follow lowercase letters
        split_part = re.sub(r'([a-z])([A-Z])', r'\1 \2', part)
        for word in split_part.split():
            if word and word[0].islower():
                word = word[0].upper() + word[1:]
            words.append(word)
    return " ".join(words)