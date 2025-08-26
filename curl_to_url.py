import yaml
import shlex
import json
import re

def parse_curl(curl_cmd: str):
    # 合并多行并去掉反斜杠
    curl_cmd = curl_cmd.replace("\\\n", " ").replace("\n", " ")
    tokens = shlex.split(curl_cmd)

    method = "get"
    url = ""
    headers = {}
    data = None

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == "curl":
            url = tokens[i + 1].strip("'\"")
            i += 1
        elif token in ("-H", "--header"):
            header = tokens[i + 1].strip("'\"")
            key, value = header.split(":", 1)
            headers[key.strip().lower()] = value.strip()
            i += 1
        elif token in ("--data", "--data-raw", "--data-binary"):
            data = tokens[i + 1].strip("'\"")
            method = "post"
            i += 1
        i += 1

    # 取 URL path，并去掉 admin-api
    path = re.sub(r"^https?://[^/]+", "", url)
    path = path.replace("/admin-api", "", 1)

    api_name = path.strip("/").split("/")[-1] if path.strip("/") else "default"
    case_name = f"{api_name}_case"

    body_json = None
    if data:
        try:
            body_json = json.loads(data)
        except Exception:
            body_json = {"raw": data}

    filtered_headers = {}
    for key in ["authorization", "content-type"]:
        if key in headers:
            filtered_headers[key] = headers[key]

    result = [
        {
            "base_info": {
                "api_name": api_name,
                "method": method,
                "url": path,
                "headers": filtered_headers
            },
            "testCase": [
                {
                    "case_name": case_name,
                    "json": body_json or {}
                }
            ]
        }
    ]
    return result


if __name__ == "__main__":
    print("按回车生成:")
    lines = []
    while True:
        line = input()
        if not line.strip():  # 空行 => 结束输入
            break
        lines.append(line)

    curl_input = "\n".join(lines)
    parsed = parse_curl(curl_input)
    print(yaml.dump(parsed, sort_keys=False, allow_unicode=True))
