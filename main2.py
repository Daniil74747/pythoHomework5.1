from main import Student, Worker
import inspect

studentDates = inspect.signature(Student)
workerDates = inspect.signature(Worker)

print('Attributes(Student): ')
for item in studentDates.parameters.keys():
    print(item)


print('Methods(Student): ')
for method in dir(Student):
    if method.startswith('info'):
        print(method)

print('Attributes(Worker): ')
for item in workerDates.parameters.keys():
    print(item)

print('Methods(Worker): ')
for method in dir(Worker):
    if method.startswith('info'):
        print(method)
