import textwrap

def wrap(string, max_width):
    length = len(string) // max_width
    if len(string) % max_width != 0:
        length += 1
    start = 0
    end = max_width
    returned_string = ""
    for i in range(length):
        returned_string = returned_string + string[start:end] + "\n"
        start = end
        end += max_width
    return returned_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)