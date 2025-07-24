def conformality_residual_v2(Z_field, dx, dt):
    """
    Improved conformality metric with gradient normalization
    """
    u = Z_field.real
    v = Z_field.imag
    
    # Spatiotemporal derivatives
    du_dt = np.gradient(u, dt, axis=0)
    dv_dx = np.gradient(v, dx, axis=1)
    dv_dt = np.gradient(v, dt, axis=0)
    du_dx = np.gradient(u, dx, axis=1)
    
    # Cauchy-Riemann residuals
    CR1 = (du_dt - dv_dx)**2
    CR2 = (dv_dt + du_dx)**2
    
    # Normalize by gradient power (as suggested)
    grad_Z = np.gradient(Z_field, dx, axis=1) + 1j * np.gradient(Z_field, dt, axis=0)
    gradient_power = np.mean(np.abs(grad_Z)**2)
    
    CR_normalized = np.mean(CR1 + CR2) / (gradient_power + 1e-10)
    
    return CR_normalized

def explore_conformality_islands():
    """
    Look for islands without assuming φ
    """
    # Ginzburg-Landau parameters
    A_range = np.linspace(-1, 1, 50)  # Crossing critical point
    B_range = np.linspace(0.1, 2, 50)
    
    conformality_map = np.zeros((50, 50))
    
    for i, A in enumerate(A_range):
        for j, B in enumerate(B_range):
            Z_traj = simulate_GL(A, B)
            conformality_map[i,j] = conformality_residual_v2(Z_traj)
    
    # Find islands (local minima)
    from scipy.ndimage import label
    islands = conformality_map < np.percentile(conformality_map, 10)
    labeled_islands, num_islands = label(islands)
    
    print(f"Found {num_islands} conformality islands")
    
    # Analyze each island
    for island_id in range(1, num_islands + 1):
        mask = labeled_islands == island_id
        A_island = A_range[np.where(mask)[0]]
        B_island = B_range[np.where(mask)[1]]
        
        # Check if any special ratios emerge
        if len(A_island) > 0 and len(B_island) > 0:
            ratio = np.mean(B_island) / (np.abs(np.mean(A_island)) + 1e-10)
            print(f"Island {island_id}: Ratio B/|A| = {ratio:.4f}")
    
    return conformality_map, labeled_islands
