import re  # re 는 정규표현식(Regular expression)을 이용한 문자열 매칭에 사용되는 파이썬 라이브러리입니다. 그리고 특정 패턴의 문자열을 매칭하는 기능을 제공한다. 문자열에서 숫자 같은 특정 패턴을 매칭하는 기능 제공


def find_file_info(file):
    numbers = re.findall("\d+", file)
    answer = file.split(numbers[0])

    head = answer[0]
    number = numbers[0]
    tail = answer[1]

    return (head, number, tail)


def solution(files):
    answer = []
    file_list = []
    key_list = []
    values_list = []

    for file in files:
        file_dict = find_file_info(file)
        file_list.append(file_dict)

    file_list.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(t) for t in file_list]
    print(f'sorted_file list: {answer}')

    return answer


def main():
    files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    solution(files)


if __name__ == "__main__":
    main()

