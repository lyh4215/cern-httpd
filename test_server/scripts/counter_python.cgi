#!/usr/bin/env python3

import cgi
import cgitb
import os
cgitb.enable()

print("Content-Type: text/html")
print()

counter_path = "/home/wonow/cern-httpd/test_server/count_data.txt"
count = 0
form = cgi.FieldStorage()
# POST 요청이면 카운터 증가
if os.environ.get("REQUEST_METHOD") == "POST":
    try:
        with open(counter_path, "r+") as f:
            count = int(f.read().strip())
            # 버튼 이름 구분
            if form.getvalue("action") == "up":
                count += 1
            elif form.getvalue("action") == "down":
                count -= 1
            f.seek(0)
            f.write(str(count))
            f.truncate()
    except Exception as e:
        print("<p><b>Error:</b> {}</p>".format(e))
else:
    # GET 요청이면 파일에서 읽기만
    try:
        with open(counter_path, "r") as f:
            count = int(f.read().strip())
    except Exception:
        count = 0  # 파일이 없으면 0으로 시작

# HTML 출력
print("""
<html>
  <body>
    <h1>Visitor count: {}</h1>
    <form method="POST" action="/cgi-bin/counter_python.cgi">
        <button type="submit" name="action" value="up">Up</button>
        <button type="submit" name="action" value="down">Down</button>
    </form>
  </body>
</html>
""".format(count))
