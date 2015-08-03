"""file exercise 1
"""

course_info = [
    ['A', '2', '良好'],
    ['B', '2', '优秀'],
    ['CD', '2', '良好']
]

if __name__ == '__main__':
    with open('test.txt', 'w') as f:
        for course in course_info:
            f.write("{}, {}, {}\n".format(*course))

    with open('test.txt', 'r') as f:
        for line in f:
            print(line[:-1].split(','))