import random
import math


class QNode:
    def __init__(self, name, mem_capacity=0):
        self.name = name
        self.mem_capacity = mem_capacity
        self.memory = []


class QNetwork():
    def __init__(self, link_lengths: list, alpha_st_gr: float, alpha_st: float):
        """
        link_lengths: distances between each node from station A to station B (km)
        alpha_st_gr: attenuation loss coefficient between a satellite repeater and ground station
        alpha_st: attenuation loss coefficient between two satellite repeaters
        """
        self.link_lengths = link_lengths
        self.alpha_st_gr = alpha_st_gr
        self.alpha_st = alpha_st

        # fill network with nodes
        self.nodes = [QNode(name=f"Node_{i}") for i in range(len(link_lengths) + 1)]
    

    def get_fidelity(self, k):
        """
        Calculates total fidelity of the network.
        """
        #F(d)=F0e^-kd
        # assume perfect initial fidelity
        total_fidelity = 1.0

        for length in self.link_lengths:
            total_fidelity *= math.exp(-k * length)

        return total_fidelity


    def get_photon_loss(self):
        """
        Calculates total photon loss of the network.
        """
        total_loss = 1.0

        for i in range(len(self.link_lengths)):
            if (i == 0) or i == (len(self.link_lengths) - 1):
                alpha = self.alpha_st_gr
            else: 
                alpha = self.alpha_st

            p_transmit = 10 ** ((-alpha * self.link_lengths[i])/10)
            total_loss *= p_transmit
        
        return 1 - total_loss
    

    def print_network(self):
        print("Quantum Network Topology:")
        for i, node in enumerate(self.nodes):
            print(f"{node.name}")
            if i < len(self.link_lengths):
                print(f"  ↓ {self.link_lengths[i]} km")
        
        # print(f"Distance between ground stations: {self.link_lengths[0] + self.link_lengths[-1]} km")
        print(f"Estimated entanglement fidelity: {self.get_fidelity(k=0.1):.4e}")
        print(f"Estimated photon loss: {self.get_photon_loss():.4e} photons/sec")