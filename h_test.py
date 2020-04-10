import p_value as stat

def test_hypothesis(h_zero, h, sample_mean, population_mean, std_dev, sample_size):
    z_s = stat.cal_z_score()