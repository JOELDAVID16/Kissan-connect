import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find split {% trans ... %} tags
    # This matches {% trans followed by whitespace/newlines, then a quoted string, then whitespace/newlines, then %}
    # We want to catch the ones that ARE split.
    pattern = re.compile(r'\{%\s*trans\s+([\s\S]*?)\s*%\}', re.MULTILINE)
    
    def replace_func(match):
        inner = match.group(1)
        # Consolidate inner part: reduce multiple spaces/newlines to single space
        # But keep the string intact. We assume the string itself doesn't have literal newlines 
        # that should be preserved in the tag itself (which is true for {% trans %}).
        
        # Extract the quoted string
        string_match = re.search(r'(".*?"|\'.*?\')', inner, re.DOTALL)
        if string_match:
            s = string_match.group(1)
            # Remove any newlines within the string if they exist (though usually they shouldn't)
            s = s.replace('\n', ' ').replace('\r', ' ')
            # Collapse multiple spaces
            s = re.sub(r'\s+', ' ', s)
            return f'{{% trans {s} %}}'
        return match.group(0)

    new_content = pattern.sub(replace_func, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed: {filepath}")
        return True, new_content
    return False, content

def extract_strings(content):
    # Find all strings in {% trans "..." %} or {% trans '...' %}
    pattern = re.compile(r'\{%\s*trans\s+(".*?"|\'.*?\')\s*%\}')
    matches = pattern.findall(content)
    return [m[1:-1] for m in matches] # Remove quotes

templates_dir = os.path.join(os.getcwd(), 'templates')
all_strings = set()

for root, dirs, files in os.walk(templates_dir):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            fixed, content = process_file(path)
            strings = extract_strings(content)
            all_strings.update(strings)

print("\nAll extracted strings:")
for s in sorted(list(all_strings)):
    print(f"- {s}")

# Also check Python files for _("...")
core_dir = os.path.join(os.getcwd(), 'core')
for root, dirs, files in os.walk(core_dir):
    for file in files:
        if file.endswith('.py'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            py_pattern = re.compile(r'_\(\s*(".*?"|\'.*?\')\s*\)')
            py_strings = [m[1:-1] for m in py_pattern.findall(content)]
            all_strings.update(py_strings)

print("\nFinal set of unique strings:")
for s in sorted(list(all_strings)):
    print(s)
