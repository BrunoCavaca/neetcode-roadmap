class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined_arr = sorted(zip(position,speed),reverse=True)
        eta_arr = []

        for pos,speed in combined_arr:
            eta = (target-pos)/speed
            if not eta_arr:
                eta_arr.append(eta)
            elif eta > eta_arr[-1]:
                eta_arr.append(eta)
        
        return len(eta_arr)
