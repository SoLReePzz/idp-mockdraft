print("SoLReePzz's IDP Mock Drafting Tool")


def main():
	print("Gathering Player Data")
	quarterbacks = load_quarterback_data()
	running_backs = load_running_back_data()
	wide_receivers = load_wide_receiver_data()
	tight_ends = load_tight_end_data()
	kickers = load_kicker_data()
	defenses = load_defense_data()


def load_quarterback_data():
	qbFile = open("/Users/SoLReePzz/Documents/IDP Project/src/resources/quarterbacks.txt")
	quarterbacks = qbFile.readlines()
	qbFile.close()
	print("Quarterbacks:")
	print(quarterbacks)
	return quarterbacks


def load_running_back_data():
	running_backs = "Empty RBs"
	print("Running backs:")
	print(running_backs)
	return running_backs


def load_wide_receiver_data():
	wide_receivers = "Empty WRs"
	print("Wide receivers:")
	print(wide_receivers)
	return wide_receivers


def load_tight_end_data():
	tight_ends = "Empty TEs"
	print("Tight ends:")
	print(tight_ends)
	return tight_ends


def load_kicker_data():
	kickers = "Empty Kickers"
	print("Kickers:")
	print(kickers)
	return kickers


def load_defense_data():
	defenses = "Empty RBs"
	print("Defenses:")
	print(defenses)
	return defenses


main()