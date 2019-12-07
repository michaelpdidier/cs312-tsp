from solver_base import SolverBase
from greedy.solver import GreedySolver


class KOptSolver(SolverBase):

    def __init__(self, tsp_solver, max_time):
        super().__init__(tsp_solver, max_time)

    def run_algorithm(self):

        route = self.build_initial_route()
        city_indices = [1, 2]

        self.swap_cities(route, city_indices)
        self.set_bssf_from_route(route)

    def swap_cities(self, route, indices):

        pass

    def get_route_cost(self, route):
        cost = 0
        route_len = len(route)

        for i in range(1, route_len):
            prev = route[i - 1]
            curr = route[i]
            cost += prev.costTo(curr)
        
        cost += route[route_len - 1].costTo(route[0])
        return cost

    def build_initial_route(self):

        greedy = GreedySolver(self.get_tsp_solver(), self.get_max_time())
        greedy.solve()
        route = greedy.get_bssf_route()

        # use default tour if greedy fails
        if route == None:
            default_results = self.get_tsp_solver().defaultRandomTour()
            route = default_results['soln'].route

        return route