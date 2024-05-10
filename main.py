# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits


class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        if self.get_intent() is not None:
            return
        if self.kickoff_flag:
            self.set_intent(kickoff())
            return
        

       #Adding comment to see github change tracking
       #Adding 2nd comment to see github change tracking

        
        
        
        
        if self.me.boost > 20:
            self.set_intent(short_shot(self.foe_goal.location))
            return
        
        
#if car near goal and car near and behind of ball short shot
        car_goal =  (self.me.location - self.foe_goal.location).magnitude()
        car_ball = (self.ball.location - self.me.location ).magnitude()
        if (car_goal <2000) and (car_ball <2000) and not self.is_in_front_of_ball():
            self.set_intent(short_shot(self.foe_goal.location))
            return
    
            
            

            


        if self.is_in_front_of_ball():
            self.set_intent(goto(self.friend_goal.location))
            return     
           

        closest_boost = self.get_closest_large_boost()
        if closest_boost is not None:
            self.set_intent(goto(closest_boost.location))
            print("Going for boost",closest_boost)
            return
        

        #  #shooting
        # targets = {
        #     "at_opponent_goal": (self.foe_goal.left_post, self.foe_goal.right_post),
        #     "away_from_our_net": (self.friend_goal.right_post, self.friend_goal.left_post)
        # }

        # hits = find_hits(self,targets)
        # if len(hits["at_opponent_goal"]) > 0:
        #     self.set_intent(hits["at_opponent_goal"][0])
        #     print("at their goal")
        #     return
        # if len(hits["away_from_our_net"]) > 0:
        #     print("away_from_our_net")
        #     self.set_intent(hits["away_from_our_net"][0])
        #     return
        



























        # if len(available_boosts) > 0:
        #     self.set_intent(goto(available_boosts[0].location))
        #     print("going for boosts", available_boosts[0].index)
        #     return



        # d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        # d2 = abs(self.me.location.y - self.foe_goal.location.y)
        # is_in_front_of_ball = d1 > d2
        # if self.kickoff_flag:
        #     # set_intent tells the bot what it's trying to do
        #     self.set_intent(kickoff())
        #     return
        # # if we're in front of the ball, retreat
        # if is_in_front_of_ball:
        #     self.set_intent(goto(self.friend_goal.location))
        #     return
        # self.set_intent(short_shot(self.foe_goal.location))
    

        
