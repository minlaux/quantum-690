from network import QNetwork
import matplotlib.pyplot as plt

# base experiments with one satellite repeater
base_experiments = [[1200, 1200], [1400, 1400], [1600, 1600], [1800, 1800], [2000, 2000]]

# experiments for two satellite repeaters
experiments = [[1200, 50, 1200], [1200, 100, 1200], [1200, 500, 1200], [1200, 1000, 1200], [1200, 2000, 1200]]

# for base experiments
fidelities1 = []
mid_lengths1 = [sum(d) for d in base_experiments]

# for two-repeater experiments
fidelities2 = []
mid_lengths2 = [d[1] for d in experiments]


if __name__ == "__main__":
    for distances in base_experiments:
        qnet = QNetwork(link_lengths=distances, alpha_st_gr=0.02, alpha_st=0.002)
        fidelity = qnet.get_fidelity(k=0.001)
        qnet.print_network()

        fidelities1.append(fidelity)


    for distances in experiments:
        qnet = QNetwork(link_lengths=distances, alpha_st_gr=0.02, alpha_st=0.002)
        fidelity = qnet.get_fidelity(k=0.001)
        qnet.print_network()

        fidelities2.append(fidelity)

    plt.figure(figsize=(8, 5))
    plt.plot(mid_lengths1, fidelities1, marker='o')
    plt.title("Fidelity vs. Distance to Ground Station")
    plt.xlabel("Distance Between Repeater and Ground Station (km)")
    plt.ylabel("Fidelity")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(mid_lengths2, fidelities2, marker='o')
    plt.title("Fidelity vs. Two-Repeater Spacing")
    plt.xlabel("Distance Between Repeaters (km)")
    plt.ylabel("Fidelity")
    plt.grid(True)
    plt.tight_layout()
    plt.show()