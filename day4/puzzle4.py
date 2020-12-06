import re

def puzzle():
    passports = []
    passport = {}
    valid = 0
    total = 0
    with open('puzzle.input') as file_input:
        for line in file_input:
            line = line.strip()
            if line == '':
                passports.append(passport)
                passport = {}
                total += 1
                continue
            entries = line.split(' ')
            for entry in entries:
                field, value = entry.split(':')
                passport[field] = value
        for passport in passports:
            if all (key in passport for key in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")):
                if re.search('^((19[2-9][0-9])|(200[0-2]))$', passport['byr']):
                    if re.search('^((201[0-9])|2020)$', passport['iyr']):
                        if re.search('^((202[0-9])|2030)$', passport['eyr']):
                            if re.search('(^1([5-8][0-9])|(9[0-3])cm$)|(^(59|6[0-9]|7[0-6])in$)', passport['hgt']):
                                if re.search('^#([0-9a-f]){6}$', passport['hcl']):
                                    if re.search('^(amb|blu|brn|gry|grn|hzl|oth)$', passport['ecl']):
                                        if re.search('^([0-9]{9})$', passport['pid']):
                                            valid += 1
    print(valid)

puzzle()


# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
#If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.