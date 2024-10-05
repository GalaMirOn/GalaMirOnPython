first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(f_s) for f_s in first_strings if len(f_s) >= 5]
print(first_result)

second_result = [(f_s, s_s) for f_s in first_strings for s_s in second_strings if len(f_s) == len(s_s)]
print(second_result)

proba = first_strings + second_strings
third_result = {x: len(x) for x in first_strings + second_strings if not len(x) % 2}
print(third_result)
