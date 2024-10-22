from dataclasses import dataclass, field

@dataclass
class Node:
    uid: str
    name: str
    position: tuple
    memory_type: str
    cooling: str
    T2: str
    status: str
    participants: str
    technologies: list = field(default_factory=list)

# Define nodes using the Node data class
nodes = {
    "MIT-FH576-A": Node("MIT-FH576-A", "Fiber Hub 576-A", (42.3619, -71.0903), "N/A", "4K", "N/A", "Online", "CQN"),
    "HARV": Node("HARV", "Harvard", (42.3656, -71.1032), "SiV", "1K", ">1ms", "Installed", "MIT-LL", ["Quantum Frequency Conversion"]),
    "MIT-LINCOLN": Node("MIT-LINCOLN", "Lincoln Lab", (42.4464, -71.2258), "SiV", "0.3K", ">1ms", "Under Construction", "Startup", ["Quantum Frequency Conversion"]),
    "MIT-FH576-B": Node("MIT-FH576-B", "Fiber Hub 576-B", (42.3619, -71.0903), "N/A", "4K", "?", "Online", "CQN"),
    "MIT-26-465": Node("MIT-26-465", "26-465", (42.3646, -71.1028), "SiV", "1K", ">1ms", "Installed", "MIT-LL"),
    "MIT-38-177": Node("MIT-38-177", "38-177 SE Wall", (42.3593, -71.0957), "SnV", "0.3K", "?", "Online", "Startup"),
    "MIT-26-368": Node("MIT-26-368", "26-368", (42.3646, -71.1028), "SnV", "4K", "?", "Online", "CQN"),
    "MIT-36-576": Node("MIT-36-576", "36-576", (42.3619, -71.0903), "SnV, SiV, silicon G-center", "1K", "soon", "Installed", "MIT-LL"),
    "MIT-NOTAROS": Node("MIT-NOTAROS", "Notaros Lab", (42.3646 + 0.00002, -71.1028), "N/A", "0.3K", "N/A", "Online", "Startup"),
    "MIT-38-185": Node("MIT-38-185", "38-185", (42.3593, -71.0957), "SnV", "1K", ">2ms", "Online", "CQN"),
    "UA": Node("UA", "University of Arizona", (32.2319, -110.9501), "SnV", "4K", "N/A", "Online", "CQN"),
    "COQREATE": Node("COQREATE", "CoQreate (Ireland)", (53.349805, -6.26031), "planned: SnV", "purchased: 1K", "1K", "Planned", "MIT-LL"),
    "MIT-MITLL": Node("MIT-MITLL", "MIT Lincoln Lab", (42.4464, -71.2258), "SiV", "0.1K", ">1ms", "Under Construction", "Government", ["Quantum Frequency Conversion"]),
    "QUNET": Node("QUNET": Node("QUNET", "QuNet", (42.3601, -71.0589), "SiV", "4K", "N/A", "Online", "CQN"),
    "UO": Node("UO", "University of Oregon", (44.0445, -123.0122), "N/A", "1K", "N/A", "Installed", "MIT-LL"),
    "BYU": Node("BYU", "BYU", (40.2338, -111.6584), "N/A", "0.3K", "N/A", "Online", "Startup"),
    "HU": Node("HU", "Howard University", (38.9175, -77.0189), "N/A", "4K", "N/A", "diamond materials R&D", "CQN"),
    "UMASS": Node("UMASS", "UMass Amherst", (42.3902, -72.5297), "N/A", "1K", "N/A", "Installed", "MIT-LL"),
    "UMD": Node("UMD", "University of Maryland", (38.9856, -76.9426), "trapped ions", "RT", ">1 s", "Online", "Startup"),
    "TRINITY": Node("TRINITY", "Trinity College (Ireland)", (53.3434, -6.2540), "SnV", "<1K", "?", "Online", "CQN"),
    "BU-QuNETT": Node("BU", "Boston University Photonics Incubator", (42.350876, -71.106918), "SiV", "<1K", "soon", "Installed", "QuNETT"),
    "ATT_HUB": Node("ATT_HUB", "AT&T Fiber Hub", (42.3633196, -71.0925566), "N/A", "N/A", "N/A", "Online", "AT&T"),
    "ENG_LAB": Node("ENG_LAB", "Englund Lab (36-575)", (42.3615, -71.0930), "SiV, SnV", "4K", "N/A", "Online", "MIT"),
    "BBN": Node("BBN", "BBN Raytheon", (42.3897538, -71.1475561), "fridge exists, in discussions", "<100mK", "N/A", "Online", "BBN"),
}
