// 연습문제: 최솟값 만들기

import java.util.Arrays;

class Solution
{
    public int solution(int []A, int []B)
    {
        Arrays.sort(A);
        Arrays.sort(B);

        int N = A.length;
        int answer = 0;
        for(int i = 0 ; i < N ; i++){
            answer += A[i] * B[N-i-1];
        }

        return answer;
    }
}