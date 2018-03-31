import SurvivalModelClasses as Cls
import scr.SamplePathClass as SamplePathSupport
import scr.FigureSupport as Fig
import scipy.stats as stat

MORTALITY_PROB = 0.1    # annual probability of mortality
TIME_STEPS = 100        # simulation length
SIM_POP_SIZE = 1000     # population size of the simulated cohort
ALPHA = 0.05            # significance level

# create a cohort of patients
myCohort = Cls.Cohort(id=1, pop_size=SIM_POP_SIZE, mortality_prob=MORTALITY_PROB)

# simulate the cohort
cohortOutcome = myCohort.simulate(TIME_STEPS)

#QUESTION 1
print("QUESTION 1: The percent of patients that will survive past 5 years is", myCohort.fiveyearmarksurvival())

#QUESTION 2
print("QUESTION 2:I believe this follows the binomial distribution because we are dividing the patients into two groups "
      "those those that survive past the 5 year mark & those that don't. Therefore the only parameter")
#QUESTION 3
print("QUESTION 3:The likelihood ratio is:", stat.binom.pmf(k=400,n=573,p=0.5))

MORTALITY_PROB = 573/1000    # annual probability of mortality
TIME_STEPS = 5        # simulation length
REAL_POP_SIZE = 573     # size of the real cohort to make the projections for
NUM_SIM_COHORTS = 1000   # number of simulated cohorts used for making projections
ALPHA = 0.05            # significance level

# calculating PI for mean survival time
# create multiple cohorts
multiCohort = Cls.MultiCohort(
    ids=range(NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    pop_sizes=[REAL_POP_SIZE] * NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    mortality_probs=[MORTALITY_PROB]*NUM_SIM_COHORTS  # [p, p, ....]
)
# simulate all cohorts
multiCohort.simulate(TIME_STEPS)

#QUESTION 4
# print projected mean survival time (years)
print('QUESTION 4: Projected mean survival time (years) is',
      multiCohort.get_overall_mean_survival())

# print projection interval
print('95% PI of average survival time (years)',
      multiCohort.get_PI_mean_survival(ALPHA))

# print the patient survival time
print('Average survival time :', Cls.CohortOutcomes.get_ave_survival_time())
print('95% CI of average survival time (years)', Cls.CohortOutcomes.get_CI_survival_time(ALPHA))
# report mean and projection interval

#QUESTION 5
print("QUESTION 5: Mean survival time and {:.{prec}%} projection interval:.format(1 - ALPHA, prec=0)",
      Cls.calibrated_model.get_mean_survival_time_proj_interval(ALPHA, deci=4))

#QUESTION 6

MORTALITY_PROB = 800/1146    # annual probability of mortality
TIME_STEPS = 5        # simulation length
REAL_POP_SIZE = 1146     # size of the real cohort to make the projections for
NUM_SIM_COHORTS = 1000   # number of simulated cohorts used for making projections
ALPHA = 0.05            # significance level

# calculating prediction interval for mean survival time
# create multiple cohorts
multiCohort = Cls.MultiCohort(
    ids=range(NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    pop_sizes=[REAL_POP_SIZE] * NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    mortality_probs=[MORTALITY_PROB]*NUM_SIM_COHORTS  # [p, p, ....]
)
# simulate all cohorts
multiCohort.simulate(TIME_STEPS)

# print projected mean survival time (years)
print("QUESTION 6: Projected mean survival time",
      multiCohort.get_overall_mean_survival())
# print projection interval
print('95% PI of average survival time',
      multiCohort.get_PI_mean_survival(ALPHA))
# Estimate of mortality probability and the posterior interval
print('Estimate of mortality probability ({:.{prec}%} credible interval):'.format(1-ALPHA, prec=0),
      Cls.get_mortality_estimate_credible_interval(ALPHA, 4))
