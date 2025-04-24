"""
Script to update imports in all notebooks.

This script updates the following imports:
1. 'import core.praser as Praser' to 'import core.parser as Parser'
2. 'from core.praser import' to 'from core.parser import'
3. 'from emdiffuse_conifg import' to 'from emdiffuse_config import'

Author: EMDiffuse Team
Date: April 2025
"""

import os
import json
import glob

def update_notebook(notebook_path):
    """
    Update imports in a Jupyter notebook.
    
    Args:
        notebook_path (str): Path to the notebook file.
    """
    print(f"Processing {notebook_path}...")
    
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Flag to track if the notebook was modified
    modified = False
    
    # Process each cell
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            for i, source in enumerate(cell['source']):
                # Update 'import core.praser as Praser'
                if 'import core.praser as Praser' in source:
                    cell['source'][i] = source.replace('import core.praser as Praser', 'import core.parser as Parser')
                    modified = True
                
                # Update 'from core.praser import'
                if 'from core.praser import' in source:
                    cell['source'][i] = source.replace('from core.praser import', 'from core.parser import')
                    modified = True
                
                # Update 'from emdiffuse_conifg import'
                if 'from emdiffuse_conifg import' in source:
                    cell['source'][i] = source.replace('from emdiffuse_conifg import', 'from emdiffuse_config import')
                    modified = True
                
                # Update 'opt = Praser.parse(config)'
                if 'opt = Praser.parse(config)' in source:
                    cell['source'][i] = source.replace('opt = Praser.parse(config)', 'opt = Parser.parse(config)')
                    modified = True
    
    # Write the updated notebook if modified
    if modified:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1)
        print(f"Updated {notebook_path}")
    else:
        print(f"No changes needed in {notebook_path}")

def main():
    """
    Main function to update all notebooks.
    """
    # Get all notebook files
    notebook_paths = glob.glob('example/**/*.ipynb', recursive=True)
    
    # Update each notebook
    for notebook_path in notebook_paths:
        update_notebook(notebook_path)

if __name__ == '__main__':
    main()
