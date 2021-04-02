//2019 카카오 공채: 매칭 점수
//body에서만 연결관계가 존재하는 것이 아니라, header에서도 연결관계가 존재할 수 있음...

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Solution {
    class Page{
        String name;
        int pageIndex;
        int baseScore;
        float linkScore;
        ArrayList<String> linkPageName;

        public Page(String name, int pageIndex, int baseScore, ArrayList<String> linkPageName) {
            this.name = name;
            this.pageIndex = pageIndex;
            this.baseScore = baseScore;
            this.linkScore = 0.0F;
            this.linkPageName = linkPageName;
        }
    }

    public int solution(String word, String[] pages) {
        HashMap< String, Page > maapingTable = new HashMap<>();
        word = word.toLowerCase();

        Pattern namePattern = Pattern.compile("<meta property=\"og:url\" content=\"(\\S*)\"");
        Pattern linkPattern = Pattern.compile("<a href=\"https://(\\S*)\"");
        Pattern wordPattern = Pattern.compile("[a-z]+");

        Matcher haedMatcher = null;
        Matcher linkMatcher = null;
        Matcher wordMatcher = null;
        int index = 0;
        for( String page : pages ){
            page = page.toLowerCase();

            // HTML에서 해당 page의 이름을 추출
            haedMatcher = namePattern.matcher(page);
            haedMatcher.find();
            String pageName = haedMatcher.group().split("=")[2].replaceAll("\"", "");

            // HTML에서 해당 page가 참조하고있는 page의 이름을 추출
            ArrayList<String> linkPageName = new ArrayList<>();
            linkMatcher = linkPattern.matcher(page);
            while( linkMatcher.find() ){
                String link = linkMatcher.group().split("\"")[1];
                linkPageName.add( link );
            }


            String body = page.split("<body>")[1].split("</body>")[0];
            // HTML에서 해당 page에 존재하는 query word갯수를 counting
            int baseScore = 0;
            wordMatcher = wordPattern.matcher(body);
            while (wordMatcher.find()) {
                if( wordMatcher.group().equals( word ) ) baseScore += 1;
            }


            Page pageObject = new Page( pageName, index, baseScore, linkPageName);
            maapingTable.put( pageName, pageObject );

            index += 1;
        }

        // 모든 page에 대해서 연결점수를 계산(참조 되고있는 page에 해당페이지의 기본점수/연결갯수를 더함)
        for( String pageName : maapingTable.keySet() ){
            Page pageObject =  maapingTable.get( pageName );
            float score = (float) pageObject.baseScore / pageObject.linkPageName.size();

            for( String linkPageName : pageObject.linkPageName ){
                try{
                    Page linkPageObject = maapingTable.get( linkPageName );
                    linkPageObject.linkScore += score;
                }catch ( Exception e ){
                    continue;
                }
            }
        }

        int resultIndex = -1;
        float resultVal = -1;
        for( String pageName : maapingTable.keySet() ) {
            Page pageObject = maapingTable.get(pageName);

            if( pageObject.linkScore + pageObject.baseScore > resultVal){
                resultVal = pageObject.linkScore + pageObject.baseScore;
                resultIndex = pageObject.pageIndex;
            }else if( pageObject.linkScore + pageObject.baseScore == resultVal &&
                    resultIndex > pageObject.pageIndex ) resultIndex = pageObject.pageIndex;
        }


        return resultIndex;
    }
}