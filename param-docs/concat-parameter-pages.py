"""
Grab all parameter files and concat them into a single file.
The header structure gets moved down 1 level
"""

import os
import shutil
import glob

sectionsLogicallyOrdered = ["TakeImage", "Alignment", "Digits", "Analog", "PostProcessing",
                           "MQTT", "InfluxDB", "InfluxDBv2", "GPIO", "AutoTimer", "DataLogging", "Debug", "System"]

parameterDocsFolder = "AI-on-the-edge-device/param-docs/parameter-pages/"
docsMainFolder = "../docs"
parameterOverviewFile = "Parameters.md"
parameterOverviewTemplateFile = "./templates/overview.md"

def appendParameterFile(section, file, parameterName):
    with open(file, 'r') as parameterFileHandle:
        parameterDoc = parameterFileHandle.read()
        parameterDoc = parameterDoc.replace("# ", "### ") # Move all headings 2 level down

    # Add parameter doc to overview page
    with open(docsMainFolder + "/" + parameterOverviewFile, 'a') as overviewFileHandle:
        overviewFileHandle.write("<a id=%s-%s></a>\n" % (section, parameterName)) # Create a html anchor so we can link to it with "section-parameter"
        overviewFileHandle.write(parameterDoc)
        overviewFileHandle.write("\n\n<hr style=\"border:2px solid\">\n\n")


# Create templated overview markdown file
if os.path.exists(docsMainFolder + "/" + parameterOverviewFile):
    os.remove(docsMainFolder + "/" + parameterOverviewFile)
#shutil.copy(parameterOverviewTemplateFile, parameterOverviewFile)

foldersRaw = sorted( filter( os.path.isdir, glob.glob(parameterDocsFolder + '/*') ) )



folders = []
for folder in foldersRaw:
    folder = folder.split("/")[-1]

    if folder == "img": # Skip the images folder
        continue

    if not folder in sectionsLogicallyOrdered:
        print("Warning: The section %r seems to be new, appending it to the end of the logically ordered folder list!" % folder)
        print("         Please update `sectionsLogicallyOrdered`!")
        sectionsLogicallyOrdered.append(folder)



"""
Create Overview Page (parameters.md)
"""
toc = ""
for section in sectionsLogicallyOrdered:
    with open(parameterOverviewTemplateFile, 'r') as overviewFileHandle:
        overviewFileContent = overviewFileHandle.read()

    # # Create TOC
    # toc += "\n\n[%s](#%s)\n\n" % (section, section.lower())
    #
    # files = sorted(filter(os.path.isfile, glob.glob(parameterDocsFolder + "/" + section + '/*')))
    # for file in files:
    #     parameter = file.split("/")[-1].replace(".md", "")
    #     parameter = parameter.replace("<", "").replace(">", "")
    #     toc += " - [`%s`](#%s-%s)\n" % (parameter, section, parameter)
    #
    # overviewFileContent = overviewFileContent.replace("$TOC", toc)

    with open(docsMainFolder + "/" + parameterOverviewFile, 'w') as overviewFileHandle:
        overviewFileHandle.write(overviewFileContent)


"""
Append all parameter pages in a sorted manner
"""
print("Appending all parameter pages to the single page %r..." % (docsMainFolder + "/" + parameterOverviewFile))
for section in sectionsLogicallyOrdered:
    # Add section
    with open(docsMainFolder + "/" + parameterOverviewFile, 'a') as overviewFileHandle:
        overviewFileHandle.write("\n## Section `%s`\n\n" % section)

    files = sorted(filter(os.path.isfile, glob.glob(parameterDocsFolder + "/" + section + '/*')))
    for file in files:
        if not ".md" in file: # Skip non-markdown files
            continue

        # print("  %s" % file)
        parameter = file.split("/")[-1].replace(".md", "")
        parameter = parameter.replace("<", "").replace(">", "")
        appendParameterFile(section, file, parameter)


"""
Copy images to main folder
"""
os.system("cp " + parameterDocsFolder + "/img/* " + docsMainFolder + "/img/")

