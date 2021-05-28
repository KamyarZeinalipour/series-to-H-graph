import moduleV2

inputs = input('/ecg.xlsx')
for i in inputs.split(", "):
    print('it\'s "{}" turn to be analysed'.format(i))
    unana = moduleV2.Stats(i, '{}_{}'.format(i, 'output'))
    unana.calInAllRows()
    unana.save()
    print(("{} analysed successfully! :)").format(i))


