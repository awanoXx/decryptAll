from Crypto.Cipher import AES
from binascii import unhexlify


def decrypt_aes(data, key, iv):
    # 使用 128 位密钥长度
    key = key[:16].encode('utf-8')

    # 将十六进制格式的数据转换为二进制格式
    data = unhexlify(data)

    # 创建 AES cipher 对象
    cipher = AES.new(key, AES.MODE_CBC, iv.encode('utf-8'))

    # 执行解密
    decrypted = cipher.decrypt(data)

    # 去除填充 (PKCS#7)
    padding_len = decrypted[-1]
    decrypted = decrypted[:-padding_len]

    return decrypted.decode('utf-8')

if __name__ == '__main__':
    # 输入加密字符串
    encrypted_string = 'D6362C89ECF83B622D20161D1EDA0C05C5BB2175B380C21A73CE9E538B479EA0B966CB5D7D2E7D0CB6138F1301A90E8F368DA14C15EEA6E98BB7221DDAF9DE5AEFE1595BCB3A413DAA979735C0D79313E5BAA9DBB375E2173FA9D14DD3D1446D1E868E6F0AE60AB3641098557DFD897F544B8FAB8EB93877EC00D0A0819559E5AF9AAD7BC08DF37454E6A102D1634ED30274B5CF07577498BA40B19EFAFF8E308C1C1C7C90075C4874C64BA271B69F26DF066A8C80831F61F91EBF0C1D22B52CD9561C91F801669F8046DA9F5E4CDB7B641AF040D60B27EBD326045972903AC8F5F584DE45C29F0C4ED697F3DA8C3CBB3C85937018F2D19968BFF53AC60948D95FD26B26A8605D9B00CA5BCEE5CC7556BC9AA16935CAF239DFB27DE06BA2EAE3B2756A0A0343AEF43F228281C0872582'
    iv = '4kYBk36s496zC82w'
    key = 'w28Cz694s63kBYk4'

    # 执行解密
    decrypted_text = decrypt_aes(encrypted_string, key, iv)
    print(decrypted_text)
