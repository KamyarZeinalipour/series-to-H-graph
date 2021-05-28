import moduleV2

inputs = input('\n********\nplease enter your exel files,\nthey should be in \'.txt\',\nand also if you have more than one exel files seperate names with \',\' ,\nfor examples: \"input1, input2\",\nit\'s your turn: ')

for i in inputs.split(", "):
    print('it\'s "{}" turn to be analysed'.format(i))
    unana = moduleV2.Stats(i, '{}_{}'.format(i, 'output'))
    unana.calInAllRows()
    unana.save()
    print(("{} analysed successfully! :)").format(i))


