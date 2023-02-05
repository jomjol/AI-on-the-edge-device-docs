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
        #overviewFileHandle.write(parameterDoc + "\n\n---\n\n")
        overviewFileHandle.write(parameterDoc)
        overviewFileHandle.write("\n\n<hr style=\"border:2px solid\">\n\n")


# Create templated overview markdown file
if os.path.exists(parameterOverviewFile):
    os.remove(parameterOverviewFile)
#shutil.copy(parameterOverviewTemplateFile, parameterOverviewFile)

folders = sorted( filter( os.path.isdir, glob.glob(parameterDocsFolder + '/*') ) )

"""
Create Table of Content
"""
toc = ""
for folder in folders:
    folder = folder.split("/")[-1]

    toc += "\n\n[%s](#%s)\n\n" % (folder, folder.lower())

    files = sorted(filter(os.path.isfile, glob.glob(parameterDocsFolder + "/" + folder + '/*')))
    for file in files:
        parameter = ".".join(file.split("/")[-1].split(".")[:-1])
        anchor = parameter.replace("<", "").replace(">", "").replace(".", "").lower()
        toc += " - [`%s`](#parameter-%s)\n" % (parameter, anchor)

    with open(parameterOverviewTemplateFile, 'r') as overviewFileHandle:
        overviewFileContent = overviewFileHandle.read()

    overviewFileContent = overviewFileContent.replace("$TOC", toc)

    with open(parameterOverviewFile, 'w') as overviewFileHandle:
        overviewFileHandle.write(overviewFileContent)


"""
Append all parameter pages in a sorted manner
"""
for folder in folders:
    folder = folder.split("/")[-1]
#    print(folder)

    # Add section
    with open(parameterOverviewFile, 'a') as overviewFileHandle:
        #overviewFileHandle.write("\n\n<hr style=\"border:5px solid\">\n\n")
        overviewFileHandle.write("\n## Section `%s`\n\n" % folder)

    files = sorted(filter(os.path.isfile, glob.glob(parameterDocsFolder + "/" + folder + '/*')))
    for file in files:
#        print("  %s" % file)
        appendParameterFile(folder, file)
