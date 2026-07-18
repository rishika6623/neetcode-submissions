class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mn = max(weights)
        mx = sum(weights)
        trial = 0

        def works(weights, days, trial):
            i = 0
            day = 1
            total = 0
            while i < len(weights) and day <= days:
                if total + weights[i]> trial:
                    total = weights[i]
                    day += 1
                else:
                    total += weights[i]

                i += 1

            return day <= days

            # print(days, i, trial, day < days)

            # if day > days and i < len(weights):
            #     return False
            # return True

        while mn < mx:
            trial = (mn+mx)//2
            print(mn, mx, trial)

            if works(weights, days, trial):
                mx = trial
            else:
                mn = trial + 1
        
        return mn

        