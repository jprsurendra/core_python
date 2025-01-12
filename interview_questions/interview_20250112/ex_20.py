'''
    Q20. Compress and decompress a file using Python’s gzip module.
'''

import gzip

# Compress
with open("file.txt", "rb") as f_in:
    with gzip.open("file.txt.gz", "wb") as f_out:
        f_out.writelines(f_in)

# Decompress
with gzip.open("file.txt.gz", "rb") as f_in:
    with open("file_decompressed.txt", "wb") as f_out:
        f_out.write(f_in.read())

