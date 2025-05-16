import math


class QNode:
    def __init__(self, name, link_length, mem_capacity=0):
        self.name = name
        self.link_length = link_length # to next node
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
        # station A
        self.nodes = [QNode(name="A", link_length=link_lengths[0])]

        # satellite repeaters
        for i in range(1, len(link_lengths) - 1):
            self.nodes.append(QNode(name="S", link_length=link_lengths[i]))

        # station B
        self.nodes.append(QNode(name="B", link_length=None))
    

    def get_fidelity(self, k=0.001):
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

        for i in range(len(self.nodes) - 1):
            if (i == 0) or i == (len(self.nodes) - 2):
                alpha = self.alpha_st_gr
            else: 
                alpha = self.alpha_st

            p_transmit = 10 ** ((-alpha * self.nodes[i].link_length)/10)
            total_loss *= p_transmit
        
        return 1 - total_loss
    

    def print_network(self):
        print("Network Topology:")
        for i, node in enumerate(self.nodes):
            print(f"{node.name}")
            if i < len(self.link_lengths):
                print(f"  ↓ {self.link_lengths[i]} km")
        
        print(f"Estimated entanglement fidelity: {self.get_fidelity():.4e}")
        print(f"Estimated photon loss: {self.get_photon_loss():.4e} dB")
