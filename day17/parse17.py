import requests


def mod():
    mod = ''
    while mod != 'easy' and mod != 'medium':
        try:
            mod = int(input('Chose mod:\nType 1 for easy mod\nType 2 for medium mod\nYou chose is: '))
            if mod == 1:
                mod = 'easy'
            elif mod == 2:
                mod = 'medium'
            else:
                print('Wrong chose')
        except ValueError:
            print('Wrong data Type. Please enter the number')
        url = f'https://opentdb.com/api.php?amount=12&category=18&difficulty={mod}&type=boolean'
    return url


def html_decode(s):
    """
    Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>.
    """
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
        )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s


def main():
    url = mod()
    result = []
    response = requests.get(url)
    data = response.json()
    approve = data.get('response_code')
    if approve != 0:
        print('Some kind of internet troubles. Cant connect to question server')
    else:
        items = data.get('results')
        for i in items:
            item_text = i.get("question")
            item_text = html_decode(item_text)
            item_answer = i.get('correct_answer')
            item_answer = html_decode(item_answer)

            result.append(
                {
                    'text': item_text,
                    'answer': item_answer
                }
            )
    return result


