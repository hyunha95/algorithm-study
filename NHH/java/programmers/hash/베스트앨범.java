package programmers.hash;

import java.util.*;

public class 베스트앨범 {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new String[]{"classic", "pop", "classic", "classic", "pop"}, new int[]{500, 600, 150, 800, 2500})));
        System.out.println(Arrays.toString(solution(new String[]{"classic"}, new int[]{500})));
    }

    public static int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> totalPlayCountByGenre = new HashMap<>();
        Map<String, List<Album>> albumsByGenre = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            totalPlayCountByGenre.put(genres[i], totalPlayCountByGenre.getOrDefault(genres[i], 0) + plays[i]);
            albumsByGenre.putIfAbsent(genres[i], new ArrayList<>());
            albumsByGenre.get(genres[i]).add(new Album(i, plays[i]));
        }

        List<String> sortedGenres = new ArrayList<>(totalPlayCountByGenre.keySet());
        Collections.sort(sortedGenres, (a, b) -> totalPlayCountByGenre.get(b) - totalPlayCountByGenre.get(a));

        List<Integer> answer = new ArrayList<>();
        for (String genre : sortedGenres) {
            List<Album> albums = albumsByGenre.get(genre);
            albums.sort(Comparator.comparing(Album::getPlayCount).reversed().thenComparing(Album::getIndex));
            for (int i = 0; i < Math.min(2, albums.size()); i++) {
                answer.add(albums.get(i).getIndex());
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }


    static class Album {
        int index;
        int playCount;

        public Album(int index, int playCount) {
            this.index = index;
            this.playCount = playCount;
        }

        public int getIndex() {
            return index;
        }

        public void setIndex(int index) {
            this.index = index;
        }

        public int getPlayCount() {
            return playCount;
        }

        public void setPlayCount(int playCount) {
            this.playCount = playCount;
        }
    }
//
//    public static int[] solution(String[] genres, int[] plays) {
//        Map<String, Integer> genreRank = new HashMap<>();
//        Map<String, List<Album>> albumRank = new HashMap<>();
//
//        // 데이터 초기화
//        for (int i = 0; i < genres.length; i++) {
//            genreRank.put(genres[i], genreRank.getOrDefault(genres[i], 0) + plays[i]);
//            albumRank.putIfAbsent(genres[i], new ArrayList<>());
//            albumRank.get(genres[i]).add(new Album(i, plays[i]));
//        }
//
//        // 장르별 총 재생 횟수에 따라 장르 정렬
//        List<String> sortedGenres = new ArrayList<>(genreRank.keySet());
//        sortedGenres.sort((a, b) -> genreRank.get(b) - genreRank.get(a));
//
//        List<Integer> ans = new ArrayList<>();
//
//        // 각 장르 내에서 앨범 정렬 및 상위 2곡 선택
//        for (String genre : sortedGenres) {
//            List<Album> genreAlbum = albumRank.get(genre);
//            Collections.sort(genreAlbum);
//            for (int i = 0; i < Math.min(2, genreAlbum.size()); i++) {
//                ans.add(genreAlbum.get(i).idx);
//            }
//        }
//
//        // 결과를 배열로 반환
//        return ans.stream().mapToInt(Integer::intValue).toArray();
//    }
//
//
//    static class Album implements Comparable<Album> {
//        int idx, playCnt;
//
//        public Album(int idx, int playCnt) {
//            this.idx = idx;
//            this.playCnt = playCnt;
//        }
//
//        @Override
//        public int compareTo(Album album) {
//            if (this.playCnt == album.playCnt) {
//                return this.idx - album.idx;
//            } else {
//                return album.playCnt - this.playCnt;
//            }
//        }
//    }
}
