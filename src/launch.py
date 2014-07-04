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
	for quarterback in quarterbacks:
		print(quarterback)
	return quarterbacks


def load_running_back_data():
	rbFile = open("/Users/SoLReePzz/Documents/IDP Project/src/resources/runningbacks.txt")
	running_backs = rbFile.readlines()
	rbFile.close()
	print("Running backs:")
	for running_back in running_backs:
		print(running_back)
	return running_backs


def load_wide_receiver_data():
	wrFile = open("/Users/SoLReePzz/Documents/IDP Project/src/resources/widereceivers.txt")
	wide_receivers = wrFile.readlines()
	wrFile.close()
	print("Wide receivers:")
	for wide_receiver in wide_receivers:
		print(wide_receiver)
	return wide_receivers


def load_tight_end_data():
	teFile = open("/Users/SoLReePzz/Documents/IDP Project/src/resources/tightends.txt")
	tight_ends = teFile.readlines()
	teFile.close()
	print("Tight ends:")
	for tight_end in tight_ends:
		print(tight_end)
	return tight_ends


def load_kicker_data():
	kFile = open("/Users/SoLReePzz/Documents/IDP Project/src/resources/kickers.txt")
	kickers = kFile.readlines()
	kFile.close()
	print("Kickers:")
	for kicker in kickers:
		print(kicker)
	return kickers


def load_defense_data():
	dFile = open("/Users/SoLReePzz/Documents/IDP Project/src/resources/defenses.txt")
	defenses = dFile.readlines()
	dFile.close()
	print("Defenses:")
	for defense in defenses:
		print(defense)
	return defenses


main()