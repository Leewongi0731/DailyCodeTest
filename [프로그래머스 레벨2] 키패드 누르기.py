// 2020 카카오 인턴십: 키패드 누르기

class Solution {
    public String solution(int[] numbers, String hand) {
        int [][] cost = {
                //0 1  2  3  4  5  6  7  8  9
                {0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 9, 9},
                {4, 0, 1, 2, 1, 2, 3, 2, 3, 4, 9, 9},
                {3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 9, 9},
                {4, 2, 1, 0, 3, 2, 1, 4, 3, 2, 9, 9},
                {3, 1, 2, 3, 0, 1, 2, 1, 2, 3, 9, 9},
                {2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 9, 9},
                {3, 3, 2, 1, 2, 1, 0, 3, 2, 1, 9, 9},
                {2, 2, 3, 4, 1, 2, 3, 0, 1, 2, 9, 9},
                {1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 9, 9},
                {2, 4, 3, 2, 3, 2, 1, 2, 1, 0, 9, 9},
                {1, 3, 4, 5, 2, 3, 4, 1, 2, 3, 9, 9}, // *
                {1, 5, 4, 3, 4, 3, 2, 3, 2, 1, 9, 9}, // #
        };

        String answer = "";

        int left = 10;
        int right = 11;
        int leftCost, rightCost;
        for( int number: numbers ) {
            leftCost = cost[left][number];
            rightCost = cost[right][number];

            // 우선적으로 누를 것
            if (number == 1 || number == 4 || number == 7) leftCost = -1;
            else if (number == 3 || number == 6 || number == 9) rightCost = -1;

            // 중간 값(2,5,9,0)에 대해서는 가까운 손이 누름
            if (leftCost == rightCost && hand.equals("left")) leftCost = -1;
            else if (leftCost == rightCost && hand.equals("right")) rightCost = -1;


            if (leftCost < rightCost) {
                left = number;
                answer += "L";
            } else if (leftCost > rightCost) {
                right = number;
                answer += "R";
            }
        }

        return answer;
    }
}