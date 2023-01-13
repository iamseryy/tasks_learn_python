# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

line = 'sdfsadf, dfsабв dffsdaf ыфвфыВ: ЫВаабввы'
line_result = ' '.join(list(filter(lambda item: not 'абв' in item, line.split())))
print(line)
print(line_result)