from network import QNetwork
import matplotlib.pyplot as plt


# one satellite repeater 
experiments1 = [[1200, 1200], [1400, 1400], [1600, 1600], [1800, 1800], [2000, 2000]]

# two repeaters (equidistant)
experiments2_eq = [[1200, 50, 1200], [1200, 100, 1200], [1200, 500, 1200], [1200, 1000, 1200], [1200, 2000, 1200]]

# two repeaters (not equidistant)
experiments2_neq = [[1200, 50, 2000], [1200, 100, 2000], [1200, 500, 2000], [1200, 1000, 2000], [1200, 2000, 2000]]


f1 = []
p1 = []

f2_eq = []
p2_eq = []

f2_neq = []
p2_neq = []

r1 = [e[0] for e in experiments1]
r2_eq = [e[1] for e in experiments2_eq]
r2_neq = [e[1] for e in experiments2_neq]


if __name__ == "__main__":
    for e in experiments1:
        qnet = QNetwork(link_lengths=e, alpha_st_gr=0.014, alpha_st=0.001)
        f1.append(qnet.get_fidelity())
        p1.append(qnet.get_photon_loss())
        # qnet.print_network()

    for e in experiments2_eq:
        qnet = QNetwork(link_lengths=e, alpha_st_gr=0.014, alpha_st=0.001)
        f2_eq.append(qnet.get_fidelity())
        p2_eq.append(qnet.get_photon_loss())
        # qnet.print_network()

    for e in experiments2_neq:
        qnet = QNetwork(link_lengths=e, alpha_st_gr=0.014, alpha_st=0.001)
        f2_neq.append(qnet.get_fidelity())
        p2_neq.append(qnet.get_photon_loss())
        # qnet.print_network()
    
    plt.figure(figsize=(8, 5))
    plt.plot(r1, f1, marker='o')
    plt.title("Total Fidelity with 1 Satellite Repeater")
    plt.xlabel("Distance Between Repeater and Ground Station (km)")
    plt.ylabel("Fidelity")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(r1, p1, marker='o')
    plt.title("Total Photon Loss with 1 Satellite Repeater")
    plt.xlabel("Distance Between Repeater and Ground Station (km)")
    plt.ylabel("Photon Loss (dB)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(r2_eq, f2_eq, marker='o')
    plt.title("Total Fidelity with 2 Satellite Repeaters (eq)")
    plt.xlabel("Distance Between Repeaters (km)")
    plt.ylabel("Fidelity")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(r2_eq, p2_eq, marker='o')
    plt.title("Total Photon Loss with 2 Satellite Repeaters (eq)")
    plt.xlabel("Distance Between Repeaters (km)")
    plt.ylabel("Photon Loss (dB)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(r2_neq, f2_neq, marker='o')
    plt.title("Total Fidelity with 2 Satellite Repeaters (eq)")
    plt.xlabel("Distance Between Repeaters (km)")
    plt.ylabel("Fidelity")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(r2_neq, p2_neq, marker='o')
    plt.title("Total Photon Loss with 2 Satellite Repeaters (eq)")
    plt.xlabel("Distance Between Repeaters (km)")
    plt.ylabel("Photon Loss (dB)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()