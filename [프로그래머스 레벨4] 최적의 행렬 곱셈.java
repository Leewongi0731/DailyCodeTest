// 연습문제: 최적의 행렬 곱셈

import java.util.ArrayList;

class Solution {
    int[][] dp = null;
    ArrayList<Integer> data = new ArrayList<>();

    public int solution(int[][] matrix_sizes) {
        int N = matrix_sizes.length;

        for( int i=0; i<N; i++ )  data.add( matrix_sizes[i][0] );
        data.add( matrix_sizes[N-1][1] );

        dp = new int[N+1][N+1];
        return getDp(1, N);
    }


    private int getDp( int i, int j ){
        if( i==j ) return 0;
        if (dp[i][j]!=0) return dp[i][j];

        dp[i][j] = Integer.MAX_VALUE;
        for(int k=i ; k<j ; k++){
            dp[i][j] = Math.min(
                    dp[i][j],
                    getDp(i, k) + getDp(k+1, j) + data.get(i-1) * data.get(k) * data.get(j)
            );
        }

        return dp[i][j];
    }
}