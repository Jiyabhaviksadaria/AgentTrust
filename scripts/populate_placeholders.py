import os

root_dir = "."

for dirpath, dirnames, filenames in os.walk(root_dir):
    if ".git" in dirpath.split(os.sep):
        continue
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        # If file is empty (0 bytes)
        if os.path.exists(filepath) and os.path.getsize(filepath) == 0:
            ext = os.path.splitext(filename)[1]
            if ext in ['.py', '.sh', '.yml', '.yaml']:
                content = f"# {filename} - AgentTrust framework\n"
            elif ext in ['.ts', '.tsx', '.js', '.mjs', '.css']:
                content = f"// {filename} - AgentTrust framework\n"
            elif ext in ['.json']:
                content = "{\n}\n"
            elif ext in ['.md']:
                content = f"# {filename}\n\nAgentTrust platform component.\n"
            elif ext in ['.html']:
                content = f"<!-- {filename} -->\n"
            else:
                content = f"# {filename}\n"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Populated placeholder content in empty files.")
