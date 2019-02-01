class BestTravel():
    best_results = []

    def sum_distances(self, distances):
        
        total = 0
        for num in distances:
            total += num
        return total if total is not None else 0

    def find_distance(self, distance_limit,
                      number_of_towns,
                      filtered_distances):
        result = []
        for distance in filtered_distances:
            if len(result) == number_of_towns:               
                break
            if (distance + self.sum_distances(result)) <= distance_limit:
                result.append(distance)
                
        total = 0
        if len(filtered_distances) < number_of_towns:
            self.best_results.append(self.sum_distances(result))

        if len(result) < number_of_towns and len(result) > 0 \
                and len(filtered_distances) > 1:
            self.best_results.append(self.find_distance(
                distance_limit,
                number_of_towns,
                filtered_distances[1:]))
        self.best_results.append(self.sum_distances(result))

    def choose_best_sum(self, distance_limit, number_of_towns, list_of_distances):
        try:
            if(distance_limit < 0 or number_of_towns < 1 or len(list_of_distances) == 0 or number_of_towns > len(list_of_distances)):
                raise InvalidInput()
        except TypeError:
            raise InvalidInput()
        self.best_results = []
        filtered_distances = [distance for distance in list_of_distances 
                              if distance < distance_limit]
        filtered_distances = sorted(filtered_distances, reverse=True)
        self.find_distance(distance_limit, number_of_towns, filtered_distances)
        
        return max([r for r in self.best_results if r is not None])

def check_distance(distance):
    try:
        if distance < 0:
            raise InvalidInput()
    except TypeError:
        raise InvalidInput()


class InvalidInput(Exception): 
    pass