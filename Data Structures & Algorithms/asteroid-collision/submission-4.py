class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            popped = 0
            if a > 0:
                stack.append(a)
            else:
                while len(stack) > 0 and stack[-1] > 0 and popped < -a:
                    popped = stack.pop()
                if popped > -a:
                    stack.append(popped)   # survivor from stack wins, a is destroyed
                elif popped < -a:
                    stack.append(a)       
                

        return stack