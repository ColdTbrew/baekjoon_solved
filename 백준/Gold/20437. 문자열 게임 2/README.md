# [Gold V] 문자열 게임 2 - 20437 

[문제 링크](https://www.acmicpc.net/problem/20437) 

### 성능 요약

메모리: 132756 KB, 시간: 332 ms

### 분류

문자열, 슬라이딩 윈도우

### 제출 일자

2025년 8월 1일 10:03:52

### 문제 설명

<p>작년에 이어 새로운 문자열 게임이 있다. 게임의 진행 방식은 아래와 같다.</p>

<ol>
	<li>알파벳 소문자로 이루어진 문자열 W가 주어진다.</li>
	<li>양의 정수 K가 주어진다.</li>
	<li>어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.</li>
	<li>어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.</li>
</ol>

<p>위와 같은 방식으로 게임을 T회 진행한다.</p>

### 입력 

 <p>문자열 게임의 수 T가 주어진다. (1 ≤ T ≤ 100)</p>

<p>다음 줄부터 2개의 줄 동안 문자열 W와 정수 K가 주어진다. (1 ≤ K ≤ |W| ≤ 10,000) </p>

### 출력 

 <p>T개의 줄 동안 문자열 게임의 3번과 4번에서 구한 연속 문자열의 길이를 공백을 사이에 두고 출력한다.</p>

<p>만약 만족하는 연속 문자열이 없을 시 -1을 출력한다.</p>

