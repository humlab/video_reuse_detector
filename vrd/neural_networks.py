"""Contains specification for the available neural networks for use in the VRD
"""
from enum import Enum
from dataclasses import dataclass
from typing import Any

from tensorflow import keras
from keras.applications import EfficientNetB4


class NeuralNetworks(Enum):
    """Enum for the different Neural Networks available"""

    efficientnetb4 = 0


@dataclass
class Network:
    """Specifics on the netowork used.
    This includes:
        * Used network and model 
        * Target size of images before prediction (Can be changed to some degree)
        * Which layer should be extracted  (Can be changed). This can be either by name, or index.
            If name is used, index will be ignored and will not be considered.


    """

    network_enum: Any
    used_network: Any
    used_model: Any
    target_size: tuple
    default_layer: int
    stop_at_layer: str = None

    def __str__(self):
        return f"Neural network used: {self.used_network}\nModel used:{self.used_model}\nInput size: {self.target_size}\nLayer used: {self.default_layer}\nStop at layer: {self.stop_at_layer}"


def get_network(network: NeuralNetworks) -> Network:
    """Gets a neural network including default settings

    Args:
        network (NeuralNetworks): The network to get, available in the NeuralNetworks enum

    Raises:
        Exception: If the enum is invalid

    Returns:
        Network: A Network class describing the desired network
    """

    if network is NeuralNetworks.efficientnetb4:
        return Network(
            network_enum=network,
            used_network=EfficientNetB4,
            used_model=EfficientNetB4(weights="imagenet"),
            target_size=(380, 380),
            default_layer=463,
            stop_at_layer="block7b_se_squeeze",
        )
    raise Exception("No such network type!")  # Add valid exception
