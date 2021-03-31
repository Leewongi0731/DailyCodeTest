// 2020 카카오 인턴십: 경주로 건설
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    class Pos{
        int i,j,c, d;
        public Pos(int i, int j , int c, int d ){
            this.i=i;
            this.j=j;
            this.c=c;
            this.d=d;
        }
    }


    public int solution(int[][] board) {
        // 직선 도로 하나를 만들 때는 100원이 소요
        // 코너를 하나 만들 때는 500원
        int N = board.length;
        int[][][] cost = new int[N][N][4];
        for( int i =0; i < N ; i++ ){
            for(int j =0 ;j <N;j++){
                cost[i][j][0] = cost[i][j][1] = cost[i][j][2] = cost[i][j][3] = 1234567890;
            }
        }

        int nextI, nextJ;
        // 위 / 아래 / 왼 / 오
        int[] mx = {-1,1,0,0};
        int[] my = {0,0,-1,1};

        Queue< Pos > queue = new LinkedList<>();
        queue.add( new Pos(0,0,0,1) );
        queue.add( new Pos(0,0,0,3) );
        cost[0][0][0] = cost[0][0][1] = cost[0][0][2] = cost[0][0][3] = 0;

        while( !queue.isEmpty() ){
            Pos pos = queue.poll();

            for( int d=0 ; d <4 ; d++ ){
                nextI = pos.i + mx[d];
                nextJ = pos.j + my[d];
                if( 0<=nextI && 0<=nextJ && nextI<N && nextJ<N && board[nextI][nextJ]==0){
                    if( d!=pos.d && pos.c+6 < cost[nextI][nextJ][d] ){
                        cost[nextI][nextJ][d] = pos.c+6;
                        queue.add( new Pos(nextI,nextJ,cost[nextI][nextJ][d], d) );
                    }
                    else if( d==pos.d && pos.c+1 < cost[nextI][nextJ][d] ){
                        cost[nextI][nextJ][d] = pos.c+1;
                        queue.add( new Pos(nextI,nextJ, cost[nextI][nextJ][d], d) );
                    }
                }
            }

        }


        int answer = 1234567890;
        for(int i=0; i<4; i++){
            if( answer > cost[N-1][N-1][i] ){
                answer = cost[N-1][N-1][i];
            }
        }
        return answer * 100;
    }
}