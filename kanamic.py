import glob
import csv
import sys
import os
import codecs
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

p = '/Users/makidaisuke/Desktop/auto//before/*'
path = glob.glob(p)

# CSVファイルの読み込み
for f in path:
    user_list = []
    staff_list = []
    date_list = []

    print(f)
    with codecs.open(f, 'r', 'Shift-JIS', 'ignore') as csv_file:
        rows = csv.DictReader(csv_file)
        for row in rows:
            user = row['利用者名']
            staff = row['スタッフ名']
            date = row['サービス日付']
            user_list.append(user.replace('\u3000', ''))
            staff_list.append(staff.replace('\u3000', ''))
            date_list.append(date)

    first_date = date_list[0].replace('-', '_')
    last_date = date_list[-1].replace('-', '_').replace('2020_', '')

    d = defaultdict(list)
    for k, v in zip(user_list, staff_list):
        if v not in d[k] and not v == '':
            
            d[k].append(v)

    write_path = ('/Users/makidaisuke/Desktop/auto/after/' + first_date + '~' + last_date + '.csv')

    with open(write_path, mode='w', encoding='Shift_JIS') as f:
        fieldnames = ['利用者名', 'スタッフ名']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in d.items():
            writer.writerow({'利用者名': key, 'スタッフ名': value})

print('完了しました')
input('終了')