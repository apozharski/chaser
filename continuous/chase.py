from random import random
from continuous.actor import ChaseActor,StationaryActor

class Chase(object):
    """Chase class which implements the backbone of the continuous experiment."""
    def __init__(self,actor_list = [],bounds = (100,100),meet_threshold = 5.):
        self.actor_list = actor_list
        for actor in self.actor_list:
            actor.set_bounds(bounds)
        self.bounds = bounds
        self.threshold = meet_threshold
        self.moves = 0

    def move(self):
        """"""
        for actor in self.actor_list:
            actor.walk()
        
    def meet_check(self):
        """"""
        for act1 in self.actor_list:
            for act2 in self.actor_list:
                if act1!=act2 and ((act1.x-act2.x)**2 + (act1.y-act2.y)**2)**.5 < self.threshold:
                    return (act1,act2,self.moves)

        return None

    def step(self):
        """"""
        self.move()
        self.moves += 1
        meeting = self.meet_check()
        if meeting is not None:
            return meeting
        return None

    def trial(self):
        """"""
        meeting = None
        while meeting is None:
            meeting = self.step()
        return meeting

    def random_trial():
        #TODO implement this randomization to be bounds safe.
        pass
        


                    
    
