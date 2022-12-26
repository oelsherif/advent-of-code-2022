import time
with open("inputs/19.txt", "r") as File:
    lines = [line.split() for line in File]


def can_build(rob_type, avail_mat, cost_rob_type):
    for mat_type in cost_rob_type:
        if avail_mat[mat_type] < cost_rob_type[mat_type]:
            return False
    return True

def generate(mnt, potential_builds, inv_mat, inv_rob):
    if mnt == minutes + 1:
        return inv_mat["geo"]
    new_mnt = mnt + 1
    num_geos = []
    new_inv_mat = inv_mat.copy()
    for built_rob in inv_rob:
        new_inv_mat[built_rob] += inv_rob[built_rob]
    if potential_builds["ore"] and (inv_mat["ore"] > max_ore or mnt >= minutes - 2):
        potential_builds["ore"] = False
    if potential_builds["clay"] and (inv_mat["clay"] > max_clay or mnt >= minutes - 4):
        potential_builds["clay"] = False
    if potential_builds["obs"] and (inv_mat["obs"] > max_obs or mnt >= minutes - 2):
        potential_builds["obs"] = False
    for type, flag in potential_builds.items():
        if flag and can_build(type, inv_mat, cost[type]):
            newer_inv_mat = new_inv_mat.copy()
            newer_inv_rob = inv_rob.copy()
            for mat_type in cost[type]:
                newer_inv_mat[mat_type] -= cost[type][mat_type]
            newer_inv_rob[type] += 1
            num_geos.append( generate(new_mnt, potential_builds.copy(), newer_inv_mat, newer_inv_rob))
    num_geos.append( generate(new_mnt, potential_builds.copy(), new_inv_mat.copy(), inv_rob.copy()) )
    return(max(num_geos))

types = {"ore", "clay", "obs", "geo"}
n_bps = len(lines)
costs = {}
for i, line in enumerate(lines):
    costs[i+1] = {
        "ore": {"ore": int(line[6])},
        "clay": {"ore": int(line[12])},
        "obs": {"ore": int(line[18]), "clay": int(line[21])},
        "geo": {"ore": int(line[27]), "obs": int(line[30])}
    }
results = {}
minutes = 32
start_time = time.time()
for bp in range(1, 4):
    inv_mat = {"ore": 0, "clay": 0, "obs": 0, "geo": 0}
    inv_rob = {"ore": 1, "clay": 0, "obs": 0, "geo": 0}
    potential_builds = {"ore": True, "clay": True, "obs": True, "geo": True}
    cost = costs[bp]
    max_ore = 2 * max( [cost["ore"]["ore"], cost["clay"]["ore"], cost["obs"]["ore"], cost["geo"]["ore"]] )
    max_clay = 4 + cost["obs"]["clay"]
    max_obs = 4 + cost["geo"]["obs"]
    results[bp] = generate(1, potential_builds, inv_mat, inv_rob)
    print(f"Bluprint number {bp} has {results[bp]} geodes opened")
    print(f"Elapsed_Time = {time.time() - start_time} seconds")

print(results)
ans = 1
for bp in results:
    ans *= results[bp]
print("part 2 answer:")
print(ans)
