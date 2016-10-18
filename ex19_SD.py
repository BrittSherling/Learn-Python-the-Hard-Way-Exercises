def fishermans_haul(total_lures, fish):
    print "The fisherman caught %d fish today!" % fish
    print "He started with %d lures" % total_lures
    lures = total_lures - fish
    print "He has %d lures left for tomorrow!\n" % lures


fishermans_haul(50, 24)

total_lures = int(raw_input("How many lures did you start with?: "))
fish = int(raw_input("How many fish did you catch?: "))

fishermans_haul(total_lures, fish)
