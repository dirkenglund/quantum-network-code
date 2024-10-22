from dataclasses import dataclass

@dataclass
class Link:
    start_uid: str
    end_uid: str
    label: str
    length: float  # in meters
    transmission: float  # in dB
    link_type: str  # fiber, switch/ROADM, satellite, free-space, etc.

# Define the corrected links
links = [
    # MIT and ATT_HUB connections
    Link("MIT-FH576-A", "ATT_HUB", "2 SMF-28", 50, -2, "fiber"),
    Link("MIT-FH576-B", "ATT_HUB", "2 SMF-28", 50, -2.5, "fiber"),
    Link("ATT_HUB", "HARV", "3 SMF-28", 85, -1.5, "fiber"),
    Link("ATT_HUB", "MIT-LINCOLN", "3 SMF-28", 80, -1.5, "fiber"),
    Link("ATT_HUB", "BBN", "3 SMF-28", 90, -1.5, "fiber"),

    # MIT internal connections
    Link("MIT-26-368", "MIT-26-465", "4 SMF-28", 10, -3, "fiber"),
    Link("MIT-26-368", "MIT-NOTAROS", "2 PM40-U40D", 10, -3, "fiber"),
    Link("MIT-26-368", "MIT-36-576", "4 SMF28", 90, -3, "fiber"),
    Link("MIT-36-576", "ENG_LAB", "2 SMF-28", 60, -1.2, "fiber"),

    # Boston University and UMD connections
    Link("MIT-FH576-A", "BU-QuNETT", "1 SMF-28", 110, -2, "fiber"),
    Link("BU-QuNETT", "UMD", "2 SMF-28", 150, -1.5, "fiber"),

    # UMD connections (new IonQ node)
    Link("UMD", "IONQ", "2 SMF-28", 2, -0.5, "fiber"),  # UMD linked to IonQ Corp
    Link("UMD", "UMD-SAT", "2 SMF-28", 5, -1, "fiber"),  # UMD linked to satellite campus

    # CoQreate and Trinity College connection (Ireland)
    Link("COQREATE", "TRINITY", "1 SMF-28", 200, -1.8, "fiber"),

    # University collaborations and fiber links
    Link("UMASS", "UO", "2 SMF-28", 130, -1.7, "fiber"),
    Link("HU", "UMD", "1 SMF-28", 140, -2, "fiber"),  # Removed incorrect HU links, this is the only correct one

    # Tucson campus connections between nodes (Arizona)
    Link("UA-ECE", "UA-BME", "Campus Link", 300, 0, "free-space"),  # ECE to BME
    Link("UA-ECE", "UA-MSE", "Campus Link", 400, 0, "free-space"),  # ECE to MSE
    Link("UA-OSC", "UA-ECE", "Campus Link", 500, 0, "free-space"),  # Optical Sciences to ECE
    Link("UA-OSC", "UA-MSE", "Campus Link", 200, 0, "free-space"),  # Optical Sciences to MSE
    Link("UA-OSC", "UA-GCRB", "Campus Link", 100, 0, "free-space"),  # Optical Sciences to GCRB
    Link("UA-GCRB", "UA-MSE", "Campus Link", 150, 0, "free-space"),  # GCRB to MSE
    Link("UA-GCRB", "UA-BME", "Campus Link", 250, 0, "free-space"),  # GCRB to BME
]
