import  csv

with open('output.csv', 'w') as file:
    file.write('id, name, category,\n')
    records = ['1, ahmed, software engineer', '2, Helena, Cyber Security']

    for count in range(2):
        id = int(input('Please Enter your id'))
        name = input('PLease enter your name')
        category = input('please enter job category')

        file.write(f'{id}, {name}, {category}\n')


