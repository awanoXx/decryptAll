import execjs

def get_anti_content(js_file):
    with open(js_file, 'r', encoding='utf-8') as f:
        script_code = f.read()
        anti_content = execjs.compile(script_code).call('getAntiContent',
                                     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36')
        print(anti_content)
    return f"{anti_content}"

if __name__ == '__main__':
    anti_content = get_anti_content('./pinduoduo-taobao_live.js')
