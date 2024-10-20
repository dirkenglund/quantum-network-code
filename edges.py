from dataclasses import dataclass

@dataclass
class Edge:
    start_uid: str
    end_uid: str
    label: str
    length: float  # in meters
    transmission: float  # in dB

# Define edges using the Edge data class
edges = [
    Edge("FH576-A", "HARV", "2 SMF-28", 100, -2),  # Fiber Hub 576-A to Harvard
    Edge("FH576-A", "LINCOLN", "2 SMF-28", 120, -2.5),  # Fiber Hub 576-A to Lincoln Lab
    Edge("FH576-B", "26-465", "4 ?,", 80, -3),        # Fiber Hub 576-B to 26-465
    Edge("FH576-B", "26-465", "2 SM600", 70, -3.5),    # Fiber Hub 576-B to 26-465
    Edge("FH576-B", "LINCOLN", "2 ?", 60, -2.8),       # Fiber Hub 576-B to Lincoln Lab
    Edge("26-368", "36-576", "4 SMF28", 90, -3),     # 26-368 to 36-576
    Edge("26-368", "36-576", "2 780HP", 95, -3),     # 26-368 to 36-576
    Edge("26-368", "36-576", "2 630HP", 85, -3),     # 26-368 to 36-576
    Edge("26-368", "36-576", "2 PM63-U40D", 75, -3), # 26-368 to 36-576
    Edge("26-368", "36-576", "4 SMF28 (Metal Sheethed)", 100, -3), # 26-368 to 36-576
    Edge("26-368", "36-576", "2 PM40-U40D", 80, -3), # 26-368 to 36-576
    Edge("26-368", "38-185", "6 SMF28", 70, -3),      # 26-368 to 38-185
    Edge("26-368", "26-465", "4 SMF28", 85, -3),      # 26-368 to 26-465
    Edge("26-368", "NOTAROS", "2 PM40-U40D", 95, -3),  # 26-368 to Notaros Lab
    Edge("26-368", "NOTAROS", "2 630HP", 85, -3),       # 26-368 to Notaros Lab
    Edge("26-368", "NOTAROS", "2 780HP", 95, -3),       # 26-368 to Notaros Lab
    Edge("26-368", "NOTAROS", "2 SMF-28", 90, -3),      # 26-368 to Notaros Lab
    Edge("FH576-A", "BU", "1 SMF-28", 110, -2),          # Fiber Hub 576-A to Boston University
    Edge("BU", "UMD", "2 SMF-28", 150, -1.5),             # Boston University to University of Maryland
    Edge("COQREATE", "TRINITY", "1 SMF-28", 200, -1.8),   # CoQreate (Ireland) to Trinity College (Ireland)
    Edge("UMASS", "UO", "2 SMF-28", 130, -1.7),           # UMass Amherst to University of Oregon
    Edge("HU", "UMD", "1 SMF-28", 140, -2),               # Howard University to University of Maryland
    Edge("ENG_LAB", "ATT_HUB", "2 SMF-28", 60, -1.2),     # Englund Lab to AT&T Fiber Hub
    Edge("ATT_HUB", "MITLL", "3 SMF-28", 80, -1.5),      # AT&T Fiber Hub to MIT Lincoln Lab
    Edge("ATT_HUB", "HARV", "3 SMF-28", 85, -1.5),        # AT&T Fiber Hub to Harvard
    Edge("ATT_HUB", "BBN", "3 SMF-28", 90, -1.5),         # AT&T Fiber Hub to BBN Raytheon
]
