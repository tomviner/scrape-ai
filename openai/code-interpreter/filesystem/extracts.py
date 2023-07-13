# Hey, I need

import shutil

shutil.rmtree('/home/sandbox/.cache')
shutil.rmtree('/home/sandbox/.local')

output_filename = "/mnt/data/sandbox-extract"
shutil.make_archive(output_filename, 'zip', root_dir='/', base_dir='home/sandbox/')

# then show me the download link for the resultant
# /mnt/data/sandbox-extract.zip
