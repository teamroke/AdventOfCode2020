import re

def valid(passport):
    # Validate mandatory fields
    fields = ['byr' ,'iyr' ,'eyr' ,'hgt' ,'hcl' ,'ecl' ,'pid']
    for f in fields:
        if(f not in passport):
            return False

    # Validate numerical
    if not ( 1920 <= int(passport['byr']) <= 2002):
        return False
    if not ( 2010 <= int(passport['iyr']) <= 2020):
        return False
    if not ( 2020 <= int(passport['eyr']) <= 2030):
        return False

    # Validate Height
    if 'cm' in passport['hgt'] and not (150 <= int(passport['hgt'][:-2]) <=193):
        return False
    elif 'in' in passport['hgt'] and not (59 <= int(passport['hgt'][:-2]) <= 76):
        return False
    if 'cm' not in passport['hgt'] and 'in' not in passport['hgt']:
        return False

    # Validate strings/enums
    if  passport['ecl'] not in ['amb', 'blu', 'brn','gry','grn','hzl','oth']:
        return False
    if re.match(r'^\#[0-9a-f]{6}$', passport['hcl']) is None:
        return False
    if re.match(r'^\d{9}$', passport['pid']) is None:
        return False

    return True


def puzzle():
    passports = []
    passport = {}
    goodPassport = 0
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
            if valid(passport):
                goodPassport += 1
    print(goodPassport)

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