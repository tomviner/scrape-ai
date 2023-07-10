import os
import re

uuid_re = re.compile(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}')
uuid_repl = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'

for key, value in sorted(os.environ.items()):
    value = uuid_re.sub(uuid_repl, value)
    print(f"{key}={value}")
