import re

file_path = r'c:\Users\Hamza Ali\OneDrive\Documents\Projects\Git\sudoers_role_project\roles\package_manager\files\baseline'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Read {len(lines)} lines")

# Extract package names: the part before the version (dash followed by digit)
# Pattern: name components (can have letters, digits, dots, hyphens) stop at dash-digit
cleaned = set()
for line in lines:
    line = line.strip()
    if not line:
        continue
    
    # Find where version starts: first occurrence of -<digit>
    # Split by hyphen and find the first component that starts with a digit
    parts = line.split('-')
    pkg_name_parts = []
    
    for part in parts:
        if part and part[0].isdigit():
            # This is where the version starts
            break
        pkg_name_parts.append(part)
    
    if pkg_name_parts:
        pkg = '-'.join(pkg_name_parts)
        cleaned.add(pkg)
        if len(cleaned) <= 5:
            print(f"  {line[:50]:50} -> {pkg}")

print(f"Found {len(cleaned)} unique packages")

# Write sorted
with open(file_path, 'w', encoding='utf-8') as f:
    for pkg in sorted(cleaned):
        f.write(pkg + '\n')

print("File written successfully")
