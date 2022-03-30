from FileLoader import FileLoader

def proportionBySport(df, olimpicYear, sport, gender):
    total = df.Name[(df.Year == olimpicYear) & (df.Sex == gender)].drop_duplicates().count()
    sp = df.Name[(df.Year == olimpicYear) & (df.Sex == gender) & (df.Sport == sport)].drop_duplicates().count()
    return sp / total

if __name__ == "__main__":
	loader = FileLoader()
	data = loader.load('../resources/athlete_events.csv')
	print(proportionBySport(data, 2004, 'Tennis', 'F'))