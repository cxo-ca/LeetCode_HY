# LeetCode Algorithm Practice

Python으로 자료구조와 알고리즘을 구현한 학습 저장소입니다. **문제 유형별 대표 풀이와 실제 코드를 바로 확인할 수 있도록** 정리했습니다.

## 대표 풀이

| 유형 | 코드 | 구현에서 확인할 내용 |
|---|---|---|
| Tree · BFS | [Binary Tree Level Order Traversal](0102-binary-tree-level-order-traversal/0102-binary-tree-level-order-traversal.py) | `deque`와 현재 레벨의 노드 수를 이용한 층별 탐색 |
| Graph · 위상 정렬 | [Course Schedule](0207-course-schedule/0207-course-schedule.py) | 진입 차수와 큐로 선수 과목 처리·사이클 여부 판단 |
| Dynamic Programming | [House Robber](0198-house-robber/0198-house-robber.py) | 인접 선택 제약을 반영한 상태 정의와 점화식 |
| Sliding Window | [Minimum Size Subarray Sum](0209-minimum-size-subarray-sum/0209-minimum-size-subarray-sum.py) | 양수 배열에서 합 조건에 따라 구간 축소 |
| Binary Search | [Binary Search](0704-binary-search/0704-binary-search.py) | 탐색 구간의 경계와 종료 조건 관리 |
| Backtracking | [Combination Sum](0039-combination-sum/0039-combination-sum.py) | 시작 인덱스로 조합 중복 방지·초과 합 가지치기 |
| Greedy | [Gas Station](0134-gas-station/0134-gas-station.py) | 전체 합으로 가능 여부를 확인하고 출발 후보 갱신 |
| Stack · Queue | [Implement Queue Using Stacks](0232-implement-queue-using-stacks/0232-implement-queue-using-stacks.py) | 입력·출력 스택을 분리해 FIFO 동작 구현 |

## 다른 풀이

- **Tree / Graph:** [Maximum Depth](0104-maximum-depth-of-binary-tree/) · [Diameter](0543-diameter-of-binary-tree/) · [Subtree](0572-subtree-of-another-tree/) · [Number of Provinces](0547-number-of-provinces/) · [Surrounded Regions](0130-surrounded-regions/)
- **DP:** [Unique Paths](0062-unique-paths/) · [Minimum Path Sum](0064-minimum-path-sum/) · [House Robber II](0213-house-robber-ii/) · [Min Cost Climbing Stairs](0746-min-cost-climbing-stairs/) · [Counting Bits](0338-counting-bits/)
- **Search / Array:** [Search Insert Position](0035-search-insert-position/) · [Rotated Sorted Array](0153-find-minimum-in-rotated-sorted-array/) · [Longest Substring](0003-longest-substring-without-repeating-characters/)
- **Greedy:** [Lemonade Change](0860-lemonade-change/) · [Can Place Flowers](0605-can-place-flowers/) · [Maximum Units on a Truck](1710-maximum-units-on-a-truck/)
- **Linked List:** [Reverse Linked List](0206-reverse-linked-list/) · [Design Linked List](0707-design-linked-list/)

## 읽는 방법

각 문제 폴더의 `README.md`에는 문제 설명이, 같은 이름의 `.py` 파일에는 제출 코드가 있습니다. 위 대표 풀이 표는 Python 구현 파일로 연결됩니다.

코드는 LeetCode의 실행 환경을 기준으로 작성했습니다. `List`, `Optional`, `TreeNode`, `ListNode` 등 플랫폼이 제공하는 타입이나 정의가 생략된 파일은 로컬 실행 시 해당 정의를 추가해야 합니다.

복습할 때는 자료구조를 선택한 이유, 경계 조건, 시간·공간 복잡도를 함께 확인합니다.
