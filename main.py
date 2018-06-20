import rrtstar
from randomPolicySampler import RandomPolicySampler
from likelihoodPolicySampler import LikelihoodPolicySampler
from particleFilterSampler import ParticleFilterSampler
from nearbyPolicySampler import NearbyPolicySampler
from mouseSampler import MouseSampler
from disjointTree import DisjointParticleFilterSampler

def main():
    epsilon = 10.0
    max_number_nodes = 300000
    goal_radius = 15
    prob_block_size = 5
    SCALING = 4
    IGNORE_STEP_SIZE = False

    sampler = NearbyPolicySampler(prob_block_size=prob_block_size)
    sampler = LikelihoodPolicySampler(prob_block_size=prob_block_size)
    sampler = RandomPolicySampler()
    sampler = MouseSampler()
    sampler = ParticleFilterSampler()
    sampler = DisjointParticleFilterSampler()

    rrt = rrtstar.RRT(
        showSampledPoint=True,
        scaling=SCALING,
        sampler=sampler,
        goalBias=False,
        image='map.png',
        epsilon=epsilon,
        max_number_nodes=max_number_nodes,
        radius=goal_radius,
        ignore_step_size=IGNORE_STEP_SIZE,
        always_refresh=False
        )
    try:
        rrt.run()
    except Exception as e:
        import traceback
        print("==============================")
        print("Exception occured: {}".format(e))
        traceback.print_tb(e.__traceback__)
        print("==============================")
        print("Waiting to be exit...")
        rrt.wait_for_exit()

if __name__ == '__main__':
    main()
