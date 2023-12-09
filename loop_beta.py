
betas = np.linspace(0, 2, num=11)
Algo_2_iteration_mumbers_array = []
for beta in betas:
    Algo_2_iteration_loop, Algo_2_resulting_vector_loop = RRR(y, A, b, beta=beta, max_iter=max_iter, tolerance=tolerance)
    Algo_2_iteration_mumbers_array.append(Algo_2_iteration_loop)

plt.plot(betas,Algo_2_iteration_mumbers_array)
plt.ylabel("Converged iterations number")
plt.xlabel("beta")

print(f"Algorithm 1(Alternative_Projections) Converged after {Algo_1_iteration} iterations.")
print(f"Algorithm 2(RRR) Converged after {Algo_2_iteration} iterations. with beta = 1")
plt.show()

