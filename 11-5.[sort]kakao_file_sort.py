import re  # re 는 정규표현식(Regular expression)을 이용한 문자열 매칭에 사용되는 파이썬 라이브러리입니다. 그리고 특정 패턴의 문자열을 매칭하는 기능을 제공한다. 문자열에서 숫자 같은 특정 패턴을 매칭하는 기능 제공


def find_file_info(file):
    file_dict = {}  # {"img12.png": "img00012.png", }
    file_detail_dict = {} # {"head": "img", "number":00002, "tail": ".jpg" }

    numbers = re.findall("\d+", file)
    split_list = file.split(numbers[0])

    head = split_list[0]

    number = str(numbers[0])
    # number_zero = format(number, '05')  # number diverse from 0 to 99999

    tail = split_list[1]

    return (head, number, tail)

    '''
    file_str = f'{head}{number_zero}{tail}'

    file_detail_dict['head'] = head
    file_detail_dict['number'] = number_zero
    file_detail_dict['tail'] = tail
    file_detail_dict['original'] = file

    # file_dict[file] = (file_str, file_detail_dict)
    # file_dict[file] = file_str
    file_dict[file] = file_detail_dict

    print(file_dict)   # {'img12.png': ('img12.png', {'head': 'img', 'number': '00012', 'tail': '.png'})}
    return file_dict
    '''

def solution(files):
    answer = []
    file_list = []
    key_list = []
    values_list = []

    for file in files:
        file_dict = find_file_info(file)
        file_list.append(file_dict)

    print(file_list)
    file_list.sort(key=lambda x: (x[0], int(x[1])))
    print(f'sorted_file list: {file_list}')
    answer = [''.join(t) for t in file_list]
    print(answer)


    '''
    # make key info
    for file in file_list:
        key_list.extend(file.keys())

    print(f'key_list : {key_list}')
    # key_list : ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
    values_list.sort()

    print(f'values_list: {values_list}')
    '''
    return answer


def main():
    files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    solution(files)


if __name__ == "__main__":
    main()

