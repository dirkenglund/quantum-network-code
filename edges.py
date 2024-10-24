from dataclasses import dataclass, field

@dataclass
class Link:
    start_uid: str
    end_uid: str
    label: str
    length: float  # in meters
    transmission: float  # in dB
    link_type: str  # fiber, switch/ROADM, satellite, free-space, etc.

# Define links using the Link data class
links = [
    Link("MIT-FH576-A", "HARV", "2 SMF-28", 100, -2, "fiber"),  # Fiber Hub 576-A to Harvard
    Link("MIT-FH576-A", "MIT-LINCOLN", "2 SMF-28", 120, -2.5, "fiber"),  # Fiber Hub 576-A to Lincoln Lab
    Link("MIT-FH576-B", "MIT-26-465", "4 ?", 80, -3, "fiber"),        # Fiber Hub 576-B to 26-465
    Link("MIT-FH576-B", "MIT-26-465", "2 SM600", 70, -3.5, "fiber"),    # Fiber Hub 576-B to 26-465
    Link("MIT-FH576-B", "MIT-LINCOLN", "2 ?", 60, -2.8, "fiber"),       # Fiber Hub 576-B to Lincoln Lab
    Link("MIT-26-368", "MIT-36-576", "4 SMF28", 90, -3, "fiber"),     # 26-368 to 36-576
    Link("MIT-26-368", "MIT-36-576", "2 780HP", 95, -3, "fiber"),     # 26-368 to 36-576
    Link("MIT-26-368", "MIT-36-576", "2 630HP", 85, -3, "fiber"),     # 26-368 to 36-576
    Link("MIT-26-368", "MIT-36-576", "2 PM63-U40D", 75, -3, "fiber"), # 26-368 to 36-576
    Link("MIT-26-368", "MIT-36-576", "4 SMF28 (Metal Sheethed)", 100, -3, "fiber"), # 26-368 to 36-576
    Link("MIT-26-368", "MIT-36-576", "2 PM40-U40D", 80, -3, "fiber"), # 26-368 to 36-576
    Link("MIT-26-368", "MIT-38-185", "6 SMF28", 70, -3, "fiber"),      # 26-368 to 38-185
    Link("MIT-26-368", "MIT-26-465", "4 SMF28", 85, -3, "fiber"),      # 26-368 to 26-465
    Link("MIT-26-368", "MIT-NOTAROS", "2 PM40-U40D", 95, -3, "fiber"),  # 26-368 to Notaros Lab
    Link("MIT-26-368", "MIT-NOTAROS", "2 630HP", 85, -3, "fiber"),       # 26-368 to Notaros Lab
    Link("MIT-26-368", "MIT-NOTAROS", "2 780HP", 95, -3, "fiber"),       # 26-368 to Notaros Lab
    Link("MIT-26-368", "MIT-NOTAROS", "2 SMF-28", 90, -3, "fiber"),      # 26-368 to Notaros Lab
    Link("MIT-FH576-A", "BU-QuNETT", "1 SMF-28", 110, -2, "fiber"),          # Fiber Hub 576-A to Boston University
    Link("BU-QuNETT", "UMD", "2 SMF-28", 150, -1.5, "fiber"),             # Boston University to University of Maryland
    Link("COQREATE", "TRINITY", "1 SMF-28", 200, -1.8, "fiber"),   # CoQreate (Ireland) to Trinity College (Ireland)
    Link("UMASS", "UO", "2 SMF-28", 130, -1.7, "fiber"),           # UMass Amherst to University of Oregon
    Link("HU", "UMD", "1 SMF-28", 140, -2, "fiber"),               # Howard University to University of Maryland
    Link("ENG_LAB", "ATT_HUB", "2 SMF-28", 60, -1.2, "fiber"),     # Englund Lab to AT&T Fiber Hub
    Link("ATT_HUB", "MIT-MITLL", "3 SMF-28", 80, -1.5, "fiber"),      # AT&T Fiber Hub to MIT Lincoln Lab
    Link("ATT_HUB", "HARV", "3 SMF-28", 85, -1.5, "fiber"),        # AT&T Fiber Hub to Harvard
    Link("ATT_HUB", "BBN", "3 SMF-28", 90, -1.5, "fiber"),         # AT&T Fiber Hub to BBN Raytheon
    # Additional edges for U-Maryland and IonQ
    Link("UMD", "IonQ", "Trapped Ions Connection", 50, -1, "fiber"),  # Example connection to IonQ
    Link("UMD", "UMD-38.982397", "Trapped Ions Connection", 50, -1, "fiber"),  # Example connection to another UMD location
]
