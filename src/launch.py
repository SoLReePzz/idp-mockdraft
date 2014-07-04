print("SoLReePzz's IDP Mock Drafting Tool")


def main():
	print("Gathering Player Data")

	#Read player data from files
	quarterbacks = load_quarterback_data()
	running_backs = load_running_back_data()
	wide_receivers = load_wide_receiver_data()
	tight_ends = load_tight_end_data()
	kickers = load_kicker_data()
	defenses = load_defense_data()

	#Load player data from file into dicts
	qbSet = list()
	for quarterback in quarterbacks:
		qbSet.__add__(quarterback)
	print(qbSet)


def load_quarterback_data():
	qbFile = open("/Users/SoLReePzz/Documents/IDP Project/src/resources/quarterbacks.txt")
	quarterbacks = qbFile.readlines()
	qbFile.close()
	return quarterbacks


def load_running_back_data():
	rbFile = open("/Users/SoLReePzz/Documents/IDP Project/src/resources/runningbacks.txt")
	running_backs = rbFile.readlines()
	rbFile.close()
	return running_backs


def load_wide_receiver_data():
	wrFile = open("/Users/SoLReePzz/Documents/IDP Project/src/resources/widereceivers.txt")
	wide_receivers = wrFile.readlines()
	wrFile.close()
	return wide_receivers


def load_tight_end_data():
	teFile = open("/Users/SoLReePzz/Documents/IDP Project/src/resources/tightends.txt")
	tight_ends = teFile.readlines()
	teFile.close()
	return tight_ends


def load_kicker_data():
	kFile = open("/Users/SoLReePzz/Documents/IDP Project/src/resources/kickers.txt")
	kickers = kFile.readlines()
	kFile.close()
	return kickers


def load_defense_data():
	dFile = open("/Users/SoLReePzz/Documents/IDP Project/src/resources/defenses.txt")
	defenses = dFile.readlines()
	dFile.close()
	return defenses


class Quarterback:
	#bool draft_status
	#int adp
	#string name
	#string team
	#string bye_week


class Running_Back:
	#bool draft_status
	#int adp
	#string name
	#string team
	#string bye_week


class Wide_Receiver:
	#bool draft_status
	#int adp
	#string name
	#string team
	#string bye_week


class Tight_End:
	#bool draft_status
	#int adp
	#string name
	#string team
	#string bye_week


class Kicker:
	#bool draft_status
	#int adp
	#string name
	#string team
	#string bye_week


class Defense:
	#bool draft_status
	#int adp
	#string name
	#string team
	#string bye_week


main()