
xtitles = {
    'v_gene' : '',
    'd_gene' : '',
    'j_gene' : '',
    'hamming_to_true_naive' : 'hamming',
    'v_hamming_to_true_naive' : 'hamming',
    'd_hamming_to_true_naive' : 'hamming',
    'j_hamming_to_true_naive' : 'hamming',
    'v_hamming_to_true_naive_normed' : '% hamming',
    'd_hamming_to_true_naive_normed' : '% hamming',
    'j_hamming_to_true_naive_normed' : '% hamming',
    'd_3p_del' : 'bases',
    'd_5p_del' : 'bases',
    'dj_insertion' : 'bases',
    'dj_insertion_content' : '',
    'j_5p_del' : 'bases',
    'mute_freqs' : 'mutation freq',
    'v_3p_del' : 'bases',
    'vd_insertion' : 'bases',
    'vd_insertion_content' : '',
    'all-mean-freq' : 'mutation freq',
    'v-mean-freq' : 'mutation freq',
    'd-mean-freq' : 'mutation freq',
    'j-mean-freq' : 'mutation freq',
    
}

plot_titles = {
    'v_gene' : 'V gene',
    'd_gene' : 'D gene',
    'j_gene' : 'J gene',
    'hamming_to_true_naive' : 'HTTN',
    'v_hamming_to_true_naive' : 'V HTTN',
    'd_hamming_to_true_naive' : 'D HTTN',
    'j_hamming_to_true_naive' : 'J HTTN',
    'v_hamming_to_true_naive_normed' : 'V HTTN',
    'd_hamming_to_true_naive_normed' : 'D HTTN',
    'j_hamming_to_true_naive_normed' : 'J HTTN',
    'd_3p_del' : 'D 3p del',
    'd_5p_del' : 'D 5p del',
    'dj_insertion' : 'DJ insert length',
    'dj_insertion_content' : 'DJ insert base content',
    'j_5p_del' : 'J 5p del',
    'mute_freqs' : 'sequence mutation freq',
    'v_3p_del' : 'V 3p del',
    'vd_insertion' : 'VD insert length',
    'vd_insertion_content' : 'VD insert base content',
    'all-mean-freq' : 'sequence mutation freq',
    'v-mean-freq' : 'V mutation freq',
    'd-mean-freq' : 'D mutation freq',
    'j-mean-freq' : 'J mutation freq',
}

true_vs_inferred_hard_bounds = {
    'hamming_to_true_naive' : (-0.5, 19.5),
    'v_hamming_to_true_naive' : (-0.5, 8.5),
    'd_hamming_to_true_naive' : (-0.5, 10.5),
    'j_hamming_to_true_naive' : (-0.5, 12.5),
    'v_hamming_to_true_naive_normed' : (-0.5, 8.5),
    'd_hamming_to_true_naive_normed' : (-0.5, 50.5),
    'j_hamming_to_true_naive_normed' : (-0.5, 20),
    'd_3p_del' : (-8.5, 8.5),
    'd_5p_del' : (-8.5, 8.5),
    'dj_insertion' : (-10.5, 15.5),
    'j_5p_del' : (-10.5, 15.5),
    'mute_freqs' : (-.05, .05),  # NOTE make sure you know where the decimal place is here!
    'v_3p_del' : (-3.5, 3.5),
    'vd_insertion' : (-8.5, 8.5)}

default_hard_bounds = {
    # 'hamming_to_true_naive' : (-0.5, 19.5),
    'hamming_to_true_naive' : (-0.5, 10),
    'v_hamming_to_true_naive' : (-0.5, 8.5),
    'd_hamming_to_true_naive' : (-0.5, 10.5),
    'j_hamming_to_true_naive' : (-0.5, 12.5),
    'v_hamming_to_true_naive_normed' : (-0.5, 8.5),
    'd_hamming_to_true_naive_normed' : (-0.5, 50.5),
    'j_hamming_to_true_naive_normed' : (-0.5, 20),
    'd_3p_del' : (-1, 15),
    'd_5p_del' : (-1, 18),
    'dj_insertion' : (-1, 13),
    'jf_insertion' : (-1, 13),
    'fv_insertion' : (-1, 13),
    'j_5p_del' : (-1, 15),
    'all-mean-freq' : (0.0, 0.25),  # NOTE make sure you know where the decimal place is here!
    'v-mean-freq' : (0.0, 0.25),  # NOTE make sure you know where the decimal place is here!
    'd-mean-freq' : (0.0, 0.4),  # NOTE make sure you know where the decimal place is here!
    'j-mean-freq' : (0.0, 0.3),  # NOTE make sure you know where the decimal place is here!
    'v_3p_del' : (-1, 6),
    'vd_insertion' : (-1, 15),
    'IGHJ6*02' : (-0.5, 39.5),
    'IGHJ3*02' : (-0.5, 26),
    'IGHJ1*01' : (-0.5, 28),
    'IGHJ2*01' : (-0.5, 28),
    'IGHJ3*01' : (-0.5, 25),
    'IGHJ4*01' : (-0.5, 23),
    'IGHJ4*02' : (-0.5, 24),
    'IGHJ4*03' : (-0.5, 24),
    'IGHJ5*01' : (-0.5, 27),
    'IGHJ5*02' : (-0.5, 28)
    # 'IGHV3-23D*01' : (260, 296),
    # 'IGHV3-33*06' : (260, 296)
}
