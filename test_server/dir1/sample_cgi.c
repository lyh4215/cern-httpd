// hello.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    // CGI 출력: 반드시 이 Content-type 헤더가 먼저 출력돼야 함!
    printf("Content-Type: text/html\r\n\r\n");

    // 환경변수에서 QUERY_STRING 읽기
    char *query = getenv("QUERY_STRING");
    char name[100] = "world";

    if (query && sscanf(query, "name=%99s", name) == 1) {
        // '+'를 공백으로 바꾸기 (간단한 디코딩)
        for (char *p = name; *p; p++) {
            if (*p == '+') *p = ' ';
        }
    }

    // HTML 응답 출력
    printf("<html><body>\n");
    printf("<h1>Hello, %s!</h1>\n", name);
    printf("</body></html>\n");

    return 0;
}
