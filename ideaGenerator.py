import numpy as np

actions = np.array(["use",
                    "make",
                    "create",
                    "design",
                    "play",
                    "find",
                    "think of",
                    "come up with"])

things = np.array(["game",
                   "puzzle",
                   "video",
                   "picture",
                   "program",
                   "project",
                   "idea",
                   "script",
                   "machine",
                   "hack"])

adjectives = np.array(["fun",
                       "cool",
                       "scary",
                       "complex",
                       "e p i c",
                       "interesting",
                       "super neat"])

effects = np.array(["explodes",
                    "helps with school",
                    "is fun to use",
                    "pranks your friend(s)",
                    "eats",
                    "thinks about the inevitable heat death of the universe",
                    "is self aware",
                    "is funny",
                    "does work for you"])

print("What should I do right now?\n")

for i in range(50):
    a = actions[np.random.randint(0,np.size(actions))]
    b = things[np.random.randint(0,np.size(things))]
    c = adjectives[np.random.randint(0,np.size(adjectives))]
    d = effects[np.random.randint(0,np.size(effects))]

    print("{0} a {1} {2} that {3}.".format(a,c,b,d))
