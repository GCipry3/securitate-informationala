import models

def test_add_algorithm():
    name = "Test Algorithm"
    type = "Symmetric"
    description = "Test Description"
    alg_id = models.add_algorithm(name, type, description)
    assert alg_id is not None, "Failed to add algorithm"
    print("Test add_algorithm passed.")

def test_get_algorithms():
    algorithms = models.get_algorithms()
    assert algorithms is not None and len(algorithms) > 0, "No algorithms found"
    print("Test get_algorithms passed.")

def test_add_and_get_keys():
    algorithms = models.get_algorithms()
    if not algorithms:
        print("No algorithms available to add a key.")
        return
    algorithm_id = algorithms[0]['_id']
    key_id = models.add_key(algorithm_id, "test_key", "2024-01-01")
    assert key_id is not None, "Failed to add key"
    keys = models.get_keys()
    assert keys is not None and len(keys) > 0, "No keys found"
    print("Test add_and_get_keys passed.")

if __name__ == "__main__":
    test_add_algorithm()
    test_get_algorithms()
    test_add_and_get_keys()
