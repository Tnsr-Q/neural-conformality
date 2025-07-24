from mne import minimum_norm
import scipy.signal as signal

def analyze_consciousness_conformality(raw_eeg, forward_model, noise_cov):
    """
    Complete pipeline with inverse solution
    
    raw_eeg: MNE Raw object
    forward_model: Forward solution for source reconstruction
    noise_cov: Noise covariance for inverse solution
    """
    results = {}
    
    # Define frequency bands
    bands = {
        'theta': (4, 8),
        'alpha': (8, 12),
        'beta': (12, 30),
        'gamma': (30, 80),
        'high_gamma': (80, 150)
    }
    
    for band_name, (f_low, f_high) in bands.items():
        # 1. Band-pass filter
        filtered = raw_eeg.copy().filter(f_low, f_high)
        
        # 2. Solve inverse problem (sensor → source space)
        inverse_operator = minimum_norm.make_inverse_operator(
            filtered.info, forward_model, noise_cov
        )
        
        # Get source time courses
        stc = minimum_norm.apply_inverse_raw(
            filtered, inverse_operator, lambda2=1/9
        )
        
        # 3. Extract complex analytic signal in source space
        source_data = stc.data
        analytic_signal = signal.hilbert(source_data, axis=1)
        Z_field = analytic_signal
        
        # 4. Calculate conformality in source space
        # Now we have true spatial derivatives!
        dx = np.mean(np.diff(stc.vertices[0]))  # Vertex spacing
        dt = 1 / filtered.info['sfreq']
        
        CR = conformality_residual_v2(Z_field, dx, dt)
        
        # 5. Also calculate PLV in this band
        PLV = compute_source_space_PLV(Z_field)
        
        results[band_name] = {
            'conformality': CR,
            'PLV': PLV,
            'product': CR * PLV,
            'frequency_range': (f_low, f_high)
        }
    
    return results

def test_consciousness_states(subjects, states):
    """
    Test across different consciousness states
    """
    all_results = {}
    
    for subject in subjects:
        for state in ['awake', 'meditation', 'drowsy', 'REM', 'deep_sleep']:
            # Load data for this subject/state
            raw_eeg = load_subject_state(subject, state)
            
            # Run analysis
            results = analyze_consciousness_conformality(
                raw_eeg, 
                forward_models[subject],
                noise_covs[subject]
            )
            
            all_results[f"{subject}_{state}"] = results
    
    # Analyze patterns
    analyze_patterns(all_results)
    
    return all_results

def analyze_patterns(results):
    """Look for PQRG signatures"""
    # 1. Does gamma-band conformality correlate with consciousness?
    gamma_CRs = []
    consciousness_levels = []
    
    for key, data in results.items():
        state = key.split('_')[1]
        gamma_CR = data['gamma']['conformality']
        
        gamma_CRs.append(gamma_CR)
        
        # Assign consciousness level
        consciousness_map = {
            'awake': 1.0,
            'meditation': 0.8,  # Or higher?
            'drowsy': 0.5,
            'REM': 0.7,
            'deep_sleep': 0.2
        }
        consciousness_levels.append(consciousness_map[state])
    
    # Check correlation
    correlation = np.corrcoef(gamma_CRs, consciousness_levels)[0,1]
    print(f"Conformality-Consciousness Correlation: {correlation:.3f}")
    
    # 2. Check if CR × PLV ≈ constant
    products = [data['gamma']['product'] for data in results.values()]
    variance = np.var(products) / np.mean(products)**2
    print(f"Relative variance in CR×PLV: {variance:.3f}")
    
    # 3. Look for special values
    mean_product = np.mean(products)
    print(f"Mean CR×PLV: {mean_product:.6f}")
    print(f"Compare to Nr: {0.641926:.6f}")
    print(f"Ratio: {mean_product/0.641926:.3f}")
