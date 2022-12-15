import ray

def get_and_squared(x: "ray.ObjectRef[float]") -> float:
    return ray.get(x)**2