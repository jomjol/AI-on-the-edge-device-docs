"""
Grab all parameter files and concat them into a single file.
The header structure gets moved down 1 level
"""

import os
import shutil
import glob


parameterDocsFolder = "parameter-pages"
parameterOverviewFile = "../docs/Parameters.md"
parameterOverviewTemplateFile = "./templates/overview.md"

def appendParameterFile(folder, file):
    #print(folder, file)

    with open(file, 'r') as parameterFileHandle:
        parameterDoc = parameterFileHandle.read()
        parameterDoc = parameterDoc.replace("# ", "### ") # Move all headings 2 level down

    # Add parameter doc to overview page
    with open(parameterOverviewFile, 'a') as overviewFileHandle:
        overviewFileHandle.write(parameterDoc + "\n\n---\n\n")


# Create templated overview markdown file
if os.path.exists(parameterOverviewFile):
    os.remove(parameterOverviewFile)
shutil.copy(parameterOverviewTemplateFile, parameterOverviewFile)

"""
Append all parameter pages in a sorted manner
"""
folders = sorted( filter( os.path.isdir, glob.glob(parameterDocsFolder + '/*') ) )
for folder in folders:
    folder = folder.split("/")[-1]
#    print(folder)

    # Add section
    with open(parameterOverviewFile, 'a') as overviewFileHandle:
        overviewFileHandle.write("\n## [%s]\n\n" % folder)

    files = sorted(filter(os.path.isfile, glob.glob(parameterDocsFolder + "/" + folder + '/*')))
    for file in files:
#        print("  %s" % file)
        appendParameterFile(folder, file)