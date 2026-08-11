class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:    # 안 거슬러 줘도 됨
                five += 1

            elif bill == 10: # 5달러 거슬러 줘야 함
                if five == 0:
                    return False
                
                five -= 1
                ten += 1

            else:   # if bill == 20, 15달러 거슬러 줘야 함
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1

                elif five >= 3:
                    five -= 3

                else:
                    return False
        return True