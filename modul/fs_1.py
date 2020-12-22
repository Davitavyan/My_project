from fs.osfs import OSFS
with OSFS("FileExamples") as myfs:
    for step in myfs.walk():
        print(step.dirs)
