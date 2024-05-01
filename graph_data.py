# Graph representation of 20 Csuf locations and paths between them
edges_distances = [
    # Nutwood Parking connections
    ("Nutwood Parking", "Dan Black Hall", 815),
    ("Nutwood Parking", "McCarthy Hall", 896),
    ("Nutwood Parking", "Clayes Performing Arts Center", 747),
    ("Nutwood Parking", "Visual Arts", 667),

    # Visual Arts connections
    ("Visual Arts", "Clayes Performing Arts Center", 421),
    ("Visual Arts", "Titan Student Union", 357),
    ("Visual Arts", "Nutwood Parking", 667),

    # Titan Student Union connections
    ("Titan Student Union", "Visual Arts", 357),
    ("Titan Student Union", "Titan Bookstore", 337),
    ("Titan Student Union", "Recreation Center", 480),

    # Recreation Center connections
    ("Recreation Center", "Titan Student Union", 480),
    ("Recreation Center", "Titan Gym", 500),
    ("Recreation Center", "Titan Bookstore", 526),
    ("Recreation Center", "Pollack Library", 930),

    # Clayes Performing Arts Center connections
    ("Clayes Performing Arts Center", "Visual Arts", 421),
    ("Clayes Performing Arts Center", "Titan Bookstore", 490),
    ("Clayes Performing Arts Center", "Pollack Library", 536),
    ("Clayes Performing Arts Center", "Humanities", 746),
    ("Clayes Performing Arts Center", "McCarthy Hall", 439),
    ("Clayes Performing Arts Center", "Dan Black Hall", 574),
    ("Clayes Performing Arts Center", "Nutwood Parking", 747),

    # Titan Bookstore connections
    ("Titan Bookstore", "Titan Student Union", 337),
    ("Titan Bookstore", "Recreation Center", 526),
    ("Titan Bookstore", "Titan Gym", 465),
    ("Titan Bookstore", "Student Health", 887),
    ("Titan Bookstore", "Pollack Library", 472),
    ("Titan Bookstore", "Clayes Performing Arts Center", 490),

    # Titan Gym connections
    ("Titan Gym", "Recreation Center", 500),
    ("Titan Gym", "Titan Bookstore", 465),
    ("Titan Gym", "Student Health", 500),
    ("Titan Gym", "Pollack Library", 605),
    ("Titan Gym", "Education Classroom", 787),

    # Dan Black Hall connections
    ("Dan Black Hall", "Nutwood Parking", 815),
    ("Dan Black Hall", "Langsdorf Hall", 411),
    ("Dan Black Hall", "Clayes Performing Arts Center", 574),
    ("Dan Black Hall", "McCarthy Hall", 165),
    ("Dan Black Hall", "Pollack Library", 855),
    ("Dan Black Hall", "Humanities", 679),
    
    # McCarthy Hall connections
    ("McCarthy Hall", "Humanities", 453),
    ("McCarthy Hall", "Dan Black Hall", 165),
    ("McCarthy Hall", "Nutwood Parking", 896),

    # Pollack Library connections
    ("Pollack Library", "Dan Black Hall", 855),
    ("Pollack Library", "Clayes Performing Arts Center", 536),
    ("Pollack Library", "Titan Bookstore", 472),
    ("Pollack Library", "Recreation Center", 930),
    ("Pollack Library", "Titan Gym", 580),
    ("Pollack Library", "Student Health", 647),
    ("Pollack Library", "Education Classroom", 600),
    ("Pollack Library", "Humanities", 528),
    
    # Langsdorf Hall connections
    ("Langsdorf Hall", "Dan Black Hall", 411),
    ("Langsdorf Hall", "SGMH", 227),
    ("Langsdorf Hall", "Carls Jr", 228),
    ("Langsdorf Hall", "Humanities", 520),
    ("Langsdorf Hall", "McCarthy Hall", 353),
    
    # Humanities connections
    ("Humanities", "Education Classroom", 337),
    ("Humanities", "Pollack Library", 528),
    ("Humanities", "Clayes Performing Arts Center", 746),
    ("Humanities", "McCarthy Hall", 453),
    ("Humanities", "Dan Black Hall", 679),
    ("Humanities", "Langsdorf Hall", 520),
    ("Humanities", "Carls Jr", 413),
    ("Humanities", "Lot F", 338),

    # Education Classroom connections
    ("Education Classroom", "Humanities", 337),
    ("Education Classroom", "Pollack Library", 600),
    ("Education Classroom", "Titan Gym", 787),
    ("Education Classroom", "Student Health", 600),
    ("Education Classroom", "Engineering Building", 477),
    ("Education Classroom", "Lot F", 497),

    # Student Health connections
    ("Student Health", "Titan Gym", 500),
    ("Student Health", "Gastronome", 586),
    ("Student Health", "Engineering Building", 409),
    ("Student Health", "Education Classroom", 600),
    ("Student Health", "Pollack Library", 647),
    ("Student Health", "Titan Bookstore", 464),

    # SGMH connections
    ("SGMH", "Carls Jr", 256),
    ("SGMH", "Langsdorf Hall", 227),

    # Carls Jr connections
    ("Carls Jr", "SGMH", 256),
    ("Carls Jr", "Langsdorf Hall", 228),
    ("Carls Jr", "Lot F", 461),
    ("Carls Jr", "East Side Parking Structure", 694),
    ("Carls Jr", "Humanities", 413),

    # Lot F connections
    ("Lot F", "Carls Jr", 461),
    ("Lot F", "East Side Parking Structure", 380),
    ("Lot F", "Gastronome", 985),
    ("Lot F", "Engineering Building", 677),
    ("Lot F", "Education Classroom", 497),
    ("Lot F", "Humanities", 338),

    # Engineering Building connections
    ("Engineering Building", "Lot F", 677),
    ("Engineering Building", "Gastronome", 416),
    ("Engineering Building", "Student Health", 409),
    ("Engineering Building", "Education Classroom", 477),

    # Gastronome connections
    ("Gastronome", "Engineering Building", 416),
    ("Gastronome", "Student Health", 586),
    ("Gastronome", "Lot F", 985),
    ("Gastronome", "East Side Parking Structure", 1045),

    # East Side Parking Structure connections
    ("East Side Parking Structure", "Carls Jr", 694),
    ("East Side Parking Structure", "Lot F", 380),
    ("East Side Parking Structure", "Gastronome", 1045)
]

