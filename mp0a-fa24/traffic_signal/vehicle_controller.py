from enum import Enum, auto
import copy
from typing import List

class TLMode(Enum):
    GREEN=auto()
    YELLOW=auto()
    RED=auto()

class VehicleMode(Enum):
    Normal = auto()
    Brake = auto()
    Accel = auto()
    HardBrake = auto()

class State:
    x: float 
    y: float 
    theta: float 
    v: float 
    agent_mode: VehicleMode 

    def __init__(self, x, y, theta, v, agent_mode: VehicleMode):
        pass 

def decisionLogic(ego: State, other: State):
    output = copy.deepcopy(ego)

    # TODO: Edit this part of decision logic
    
    if ego.agent_mode != VehicleMode.Accel and (other.signal_mode == TLMode.GREEN):
        output.agent_mode = VehicleMode.Accel
    if ((other.signal_mode == TLMode.YELLOW ) or (other.signal_mode == TLMode.RED ))and (ego.x > other.x - 15 - 40 )and ( (ego.x < other.x - 40))and(ego.agent_mode != VehicleMode.HardBrake):
        output.agent_mode = VehicleMode.HardBrake
    # DO NOT CHANGE THIS
    assert not (other.signal_mode == TLMode.RED and (ego.x>other.x-20 and ego.x<other.x-15)), "Run Red Light"  
    assert not (other.signal_mode == TLMode.RED and (ego.x>other.x-15 and ego.x<other.x) and ego.v<1), "Stop at Intersection"

    return output 