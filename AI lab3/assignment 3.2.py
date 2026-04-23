def reflex_agent(percepts):
    """
    percepts: dictionary with keys
        'track_inbound' : True/False
        'track_outbound': True/False
        'obstacle'      : True/False
        'manual_lever'  : True/False
    """

    actions = {
        "Gate Arm": "Raised",
        "Hooter": "Off",
        "Signal to Train": "Green"
    }
    decision = ""

    # Priority 1: Manual Emergency Input
    if percepts["manual_lever"]:
        actions["Gate Arm"] = "Raised"
        actions["Hooter"] = "On"
        actions["Signal to Train"] = "Red"
        decision = "Manual override: Emergency Stop"

    # Priority 2: Obstacle Sensors
    elif percepts["obstacle"]:
        actions["Gate Arm"] = "Raised"
        actions["Hooter"] = "On"
        actions["Signal to Train"] = "Red"
        decision = "Obstacle detected: Stop train, keep gate open"

    #Priority 3: Track Sensors
    elif percepts["track_inbound"]:
        actions["Gate Arm"] = "Lowered"
        actions["Hooter"] = "On"
        actions["Signal to Train"] = "Green"
        decision = "Inbound train: Close gate, allow train"

    elif percepts["track_outbound"]:
        actions["Gate Arm"] = "Lowered"
        actions["Hooter"] = "On"
        actions["Signal to Train"] = "Green"
        decision = "Outbound train: Keep gate closed until clear"

    
    else:
        actions["Gate Arm"] = "Raised"
        actions["Hooter"] = "Off"
        actions["Signal to Train"] = "Green"
        decision = "Safe: Gate open, road traffic allowed"

    return {
        "Percepts": percepts,
        "Actions": actions,
        "Decision": decision
    }



scenarios = [
    {"track_inbound": True,  "track_outbound": False, "obstacle": False, "manual_lever": False},
    {"track_inbound": False, "track_outbound": True,  "obstacle": False, "manual_lever": False},
    {"track_inbound": False, "track_outbound": False, "obstacle": True,  "manual_lever": False},
    {"track_inbound": False, "track_outbound": False, "obstacle": False, "manual_lever": True},
    {"track_inbound": False, "track_outbound": False, "obstacle": False, "manual_lever": False}
]

for i, s in enumerate(scenarios, 1):
    result = reflex_agent(s)
    print(f"\nScenario {i}:")
    print("Percepts:", result["Percepts"])
    print("Actions:", result["Actions"])
    print("Decision:", result["Decision"])