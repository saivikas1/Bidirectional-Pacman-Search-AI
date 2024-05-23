import os
import shutil



def getlayoutsNames():
    obj = os.scandir('1.search/layouts/')
    layouts = []
    for entry in obj:
        if entry.is_file():
            layouts.append(entry.name.split('.')[0])
    return layouts


def getLayouts(layouts):
    existing_layouts = {}
    for eachLayout in range(len(layouts)):
        with open(os.getcwd() + "/1.search/layouts/" + layouts[eachLayout] + ".lay", "r") as layoutFiles:
            layoutPattern = []
            for eachLine in layoutFiles:
                eachRow = eachLine.rstrip("\n")
                finaleachRow = list(filter(lambda i: (i in eachRow), eachRow))
                layoutPattern.append(finaleachRow)
            existing_layouts[layouts[eachLayout]] = layoutPattern
    return existing_layouts


def generateCombinations(key, existingLayouts):
    emptyPositions = []
    pacmanPosition = []

    for eachRow in range(len(existingLayouts)):
        for eachCol in range(len(existingLayouts[eachRow])):
            if existingLayouts[eachRow][eachCol] == " ":
                emptyPositions.append((eachRow, eachCol))
            if existingLayouts[eachRow][eachCol] == "P":
                pacmanPosition.append((eachRow, eachCol))

    finalLayouts = {}

    existingRow = []
    for eachRow in existingLayouts:
        existingRow.append(''.join(map(str, eachRow)))
    finalLayouts[key] = existingRow

    for combinationNumber, (newRow, newCol) in enumerate(emptyPositions):

        for eachRow in range(len(existingLayouts)):
            for eachCol in range(len(existingLayouts[eachRow])):
                if existingLayouts[eachRow][eachCol] == "P":
                    existingLayouts[eachRow][eachCol] = " "

        generateLayouts = existingLayouts
        generateLayouts[newRow][newCol] = "P"
        finalRow = []

        for eachRow in generateLayouts:
            finalRow.append(''.join(map(str, eachRow)))
        finalLayouts[key + '_' + str(combinationNumber)] = finalRow

    return finalLayouts


def writeToFile(new_layouts):
    for layout_name, layout_pattern in new_layouts.items():
        with open(os.getcwd() + "/1.search/layouts/Combination/" + layout_name + ".lay", "w") as f:
            for eachRow in layout_pattern:
                f.write(eachRow)
                f.write("\n")
            f.close()


def main_fn():
    path = os.getcwd() + "/1.search/layouts/Combination"
    if os.path.exists(path):
        shutil.rmtree(path,ignore_errors=True)
    os.mkdir(path)

    layouts = getlayoutsNames()
    existingLayouts = getLayouts(layouts)
    for layoutName, actualLayout in existingLayouts.items():
        print("Generating Combinations for {0}".format(layoutName))
        newLayout = generateCombinations(layoutName, actualLayout)
        writeToFile(newLayout)
    print("Generation of layout combinations completed")
