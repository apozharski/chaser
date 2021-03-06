from continuous.chase import Chase
from continuous.actor import *

if __name__ == "__main__":
    c_actor = ChaseActor(x_i = random()*100-50,y_i = random()*100-50)
    s_actor = StationaryActor(x_i = random()*100-50,y_i = random()*100-50)
    chase = Chase(actor_list =[c_actor,s_actor],bounds = (100,100))
    print(chase.trial()[2])
