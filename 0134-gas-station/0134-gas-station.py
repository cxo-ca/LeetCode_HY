class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0   # 총 기름 양
        tank = 0    # 남아있는 기름 양
        start = 0   # 출발점

        for i in range(len(gas)):
            remain = gas[i] - cost[i]

            total += remain
            tank += remain

            if tank < 0:    # 남아있는 기름이 없을 때
                start = i + 1
                tank = 0

        if total < 0:   # 총 기름 양이 없을 때
            return -1

        return start