edges_explicit = [
    ('0', '1'), ('0', '4'), ('0', '7'), ('0', '8'),
    ('1', '0'), ('1', '4'), ('1', '2'),
    ('2', '1'), ('2', '5'), ('2', '3'),
    ('3', '2'), ('3', '5'), ('3', '6'), ('3', '9'),
    ('4', '0'), ('4', '1'), ('4', '5'), ('4', '9'), ('4', '8'), ('4', '7'),
    ('5', '2'), ('5', '4'), ('5', '9'), ('5', '3'), ('5', '6'), ('5', '13'),
    ('6', '3'), ('6', '5'), ('6', '9'), ('6', '12'), ('6', '13'),
    ('7', '0'), ('7', '4'), ('7', '8'), ('7', '10'),
    ('8', '4'), ('8', '0'), ('8', '7'), ('8', '10'), ('8', '11'), ('8', '9'),
    ('9', '8'), ('9', '4'), ('9', '5'), ('9', '3'), ('9', '6'), ('9', '13'), ('9', '12'), ('9', '11'),
    ('10', '7'), ('10', '8'), ('10', '11'), ('10', '15'), ('10', '14'),
    ('11', '8'), ('11', '4'), ('11', '9'), ('11', '12'), ('11', '16'), ('11', '15'),
    ('12', '11'), ('12', '16'), ('12', '9'), ('12', '6'), ('12', '13'), ('12', '17'),
    ('13', '6'), ('13', '5'), ('13', '9'), ('13', '12'), ('13', '17'), ('13', '18'),
    ('14', '10'), ('14', '15'),
    ('15', '14'), ('15', '10'), ('15', '11'), ('15', '16'), ('15', '19'),
    ('16', '11'), ('16', '15'), ('16', '19'), ('16', '12'), ('16', '17'), ('16', '18'),
    ('17', '12'), ('17', '13'), ('17', '18'), ('17', '16'),
    ('18', '13'), ('18', '17'), ('18', '16'), ('18', '19'),
    ('19', '15'), ('19', '16'), ('19', '18')
]

# Positions for the nodes
positions = [
    (113.6, 727.4), # Nutwood Parking (Node 0)
    (170.2, 454.0), # Visual Arts (Node 1)
    (166.3, 304.8), # Titan Student Union (Node 2)
    (205.0, 108.9), # Recreation Center (Node 3)
    (344.3, 487.8), # Clayes Performing Arts Center (Node 4)
    (322.4, 291.9), # Titan Bookstore (Node 5)
    (427.8, 108.9), # Titan Gym (Node 6)
    (458.6, 708.5), # Dan Black Hall (Node 7)
    (492.4, 627.0), # McCarthy Hall (Node 8)
    (510.3, 350.5), # Pollack Library (Node 9)
    (633.6, 717.5), # Langsdorf Hall (Node 10)
    (663.5, 501.7), # Humanities (Node 11)
    (645.6, 359.5), # Education Classroom (Node 12)
    (656.5, 107.9), # Student Health (Node 13)
    (717.2, 775.2), # SGMH (Node 14)
    (711.2, 665.8), # Carls Jr (Node 15)
    (804.7, 498.7), # Lot F (Node 16)
    (787.8, 216.3), # Engineering Building (Node 17)
    (903.1, 90),    # Gastronome (Node 18)
    (965.8, 523.6), # East Side Parking Structure (Node 19)
]