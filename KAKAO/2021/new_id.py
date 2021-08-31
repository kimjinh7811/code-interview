import re

def solution(new_id):
    answer = ''
    

    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9\-\_\.]', '', new_id)
    new_id = re.sub('\.{2,}', '.', new_id)
    new_id = re.sub('^\.|\.$', '', new_id)
    new_id = 'a' if not new_id else new_id
    new_id = new_id[:15] if len(new_id) > 15 else new_id
    new_id = re.sub('\.$', '', new_id)
    
    while len(new_id) <= 2:
        new_id += new_id[-1]

    answer = new_id

    return answer


test_case = [
    # ["...!@BaT#*..y.abcdefghijklm", "bat.y.abcdefghi"],
    # ["z-+.^.", "z--"],
    # ["=.=", "aaa"],
    # ["123_.def", "123_.def"],
    ["abcdefghijklmn.p", "abcdefghijklmn"]
]

for t1, ans in test_case:
    a = solution(t1)
    print(a == ans)