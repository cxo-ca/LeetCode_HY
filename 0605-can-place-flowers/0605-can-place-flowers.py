class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue

            left = (i == 0 or flowerbed[i - 1] == 0)    # 왼쪽이 비었는지 확인
            right = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)  # 오른쪽이 비었는지 확인

            if left and right:  # 양옆이 모두 빔
                flowerbed[i] = 1
                n -= 1

                if n == 0:  # 꽃 모두 심음
                    return True

        return n <= 0