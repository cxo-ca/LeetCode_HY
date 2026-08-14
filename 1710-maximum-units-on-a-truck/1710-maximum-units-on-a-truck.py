class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True) # 박스 1개당 실을 수 있는 unit 수가 많은 순대로 정렬
        total = 0

        for boxes, units in boxTypes:
            take = min(boxes, truckSize)    # 현재 실제로 실을 수 있는 박스 수

            total += take * units
            truckSize -= take

            if truckSize == 0:  # 트럭이 다 차면 종료
                break

        return total