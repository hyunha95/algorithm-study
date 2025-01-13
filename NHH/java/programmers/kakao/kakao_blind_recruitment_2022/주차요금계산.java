package programmers.kakao.kakao_blind_recruitment_2022;

import java.time.LocalTime;
import java.util.*;
import java.util.stream.Collectors;

public class 주차요금계산 {

    public static void main(String[] args) {
        int[] fees = {180, 5000, 10, 600};
        String[] records = {"05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"};
        System.out.println(Arrays.toString(solution(fees, records)));
    }

    public static int[] solution(int[] fees, String[] records) {
        int baseMinute = fees[0];
        int basePrice = fees[1];
        int perMinute = fees[2];
        int perMinutePrice = fees[3];

        Map<String, List<DriveRecord>> driveRecordsByCarNumber = Arrays.stream(records)
                .map(DriveRecord::new)
                .collect(Collectors.groupingBy(dr -> dr.carNumber));

        Map<Integer, Integer> map = new HashMap<>();
        for (String carNumber : driveRecordsByCarNumber.keySet()) {
            int totalMinute = 0;
            for (DriveRecord dr : driveRecordsByCarNumber.get(carNumber)) {
                if (dr.desc.equals("IN")) {
                    totalMinute -= dr.minute;
                } else {
                    totalMinute += dr.minute;
                }

            }

            if (driveRecordsByCarNumber.get(carNumber).size() % 2 != 0) {
                totalMinute += 23 * 60 + 59;
            }


            int price = basePrice + (int) Math.ceil((totalMinute > baseMinute ? totalMinute - baseMinute : 0) / (double) perMinute) * perMinutePrice;
            map.put(Integer.parseInt(carNumber), price);
        }

        return map.entrySet().stream()
                .sorted(Map.Entry.comparingByKey())
                .map(Map.Entry::getValue)
                .mapToInt(Integer::intValue)
                .toArray();
    }

    static class DriveRecord {
        int minute;
        String carNumber;
        String desc;

        public DriveRecord(String record) {
            String strTime = record.split(" ")[0].split(":")[0];
            String minuteTime = record.split(" ")[0].split(":")[1];

            this.minute = Integer.parseInt(strTime) * 60 + Integer.parseInt(minuteTime);
            this.carNumber = record.split(" ")[1];
            this.desc = record.split(" ")[2];
        }
    }
}
