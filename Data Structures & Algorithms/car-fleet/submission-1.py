class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p, s in zip(position,speed)]
        pair.sort(reverse=True)

        count = 1
        curfleet = (target-pair[0][0]) / pair[0][1]

        for i in range(1,len(position)):
            time = (target-pair[i][0])/pair[i][1]
            if time > curfleet:
                count +=1
                curfleet = time

        return count