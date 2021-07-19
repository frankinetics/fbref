### Import necessary packages

import numpy as np
import pandas as pd
import pymc3 as pm
import seaborn as sb
import best as best
import scipy.stats
import statistics
from numba import jit
from math import lgamma
from scipy.stats import beta
from numba import jit
import matplotlib.pyplot as plt

### Bayesiam estimation supersedes the t-test function

def bayesian_estimation_supersedes_t_test(x, y, sd_low = "1", sd_high = "10"):
    
    y1 = x # Control data-frame
    y2 = y # Variant data-frame
    
    data = pd.DataFrame(dict(value=np.r_[y1, y2], group=np.r_[['y2']*len(y2), ['y1']*len(y1)])) # Concatenate
    
    μ_m = data.value.mean() # Prior: Group mean
    μ_s = data.value.std() * 2 # Prior: Group sd
    σ_low = sd_low # Prior: sd low
    σ_high = sd_high # Prior: sd high
    mean_control_1 = x.mean() # Mean Control
    sd_control = scipy.stats.tstd(x) # sd Control
    mean_NBA = y.mean() # Mean Variant
    sd_NBA = scipy.stats.tstd(y) # sd Variant

    print("The mean of the Control group was:",round(mean_control_1,2),". With a standard deviation of:",round(100*sd_control,2),".")
    print("The mean of the NBA group was:",round(mean_NBA,2),". With a standard deviation of:",round(100*sd_NBA,2),".")
    print("The relative difference between the NBA and Control group was:",round((100*(mean_NBA-mean_control_1)/mean_control_1),2),"%.")
    
    with pm.Model() as model:
        group1_mean = pm.Normal('group1_mean', mu = μ_m, sd = μ_s)
        group2_mean = pm.Normal('group2_mean', mu = μ_m, sd = μ_s)
        group1_std = pm.Uniform('group1_std', lower = σ_low, upper = σ_high)
        group2_std = pm.Uniform('group2_std', lower = σ_low, upper = σ_high)
        ν = pm.Exponential('ν_minus_one', 1/29.) + 1
        λ1 = group1_std**-2
        λ2 = group2_std**-2
        group1 = pm.StudentT('Control_1', nu = ν, mu = group1_mean, lam = λ1, observed = y1)
        group2 = pm.StudentT('NBA', nu = ν, mu = group2_mean, lam = λ2, observed = y2)
        diff_of_means = pm.Deterministic('difference of means', group2_mean - group1_mean)
        diff_of_stds = pm.Deterministic('difference of stds', group2_std - group1_std)
        effect_size = pm.Deterministic('effect size', diff_of_means / np.sqrt((group1_std**2 + group2_std**2) / 2))
        trace = pm.sample(5000)
        
    group_means = pm.plot_posterior(trace, var_names=['group2_mean','group1_mean', 'group1_std', 'group2_std', 'ν_minus_one'], color='#87ceeb'); 
    diff_means = pm.plot_posterior(trace, var_names=['difference of means','difference of stds', 'effect size'], ref_val=0, color='#87ceeb');
   
    return group_means, diff_means



### Beta calculations from jit


@jit
def h(a, b, c, d):
    num = lgamma(a + c) + lgamma(b + d) + lgamma(a + b) + lgamma(c + d)
    den = lgamma(a) + lgamma(b) + lgamma(c) + lgamma(d) + lgamma(a + b + c + d)
    return np.exp(num - den)

@jit
def g0(a, b, c):    
    return np.exp(lgamma(a + b) + lgamma(a + c) - (lgamma(a + b + c) + lgamma(a)))

@jit
def hiter(a, b, c, d):
    while d > 1:
        d -= 1
        yield h(a, b, c, d) / d

def g(a, b, c, d):
    return g0(a, b, c) + sum(hiter(a, b, c, d))

def calc_prob_between(beta1, beta2):
    return g(beta1.args[0], beta1.args[1], beta2.args[0], beta2.args[1])



### Bayesian conversion probabilities function


def bayesian_conversion_probabilities(n_control, n_variant, e_control, e_variant):
    a_control = e_control + 1
    b_control = n_control - (e_control + 1)
    beta_control = beta(a_control, b_control)
    a_variant = e_variant + 1
    b_variant = n_variant - (e_variant + 1)
    beta_variant = beta(a_variant, b_variant)
    uplift = (beta_variant.mean() - beta_control.mean())/beta_control.mean()
    prob = calc_prob_between(beta_variant, beta_control)
    
    print("The conversion rate of the control is:",round(e_control/n_control,4)*100,"%")
    print("The conversion rate of NBA variant is:",round(e_variant/n_variant,4)*100,"%")
    print("The relative uplift/decrease between NBA and Control group is:",round(uplift*100,4),"%")
    print("The probability that NBA beat Control is:",round(prob*100,5),"%")
    
    with pm.Model() as model:
    
        # Define priors (use the control pirior as the null hypothesis where no difference exists between variants)

        prior_control = pm.Beta('prior_control', alpha = e_control, beta = n_control - e_control)
        prior_variant = pm.Beta('prior_variant', alpha = e_variant, beta = n_variant - e_variant)

        # Define likelihood

        likelihood_control = pm.Binomial('like_control', n = n_control, p = prior_control, observed = e_control)
        likelihood_variant = pm.Binomial('like_variant', n = n_variant, p = prior_variant, observed = e_variant)

        # Define metrics

        pm.Deterministic('absolute difference', prior_variant - prior_control)
        pm.Deterministic('relative difference', (prior_variant / prior_control) - 1)

        # Inference using MCMC
        trace = pm.sample(draws = 20000, step = pm.Metropolis(), start = pm.find_MAP(), progressbar=True)
        
    _ = pm.traceplot(trace[1000:])
    group_convs = pm.plot_posterior(trace, var_names=['prior_control', 'prior_variant'], ref_val=0)
    diff_convs = pm.plot_posterior(trace[1000:], varnames=['absolute difference', 'relative difference'], 
                      ref_val=0, color='purple')
        
    return _, group_convs, diff_convs 
    
    
### Boxplot visualisation    
    
def bayes_t_test_boxplot(df):
    results = [] # create an empty list into which I insert the sampled means
    random_state = np.arange(0,1000) # random seeds for reproducibility
    df_filtered = df

    for i in range(1000):
        sample = df_filtered.sample(frac=0.5, replace=True, random_state=random_state[i]).groupby(by='model_version')['pvs_pb'].mean()
        results.append(sample)
        dist_samples = pd.DataFrame(results)
    
    plt.figure(figsize=(10,8))
    plot = dist_samples.boxplot()
    
    return plot
        
    
### Displot visualisation    
    
    
def bayes_t_test_displot(df):
    results = [] # create an empty list into which I insert the sampled means
    random_state = np.arange(0,1000) # random seeds for reproducibility
    df_filtered = df

    for i in range(1000):
        sample = df_filtered.sample(frac=0.5, replace=True, random_state=random_state[i]).groupby(by='model_version')['pvs_pb'].mean()
        results.append(sample)
        dist_samples = pd.DataFrame(results)
        
        
    for col in dist_samples:
        sb.distplot(dist_samples[col], hist=True)
        plot_2 = plt.show()    
        
    
    return plot_2