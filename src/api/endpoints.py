from fastapi import APIRouter
import os


router = APIRouter()


@router.get("/Deep Q-Networks: Write up", tags=["RL Research"])
def DQN_info():
    """
    Provides information about the Deep Q-Network (DQN) algorithm.
    
    This endpoint returns details such as the name of the algorithm, 
    a link to the research resource, and a brief description of 
    DQN's implementation and significance in the field of deep 
    reinforcement learning.
    """
    return { 
        "Algorithm": "Deep Q-Networks",
        "Research": "https://damareh-reflections.notion.site/Deep-Q-Networks-2513fa3a39ac804e87c9ed2e76c92866", 
        "Description": "Deep Q-Network (DQN) is a seminal algorithm in deep reinforcement learning that successfully combined Q-learning (which is a model free algorithm that learns purely from experience by trying different actions and seeing their results) with deep neural networks to handle complex problems with high-dimensional state spaces." 
    }

@router.post("/Deep Q-Networks", tags=["RL Research"])
def DQN():
    """
    
    """

